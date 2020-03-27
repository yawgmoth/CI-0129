---
title: "Lab 1"
layout: single
excerpt: "Lab 1: Search"
sitemap: true
permalink: /labs/lab1.html
frontpageorder: 4
categories: []
---

* TOC
{:toc}

Lab 1: Search, deadline: TBD

## Search Algorithms

In this lab, you will implement four "different" (directed) graph search algorithms in python:
 - Breadth-First Search 
 - Depth-First Search 
 - Greedy Search 
 - A*
 
Each of these algorithms takes a graph, represented as an initial node that can produce its neighbors, and a goal predicate/function that tells you when you have reached a goal node. The last two algorithms additionally 
get a heuristic that tells you how close a node is **estimated** to be to the goal.

To get started download [this zip file](/CI-0129/assets/pathfinding.zip), which contains two python files: `pathfinding.py` and `graph.py`. You only have to modify `pathfinding.py`, but you can and should 
use `graph.py` to come up with more test cases!

The graph representation is implemented in `graph.py`, and does not have to be modified. If you want to modify `graph.py`, please do not 
change `Node` and `Edge` and their interfaces. When in doubt what you can change, ask. For this task, you only have to implement four functions: `bfs(start, goal)`, `dfs(start, goal)`, `greedy(start, heuristic, goal)`
and `astar(start, heuristic, goal)`. 
The result of each of the functions should be four values:
   - The path, represented as a sequence of `Edge` objects
   - The total length of the path
   - The number of nodes visited, i.e. added to the frontier, during search
   - The number of nodes expanded, i.e. removed from the frontier, during search
If no path is found, the first two values should be `None`, but the number of visited and expanded nodes should still be reported.

Note that all four functions have the same basic structure, and only differ in how they select which node to expand next, i.e. which data structure they use for the frontier. You could implement a base `search` function 
and pass it the appropriate data structure to get each of the four algorithms, or you can implement them individually.

As mentioned above, the graph is not represented explicitly, instead only a single `Node` object is passed to the algorithm, which has a method `get_neighbors` which returns a list of `Edge` objects representing 
outgoing edges. Each `Edge` object stores its target, the cost to use the edge, and its name (used for printing the path). The target is another `Node` object, which can then in turn be asked for its own neighbors, 
and so on. Note that to simplify development, nodes do not need to be cached between calls, and are instead identified by a unique id, which can be obtained from the `get_id` method. `graph.py` shows how this 
representation can be used to represent finite and infinite graphs.

Mandatory functions in `pathfinding.py`, following the API described there (and above):
   - `bfs`
   - `dfs`
   - `greedy`
   - `astar`
   
Do **not** remove or change the `default_heuristic` in `pathfinding.py`.

In your report, note how the different algorithms perform on the given examples. Which visits/expands the least nodes, which one finds the shortest path? Come up with **at least** one graph of your own and test the four 
algorithms on it. Try to define a reasonable heuristic, and see how it affects performance (use the `run_all` function, which will run greedy search and A* with the default heuristic as well as with the provided heuristic).

## Submission

Send the finished code (all python files you have!), and your report pdf in a zip file by email to me and Christian ([markus.eger.ucr@gmail.com](mailto:markus.eger.ucr@gmail.com), 
[aiexistencialrisk@gmail.com](mailto:aiexistencialrisk@gmail.com)). Use `[CI-0129]Lab 1, carné 1 carné 2` as the subject line. Do not forget to put the names and 
carn&eacute;'s of both team members in the report as well!
