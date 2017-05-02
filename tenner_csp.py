#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete the warehouse domain.  

'''
Construct and return Tenner Grid CSP models.
'''

from cspbase import *
import itertools

def tenner_csp_model_1(initial_tenner_board):
    '''Return a CSP object representing a Tenner Grid CSP problem along 
       with an array of variables for the problem. That is return

       tenner_csp, variable_array

       where tenner_csp is a csp representing tenner grid using model_1
       and variable_array is a list of lists

       [ [  ]
         [  ]
         .
         .
         .
         [  ] ]

       such that variable_array[i][j] is the Variable (object) that
       you built to represent the value to be placed in cell i,j of
       the Tenner Grid (only including the first n rows, indexed from 
       (0,0) to (n,9)) where n can be 3 to 8.
       
       
       The input board is specified as a pair (n_grid, last_row). 
       The first element in the pair is a list of n length-10 lists.
       Each of the n lists represents a row of the grid. 
       If a -1 is in the list it represents an empty cell. 
       Otherwise if a number between 0--9 is in the list then this represents a 
       pre-set board position. E.g., the board
    
       ---------------------  
       |6| |1|5|7| | | |3| |
       | |9|7| | |2|1| | | |
       | | | | | |0| | | |1|
       | |9| |0|7| |3|5|4| |
       |6| | |5| |0| | | | |
       ---------------------
       would be represented by the list of lists
       
       [[6, -1, 1, 5, 7, -1, -1, -1, 3, -1],
        [-1, 9, 7, -1, -1, 2, 1, -1, -1, -1],
        [-1, -1, -1, -1, -1, 0, -1, -1, -1, 1],
        [-1, 9, -1, 0, 7, -1, 3, 5, 4, -1],
        [6, -1, -1, 5, -1, 0, -1, -1, -1,-1]]
       
       
       This routine returns model_1 which consists of a variable for
       each cell of the board, with domain equal to {0-9} if the board
       has a -1 at that position, and domain equal {i} if the board has
       a fixed number i at that cell.
       
       model_1 contains BINARY CONSTRAINTS OF NOT-EQUAL between
       all relevant variables (e.g., all pairs of variables in the
       same row, etc.).
       model_1 also constains n-nary constraints of sum constraints for each 
       column.
    '''
    
    var_array = []
    row_num = 1
    for row in initial_tenner_board[0]:
        var_row = []
        col_num = 1
        for item in row:
            if item == -1:
                var = Variable('V' + str(row_num) + ',' + str(col_num),[0,1,2,3,4,5,6,7,8,9])
            else:
                var = Variable('V' + str(row_num) + ',' + str(col_num),[item])
            var_row.append(var)
            col_num += 1
        var_array.append(var_row)
        row_num += 1
    var_list = []
    for i in range(0,len(var_array)):
        var_list += var_array[i]
    csp = CSP('model_1',var_list)
    for i in range(0,len(var_array)):
        for j in range(0, 9):
            c = Constraint(str((i+1,j+1))+'->'+str((i+1,j+2)),[var_array[i][j],var_array[i][j+1]])
            tuple_list = []
            for val1 in var_array[i][j].dom:
                for val2 in var_array[i][j+1].dom:
                   if val1 != val2:
                       tuple_list.append((val1,val2))
            c.add_satisfying_tuples(tuple_list)
            csp.add_constraint(c)
    for i in range(0,len(var_array)):
        for j in range(0, 8):
            c = Constraint(str((i+1,j+1))+'->'+str((i+1,j+3)),[var_array[i][j],var_array[i][j+2]])
            tuple_list = []
            for val1 in var_array[i][j].dom:
                for val2 in var_array[i][j+2].dom:
                   if val1 != val2:
                       tuple_list.append((val1,val2))
            c.add_satisfying_tuples(tuple_list)
            csp.add_constraint(c)
    for i in range(0,len(var_array)):
        for j in range(0, 7):
            c = Constraint(str((i+1,j+1))+'->'+str((i+1,j+4)),[var_array[i][j],var_array[i][j+3]])
            tuple_list = []
            for val1 in var_array[i][j].dom:
                for val2 in var_array[i][j+3].dom:
                   if val1 != val2:
                       tuple_list.append((val1,val2))
            c.add_satisfying_tuples(tuple_list)
            csp.add_constraint(c)
    for i in range(0,len(var_array)):
        for j in range(0, 6):
            c = Constraint(str((i+1,j+1))+'->'+str((i+1,j+5)),[var_array[i][j],var_array[i][j+4]])
            tuple_list = []
            for val1 in var_array[i][j].dom:
                for val2 in var_array[i][j+4].dom:
                   if val1 != val2:
                       tuple_list.append((val1,val2))
            c.add_satisfying_tuples(tuple_list)
            csp.add_constraint(c)
    for i in range(0,len(var_array)):
        for j in range(0, 5):
            c = Constraint(str((i+1,j+1))+'->'+str((i+1,j+6)),[var_array[i][j],var_array[i][j+5]])
            tuple_list = []
            for val1 in var_array[i][j].dom:
                for val2 in var_array[i][j+5].dom:
                   if val1 != val2:
                       tuple_list.append((val1,val2))
            c.add_satisfying_tuples(tuple_list)
            csp.add_constraint(c)
    for i in range(0,len(var_array)):
        for j in range(0, 4):
            c = Constraint(str((i+1,j+1))+'->'+str((i+1,j+7)),[var_array[i][j],var_array[i][j+6]])
            tuple_list = []
            for val1 in var_array[i][j].dom:
                for val2 in var_array[i][j+6].dom:
                   if val1 != val2:
                       tuple_list.append((val1,val2))
            c.add_satisfying_tuples(tuple_list)
            csp.add_constraint(c)
    for i in range(0,len(var_array)):
        for j in range(0, 3):
            c = Constraint(str((i+1,j+1))+'->'+str((i+1,j+8)),[var_array[i][j],var_array[i][j+7]])
            tuple_list = []
            for val1 in var_array[i][j].dom:
                for val2 in var_array[i][j+7].dom:
                   if val1 != val2:
                       tuple_list.append((val1,val2))
            c.add_satisfying_tuples(tuple_list)
            csp.add_constraint(c)
    for i in range(0,len(var_array)):
        for j in range(0, 2):
            c = Constraint(str((i+1,j+1))+'->'+str((i+1,j+9)),[var_array[i][j],var_array[i][j+8]])
            tuple_list = []
            for val1 in var_array[i][j].dom:
                for val2 in var_array[i][j+8].dom:
                   if val1 != val2:
                       tuple_list.append((val1,val2))
            c.add_satisfying_tuples(tuple_list)
            csp.add_constraint(c)
    for i in range(0,len(var_array)):
        for j in range(0, 1):
            c = Constraint(str((i+1,j+1))+'->'+str((i+1,j+10)),[var_array[i][j],var_array[i][j+9]])
            tuple_list = []
            for val1 in var_array[i][j].dom:
                for val2 in var_array[i][j+9].dom:
                   if val1 != val2:
                       tuple_list.append((val1,val2))
            c.add_satisfying_tuples(tuple_list)
            csp.add_constraint(c)
    for i in range(0,len(var_array)-1):
        for j in range(0, 10):
            c = Constraint(str((i+1,j+1))+'->'+str((i+2,j+1)),[var_array[i][j],var_array[i+1][j]])
            tuple_list = []
            for val1 in var_array[i][j].dom:
                for val2 in var_array[i+1][j].dom:
                   if val1 != val2:
                       tuple_list.append((val1,val2))
            c.add_satisfying_tuples(tuple_list)
            csp.add_constraint(c)
    for i in range(0,len(var_array)-1):
        for j in range(0, 9):
            c = Constraint(str((i+1,j+1))+'->'+str((i+2,j+2)),[var_array[i][j],var_array[i+1][j+1]])
            tuple_list = []
            for val1 in var_array[i][j].dom:
                for val2 in var_array[i+1][j+1].dom:
                   if val1 != val2:
                       tuple_list.append((val1,val2))
            c.add_satisfying_tuples(tuple_list)
            csp.add_constraint(c)
    for i in range(1,len(var_array)):
        for j in range(0, 9):
            c = Constraint(str((i+1,j+1))+'->'+str((i,j+2)),[var_array[i][j],var_array[i-1][j+1]])
            tuple_list = []
            for val1 in var_array[i][j].dom:
                for val2 in var_array[i-1][j+1].dom:
                   if val1 != val2:
                       tuple_list.append((val1,val2))
            c.add_satisfying_tuples(tuple_list)
            csp.add_constraint(c)
    array_col = []
    for j in range(0,10):
        list_col = []
        for i in range(0,len(var_array)):
            list_col.append(var_array[i][j])
        array_col.append(list_col)
    for j in range(0,10):
        c = Constraint('col'+str(j),array_col[j])
        col_sum = initial_tenner_board[1][j]
        ite_list = []
        for i in range(0,len(var_array)):
            ite_list.append(var_array[i][j].dom)
        final_tuple = []
        for element in itertools.product(*ite_list):
            if sum(element) == col_sum:
                final_tuple.append(element)
        c.add_satisfying_tuples(final_tuple)
        csp.add_constraint(c)
    return csp,var_array            
            

