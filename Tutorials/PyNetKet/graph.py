# Copyright 2018 The Simons Foundation, Inc. - All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import netket as nk
import networkx as nx
from mpi4py import MPI

g = nk.graph.Hypercube(L=10, ndim=1)
print(g.Distances(1))
print(g.IsBipartite())
print(g.IsConnected())

Gx = nx.star_graph(10)
g = nk.graph.CustomGraph(edges=list(Gx.edges))
print(g.Distances(0))
print(g.IsConnected())
print(g.AdjacencyList())