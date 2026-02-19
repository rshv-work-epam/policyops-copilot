END = "__end__"


class CompiledGraph:
    def __init__(self, nodes, entry, edges, cond_edges):
        self.nodes = nodes
        self.entry = entry
        self.edges = edges
        self.cond_edges = cond_edges

    def invoke(self, state):
        current = self.entry
        while current != END:
            state = self.nodes[current](state)
            if current in self.cond_edges:
                router, mapping = self.cond_edges[current]
                current = mapping[router(state)]
            else:
                current = self.edges.get(current, END)
        return state


class StateGraph:
    def __init__(self, _):
        self.nodes = {}
        self.edges = {}
        self.cond_edges = {}
        self.entry = None

    def add_node(self, name, fn):
        self.nodes[name] = fn

    def set_entry_point(self, name):
        self.entry = name

    def add_edge(self, src, dst):
        self.edges[src] = dst

    def add_conditional_edges(self, src, router, mapping):
        self.cond_edges[src] = (router, mapping)

    def compile(self):
        return CompiledGraph(self.nodes, self.entry, self.edges, self.cond_edges)
