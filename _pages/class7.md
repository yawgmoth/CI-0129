---
title: "Virtual Class: Logic"
layout: single
excerpt: "Virtual Class: Logic"
sitemap: true
permalink: /classes/class7.html
frontpageorder: 4
categories: []
---

* TOC
{:toc}

## Introduction

Classes 7a and 7b, which are about logic, will be held in virtual form. This page guides you through the lecture, which consists of short videos done live during class hours, and some text containing tasks
for you to think about and/or discuss with other students. The idea is that the instructor gives short 10-15 minute lectures about each topic and you work through the problems between these videos and discuss
them with the instructor and other students over the video call. However, the videos will be recorded and you also have the option to work through the class content at another time, and send questions 
via email or slack. Please indicate which section your question is about, to make it easier for me to respond effectively.
This page contains all materials for classes 7a **and** 7b, because they form one logical unit. The class is designed to be
held as two separate 1-1.5 hour lectures, including the exercises. The videos will use the slides for [lecture 7](/CI-0129/slides/lecture7.html) from the website. 

## Propositional Logic and Interpretations

Follow the lecture on propositional logic given by the instructor before you continue.



You are given an interpretation $W = \\{ a, b, c }$. For each of the following formulas determine if $W$ is a model for that formula.
$$
\text{1. } (a \wedge b)\\
\text{2. } (b \rightarrow d)\\
\text{3. } (d \rightarrow b)\\
\text{4. } b \wedge ((c \rightarrow e) \rightarrow d)\\
\text{5. } e \vee (c \wedge \neg d)\\
\text{6. } \neg d \rightarrow \neg e
$$
<div style="margin:20px; margin-top:5px; margin-right:15px; border: 1px solid #3bbfe7;" class="codebox">
<dt style="height:40px; text-align: center;"><strong>Answer:</strong>
<input type="button" value="Show" style="width:78px; font-size:14px; margin:0px; padding:0px;" onclick="var spoiler = $(this).parents('.codebox').find('.content').toggle('slow');
if ( this.value == 'Hide' ) { this.value = 'Show'; } else { this.value = 'Hide'; };
return false;"></dt>
<dd><div class="content" name="spoiler" style="display: none; margin-right:15px;">
$W$ is a model of 1., because both $a$ and $b$ are elements of the interpretation.<br/><br/>

$W$ is not a model of 2., because $b$ is an element of the interpretation, but d is not. The implication holds if the antecedent (here b) is false or the consequence (here d) is true, which is not the case.<br/><br/>

$W$ is a model of 3., because d is not an element of the interpretation, which means that the antecedent is false, which makes the entire implication true!<br/><br/>

$W$ is a model of 4. First, note that $b$ is an element of $W$. Then we determine if $W$ is a model for the right hand side of the conjunction: $c \rightarrow e$ is false, since $e$ is not an element of $W$, but $c$ is. 
Therefore, the larger implication is true, because its antecedent is false!<br/><br/>

$W$ is a model of 5. While $e$ is false, $c$ is true, and the negation of $d$ is also true.<br/><br/>

$W$ is a model of 6. The negation of $d$ is true, as is the negation of $e$.
</div></dd></div>

Next, define your own interpretation $W$, which is a model for **all** of the following formulas:

$$
\text{1. } (a \wedge \neg b)\\
\text{2. } (b \rightarrow c)\\
\text{3. } (c \vee d \vee \neg a)\\
\text{4. } (a \rightarrow e)\\
\text{5. } (e \rightarrow (\neg a \vee \neg b \vee \neg c \vee \neg d))
$$

<div style="margin:20px; margin-top:5px; margin-right:15px; border: 1px solid #3bbfe7;" class="codebox">
<dt style="height:40px; text-align: center;"><strong>Answer:</strong>
<input type="button" value="Show" style="width:78px; font-size:14px; margin:0px; padding:0px;" onclick="var spoiler = $(this).parents('.codebox').find('.content').toggle('slow');
if ( this.value == 'Hide' ) { this.value = 'Show'; } else { this.value = 'Hide'; };
return false;"></dt>
<dd><div class="content" name="spoiler" style="display: none; margin-right:15px;">
From 1 we conclude that a has to be an element of $W$, but $b$ must not be. <br/><br/>

Using 3, we determine that $c$ or $d$ have to be in $W$, so let us choose $c$. <br/><br/>

From 4 we can then conclude, since $a$ is in $W$, $e$ has to be too. <br/><br/>

