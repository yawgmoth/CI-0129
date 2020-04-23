---
title: "Lab 2"
layout: single
excerpt: "Lab 2: Monte Carlo Tree Search"
sitemap: true
permalink: /labs/lab2.html
frontpageorder: 4
categories: []
---

* TOC
{:toc}

Lab 2: Monte Carlo Tree Search, deadline: May 22

## Introduction

In this lab, you will implement a simple Monte Carlo Tree Search (MCTS) agent for the game blackjack. Start by downloading [this python file](/CI-0129/assets/blackjack.py), which contains an implementation of the game and 
several sample agents. The game is implemented in the class `Game`, and can be played by any agent that implements the `Player` interface, described below.
  
In the game Blackjack (you can find the full rules online, for example [here](https://bicyclecards.com/how-to-play/blackjack/)), a player bets an amount of money and
is then dealt two cards, and can keep asking for more from the dealer until the total value of their cards is over 21. The dealer then does the same, following fixed rules, 
where they ask for more cards as long as their total is below 17. The goal for the player is to get a higher total than the dealer, without getting more than 21 points. After 
being dealt their initial two cards, the dealer is also dealt two cards, one of which is dealt face-up so that the player can see it. A player then has up to four different options, 
which are repeated until the player chooses the option to stand:

  - **Stand**, which means not taking any more cards 
  - **Hit**, which means asking for another card 
  - **Double Down**, which means doubling the initial bet and getting *exactly* one more card 
  - **Split**, which can only be done if the player has two cards of the same rank or value (exact rules vary from place to place), and separates these two cards into *two* new hands, each of which is played separately. 
    
After a player stands (or stands for both of their hands in case they split), the dealer follows their fixed procedure, of hitting until their total is 17 or more. If the player has a higher total than 21, they lose the
amount they bet. If the player has more points than the dealer, or the dealer has more than 21 points, the player wins the amount bet. If the two scores are the same (a so-called *push*), no one wins. A *blackjack* is 
a hand consisting of an ace and one card worth 10 points (10, Jack, Queen, King), and wins against other hands that would also be worth 21 points. If the player has a blackjack, and the dealer does not, the player wins 
an additional bonus of one half times their bet. 

Note that there are several basic strategies for Blackjack, which are often presented in tables that give the best action depending on the player's cards and the face-up dealer card. Our goal is to develop an agent 
that uses a forward simulation of the game to determine the action that is likely to produce the highest expected value, using a simple Monte Carlo Tree Search procedure. This agent has the advantage that it will 
work with all kinds of rules variations, and even with non-standard decks (what if there was a card worth 12 in each suit?).

## The Framework 

The implementation you are provided with contains the `Game` class, which can be passed a deck of cards, and a player, and then provides two key methods:
   
   - `round` will start a game of blackjack using the rules outlined above, and returns the amount of money won (or lost) by the player 
   - `continue_round` can be used to pass an initial hand of cards to the player and the dealer, and will continue the game from there 
   
The player that is passed to the game has to implement two methods:

   - `get_action` which selects the action the player should perform on their turn. This method is passed the current game state, consisting of the player's cards, the actions they have available to them (which may or may 
   not include the option to split), as well as the visible card in the dealer's hand. 
   - `reset`, which can be used to clear any member variables the player might use during a game, such as remembering which sequence of actions it used.
   
   
The framework provides several sample players, including `Player` (randomly chooses an action), `TimidPlayer` (always stands), `BasicStrategyPlayer` (hits when the dealer card is less than a seven until it has more than 12 
points, or until it has more than 17 points otherwise), and `MCTS` (the skeleton for an MCTS implementation, to be completed by you). Take some time to look through the different player types. Apart from the MCTS player, 
their implementations should be self-explanatory.

## MCTS for Blackjack

Your task is to implementat an agent using Monte Carlo Tree Search to play Blackjack. You can use the already implemented `MCTS` agent as the basis. Concretely, you will need to implement:

  - A selection strategy 
  - A rollout strategy 
  - State evaluation
  - Backpropagation 
  
Take the time to read through and understand the existing implementation. What it does is to play `MCTS_N` games starting from the observed game state, where each game is played with a shuffled deck with the 
observed cards removed, and actions are chosen at random. For each game, the result is recorded based on the first action taken, and at the end, the average score (over these forward simulations) for each 
potential action is calculated, and the action resulting in the maximum value used. What this implementation does **not** do is construct the actual tree needed for a smarter selection. 

What you have to do: When the agent has to decide on an action, you have to run `MCTS_N` simulations, which construct a tree of possible state/action sequences, with the current (observed) game state at the top. 
In the first iteration, the tree only consists of this root node. You then have to use your rollout strategy (which may just be the `RolloutPlayer`, i.e. a random selection) to play the game until the end, and record 
the result (state evaluation), for which you can use the money won by the agent. With this result, you then have to **add** a child node to the root, using the first action taken by your rollout, and mark it with the
obtained result as its expected value. In subsequent iterations the agent then has to decide whether to use the child with the highest expected value, or choose one at random (this is the selection strategy). After 
`MCTS_N` iterations, you should have a tree of actions, each of which is played until the end of the game, and for each node you have the expected value for the amount of money the player wins/loses. 

Note that blackjack is a rather simple game, where the tree will rarely be deeper than 2 or 3 actions, as players are likely to reach more than 21 points with a few cards. **However**, the implementation allows the use
of custom decks. Try, for example, what happens if the deck only contains low valued cards. You can run `blackjack.py` with the `--help` option (or read the source code) to see the various command line parameters that 
are offered, which includes playing games with different types of decks. Also note that the default number of games (100) results in a very high variance of results, and you should test your implementation with 10000 
or more simulations at the end. You may want to keep a copy of the original implementation to have a baseline to compare to. In your report, please note how your agent performs with the different deck types, 
and any observations you have made about its behavior. Also note that the number of rollouts (the `MCTS_N`) your agent performs will have an impact on its performance, and you should try different values and report 
how that affects your agent's expected performance. 

## Submission

Send the finished code (all python files you have!), and your report pdf in a zip file by email to me and Christian ([markus.eger.ucr@gmail.com](mailto:markus.eger.ucr@gmail.com), 
[aiexistencialrisk@gmail.com](mailto:aiexistencialrisk@gmail.com)). Use `[CI-0129]Lab 2, carné 1 carné 2` as the subject line. Do not forget to put the names and 
carn&eacute;'s of both team members in the report as well!
