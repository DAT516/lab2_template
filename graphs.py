class Graph(nx.Graph):
    def __init__(self, start=None):
        super().__init__(start)

    # here are some of the public methods to implement
    def vertices(self):
    def add_vertex(self,a):
    def get_vertex_value(self, v):
    def set_vertex_value(self, v, x):


class WeightedGraph(Graph):
    def set_weight(self, a, b, w):
    def get_weight(self, a, b):
    	# etc etc
    	# check the lab assignment for details