Checking 2, we see that since $b$ is not in $W$, $W$ is already a model for 2. <br/><br/>

Finally, for 5 the consequence must hold (since $e$ is an element of $W$). We already know that $b$ is not an element of $W$, 
so the consequence also holds, and we found an interpretation that is a model for all five formulas:

$$
W = \{a, c, e\}
$$
</div></dd></div>

## Predicate Logic 

Follow the lecture on predicate logic given by the instructor before you continue.

You are given an interpretation

$$
W = \{ \mathit{Lannister}(\mathit{Tywin}), \mathit{Lannister}(\mathit{Tyrion}), \\
       \mathit{Lannister}(\mathit{Cersei}), \mathit{Lannister}(\mathit{Jaime}),\\
       \mathit{owes}(\mathit{Tyrion}, \mathit{Bronn}), \mathit{owes}(\mathit{Jaime},\mathit{Brienne}), \\
       \mathit{owes}(\mathit{Brienne}, \mathit{Catelyn}),\\
       \mathit{paidDebt}(\mathit{Tyrion}, \mathit{Bronn}), \\
       \mathit{paidDebt}(\mathit{Jaime}, \mathit{Brienne}) \}
$$
Over the domain

$$
D= \{\mathit{Tywin},  \mathit{Tyrion}, \mathit{Cersei}, \\
     \mathit{Jaime}, \mathit{Bronn}, \mathit{Brienne}, \mathit{Catelyn}\}
$$

For each of the following formulas, determine if $W$ is a model of that formula over $D$.

$$
\text{1. } \forall x \forall y \in Lannister: \mathit{owes}(y,x) \rightarrow \mathit{paidDebt}(y,x)\\
\text{2. } \exists x \forall y: \neg \mathit{owes}(x,y)\\
\text{3. } \exists x \forall y: \neg \mathit{owes}(y,x)\\
\text{4. } \forall y \exists x: \mathit{owes}(y,x) \vee \mathit{owes}(x,y)\\
\text{5. } \forall x: \mathit{owes}(x, \mathit{Catelyn}) \rightarrow \neg \mathit{Lannister}(x)
$$
<div style="margin:20px; margin-top:5px; margin-right:15px; border: 1px solid #3bbfe7;" class="codebox">
<dt style="height:40px; text-align: center;"><strong>Answer:</strong>
<input type="button" value="Show" style="width:78px; font-size:14px; margin:0px; padding:0px;" onclick="var spoiler = $(this).parents('.codebox').find('.content').toggle('slow');
if ( this.value == 'Hide' ) { this.value = 'Show'; } else { this.value = 'Hide'; };
return false;"></dt>
<dd><div class="content" name="spoiler" style="display: none; margin-right:15px;">
$W$ is a model of 1. We need to consider all $x$ and $y$ (for which $y$ is in the set Lannister). If $y$ owes $x$ $\mathit{owes}(y,x)$ is true, they also have to pay their debt 
($\mathit{paidDebt}(y,x)$). Tyrion owes Bronn, and Jaime owes Brienne, which are the only Lannisters to owe anyone, and both paid their debt. *A Lannister always pays his debt*<br/><br/>

$W$ is a model of 2. This formula means "There is someone for whom it is false that they owe them, for everyone else" ("There is someone that does not owe anyone"). Tywin, in our interpretation, does not 
owe anyone, therefore $\mathit{owes}(\mathit{Tywin},y)$ is false for all $y$.<br/><br/>

$W$ is a model of 3. This formula means "There is someone for whom it is false that they are owed something, for everyone else" ("There is someone that is not owed by anyone"). Once again, we can use Tywin as $x$, because 
$\mathit{owes}(y,\mathit{Tywin})$ is false for all $y$.<br/><br/>

$W$ is not a model of 4. This sentence means "For everyone there is someone that they owe to or that owes them". To check this, we need to look at each character and see if they have any outgoing or incoming 
debts. However, Tywin has (as we discovered in formula 2) no one that he owes, nor (as we discovered in formula 3) anyone that owed him, and therefore $W$ is not a model for formula 4.<br/><br/>

$W$ is a model of 5. This sentence means "Everyone that owes Catelyn is not a Lannister". For every $x$ we first need to determine if they owe Catelyn, which is only true for Brienne, for every other $x$ the antecendent is 
false, and therefore the implication is true. For Brienne, the consequence is true, since she is not a Lannister. Therefore, the implication holds for all $x$.<br/><br/>
</div></dd></div>


