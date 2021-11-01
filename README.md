# CSE107 - Lab 10

This lab plays manipulating content in files as well as writing 
to new files.

## Purpose

### markov.py

This program opens a file specified by the user and generates
a markov chain using the contents. It then generates a random 
sentense from the chain.

### piglatin.py

This program opens a file specified by the user and translates
the contents into pig latin. It then writes the translation to
a new file also specified by the user.

### navigate3.py

This program opens a file specified by the user and reads commands
from it. It then executes these commands as movements for a turtle.
It also implements cloning a turtle with "split"

## Conclusion

* In this lab I practiced opening files and manipulating the contents
to solve problems.
* Pair programming aided in giving me an outside look at my code
  and allowed me to ask questions and give help to my partner when
  it was needed.
* I did not work with my buddy on the lab.
* I had a problem with [navigate3.py](#navigate3py) where when the split command
was used, the program would get stuck in an infinite loop and continue to clone 
the turtles. This was caused by iterating through the turtle loop directly even
while elements in it were being cloned. I was able to fix this by using standard
for loop with a set amound of iterations.
* I think I could improve my code by getting my previous code to work with the 
better way of iterating through the turtles list. This could probably be done by 
making a copy of the list prior to iterating and iterating through the copy.