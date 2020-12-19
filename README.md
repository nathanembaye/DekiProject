# Table of Contents

1. [What does this solve?](#deki-project)
2. [Why does this work?](#why-does-this-work)
3. [Care packages](#installation)
4. [Members](#members)


## Deki Project

During COVID myself and a good friend, Nathanael, were concerned about students in the community falling behind academically due to lockdown restrictions. We decided to start an initiative ([The Deki Ottawa Project](https://www.instagram.com/thedekiottawaproject/?hl=en)) where undergrads and young professionals would tutor grade 7-12 students to combat this. As the number of tutors and students signing up grew, reaching approximately 30+ and 45+, we found optimally pairing everyone to be difficult. For every person, we had to consider: subjects, days of availability, suitable times, etc. This python program solves just that using combinatorial optimization. 



### Why Does This Work?

The idea is very straight forward. Give each student a compatibility score with every tutor. Then, try to find the combination of pairs that results in the greatest total compatibility score possible.

The graph from [Wikipedia](https://en.wikipedia.org/wiki/Hungarian_algorithm) below communicates the idea. It illustrates different contractors prices for cleaning varying household objects. Seeing their scores, there is a x, y combination that results in the lowest cost possible.


|       | Bathroom | Floors | Windows |
|-------|----------|--------|---------|
| Paul  | $2       | $3     | $3      |
| Dave  | $3       | $2     | $3      |
| Chris | $3       | $3     | $2      |


The minimum cost is $6, achieved by having Paul cleaning the bathroom, Dave sweeping the floors, and Chris washing the windows.

My program is the same idea. The difference is that students are on the y axis, tutors are on the x axis, and that each matrix entry is actually a compatiblity score. From there, we are actually trying to **maximize the final value** which is **maximizing student and tutor compatibility**.



## Installation

Packages to install

```
pip install numpy
pip install script 
pip install pandas 
```

## Members
[Nathan Embaye](https://nathanembaye.me)

