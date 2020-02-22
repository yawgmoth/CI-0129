---
title: "Lab 3"
layout: single
excerpt: "Lab 3: Logic"
sitemap: true
permalink: /labs/lab3.html
frontpageorder: 4
categories: []
---

* TOC
{:toc}

## Logical Formula Representation

The goal of this task is to develop a class structure representing logical formulas and worlds, that support querying whether or not a world models a formula, and applying changes to the world. The input is given as 
an abstract syntax tree of the logical formulas in question. Later on, in task 3, we will generate these abstract syntax trees by parsing PDDL files, but for now we'll just assume that they are provided. The file 
`expressions.py` describes the expected API and provides some examples for the expected capabilities. You will have to implement the functions 
   
   - `make_expression`, which turns an abstract syntax tree into a suitable python object representing an expression
   - `make_world`, which turns a list of atoms and a dictionary of sets into a suitable python object representing a world 
   - `models`, which determines whether a world models an expression, i.e. if the expression holds in that world 
   - `substitute`, which replaces all occurrences of a variable in an expression with a value, and returns a **new** expression with this substitution. This may be used for formulas with quantifiers, but is **required** even if quantifiers are not implemented.
   - `apply`, which applies an effect, expressed as a logical expression with certain restrictions, to a world, and returns a new world

The return values of `make_expression`, `make_world`, `substitute` and `apply` will only be used to pass them into these functions. `models`, on the other hand, **has** to return a truth value, `True` if the world models the 
expression, and `False` otherwise. The format of the Abstract Syntax Tree passed to the `make_*` functions is described in more detail in the doc strings of `expressions.py`, but a typical input could look like this:
```
("and", 
        ("not", ("at", "home", "mickey")), 
        ("or", 
              ("at", "park", "mickey"), 
              ("at", "store", "mickey"), 
              ("at", "theater", "mickey"), 
              ("at", "airport", "mickey")), 
        ("imply", 
                  ("friends", "mickey", "minny"), 
                  ("forall", 
                            ("?l", "-", "Locations"),
                            ("imply",
                                    ("at", "?l", "mickey"),
                                    ("at", "?l", "minny")))))
```
or
```
("exists", ("?l", "-", "Locations"),
        ("and",
              ("at", "?l", "mickey"),  
              ("at", "?l", "minny") 
              ))
```


A world consists of a set of atoms, which are what is considered to be true, and everything else is considered to be false (Closed World Assumption).

In addition to the basic operators, you also have to implement:
   - `when` expressions 
   - Quantifiers `forall` and `exists`
   - Equality
   
Because these three operations simplify domain writing significantly, many standard PDDL input files use them, and by including them, our planner will be able to support these files. Once you have the other operators,
including these three should be fairly straightforward.

Note, if you are wondering why there is this weird extra `-` in the specification of quantified variables: When we parse the PDDL files later on, which are written in a LISP-inspired syntax, we can get the 
Abstract Syntax Tree used in this task almost "for free", but it does include the dash. Rather than complicating the parsing for this edge-case, we will just keep the dash around and ignore it here.

Mandatory functions in `expressions.py`, following the API described there:
   - `make_expression`
   - `make_world`
   - `models`
   - `substitute`
   - `apply`

