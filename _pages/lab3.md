---
title: "Lab 3"
layout: single
excerpt: "Lab 3: Planning"
sitemap: true
permalink: /labs/lab3.html
frontpageorder: 4
categories: []
---

* TOC
{:toc}

Lab 3: Planning, deadline: Jun 5

## Introduction

In this lab, you will be given a simple planner, written in python, and a sample domain that models an elevator. You will then have to extend this domain to include multiple elevators, and come up with problems to solve 
for the planner. You will then further extend the domain to include restrictions for the elevators, to force the planner to choose which elevator to use, and in which order.

## The Planner

You can download the planner [here](/CI-0129/assets/lab3.zip). It is written in python 3, and for educational purposes, so do not expect competitive performance. Instead, take some time to look at the structure 
and implementation of the planner:

  - `pddl.py` contains a parser for PDDL files. It tokenizes the input and then constructs the syntax tree
  - `expressions.py` contains the implementation of the logical reasoning necessary for the planner, in particular a representation for predicate logic formulas and interpretations/states/worlds. You can see that each operator type has its own subclass, that implementes `isModeledBy` and `substitute`.
  - `graph.py` contains the graph representation that you already know from lab 1
  - `pathfinding.py` contains an implementation of A\*, which should be similar to your implementation from lab 1
  - `planner.py`, is the main program, it takes two parameters: a PDDL domain file and a PDDL problem file. It will then parse both of these files using `pddl.py`, and construct a pathfinding problem: The initial state becomes a `Node` (here represented by the class `PlanningNode` which is a subclass of `Node` and of `World`), and each node has a neighbor for each (ground) action that can be applied to that node. The planner then runs A\* on this graph, with the goal of finding a node which is a model for the goal condition.
  - `test_planner.py` will run a larger test suite, consisting of several domains and problems you can find in the `test/` directory. You don't have to use this, but taking a look at these additional domains may lead to a better understanding of PDDL.

You can run the planner with `python planner.py elevator-domain.pddl elevator-problem.pddl`, and it will produce a "path", or plan, that solves this particular problem. For the lab, you will **not** have to modify 
the planner code in any way. Instead, you will only be creating new pddl files to use as input for the planner!  

## The Elevator Domain

Open `elevator-domain.pddl` in a text editor and look at its contents. First, each domain has a name, in this case "<a href="https://elevation.fandom.com/wiki/Schindler_Miconic_10">miconic</a>", and which PDDL features 
it requires (here adl and typing). The typing feature lets us define types for our constants, which is what is done next. The following predicate definitions also include the types of all parameters. The main part of 
the domain file is the definition of actions. Each action has a name and a list of parameters, which means it is technically just an action *template*, that will be expanded to a **ground action** when values for 
these parameters are chosen. Each action then has a **precondition** and an **effect**. The precondition can be an arbitrary formula that defines in which states an action can be applied, namely only in states that 
are models for the precondition. The effect, on the other hand, can only be an effect formula (a conjunction of positive and negative literals, foralls and when-expressions), and defines what an action changes in the world. 

