"""
Cherrypy based webserver for serving an index (or in future) a set of indexes.

"""
import csv
import io
import math
import os
from urllib.parse import parse_qsl

import cherrypy
from jinja2 import PackageLoader, Environment, select_autoescape

import hyperreal.index


templates = Environment(
    loader=PackageLoader("hyperreal"), autoescape=select_autoescape()
)


@cherrypy.tools.register("before_handler")
def lookup_index():
    """This tool looks up the provided index using the configured webserver."""
    index_id = int(cherrypy.request.params["index_id"])
    cherrypy.request.index = cherrypy.request.config["index_server"].index(index_id)


@cherrypy.tools.register("on_end_request")
def cleanup_index():
    """If an index has been setup for this request, close it."""

    if hasattr(cherrypy.request, "index"):
        cherrypy.request.index.close()


@cherrypy.tools.register("before_handler")
def ensure_list(**kwargs):
    """Ensure that the given variables are always a list of the given type."""

    for key, converter in kwargs.items():
        value = cherrypy.request.params.get(key)
        if value is None:
            cherrypy.request.params[key] = []
        elif isinstance(value, list):
            cherrypy.request.params[key] = [converter(item) for item in value]
        else:
            cherrypy.request.params[key] = [converter(value)]


class Cluster:
    @cherrypy.expose
    def index(
        self,
        index_id,
        cluster_id,
        feature_id=None,
        filter_cluster_id=None,
        exemplar_docs="30",
        scoring="jaccard",
    ):
        template = templates.get_template("cluster.html")

        cluster_id = int(cluster_id)

        # Work out
        other_clusters = cherrypy.request.index.cluster_ids

        try:
            cluster_index = other_clusters.index(cluster_id)
        except ValueError:
            raise cherrypy.HTTPError(404)

        # If we're at the start/end, wrap around to the end/start.
        prev_cluster_id = other_clusters[cluster_index - 1]
        next_cluster_id = other_clusters[
            (cluster_index + 1) if cluster_index < (len(other_clusters) - 1) else 0
        ]

        features = cherrypy.request.index.cluster_features(cluster_id)
        n_features = len(features)
        rendered_docs = []
        query = None

        if feature_id is not None:
            feature_id = int(feature_id)
            query = cherrypy.request.index[feature_id]

        if filter_cluster_id is not None:
            filter_cluster_id = int(filter_cluster_id)
            if query:
                query &= cherrypy.request.index.cluster_docs(filter_cluster_id)
            else:
                query = cherrypy.request.index.cluster_docs(filter_cluster_id)

        if query:
            sorted_features = list(
                cherrypy.request.index.pivot_clusters_by_query(
                    query,
                    cluster_ids=[cluster_id],
                    top_k=n_features,
                    scoring=scoring,
                )
            )

            # Make sure that there are actually matching features.
            if sorted_features:
                features = sorted_features[0][-1]

            # Make sure to only show the intersection of the requested feature with
            # the current cluster.
            retrieve_docs = query & cherrypy.request.index.cluster_docs(cluster_id)

            visible_features = [feature[0] for feature in features]

        else:
            retrieve_docs = cherrypy.request.index.cluster_docs(cluster_id)
            visible_features = None

        # Retrieve matching documents if we have a corpus to render them.
        if cherrypy.request.index.corpus is not None:
            rendered_docs = cherrypy.request.index.render_docs_html(
                retrieve_docs, random_sample_size=int(exemplar_docs)
            )

        total_docs = len(retrieve_docs)

        fields = [row[0] for row in cherrypy.request.index.indexed_field_summary()]

        pinned = int(cluster_id in cherrypy.request.index.pinned_cluster_ids)

        return template.render(
            cluster_id=cluster_id,
            highlight_feature_id=feature_id,
            features=features,
            index_id=index_id,
            cluster_score=None,
            rendered_docs=rendered_docs,
            total_docs=total_docs,
            prev_cluster_id=prev_cluster_id,
            next_cluster_id=next_cluster_id,
            pinned=pinned,
            visible_features=visible_features,
            fields=fields,
        )

    @cherrypy.expose
    def search(self, index_id, cluster_id, field, value):
        """
        Search a specific field for a specific value.

        Currently this is limited to exact matches on a single value only.

        """

        feature_id = cherrypy.request.index.lookup_feature_id((field, value))

        raise cherrypy.HTTPRedirect(
            f"/index/{index_id}/cluster/{cluster_id}/?feature_id={feature_id}"
        )


