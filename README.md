# Table of Contents

1. [What does this solve?](#deki-project)
2. [How does this work?](#how-does-this-work)
3. [Care packages](#installation)
4. [Members](#members)


## Deki Project

During COVID myself and a good friend, Nathanael, were concerned about students in the community falling behind academically due to lockdown restrictions. We decided to start an initiative ([The Deki Ottawa Project](https://www.instagram.com/thedekiottawaproject/?hl=en)) where undergrads and young professionals would be paired with students in grade 7-12 for tutoring. As the number of tutors and students signees grew, reaching approximately 30+ and 45+ respectively, optimally pairing everyone became difficult. For every individual, we had to consider: subjects, days of availability, suitable times, etc. This python program solves that issue using combinatorial optimization. 



## How Does This Work?

The solution is simple but effective. Give each student a compatibility score with each tutor. Then, try to find the combination of pairs that results in the greatest total score possible. This means that compability among tutors and students has been maximized. 

The graph from [Wikipedia](https://en.wikipedia.org/wiki/Hungarian_algorithm) below communicates the idea. A business wants to hire workers for cleaning. It lists the different workers prices for cleaning various objects. Seeing their prices, there is a (x, y) combination that results in the smallest financial cost possible.


|       | Bathroom | Floors | Windows |
|-------|----------|--------|---------|
| Paul  | $2       | $3     | $3      |
| Dave  | $3       | $2     | $3      |
| Chris | $3       | $3     | $2      |


The minimum cost is $6, achieved by having Paul cleaning the bathroom, Dave sweeping the floors, and Chris washing the windows.

My program is the same idea. The difference is that tutors are on the x axis and students are on the y axis, and that each matrix entry is actually a compatiblity score. Then from there, we are actually trying to **maximize the final value** which is **maximizing total student and tutor compatibility**.



## Installation

What to install

```
pip install numpy
pip install script 
pip install pandas 
```

## Members
[Nathan Embaye](https://nathanembaye.me)

