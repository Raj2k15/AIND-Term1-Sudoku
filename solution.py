from collections import Counter
assignments = []


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    for unit in unitlist:
        print (unit)
        #identyfing duplicates for all the two digit boxes
        nk=[k for k,v in Counter(values[u] for u in unit if len(values[u])==2).items() if v>1]
        #identifying the cells which have duplicates
        nkd=[u for u in unit for j in nk if set(values[u])==set(j) ]
        #removing twins from the peers
        not_twins=set(unit)-set(nkd)
        #replacing the digits in naked twins from its peers with 
        for box in nkd:
                for d in values[box]:
                    for n in not_twins:
                        if len(values[n])>1:
                            assign_value(values,n,values[n].replace(d,'')) 
    return values

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

rows = 'ABCDEFGHI'
cols = '123456789'
#all possible boxes
boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
#Diagnol cells in sudoku
unit1= [(j+str(i+1)) for i, j in enumerate(rows)]
unit2=[(j+str(len(rows)-i)) for i, j in enumerate(rows) ]
diag_unit=[unit1,unit2]
unitlist = row_units + column_units + square_units + diag_unit
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
    

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
    
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    whole_list={}
    for cell,val in zip(cross(rows,cols),grid):
        #print (cell,val)
        #assigning values from the grid to the dictionary
        whole_list[cell]=val
    dic=whole_list
    #if the input grid does not have any value replace it with '123456789'
    for key in dic.keys():
        if dic[key]=='.':
            dic.update({key:'123456789'})
    return(dic)

    

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    #check for boxes which already have a single solved value
    already_solved = [box for box in values.keys() if len(values[box]) == 1]
    for box in already_solved:
        #getting the solved value for that box
        digit = values[box]
        #loop throug all the peers of the solved box.
        for peer in peers[box]:
            #replace the solved values of the box with empty string in all the peer boxes.
            values[peer] = values[peer].replace(digit,'')
    return values
    

def only_choice(values):
    #loop through all the boxes and assign a purticular box with the values if the values is the only choice for that box.    
    for unit in unitlist:
        #looping through each digits from 1 to 10 and identyfing all the boxes which match the digit
        for digit in range(1,10):
            dplaces = [box for box in unit if str(digit) in values[box]]
            #all the boxes in the dictionary with only one possible value that can be assigned to it
            if len(dplaces) == 1:
                #assigning the digit to the box with only one possible value
                values[dplaces[0]] = str(digit)
    return values  

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a solved value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        #  Using the Eliminate function
        values=eliminate(values)

        # using the only_choice function
        values=only_choice(values)

        # Check how many boxes have a solved value after the functions are applied
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values
    
def search(values):
    #using reduce_puzzle func to solve the sudoku
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with minimum possibilities other than 1
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) != 1)
    #print(n,s)
    
    # Now use constraint propogation to solve each one of the resulting sudokus from the possibilites 
    for value in values[s]:
        #print(value)
        new_sudoku = values.copy()
        #print(new_sudoku)
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            #print(attempt)
            return attempt


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values=grid_values(grid)
    solved_sudoku=search(values)
    return(solved_sudoku)
    
if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
