# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Constraint propagation is the process of applying constraints or a set of rules while finding an optimal solution. Constraint satisfaction is important when finding an optimal solution because it keeps the search process in a check and make sure that the search agent adheres to the rules of a game. Sometimes constrains are implemented along with the search algorithm to effectively reduce the search space. 
Naked twin rule is one such constraint/rule that is applied while playing Sudoku to improve the search process. Naked twins are all the pairs of boxes/cells in a row or column or a 3x3 unit that have the exact same 2 digits in them. The constraint that needs to be applied when the agent comes across a pair of naked twins is as follows:  Assign the two digits to the pair of boxes i.e. one each and remove the two digits from all its peers (along the row or column or a 3x3 unit) as the digits have already been assigned to the pair of boxes. 


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: The Diagonal Sudoku is solved just like the normal Sudoku but now the search agent should also apply the constraints for the Diagonal cells, adding the diagonal constraint reduces the search space of the problem. The basic constraints applied for the diagonal Sudoku implemented in this assignment are
1.)	Elimination Rule: If a value is assigned to a particular box eliminate that value from all its peers.
2.)	Only Choice Rule: if a box can take only one value that box should be assigned with that value.
3.)	Naked Twins: The naked twins constraint described above can also be incorporated into solving the diagonal Sudoku.


### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the `assign_value` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login) for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