Now define an interpretation $W$ that is a model for **none** of the following formulas:

$$
\text{1. } \forall x: \mathit{bird}(x)\\
\text{2. } \forall x \exists y: \mathit{eats}(x,y)\\
\text{3. } \neg \exists x: \mathit{cat}(x)\\
\text{4. } \forall x: \mathit{cat}(x) \rightarrow \neg \exists y \mathit{eats}(y,x)\\
\text{5. } \neg \mathit{dog}(\mathit{pluto})
$$

<div style="margin:20px; margin-top:5px; margin-right:15px; border: 1px solid #3bbfe7;" class="codebox">
<dt style="height:40px; text-align: center;"><strong>Answer:</strong>
<input type="button" value="Show" style="width:78px; font-size:14px; margin:0px; padding:0px;" onclick="var spoiler = $(this).parents('.codebox').find('.content').toggle('slow');
if ( this.value == 'Hide' ) { this.value = 'Show'; } else { this.value = 'Hide'; };
return false;"></dt>
<dd><div class="content" name="spoiler" style="display: none; margin-right:15px;">
First: We need to determine a domain for our interpretation, too! Let's use a domain with two elements: pluto and tweety.<br/><br/>

Remember: We want all formulas to be false, i.e. our interpretation should be a model for none of them.<br/><br/>

From formula 1, we conclude that not both of our elements can be birds, so let's have tweety be a bird, and pluto not. Formula 3 says that there must be at least one cat, let us say pluto. 
Formula 5 then says that he also has to be a dog (logic allows us to construct a cat-dog!).<br/><br/>

Our current interpretation is not a model for formula 2, so let us look at formula 4 first: It basically says that for every cat there is nothing that would eat that cat. Our only cat is pluto,
and nothing is eating pluto, so our current interpretation would be a model for formula 4. We therefore need to add something that eats pluto, for example pluto.<br/><br/> 

One final check for formula 2: It says that for every $x$ there is a $y$ that $x$ eats. Since there is nothing tweety eats, $W$ is not a model for this formula, and we are done with the following interpretation:

$$
W = \{\mathit{bird}(\mathit{tweety}), \mathit{dog}(\mathit{pluto}), \mathit{cat}(\mathit{pluto}), \mathit{eats}(\mathit{pluto}, \mathit{pluto})\}
$$

Note that your solution may look very different. Maybe you have three characters, one of which is a cat, one a dog, and the third a bird. Maybe you don't have characters that eat themselves. There are 
(infinitely) many possible solution to this problem!
</div></dd></div>

## Data Structures

Follow the lecture on data structures for propositional and predicate logic given by the instructor.

This concludes part 1.

## Inference

Follow the lecture on inference given by the instructor before you continue.

You have a robot with a knowledge base 

$$
B = \{ \mathit{tropical}(\mathit{CostaRica}), \mathit{tropical}(\mathit{Singapore}), \\\quad\mathit{subarctic}(\mathit{Canada}), \mathit{subarctic}(\mathit{Sweden}) \}
$$

The robot also knows two rules:

$$
\forall X: \mathit{tropical}(X) \rightarrow \mathit{hot}(X) \\\\

\forall X: \neg \mathit{hot}(X) \rightarrow \mathit{cold}(X)
$$

Answer the query: Is Canada cold? What is your proof?

<div style="margin:20px; margin-top:5px; margin-right:15px; border: 1px solid #3bbfe7;" class="codebox">
<dt style="height:40px; text-align: center;"><strong>Answer:</strong>
<input type="button" value="Show" style="width:78px; font-size:14px; margin:0px; padding:0px;" onclick="var spoiler = $(this).parents('.codebox').find('.content').toggle('slow');
if ( this.value == 'Hide' ) { this.value = 'Show'; } else { this.value = 'Hide'; };
return false;"></dt>
<dd><div class="content" name="spoiler" style="display: none; margin-right:15px;">
The answer to the query $\mathit{cold}(\mathit{Canada})$ is "yes" (or "true").<br/><br/>

The proof is:

$$
B, \forall X: \mathit{tropical}(X) \rightarrow \mathit{hot}(X) \models \\\quad \{ \mathit{hot}(\mathit{CostaRica}), \mathit{hot}(\mathit{Singapore})\} \\\\
B, \{ \mathit{hot}(\mathit{CostaRica}), \mathit{hot}(\mathit{Singapore})\}, \forall X: \neg \mathit{hot}(X) \rightarrow \mathit{cold}(X) \models \\\quad \{ \mathit{cold}(Canada), \mathit{cold}(Sweden) \}
$$

