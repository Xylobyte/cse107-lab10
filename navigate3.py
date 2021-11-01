"""
A program that opens a file and reads commands from it. A turtle follows the commands.

file: navigate3.py

author: Donovan Griego

Date: 11-01-2021

assignment: Lab 10
"""
import turtle
import os


def main():
    # Open a file
    file = input("Enter a file name: ")
    turtles = []
    if not os.path.exists(file):
        print("Error: File", file, "does not exist")
        exit(1)
    with open(file, 'r') as f:
        lines = f.readlines()
    queue = ["start"]
    for line in lines:
        queue += line.split()
    window = turtle.Screen()
    turtles.append(turtle.Turtle())
    turtles[0].speed(5)
    i = 0
    print("Running...")
    # goes through queue and runs the stored commands until "stop" is read
    while i < len(queue):
        if queue[i] == "start":
            for t in turtles:
                t.pendown()
            i += 1
        elif queue[i] == "forward":
            for t in turtles:
                t.forward(float(queue[i + 1]))
            i += 2
        elif queue[i] == "right":
            for t in turtles:
                t.right(float(queue[i + 1]))
            i += 2
        elif queue[i] == "left":
            for t in turtles:
                t.left(float(queue[i + 1]))
            i += 2
        # For each turtle clone it and move it to the right by the amount in the queue
        elif queue[i] == "split":
            for j in range(len(turtles)):
                t2 = turtles[j].clone()
                t2.right(float(queue[i + 1]))
                turtles.append(t2)
            i += 2
        else:
            print("Invalid commad '{}'; ignoring".format(queue[i]))
            i += 1
    print("Done.")
    window.mainloop()
    exit(0)

if __name__ == "__main__":
    main()