Take the `up` action, for example. It has two parameters: the floor the elevator is departing from (`?f1`) and the floor the elevator is going to (`?f2`). Note that names, including parameters, variables, but also constants,
can contain basically any character except for spaces and parenthesis. It is customary, but not mandatory, to begin variable names with a question mark. The action has a precondition, which limits when it can be applied:
Only when `?f2` is above `?f1` and when the elevator is currently at `?f1`. In this particular example, `above` will likely never change (as floors don't move), but `lift-at` will as the elevator moves. The planner, however,
does not know this, and treats static information and dynamic information the same way, in a logical formula. The effect of the action similarly consists of a logical (effect) formula, which tells the planner which atoms 
to add and remove from a state to obtain the following state. In a state in which the action can be applied, e.g. if the lift is currently at `f1`, and we are trying to move it to `f3`, we can apply the ground action 
`up(f1, f3)`. First we replace all occurrences of `?f1` with `f1` and all occurrences of `?f2` with `f3`, and make sure that the current state is a model for the precondition `(and (lift-at f1) (above f1 f3))`, and, iff 
that is the case, then apply the effect `(and (lift-at f3) (not (lift-at f1)))` to that state, which will remove `lift-at(f1)` from the state and add `lift-at(f3)` instead.

The other actions are defined in a similar manner, with the `stop` action having the notable property of including a `when` expression in its effect. `when` expressions are different from preconditions: While preconditions
are a check if an action can even be applied or not, a `when` expression conditionally applies an effect or not. This means, the elevator can always "stop" at a floor, if the current state is a model for the precondition,
i.e. the lift is currently at that floor. When that is true, the effect will be applied, consisting of two parts: For all passengers, we check if the current floor is their destination and they have boarded the lift. For 
the passengers for which this is true, the effect of the `when` expression will be applied: The passenger will leave the lift and be marked as being `served`. The second part handles passenger's origins in the same manner.

To see what the planner is actually supposed to do with these actions, open the file `elevator-problem.pddl`. This defines one possible problem, consisting of an initial state and a goal condition, for the planner to solve.
First, the problem also contains a name and a reference to the domain it uses. Then, we declare objects that exist in the world, such as the passengers and floors, together with their types. The definition of the initial 
state, starting with `:init` is just a list of atoms that are true in the initial state, in our case to declare each passenger's origin and destination, the location of the lift, but also which floors are above each other 
(remember, the planner does not know what any of our predicates mean. We could build an M.C. Escher house where each floor is above each other floor.) The goal, finally, is declared as an arbitrary logical formula. The 
planner will look for a state which is a model for this formula, in this case to ensure that all passengers have been served.

## Multiple Elevators

For this lab, you will perform two tasks, each of which resulting in a new PDDL domain and problem (feel free to come up with more than one problem using the same domain!). For the first task, create a file 
`elevator-domain-multi.pddl` as a copy of the `elevator-domain.pddl`, and extend it to allow for multiple elevators. To achieve this, you will need to do three things:

 - Add a type representing all available elevators 
 - Add a parameter to the relevant predicates, so you know which elevator is at which floor, and which passenger has boarded which elevator
 - Add a parameter to each action, to indicate which elevator performs this action (and use this new parameter accordingly)
 
The planner will then plan the actions for **all elevators together**. Also create a problem file `elevator-domain-multi.pddl` with at least two elevators, 5 passengers and 8 floors, and let the planner find a plan.
Does it use both elevators? 

## Floor Restrictions

Depending on the exact problem you defined, you may have observed in the first task that the planner does not use both elevators. Maybe it found a more efficient plan that uses only one elevator, maybe it just found
one quicker (the planner will find **a** plan, not necessarily the shortest one, because the heuristic it uses may overestimate the cost). In the second task, you should create two more files 
`elevator-domain-multiple-limited.pddl` and `elevator-problem-multiple-limited.pddl`, which are based on your domain and problem from before. Now, however, we will introduce restrictions on elevators. For our 
purposes, we will say that there are three elevators: One can only stop on even numbered floors (0 is even for our purposes), one can only stop on odd numbered floors, and the third can only stop on floors with 
numbers that are divisible by three. Now, to move a passenger from floor 6 to floor 1, we have to use at least two different elevators. For example, by using the third elevator to move the passenger to floor 3,
and the second elevator to move them to floor 1. 

You will have to change several things in the domain for this to work:

 - You need a new predicate to represent the restriction of which elevator can stop on which floor
 - The problem file needs to use the new predicate to properly restrict the three elevators. You can do this by manually writing out which floors each elevator can reach.
 - Passengers need to be able to leave the elevator on floors that are not their destination. One way to do this is to give passengers a position, and when they leave the elevator at a floor, their position changes 
 to that floor. Only **when** they leave on their destination floor will they "disappear" and be marked as served.

For both tasks, report the plans found by the planner in your report. Do not just use the output from the planner, but describe it in words. Also mention any inefficient or otherwise strange behavior that you may notice.

## Submission

Send the finished code (all pddl files you have!), and your report pdf in a zip file by email to me and Christian ([markus.eger.ucr@gmail.com](mailto:markus.eger.ucr@gmail.com), 
[aiexistencialrisk@gmail.com](mailto:aiexistencialrisk@gmail.com)). Use `[CI-0129]Lab 3, carné 1 carné 2` as the subject line. Do not forget to put the names and 
carn&eacute;'s of both team members in the report as well!
