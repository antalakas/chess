A chess independence game in python
==============================================================================

##The problem

Find all unique configurations of a set of normal chess
pieces on a chess board with dimensions M×N where none of
the pieces is in a position to take any of the others.
Assume the colour of the piece does not matter, and that
there are no pawns among the pieces.

Write a program which takes as input:
The dimensions of the board: M, N
The number of pieces of each type (King, Queen, Bishop,
Rook and Knight) to try and place on the board.
As output, the program should list all the unique
configurations to the console for which all of the pieces
can be placed on the board without threatening each other.

##Solution path

The algorithm, keeps placing pieces on the board until there
is no longer a safe square, modelling the human reaction to
the problem. The order of placement will be computed based
on the number of unique combinations of input pieces.

If the last piece has been placed, the solution is noted. If
fewer pieces than the total number of pieces have been placed,
then this is a dead end.  In either case, backtracking occurs.
The last piece placed on the board gets pulled, then it gets
moved to the next safe square. Backtrack occurs even after a
"good" attempt in order to get to a new solution. Backtracking
may repeat itself several times until the original misplaced
piece finally is proven to be a dead end.

The "attack graph" for each piece is precomputed up front,
and then we essentially ignore the geometry of the problem.
The "attack graph" is presented as a bit board, a one
dimensional array transformation of the rectangular board
(according to the problem). Coordinate (0, 0) represents
the lower-left board square.

https://en.wikipedia.org/wiki/Mathematical_chess_problem
