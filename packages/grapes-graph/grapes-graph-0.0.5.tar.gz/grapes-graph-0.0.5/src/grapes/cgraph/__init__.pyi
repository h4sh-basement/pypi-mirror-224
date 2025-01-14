from typing import Type

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Multigraph:
    """Underlying graph type.

    .. note::
        Nodes are represented as 0-based indices.
    """

    def __init__(self: Self, is_directed: bool, node_count: int = 0) -> None:
        """Initialize a graph.

        :param is_directed: Whether or not the graph is directed.
        :type is_directed: bool
        :param node_count: The initial number of nodes within the graph,
            defaults to 0.
        :type node_count: int
        :rtype: None
        """
    def get_node_count(self: Self) -> int:
        """Get the number of nodes in the graph.

        :rtype: int
        """
    def get_edge_count(self: Self) -> int:
        """Get the number of edges in the graph.

        .. note::
            Edges are considered as having their own identity, so multiple
            edges with the same nodes will be counted separately.

        :rtype: int
        """
    def get_edges(self: Self) -> list[tuple[int, int]]:
        """Get the edges in the graph.

        .. note::
            If the graph is undirected and (u, v) is in edges, (v, u) will not
            also be returned. However, edges are considered as having their own
            identity, so multiple edges will be returned.

        :returns: List of edges
        :rtype: list[tuple[int, int]]
        """
    def add_node(self: Self) -> int:
        """Add a node to the graph.

        :returns: The index to the new node added.
        :rtype: int
        """
    def add_edge(self: Self, u: int, v: int, *, weight: float = 1.0) -> None:
        """Add an edge between two nodes.

        .. note::
            Edges are considered as having their own identity.

        :param u: node
        :type u: int
        :param v: node
        :type v: int
        :param weight: weight of edge, defaults to 1.0
        :type weight: float
        :rtype: None
        """
    def dijkstra_path(self: Self, src: int, dst: int) -> list[int]:
        """Get the shortest path in the graph using Dijkstra's algorithm.

        :param src: Begin (source) node
        :type src: int
        :param dst: End (destination) node
        :type dst: int
        :return: List of nodes, starting from `src` and ending with `dst`.
            Returns an empty list if no path found.
        :rtype: list[int]
        """
    def get_component_sizes(self: Self) -> list[int]:
        """Return the sizes of the (connected) components in the graph.

        :rtype: list[int]
        """
    def is_bipartite(self: Self) -> bool:
        """Return whether the graph is bipartite or not.

        :returns: Returns `True` if the graph is bipartite; otherwise, `False`.
        :rtype: bool
        """