@cherrypy.popargs("cluster_id", handler=Cluster())
class ClusterOverview:
    @cherrypy.expose
    def index(self, index_id, cluster_id=None, feature_id=None):
        pass

    @cherrypy.expose
    @cherrypy.tools.allow(methods=["POST"])
    @cherrypy.tools.ensure_list(cluster_id=int)
    def delete(self, index_id, cluster_id=None, return_cluster_id=None, **params):
        cherrypy.request.index.delete_clusters(cherrypy.request.params["cluster_id"])

        if return_cluster_id:
            redirect_to = f"/index/{index_id}/cluster/{return_cluster_id}"
        else:
            redirect_to = f"/index/{index_id}"
        raise cherrypy.HTTPRedirect(redirect_to)

    @cherrypy.expose
    @cherrypy.tools.allow(methods=["POST"])
    @cherrypy.tools.ensure_list(feature_id=int)
    def create(self, index_id, feature_id=None, **params):
        new_cluster_id = cherrypy.request.index.create_cluster_from_features(
            cherrypy.request.params["feature_id"]
        )
        raise cherrypy.HTTPRedirect(f"/index/{index_id}/cluster/{new_cluster_id}")

    @cherrypy.expose
    @cherrypy.tools.allow(methods=["POST"])
    @cherrypy.tools.ensure_list(cluster_id=int)
    def merge(self, index_id, cluster_id=None, **params):
        merge_cluster_id = cherrypy.request.index.merge_clusters(
            cherrypy.request.params["cluster_id"]
        )
        raise cherrypy.HTTPRedirect(f"/index/{index_id}/cluster/{merge_cluster_id}")

    @cherrypy.expose
    @cherrypy.tools.allow(methods=["POST"])
    @cherrypy.tools.ensure_list(cluster_id=int)
    def refine(
        self,
        index_id,
        cluster_id=None,
        target_clusters=None,
        iterations="10",
        return_to="cluster",
        minimum_cluster_features="1",
    ):
        if target_clusters:
            target_clusters = int(target_clusters)
        else:
            target_clusters = None

        cherrypy.request.index.refine_clusters(
            cluster_ids=cherrypy.request.params["cluster_id"],
            target_clusters=target_clusters,
            minimum_cluster_features=int(minimum_cluster_features),
            iterations=int(iterations),
        )
        if return_to == "cluster":
            raise cherrypy.HTTPRedirect(f"/index/{index_id}/cluster/{cluster_id[0]}")
        else:
            raise cherrypy.HTTPRedirect(
                f"/index/{index_id}/?cluster_id={cluster_id[0]}"
            )

    @cherrypy.expose
    @cherrypy.tools.allow(methods=["POST"])
    @cherrypy.tools.ensure_list(cluster_id=int)
    def pin(self, index_id, cluster_id=None, pinned="1", return_to="cluster"):
        """
        Pin or unpin the selected clusters.

        Pinned clusters will not be affected by future iterations of the algorithm.

        """
        cherrypy.request.index.pin_clusters(
            cluster_ids=cherrypy.request.params["cluster_id"], pinned=int(pinned)
        )
        if return_to == "cluster":
            raise cherrypy.HTTPRedirect(f"/index/{index_id}/cluster/{cluster_id[0]}")
        else:
            raise cherrypy.HTTPRedirect(
                f"/index/{index_id}/?cluster_id={cluster_id[0]}"
            )


