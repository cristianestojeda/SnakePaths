# Snake’s paths Project:
In this project, the main objective is to find all distinct valid paths a Snake can make in a rectangular board of n x m cells. The Snake consists of one or more cells that are positioned consecutively either horizontally or vertically. The Snake is composed of a vector of coordinates, where the first one is the head, the rest corresponds with the body and the last one with the tail. There are certain restrictions in this task: the snake cannot move outside of the board and cannot make self-intersections. I solved this project using Python.

## Algorithms and data structures
This project involves the use of algorithms and data structures. In this case, I used the following methods and techniques: 
* Tree structure: each path in the tree corresponds to a path the snake could take, I cut branches that are impossible to take due to movements out of the board and movements that self-intersects with any Snake’s body part. With that, the valid paths search is optimized.
* Recursion: the recursion allows me to go through the tree structure, finding all the valid possibilities and cutting branches that cannot be taken.
* Modularity: isolated methods allowed me to define project’s constraints, snake movements, recursion and tests. This allows the code to be easier to understand and to be improved.

## Method description and constraints
The main method is number_of_available_different_paths() and outputs an integer corresponding to the number of distinct valid paths of length p that the snake can make. It has the following inputs:
* Board: Array describing the dimensions of the board. Board[0] corresponds to number of rows and Board[1] to the number of columns. Board length must be 2 and each board axis must be higher or equal to 1 and lower or equal to 10.
* Snake: Array that describes the configuration of the snake’s body on the board. It’s an array of coordinates. The first one is the head, the rest correspond to the body and the last one with the tail. All of them must be connected either horizontally or vertically. The Snake’s length must be higher or equal to 3 and lower or equal to 7. There must be only two coordinate axes for each position and the Snake must be inside the board.
* Depth: Paths depth, also related with the tree structure depth. Must be higher or equal to 1 and lower or equal to 20.
