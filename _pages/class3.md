---
title: "Virtual Class: Pathfinding"
layout: single
excerpt: "Virtual Class: Pathfinding"
sitemap: true
permalink: /classes/class3.html
frontpageorder: 4
categories: []
---

* TOC
{:toc}

## Introduction

Classes 3 and 4, which are about path finding, will be held in virtual form. This page guides you through the lecture, which consists of short videos, and some text containing tasks
for you to think about and/or discuss with other students. The idea is that you work through this page during normal class hours, and use the available online-channels, including the video conference call and slack, or 
any other medium that you find useful (like Skype, or WhatsApp) to communicate with your classmates and the instructor. However, you also have the option to work through the class content at another time, and send questions 
via email. Please indicate which section your question is about, to make it easier for me to respond effectively.
This page contains all materials for classes 3 **and** 4, because they form one logical unit. For each section, I will also indicate how long it should take you to work through it. The class is designed to be
held as two separate 2 hour lectures, as indicated below. The videos will use the slides for [lecture 3](/CI-0129/slides/lecture3.html) and [lecture 4](/CI-0129/slides/lecture4.html) from the website. 

## Trees ( + 10 minutes discussion)

First, watch this video: 

Think about, or discuss with a partner, how you would perform a search in this game tree, starting with the root node, until you have found a solution. Think about it from an algorithmic perspective, 
and how you write code to solve the problem.

## Tree Search ( + 15 minutes discussion)

Continue with this video:

Assuming the nodes are ordered from left to right in the tree below, how many nodes would you visit (add to the frontier) and expand (remove from the frontier to add all of its children to the frontier) when you 
search for a path from the root (1) to the node labeled 7, with Breadth-First Search? How about Depth-First Search? Discuss with a partner, or try to figure it out yourself, before checking your answer below.

<svg version="1.1"
    xmlns="http://www.w3.org/2000/svg" 
	xmlns:xlink="http://www.w3.org/1999/xlink"
	overflow="visible"
	viewBox="-10 -10 380 240"
	width="600" height="400"
	enable-background="new -10 -10 380 240" 
	>

<desc>Tree</desc>

<defs>
	<radialGradient id="radialGradient00">
      <stop style="stop-color:#c0d9ea;stop-opacity:1;" offset="70%"/>
      <stop style="stop-color:#7d7d7d;stop-opacity:1;" offset="100%"/>
    </radialGradient>

    <symbol id="node" >
        <circle cx="22" cy="22" r="20" style="fill:url(#radialGradient00)"/>
    </symbol>	

	
	<filter  id="GaussianBlur00" x="-0.2" width="1.3" y="-0.2" height="1.3">
		<feGaussianBlur  stdDeviation="3"></feGaussianBlur>
	</filter>
	
	<symbol id="gr1" >
		<g id="g01" style="stroke:#000000;stroke-width:2">
			<path d="M 200 20 L 20 200"/>
			<path d="M 200 20 L 320 140"/>	
			<path d="M 200 20 L 200 80"/>	
			<path d="M 260 80 L 260 140"/>
			<path d="M 140 80 L 140 140"/>	
			<path d="M 260 140 L 320 200"/>
			<path d="M 260 140 L 260 200"/>
			<path d="M 80 140 L 80 200"/>
		</g>
		<g id="g02">
			<use x="178" y="-1" xlink:href="#node"/>
			<use x="118" y="60" xlink:href="#node"/>
			<use x="178" y="60" xlink:href="#node"/>
			<use x="238" y="60" xlink:href="#node"/>	
			<use x="58" y="118" xlink:href="#node"/>
			<use x="118" y="118" xlink:href="#node"/>
			<use x="238" y="118" xlink:href="#node"/>
			<use x="298" y="118" xlink:href="#node"/>
			<use x="0" y="178" xlink:href="#node"/>
			<use x="58" y="178" xlink:href="#node"/>
			<use x="238" y="178" xlink:href="#node"/>
			<use x="298" y="178" xlink:href="#node"/>
		</g>
		<g id="g03" style="font-family:Calibri; font-size:25px; text-anchor:middle;" transform = "translate(1, -2)">
			<text x="200" y="32">1</text>
			<text x="139" y="93">2</text>
			<text x="200" y="93">3</text>
			<text x="259" y="93">4</text>
			<text x="79" y="150">5</text>
			<text x="139" y="150">6</text>
			<text x="259" y="150">7</text>
			<text x="319" y="150">8</text>
			<text x="22" y="210">9</text>
			<text x="79" y="210">10</text>
			<text x="259" y="210">11</text>
			<text x="319" y="210">12</text>
		</g>
    </symbol>