class FeatureOverview:
    @cherrypy.expose
    def index(self, index_id, feature_id=None):
        return "feature"

    @cherrypy.expose
    @cherrypy.tools.allow(methods=["POST"])
    @cherrypy.tools.ensure_list(feature_id=int)
    def remove_from_model(self, index_id, feature_id=None, cluster_id=None):
        cherrypy.request.index.delete_features(cherrypy.request.params["feature_id"])
        if cluster_id is not None:
            raise cherrypy.HTTPRedirect(f"/index/{index_id}/cluster/{cluster_id}")
        else:
            raise cherrypy.HTTPRedirect(f"/index/{index_id}/")

    @cherrypy.expose
    @cherrypy.tools.allow(methods=["POST"])
    @cherrypy.tools.ensure_list(feature_id=int)
    def pin(self, index_id, feature_id=None, cluster_id=None, pinned="1"):
        """
        Pin the selected features.

        Pinned features will not be moved algorithmically, and clusters containing any
        pinned features will not be automatically split.

        """
        cherrypy.request.index.pin_features(
            cherrypy.request.params["feature_id"], pinned=int(pinned)
        )
        if cluster_id is not None:
            raise cherrypy.HTTPRedirect(f"/index/{index_id}/cluster/{cluster_id}")
        else:
            raise cherrypy.HTTPRedirect(f"/index/{index_id}/")


@cherrypy.popargs("index_id")
@cherrypy.tools.cleanup_index()
@cherrypy.tools.lookup_index()
class Index:
    cluster = ClusterOverview()
    feature = FeatureOverview()

    @cherrypy.expose
    @cherrypy.config(**{"response.stream": True})
    def index(
        self,
        index_id,
        feature_id=None,
        cluster_id=None,
        exemplar_docs="5",
        top_k_features="40",
        scoring="jaccard",
    ):
        template = templates.get_template("index.html")

        rendered_docs = []
        total_docs = 0
        query = None
        highlight_cluster_id = None
        highlight_feature_id = None

        # Redirect to the index overview page to create a new model if no
        # index has been created.
        if not cherrypy.request.index.cluster_ids:
            raise cherrypy.HTTPRedirect(f"/index/{index_id}/details")

        if feature_id is not None:
            query = cherrypy.request.index[int(feature_id)]
            highlight_feature_id = int(feature_id)

        elif cluster_id is not None:
            query = cherrypy.request.index.cluster_docs(int(cluster_id))
            highlight_cluster_id = int(cluster_id)

        if query:
            clusters = cherrypy.request.index.pivot_clusters_by_query(
                query, scoring=scoring, top_k=int(top_k_features)
            )

            if cherrypy.request.index.corpus is not None:
                rendered_docs = cherrypy.request.index.render_docs_html(
                    query, random_sample_size=int(exemplar_docs)
                )

            total_docs = len(query)

        else:
            clusters = cherrypy.request.index.top_cluster_features(
                top_k=int(top_k_features)
            )
            total_docs = 0

        fields = [row[0] for row in cherrypy.request.index.indexed_field_summary()]

        return template.generate(
            clusters=clusters,
            total_docs=total_docs,
            rendered_docs=rendered_docs,
            # Design note: might be worth letting templates grab the request
            # context, and avoid passing this around for everything that
            # needs it?
            index_id=index_id,
            highlight_feature_id=highlight_feature_id,
            highlight_cluster_id=highlight_cluster_id,
            fields=fields,
        )

    @cherrypy.expose
    def search(self, index_id, field, value, cluster_id=None):
        """
        Search a specific field for a specific value.

        Currently this is limited to exact matches on a single value only.

        If a cluster_id is provided the search will return to that specific
        cluster view.

        """

        feature_id = cherrypy.request.index.lookup_feature_id((field, value))

        if cluster_id is not None:
            raise cherrypy.HTTPRedirect(
                f"/index/{index_id}/cluster/{cluster_id}?feature_id={feature_id}"
            )
        else:
            raise cherrypy.HTTPRedirect(f"/index/{index_id}/?feature_id={feature_id}")

    @cherrypy.expose
    def details(self, index_id):
        """
        Show the details of the index, including indexed fields and associated cardinalities.

        """

        template = templates.get_template("details.html")
        current_clusters = len(cherrypy.request.index.cluster_ids)
        field_summary = cherrypy.request.index.indexed_field_summary()

        return template.render(
            field_summary=field_summary,
            index_id=index_id,
            current_clusters=current_clusters,
        )

    @cherrypy.expose
    def export_clusters(self, index_id):
        """
        Export a spreadsheet of the model information, including features and cluster assignments.

        """

        cherrypy.response.headers["Content-Type"] = "text/csv"
        cherrypy.response.headers[
            "Content-Disposition"
        ] = 'attachment; filename="feature_clusters.csv"'
        all_features = cherrypy.request.index.top_cluster_features(top_k=2**62)

        output = io.StringIO()
        writer = csv.writer(output, dialect="excel", quoting=csv.QUOTE_ALL)
        writer.writerow(("cluster_id", "feature_id", "field", "value", "docs_count"))

        for cluster_id, _, cluster_features in all_features:
            for row in cluster_features:
                writer.writerow([cluster_id, *row])

        output.seek(0)

        return cherrypy.lib.file_generator(output)

    @cherrypy.expose
    @cherrypy.tools.allow(methods=["POST"])
    @cherrypy.tools.ensure_list(include_fields=str)
    def recreate_model(
        self,
        index_id,
        include_fields=None,
        min_docs="10",
        clusters="64",
        iterations="10",
        minimum_cluster_features="1",
    ):
        """
        (Re)Create the model for this index with the given parameters.

        Note that this does not actually run any iterations of refinement.

        """
        cherrypy.request.index.initialise_clusters(
            n_clusters=int(clusters),
            min_docs=int(min_docs),
            include_fields=include_fields or None,
        )

        cherrypy.request.index.refine_clusters(
            iterations=int(iterations),
            minimum_cluster_features=int(minimum_cluster_features),
        )

        raise cherrypy.HTTPRedirect(f"/index/{index_id}")

    @cherrypy.expose
    @cherrypy.tools.allow(methods=["POST"])
    def refine_model(
        self,
        index_id,
        iterations="10",
        target_clusters="0",
        minimum_cluster_features="1",
    ):
        """
        Refine the existing model for the given number of iterations.

        """
        if target_clusters:
            target_clusters = int(target_clusters)
        else:
            target_clusters = None
        cherrypy.request.index.refine_clusters(
            iterations=int(iterations),
            target_clusters=target_clusters,
            minimum_cluster_features=int(minimum_cluster_features),
        )

        raise cherrypy.HTTPRedirect(f"/index/{index_id}")


