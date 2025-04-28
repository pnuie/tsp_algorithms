# tsp_algorithms

This repository investigates the performance of various algorithms on the Traveling Salesman Problem (TSP), a representative NP-hard combinatorial optimization problem. <br>
Implemented algorithms include Large Neighborhood Search (LNS), 2-opt, Backtracking, and Greedy heuristics. <br>
The algorithms are evaluated across instances of varying sizes (10, 25, 50, 75, 200, and 500 nodes), with comparative analyses focusing on solution quality and computational time.

---
## 2-opt
2-opt is a simple local search heuristic that iteratively improves an initial solution by swapping two edges if it results in a shorter total tour length. It helps escape poor local optima by making small, beneficial changes to the route structure.

![image](https://github.com/user-attachments/assets/d07e81cc-00f9-45e1-9441-b214047d13a9)

--
## Large Neighborhood Search
Large Neighborhood Search (LNS) improves solutions by repeatedly destroying and repairing parts of the current solution. In the destroy phase, random nodes are removed, and in the repair phase, they are reinserted to create new candidate solutions. This allows the search to jump out of local minima and explore larger regions of the solution space.

During the implementation of the destroy phase, to reduce computing time when accessing distances between nodes, a **dictionary data structure** was used instead of a 2D list.  
This enables faster distance lookups (constant-time access) and enhances overall performance, especially when the number of nodes is large.

![image](https://github.com/user-attachments/assets/1e00b81e-970f-49a9-81de-8acbcf0a29f9)

