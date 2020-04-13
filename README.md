# Lazor_Project_041320
Author: Tien Jung, Lee & Dung-Yi, Wu

1. How to use?

   Put the bff file's name in "filename", which is at the main main function.

2. Principles:

   1. Reader class reader function will read the .bff profile. It extracts 
      useful information such as the position of o, x, B, the number of flexible
      A, B, C blocks, lazer position & directions and intersections. The
      infromation will store in a dictionay for the next operation.

      Reference: https://www.programiz.com/python-programming/

   2. The o_list, num_A_block, num_B_block, num_C_block, grid_size,
      l_list, p_list in formation are passed to place_test function.
      This function allow us to show all the arrangements of placing
      , A, B, C blocks. This function returns all position on A, B, C
      for each arrangement. Then, each result is paased to test_block
      to do calculation by trial and error. Once it finds the result in
      this test_block function it will return and stop the loop.
      The method used here is combinations in itertools. for example,
      "combinations(o_list, num_A_block)"" is pick number of A blocks(given by
      .bff) frpm o positions (given by .bff). Then, it will show all the possible
      arrangements by list of tuple of list.

      Reference: https://www.geeksforgeeks.org/itertools-combinations
   
   3. We test the placement from the place_test by test_block function. Once the 
      new arrangement of the blocks are assigned, the test_block is operated. We 
      store the coordinates needed to pass by in a list. The lazor path is also 
      recorded real time. Whenever the lazer path go through the must-pass coordinates
      , we eliminates them one by one from the list. The function keep working 
      Until the list is empty.
   
   4. We use matplotlib to output the images of the solution. The default function 
      for drawing the rectangle is used. The left-bottom point of the rectangle  
      is set as the starting point. The length and the width can be set by adding 
      the parameter, which stretch forward +x and +y direction. The type of blocks 
      are specified by applying diffenrent color. The block where cannot be place 
      is set as black. 