def tenner_csp_model_2(initial_tenner_board):
    '''Return a CSP object representing a Tenner Grid CSP problem along 
       with an array of variables for the problem. That is return

       tenner_csp, variable_array

       where tenner_csp is a csp representing tenner using model_1
       and variable_array is a list of lists

       [ [  ]
         [  ]
         .
         .
         .
         [  ] ]

       such that variable_array[i][j] is the Variable (object) that
       you built to represent the value to be placed in cell i,j of
       the Tenner Grid (only including the first n rows, indexed from 
       (0,0) to (n,9)) where n can be 3 to 8.

       The input board takes the same input format (a list of n length-10 lists
       specifying the board as tenner_csp_model_1.
    
       The variables of model_2 are the same as for model_1: a variable
       for each cell of the board, with domain equal to {0-9} if the
       board has a -1 at that position, and domain equal {i} if the board
       has a fixed number i at that cell.

       However, model_2 has different constraints. In particular,
       model_2 has a combination of n-nary 
       all-different constraints and binary not-equal constraints: all-different 
       constraints for the variables in each row, binary constraints for  
       contiguous cells (including diagonally contiguous cells), and n-nary sum 
       constraints for each column. 
       Each n-ary all-different constraint has more than two variables (some of 
       these variables will have a single value in their domain). 
       model_2 should create these all-different constraints between the relevant 
       variables.
    '''

    var_array = []
    row_num = 1
    for row in initial_tenner_board[0]:
        var_row = []
        col_num = 1
        for item in row:
            if item == -1:
                var = Variable('V' + str(row_num) + ',' + str(col_num),[0,1,2,3,4,5,6,7,8,9])
            else:
                var = Variable('V' + str(row_num) + ',' + str(col_num),[item])
            var_row.append(var)
            col_num += 1
        var_array.append(var_row)
        row_num += 1
    var_list = []
    for i in range(0,len(var_array)):
        var_list += var_array[i]
    csp = CSP('model_2',var_list)

    for i in range(0,len(var_array)-1):
        for j in range(0, 10):
            c = Constraint(str((i+1,j+1))+'->'+str((i+2,j+1)),[var_array[i][j],var_array[i+1][j]])
            tuple_list = []
            for val1 in var_array[i][j].dom:
                for val2 in var_array[i+1][j].dom:
                   if val1 != val2:
                       tuple_list.append((val1,val2))
            c.add_satisfying_tuples(tuple_list)
            csp.add_constraint(c)
    for i in range(0,len(var_array)-1):
        for j in range(0, 9):
            c = Constraint(str((i+1,j+1))+'->'+str((i+2,j+2)),[var_array[i][j],var_array[i+1][j+1]])
            tuple_list = []
            for val1 in var_array[i][j].dom:
                for val2 in var_array[i+1][j+1].dom:
                   if val1 != val2:
                       tuple_list.append((val1,val2))
            c.add_satisfying_tuples(tuple_list)
            csp.add_constraint(c)
    for i in range(1,len(var_array)):
        for j in range(0, 9):
            c = Constraint(str((i+1,j+1))+'->'+str((i,j+2)),[var_array[i][j],var_array[i-1][j+1]])
            tuple_list = []
            for val1 in var_array[i][j].dom:
                for val2 in var_array[i-1][j+1].dom:
                   if val1 != val2:
                       tuple_list.append((val1,val2))
            c.add_satisfying_tuples(tuple_list)
            csp.add_constraint(c)
    array_col = []
    for j in range(0,10):
        list_col = []
        for i in range(0,len(var_array)):
            list_col.append(var_array[i][j])
        array_col.append(list_col)
    for j in range(0,10):
        c = Constraint('col'+str(j),array_col[j])
        col_sum = initial_tenner_board[1][j]
        ite_list = []
        for i in range(0,len(var_array)):
            ite_list.append(var_array[i][j].dom)
        tuple_list = []
        for ele in itertools.product(*ite_list):
            tuple_list.append(ele)
        final_tuple = []
        for element in tuple_list:
            if sum(element) == col_sum:
                final_tuple.append(element)
        c.add_satisfying_tuples(final_tuple)
        csp.add_constraint(c)
    
    for i in range(0,len(var_array)):
        c = Constraint('row'+str(i),var_array[i])
        ite_list = []
        illegal_list = []
        for j in range(0,10):
            ite_list.append(var_array[i][j].dom)
            if var_array[i][j].cur_domain_size == 1:
                illegal_list.append(var_array[i][j].dom[0])
        new_ite_list = []
        for ele in ite_list:
            if len(ele) != 1:
                new_ele = []
                for item in ele:
                    if item not in illegal_list:
                        new_ele.append(item)
                new_ite_list.append(new_ele)
            else:
                new_ite_list.append(ele)
        final_tuple = []
        for element in itertools.product(*new_ite_list):
            if len(element) == len(set(element)):
                final_tuple.append(element)
        c.add_satisfying_tuples(final_tuple)
        csp.add_constraint(c)

    return csp,var_array

