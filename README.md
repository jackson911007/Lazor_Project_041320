# Lazor_Project_041320
Author: Tien Jung, Lee & Dung-Yi, Wu

How to use?

1. put the bff file's name in "filename", which is a t the main main function.

2. Reader class reader function will read the .bff profile. It extracts 
   useful information such as the position of o, x, B, the number of flexible
   A, B, C blocks, lazer position & directions and intersections. The
   infromation will store  a dictionay ready for the next function.

   Reference: https://www.programiz.com/python-programming/

3. The o_list, num_A_block, num_B_block, num_C_block, grid_size,
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