Note that this is an ad-hoc inference procedure that is *not* based on resolution. The challenge we face is that we need to generate **all** hot places before we can determine which are not hot, which we achieved by 
first applying the first rule and then applying the second rule.
</div></dd></div>

## Actions

Follow the lecture on logical actions given by the instructor before you continue.

## Transition Systems

Follow the lecture on transition systems given by the instructor before you continue.

Below you are given the state $s_0$ and the effects $e_1$, $e_2$, $e_3$ of three actions. 
Apply $e_1$ to $s_0$ and determine the resulting state $s_1$. Apply $e_2$ to $s_1$ and determine 
the resulting state $s_2$. Finally, apply $e_3$ to $s_2$ and determine a final state $s_3$.

$$
s_0 = \{ \mathit{at}(\mathit{Sherlock}, \mathit{BakerStreet}), \mathit{murderer}(\mathit{Moriarty}), \mathit{victim}(\mathit{ReginaldMusgrave}) \}\\
e_1 = \left(\forall x: \text{when}\:(\mathit{at}(\mathit{Sherlock}, x))\:(\neg \mathit{at}(\mathit{Sherlock}, x)) \right) \wedge \mathit{at}(\mathit{Sherlock}, \mathit{ScotlandYard})\\
e_2 = \left(\forall x: \text{when}\:(\mathit{victim}(x))\:(\mathit{knowsVictim}(\mathit{Sherlock}, x))\right) \wedge \\
      \left(\forall x: \text{when}\:(\mathit{murderer}(x))\:\mathit{knownsMurderer}(\mathit{Sherlock}, x)\right)\\
e_3 = \text{when}\:(\exists x: \mathit{murderer}(x) \wedge \mathit{knownsMurderer}(\mathit{Sherlock}, x))\:(\mathit{solvedCrime}(\mathit{Sherlock}))
$$

<div style="margin:20px; margin-top:5px; margin-right:15px; border: 1px solid #3bbfe7;" class="codebox">
<dt style="height:40px; text-align: center;"><strong>Answer:</strong>
<input type="button" value="Show" style="width:78px; font-size:14px; margin:0px; padding:0px;" onclick="var spoiler = $(this).parents('.codebox').find('.content').toggle('slow');
if ( this.value == 'Hide' ) { this.value = 'Show'; } else { this.value = 'Hide'; };
return false;"></dt>
<dd><div class="content" name="spoiler" style="display: none; margin-right:15px;">
The first effect basically states that whichever place sherlock is at, they are no longer there after the action and are instead at Scotland Yard, so the state will be:

$$
s_1 = \{ \mathit{at}(\mathit{Sherlock}, \mathit{ScotlandYard}), \\\quad\mathit{murderer}(\mathit{Moriarty}), \mathit{victim}(\mathit{ReginaldMusgrave}) \}
$$

The second effect causes Sherlock to determine the victim and the murderer: For each x, if the x is the victim, Sherlock will then know that they are the victim, and likewise for the murderer.

$$
s_2 = \{ \mathit{at}(\mathit{Sherlock}, \mathit{ScotlandYard}), \\\quad\mathit{murderer}(\mathit{Moriarty}), \mathit{victim}(\mathit{ReginaldMusgrave}),  \\\quad\mathit{knowsVictim}(\mathit{Sherlock},
\mathit{ReginaldMusgrave}), \\\quad\mathit{knowsMurderer}(\mathit{Sherlock}, \mathit{Moriarty}) \}
$$

Finally, effect 3 says when there is an x such that x is the murderer and Sherlock knows that they are the murderer, Sherlock has solved the crime.

$$
s_3 = \{ \mathit{at}(\mathit{Sherlock}, \mathit{ScotlandYard}), \\\quad\mathit{murderer}(\mathit{Moriarty}), \mathit{victim}(\mathit{ReginaldMusgrave}), \\\quad\mathit{knowsVictim}(\mathit{Sherlock}, 
         \mathit{ReginaldMusgrave}), \\\quad\mathit{knowsMurderer}(\mathit{Sherlock},  \mathit{Moriarty}), \mathit{solvedCrime}(\mathit{Sherlock}) \}
$$

</div></dd></div>



