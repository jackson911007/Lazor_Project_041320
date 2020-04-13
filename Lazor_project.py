from itertools import combinations
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class Reader:
    # This class is used to read the .bff profile. It extracts useful
    # information such as the position of o, x, B, the number of flexible
    # A, B, C blocks, lazer position & directions and intersections.
    # I designed a dictionay to store all information neceesary for
    # algorithm.

    # **Parameters**
    # self : *str*
    # filename

    # **return**
    # a dictionary {} to store useful information

    def __init__(self, filename):
        self.filename = filename

    def reader(self):

        # This function opens the bff file, read it and store the informatin.
        # Use list to store all the positions

        self.filename
        grid_start = False
        y = 0
        stack = {"num_A_block": 0, "num_B_block": 0, "num_C_block": 0}
        o_list = []
        x_list = []
        A_list = []
        B_list = []
        C_list = []
        Lazor = []
        P_list = []
        with open(self.filename, 'r') as file:

            # Read the information line by line, delete the space
            # between the words
            # The length of line is coordination x and the width
            # of number of lines from GRID START to GRID STOP

            for line in file.readlines():
                line = line.strip()
                cells = line.split()
                if line == "GRID START":
                    grid_start = True

                elif line == "GRID STOP":
                    grid_start = False

    # Bellow GRID START append each information in list. Here, using
    # enumerate to label the index. That is, our x
    # Reference: https://www.geeksforgeeks.org/enumerate-in-python/

                elif grid_start:
                    # put index for each element
                    for x, cell in enumerate(cells):
                        if cell == 'o':
                            o_list.append([x, y])
                        if cell == 'x':
                            x_list.append([x, y])
                        if cell == 'A':
                            A_list.append([x, y])
                        if cell == 'B':
                            B_list.append([x, y])
                        if cell == 'C':
                            C_list.append([x, y])

                    y += 1

# We have transfer our coordination number because our coordination
# system for plotting starts from left bottom.

                else:
                    if line != "":
                        info = line.split()
                        if info[0] == "A":
                            stack.update({"num_A_block": int(info[1])})
                        if info[0] == "B":
                            stack.update({"num_B_block": int(info[1])})
                        if info[0] == "C":
                            stack.update({"num_C_block": int(info[1])})
                        if info[0] == "L":
                            Lazor.append(
                                [int(info[1]) / 2, (int(y) * 2 -
                                 int(info[2])) / 2, int(info[3]) / 2, -
                                 int(info[4]) / 2])
                        if info[0] == "P":
                            P_list.append(
                                [int(info[1]) / 2, (int(y) * 2 -
                                 int(info[2])) / 2])


# Transfer coordination number our plotting coordination system
        for i in o_list:
            i[1] = y - i[1] - 1
        for i in A_list:
            i[1] = y - i[1] - 1
        for i in B_list:
            i[1] = y - i[1] - 1
        for i in C_list:
            i[1] = y - i[1] - 1
        for i in x_list:
            i[1] = y - i[1] - 1

# Store data in the dictionary and pass them to other function
# Reference: https://www.programiz.com/python-programming/
# methods/dictionary/update

        stack.update({
            "Grid_size": [x + 1, y],
            "o_list": o_list,
            "x_list": x_list,
            "A_list": A_list,
            "B_list": B_list,
            "C_list": C_list,
            "Lazor": Lazor,
            "P_list": P_list
        })
        return stack


# Show the possible arrangement
def place_test(o_list, num_A_block, num_B_block, num_C_block, grid_size,
               l_list, p_list):

    # This function calculates all the possible arrangements. Listed
    # all the possibilites and use test_block function to find the
    # answer. If test_function is TRUE, it will return the answer
    # **Parameters**
    # o_list : *list*
    # filename
    # num_A_block : *int*
    # number of A block
    # num_B_block : *int*
    # number of B block
    # num_C_block : *int*
    # number of C block
    # **return**
    # block_info *list of list*
    # This shows the positions of A, B, C blocks' placement.
    # e.g. [[A, 3, 4][B, 2, 5][C, 2, 3]...]

    def combined_block_info(block_position, block_type):
        for i in block_position:
            block_info.extend([[block_type, i[0], i[1]]])
        return block_info

# This function is used to modify the data pass to test_block.
# (Formatting the result after calculation)

# **Parameters**
# block_position: *list of list*
# A, B, C coodination numbers
# block_type: *int*
# A, B, C

# **return**
# block_info *list of list*
# e.g. [[A, 3, 4][B, 2, 5][C, 2, 3]...]
# '''
    a_block_combination = list(combinations(o_list, num_A_block))
# Use combinations method in itertools. This can list all the
# possiblity picking number of A blocks in o_list without
# considering the sequence. Repeat this loop for A, B, C blocks.

# Important:
#     (1) Remove the elements in each list after each possibilty!
# Do not want collections
#     (2) Add back the remove compenets to o_list for next loop


# Reference: https://www.geeksforgeeks.org/itertools-combinations
# -module-python-print-possible-combinations/

    for i in a_block_combination:
        A_list = []
        A = list(i)
        A_list.extend(A)
        for j in A:
            o_list.remove(j)

        b_block_combination = list(combinations(o_list, num_B_block))
        for i in b_block_combination:
            B_list = []
            B = list(i)
            B_list.extend(B)
            for j in B:
                o_list.remove(j)

            c_block_combination = list(combinations(o_list, num_C_block))
            for i in c_block_combination:
                C_list = []
                C = list(i)
                C_list.extend(C)
                block_info = []

                combined_block_info(A_list, 'A')
                combined_block_info(B_list, 'B')
                combined_block_info(C_list, 'C')
                if test_block(grid_size, block_info, l_list, p_list):
                    return block_info

# Here, Delete all the number of elements added to A, B, C list
# Clean the lsit. Meanwhile add the deleted elements black to
# o_list

                if num_C_block > 0:
                    del C_list[-num_C_block:]
                elif num_C_block == 0:
                    pass

            if num_B_block > 0:
                del B_list[-num_B_block:]
            elif num_B_block == 0:
                pass
            o_list.extend(B)

        if num_A_block > 0:
            del A_list[-num_A_block:]
        elif num_A_block == 0:
            pass
        o_list.extend(A)
