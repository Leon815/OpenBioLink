import os
from typing import Mapping

from openbiolink.graph_creation import graphCreationConfig as gcConst
from openbiolink.graph_creation.graph_writer.base import OpenBioLinkGraphWriter


class GraphRDFWriter(OpenBioLinkGraphWriter):
    identifiersURL = "https://identifiers.org/"

    def output_graph(
        self, nodes: Mapping = None, edges: Mapping = None, prefix=None, node_edge_list=True,
    ):
        if prefix is None:
            prefix = ""

        if self.multi_file:
            self._output_graph_in_multi_files(prefix=prefix, nodes=nodes, edges=edges)
        else:
            self._output_graph_in_single_file(prefix=prefix, nodes=nodes, edges=edges)

        # lists of all nodes and metaedges
        if node_edge_list:
            self.write_node_and_edge_list(prefix, nodes.keys(), edges.keys())

        # niceToHave (8) adjacency matrix
        # key, value = nodes_dic
        # d = {x: i for i, x in enumerate(value)}
        # niceToHave (8) outputformat for graph DB

    def _output_graph_in_single_file(self, *, prefix, nodes, edges):
        if nodes is not None:
            with open(os.path.join(self.graph_dir_path, prefix + gcConst.NODES_FILE_PREFIX + ".N3"), "w") as out_file:
                for key, value in nodes.items():
                    for node in value:
                        out_file.write("<" + self.identifiersURL + node.id + "> a #" + str(node.type) + " .\n")
        if edges is not None:
            with open(os.path.join(self.graph_dir_path, prefix + gcConst.EDGES_FILE_PREFIX + ".N3"), "w") as out_file:
                for key, value in edges.items():
                    for edge in value:
                        if self.print_qscore:
                            out_file.write(
                                "<"
                                + self.identifiersURL
                                + edge.id1
                                + "> <#"
                                + str(edge.type)
                                + "> <"
                                + self.identifiersURL
                                + edge.id2
                                + "> . #quality:"
                                + str(edge.qScore)
                                + " source:"
                                + edge.sourcedb
                                + "\n"
                            )
                        else:
                            out_file.write(
                                "<"
                                + self.identifiersURL
                                + edge.id1
                                + "> <#"
                                + str(edge.type)
                                + "> <"
                                + self.identifiersURL
                                + edge.id2
                                + "> . #source:"
                                + edge.sourcedb
                                + "\n"
                            )

    def _output_graph_in_multi_files(self, *, prefix, nodes, edges):
        # write nodes
        for key, value in nodes.items():
            with open(
                os.path.join(self.graph_dir_path, prefix + gcConst.NODES_FILE_PREFIX + "_" + key + ".N3"), "w"
            ) as out_file:
                for node in value:
                    out_file.write("<" + self.identifiersURL + node.id + "> a #" + str(node.type) + " .\n")
        # write edges
        for key, value in edges.items():

            with open(
                os.path.join(self.graph_dir_path, prefix + gcConst.EDGES_FILE_PREFIX + "_" + key + ".N3"), "w"
            ) as out_file:
                for edge in value:
                    if self.print_qscore:
                        out_file.write(
                            "<"
                            + self.identifiersURL
                            + edge.id1
                            + "> <#"
                            + str(edge.type)
                            + "> <"
                            + self.identifiersURL
                            + edge.id2
                            + "> . #quality:"
                            + str(edge.qScore)
                            + " source:"
                            + edge.sourcedb
                            + "\n"
                        )
                    else:
                        out_file.write(
                            "<"
                            + self.identifiersURL
                            + edge.id1
                            + "> <#"
                            + self.identifiersURL
                            + str(edge.type)
                            + "> <"
                            + self.identifiersURL
                            + edge.id2
                            + "> . #source:"
                            + edge.sourcedb
                            + "\n"
                        )