</defs>

<use x="1" y="1" xlink:href="#gr1" filter="url(#GaussianBlur00)" />
<use xlink:href="#gr1" />

</svg>

<div style="margin:20px; margin-top:5px; border: 1px solid #3bbfe7;" class="codebox">
<dt style="height:40px; text-align: center;"><strong>Answer:</strong>
<input type="button" value="Show" style="width:78px; font-size:10px; margin:0px; padding:0px;" onclick="var spoiler = $(this).parents('.codebox').find('.content').toggle('slow');
if ( this.value == 'Hide' ) { this.value = 'Show'; } else { this.value = 'Hide'; };
return false;"></dt>
<dd><div class="content" name="spoiler" style="display: none;">
Breadth-First Search will start with 1 in the frontier, then add 2, 3, 4, then add 5, 6, and then reach 7 and stop. The nodes we visited were therefore 1, 2, 3, 4, 5, 6, 7, and the nodes we expanded were 1, 2, 
3 (which has no children), and 4.

Depth-First Search will start with 1 in the frontier, then add 2, 3, 4, then add 5, 6, then add 9, 10, and finally add 7 and stop. We visited 1, 2, 3, 4, 5, 6, 9, 10, 7, and expanded 1, 2, 5, 9, 10, 6, 3, 4.
</div></dd></div>

## Uninformed Search in Graphs ( + 25 minutes discussion)

Continue with this video:


Look at the map of UCR campus below. Find a path from Chemistry (Quimica) to ECCI Anexo using Breadth-First Search. Which nodes do you visit and expand? How about Depth-First Search? (Assume that the neighbors are 
ordered starting north, and continuing clockwise. For example, the neighbors of Quimica are, in order, Educacion, Estudios Generales and Biologia (because Biologia is slightly to the left)

<img src="/CI-0129/assets/img/campo.png" width="100%"/>

<div style="margin:20px; margin-top:5px; border: 1px solid #3bbfe7;" class="codebox">
<dt style="height:40px; text-align: center;"><strong>Answer:</strong>
<input type="button" value="Show" style="width:78px; font-size:10px; margin:0px; padding:0px;" onclick="var spoiler = $(this).parents('.codebox').find('.content').toggle('slow');
if ( this.value == 'Hide' ) { this.value = 'Show'; } else { this.value = 'Hide'; };
return false;"></dt>
<dd><div class="content" name="spoiler" style="display: none;">
Breadth-First Search will start at Quimica, and add Educacion, Estudios Generales and Biologia. Then, we will add Instituto Confucio, Economicas, Farmacia. Then we will add Registro (neighbor of Instituto Confucio), Derecho, 
and ECCI Anexo and we are done. The resulting path is Quimica - Estudios Generales - Economicas - ECCI Anexo, with a total length of 80 + 55 + 35 = 170

Depth-First Search start at Quimica, and add Educacion, Estudios Generales and Biologia in reverse order, so that the top element of the stack is Educacion. Then we expand Educacion, and add Estudios Generales (note: 
we **only** avoid adding Quimica, because we have already expanded it, but we will add a node that we have already added, such as Estudios Generales, if we have **not** expanded it yet. In an actual implementation, 
you can either remove the other node from the stack right now, or ignore it later when it might be expanded a second time). Then we expand Estudios Generales, adding Instituto Confucio, and Economicas in reverse order. 
The top element of the stack is now Instituto Confucio, we expand that, and add Economicas and Registro. Then we expand Economicas, adding Derecho and ECCI Anexo. We have found a path Quimica - Educacion - Estudios Generales -
Instituo Confucio - Economicas - ECCI Anexo, with a total length of 35 + 60 + 100 + 70 + 35 = 300
</div></dd></div>

Is there a shorter path than the ones found by Breadth-First and Depth-First Search? Which one? Why did we not find it?

<div style="margin:20px; margin-top:5px; border: 1px solid #3bbfe7;" class="codebox">
<dt style="height:40px; text-align: center;"><strong>Answer:</strong>
<input type="button" value="Show" style="width:78px; font-size:10px; margin:0px; padding:0px;" onclick="var spoiler = $(this).parents('.codebox').find('.content').toggle('slow');
if ( this.value == 'Hide' ) { this.value = 'Show'; } else { this.value = 'Hide'; };
return false;"></dt>
<dd><div class="content" name="spoiler" style="display: none;">
The shorter path is Quimica - Biologia - Farmacia - RSN - ECCI - ECCI Anexo with a total length of 25 + 40 + 50 + 17 + 20 = 152. Breadth-First Search does not find it, because it has more edges than the path it found, 
even though each edge is short. Depth-First Search, on the other hand, searched in the completely wrong "direction", given our node ordering. 
</div></dd></div>

## Graphs (video)

Continue with this video:



This concludes the material for lecture 3. Continue below for lecture 4.

## Best-First Search ( + 15 minutes discussion)

In lecture 4, we are looking at how we can incorporate the distances/edge weights we have, and how we could use extra information we may have about a search problem. Continue with this video:

Recall the map of UCR campus (also shown below). Find a path from Chemistry (Quimica) to ECCI Anexo using Best-First Search. Which nodes do you visit and expand? 

<img src="/CI-0129/assets/img/campo.png" width="100%"/>

<div style="margin:20px; margin-top:5px; border: 1px solid #3bbfe7;" class="codebox">
<dt style="height:40px; text-align: center;"><strong>Answer:</strong>
<input type="button" value="Show" style="width:78px; font-size:10px; margin:0px; padding:0px;" onclick="var spoiler = $(this).parents('.codebox').find('.content').toggle('slow');
if ( this.value == 'Hide' ) { this.value = 'Show'; } else { this.value = 'Hide'; };
return false;"></dt>
<dd><div class="content" name="spoiler" style="display: none;">
Breadth-First Search will start at Quimica, and add Educacion, Estudios Generales and Biologia. Then, we will add Instituto Confucio, Economicas, Farmacia. Then we will add Registro (neighbor of Instituto Confucio), Derecho, 
and ECCI Anexo and we are done. The resulting path is Quimica - Estudios Generales - Economicas - ECCI Anexo, with a total length of 80 + 55 + 35 = 170

Depth-First Search start at Quimica, and add Educacion, Estudios Generales and Biologia in reverse order, so that the top element of the stack is Educacion. Then we expand Educacion, and add Estudios Generales (note: 
we **only** avoid adding Quimica, because we have already expanded it, but we will add a node that we have already added, such as Estudios Generales, if we have **not** expanded it yet. In an actual implementation, 
you can either remove the other node from the stack right now, or ignore it later when it might be expanded a second time). Then we expand Estudios Generales, adding Instituto Confucio, and Economicas in reverse order. 
The top element of the stack is now Instituto Confucio, we expand that, and add Economicas and Registro. Then we expand Economicas, adding Derecho and ECCI Anexo. We have found a path Quimica - Educacion - Estudios Generales -
Instituo Confucio - Economicas - ECCI Anexo, with a total length of 35 + 60 + 100 + 70 + 35 = 300
</div></dd></div>

Is there a shorter path than the ones found by Breadth-First and Depth-First Search? Which one? Why did we not find it?

<div style="margin:20px; margin-top:5px; border: 1px solid #3bbfe7;" class="codebox">
<dt style="height:40px; text-align: center;"><strong>Answer:</strong>
<input type="button" value="Show" style="width:78px; font-size:10px; margin:0px; padding:0px;" onclick="var spoiler = $(this).parents('.codebox').find('.content').toggle('slow');
if ( this.value == 'Hide' ) { this.value = 'Show'; } else { this.value = 'Hide'; };
return false;"></dt>
<dd><div class="content" name="spoiler" style="display: none;">
The shorter path is Quimica - Biologia - Farmacia - RSN - ECCI - ECCI Anexo with a total length of 25 + 40 + 50 + 17 + 20 = 152. Breadth-First Search does not find it, because it has more edges than the path it found, 
even though each edge is short. Depth-First Search, on the other hand, searched in the completely wrong "direction", given our node ordering. 
</div></dd></div>

## Heuristics (video)

Continue with this video:

## Greedy Search (video + 10 minutes discussion)

Continue with this video:

Look at the map of Austria (and Bavaria) given below. You want to find a path from Graz to Munich. From the map, you have calculated the straight-line distances from each city to Munich as follows:

Bregenz: 101, Bruck: 203, Eisenstadt: 400, Graz: 301, Innsbruck: 100, Klagenfurt: 202, Lienz: 201, Linz: 200, Munich: 0, Salzburg: 100, Vienna: 300

<img src="/CI-2700/assets/img/austriaroads.png" width="100%"/>

Find a path from Graz to Munich using Greedy Search. Which nodes do you visit? Which ones do you expand? How long is the resulting path?

<div style="margin:20px; margin-top:5px; border: 1px solid #3bbfe7;" class="codebox">
<dt style="height:40px; text-align: center;"><strong>Answer:</strong>
<input type="button" value="Show" style="width:78px; font-size:10px; margin:0px; padding:0px;" onclick="var spoiler = $(this).parents('.codebox').find('.content').toggle('slow');
if ( this.value == 'Hide' ) { this.value = 'Show'; } else { this.value = 'Hide'; };
return false;"></dt>
<dd><div class="content" name="spoiler" style="display: none;">
We start with the initial node, Graz (301) in the frontier, which we expand, adding Klagenfurt (202), Bruck (203), Vienna (300) and Eisenstadt (400). We then expand Klagenfurt, adding Lienz (201) to the frontier.
Lienz has the lowest heuristic value, so we expand it, adding Innsbruck (100) to the frontier. Innsbruck now has the lowest heuristic value, and we'll add Munich (0) (and Bregenz (101)), and we are done. The path we found 
is Graz - Klagenfurt - Lienz - Innsbruck - Munich, with a total length of 136 + 145 + 180 + 151 = 612. We have visited Graz, Klagenfurt, Bruck, Vienna, Eisenstadt, Lienz, Innsbruck and Munich (and Bregenz), and have 
expanded Graz, Klagenfurt, Lienz, and Innsbruck.
</div></dd></div>


## A* (video + 15 minutes discussion)

Continue with this video:

Using the same map and heuristic information, find a path from Graz to Munich using A*. 
Which nodes do you visit? Which ones do you expand? How long is the resulting path?

<img src="/CI-2700/assets/img/austriaroads.png" width="100%"/>

Bregenz: 101, Bruck: 203, Eisenstadt: 400, Graz: 301, Innsbruck: 100, Klagenfurt: 202, Lienz: 201, Linz: 200, Munich: 0, Salzburg: 100, Vienna: 300

<div style="margin:20px; margin-top:5px; border: 1px solid #3bbfe7;" class="codebox">
<dt style="height:40px; text-align: center;"><strong>Answer:</strong>
<input type="button" value="Show" style="width:78px; font-size:10px; margin:0px; padding:0px;" onclick="var spoiler = $(this).parents('.codebox').find('.content').toggle('slow');
if ( this.value == 'Hide' ) { this.value = 'Show'; } else { this.value = 'Hide'; };
return false;"></dt>
<dd><div class="content" name="spoiler" style="display: none;">
We start with the initial node, Graz (0 + 301 = 301) in the frontier, which we expand, adding Bruck (55 + 203 = 258), Klagenfurt (136 + 202 = 338), Vienna (200 + 300 = 500) and Eisenstadt (173 + 400 = 573). We then expand 
Bruck, adding Salzburg (55 + 215 + 100 = 370), and Linz (55 + 195 + 200 = 450) to the frontier. <b>Important:</b> We also have to check if Klagenfurt has a lower cost if we go via Bruck. Currently, Klagenfurt is in our 
frontier with a cost of 136. Via Bruck the cost would be 55 + 152 = 207, which is more, so we do not change the value (and ancestor) of Klagenfurt in our list. If we had found a lower cost way we would have to update 
the frontier entry!

Continuing, the lowest sum of heuristic and cost is now the one of Klagenfurt (338), so we expand this node, adding Lienz (136 + 145 + 201 = 482). Here we also have to check if we need to update Salzburg in the frontier, 
which has a cost of 136 + 223 = 359 to reach via Klagenfurt, which is more than we already have and is thus not changed. Next, the lowest sum of heuristic and cost is held by Salzburg (370), which we expand, 
adding Munich (55 + 215 + 145 + 0 = 415), and we also check if we need to update Linz (we do not). <b>Also important:</b> Just because we have reached Munich does not automatically mean that we are done.
Our search frontier currently has Munich (415), Linz (450), Lienz (482), Vienna (500), and Eisenstadt (573). Because Munich has the lowest value in this list, we are indeed done, but if it didn't, we would have to continue 
until Munich has the lowest value.
</div></dd></div>

## Lab 1: Introduction (video)

Finally, watch this video:


Next week (Monday, 23/3), you will start with [lab 1](/labs/lab1.html), in which you will implement Breadth-First Search, Depth-First Search, Greedy Search and A*.
