# Deki Ottawa

# Table of Contents

1. [What does this solve?](#deki-project)
2. [How does this work?](#how-does-this-work)


## What does this solve?

During COVID myself and a good friend, Nathanael, were concerned about students in the Eritrean community falling behind academically due to lockdown restrictions. After discussion we came to start an initiative ([The Deki Ottawa Project](https://www.instagram.com/thedekiottawaproject/?hl=en)) where undergrads and young professionals would be paired with students in grades 7-12 to tutor them. As the project's tutor and student signees grew, approximating 35+ and 40+ respectively, optimally matching everyone became difficult. For every pair made we had to strenuously consider: subjects, days of availability, suitable times and more. This python program automates that labour using combinatorial optimization. 



## How Does This Work?

The solution is simple yet effective. Give each student a weighted compatibility score with each tutor. Then, try to find the combination of pairs that results in the greatest total score possible. This means that compability among tutors and students has been maximized. 

The graph from [Wikipedia](https://en.wikipedia.org/wiki/Hungarian_algorithm) below communicates the idea. Say a business wants to hire workers for cleaning and it lists the different workers prices for cleaning various objects. 


|       | Bathroom | Floors | Windows |
|-------|----------|--------|---------|
| Paul  | $2       | $3     | $3      |
| Dave  | $3       | $2     | $3      |
| Chris | $3       | $3     | $2      |


Seeing their prices, there is a set of (x, y) combinations that results in the smallest total cost possible. The minimum cost here is $6, achieved by Paul cleaning the bathroom, Dave sweeping the floors and Chris washing the windows.

My solution is the same idea. The difference is that tutors are on the x-axis and students are on the y-axis and that each matrix entry is actually a compatiblity score. Then from there, we're actually trying to **maximize** the final value which is **optimizing total student and tutor compatibility**.