@cherrypy.popargs("index_id", handler=Index())
class IndexOverview:
    @cherrypy.expose
    def index(self):
        template = templates.get_template("index_listing.html")
        indices = cherrypy.request.config["index_server"].list_indices()
        return template.render(indices=indices)


class Root:
    """
    There will be more things at the base layer in the future.

    But for now we will only worry about the /index layer and
    associated operations.
    """

    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect("/index/")


class SingleIndexServer:
    def __init__(
        self,
        index_path,
        corpus_class=None,
        corpus_args=None,
        corpus_kwargs=None,
        pool=None,
    ):
        """
        Helper class for serving a single index via the webserver.

        An index will be created on demand when a request requires.

        This will create a single multiprocessing pool to be shared across
        indexes.

        """
        self.corpus_class = corpus_class
        self.corpus_args = corpus_args
        self.corpus_kwargs = corpus_kwargs
        self.index_path = index_path

        self.pool = pool

    def index(self, index_id):
        if index_id != 0:
            raise cherrypy.HTTPError(404)

        if self.corpus_class:
            corpus = self.corpus_class(
                *(self.corpus_args or []), **(self.corpus_kwargs or {})
            )
        else:
            corpus = None

        return hyperreal.index.Index(self.index_path, corpus=corpus, pool=self.pool)

    def list_indices(self):
        return {
            0: (
                self.index_path,
                self.corpus_class,
                self.corpus_args,
                self.corpus_kwargs,
            )
        }


def launch_web_server(index_server, auto_reload=False):
    """Launch the web server using the given instance of an index server."""

    if not auto_reload:
        cherrypy.config.update(
            {
                "global": {
                    "engine.autoreload.on": False,
                }
            }
        )

    cherrypy.tree.mount(
        Root(),
        "/",
        {
            "/": {
                "tools.response_headers.on": True,
                "tools.response_headers.headers": [
                    ("Connection", "close"),
                ],
            }
        },
    )
    cherrypy.tree.mount(
        IndexOverview(),
        "/index",
        {
            "/": {
                "index_server": index_server,
                "tools.response_headers.on": True,
                "tools.response_headers.headers": [
                    ("Connection", "close"),
                ],
            }
        },
    )

    cherrypy.log.access_log.propagate = False
    cherrypy.log.error_log.propagate = False

    cherrypy.engine.signals.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()
