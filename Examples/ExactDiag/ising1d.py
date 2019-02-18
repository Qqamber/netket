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

import netket as nk

# 1D Lattice
g = nk.graph.Hypercube(length=16, n_dim=1, pbc=True)

# Hilbert space of spins on the graph
hi = nk.hilbert.Spin(s=0.5, graph=g)

# Ising spin hamiltonian
ha = nk.operator.Ising(h=1.0, hilbert=hi)

# Perform Lanczos Exact Diagonalization to get lowest three eigenvalues 
res = nk.exact.lanczos_ed(ha, first_n=3, compute_eigenvectors=True)

# Print eigenvalues
print("eigenvalues:", res.eigenvalues)

# Compute energy of ground state
print("g.s. energy:", res.mean(ha, 0))

# Compute energy of first excited state
print("first excited energy:", res.mean(ha, 1))