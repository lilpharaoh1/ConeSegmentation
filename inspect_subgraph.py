from logging import root


def get_child_subgraph_dpu(graph: "Graph"):
    assert graph is not None, \
        "Inout Graph object should not be None"
    root_subgraph = graph.get_root_subgraph()
    if root_subgraph.is_leaf:
        return[]
    child_subgraphs = root_subgraph.toposort_child_subgraph()
    return [cs
            for cs in child_subgraphs
            if cs.has_attr("device") and cs.get_attr("device").upper() == "DPU"]

import vart
import xir

graph = xir.Graph.deserialize("CGNet_subgraph_testing.xmodel")
subgraphs = get_child_subgraph_dpu(graph)
print(subgraphs)