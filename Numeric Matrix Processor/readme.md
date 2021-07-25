Description
In this stage, you should find the inverse of a matrix.

The inverse matrix A^{−1}A 
−1
  is the matrix whose product with the original matrix AA is equal to the identity matrix.

A \times A^{-1} = A^{-1} \times A = IA×A 
−1
 =A 
−1
 ×A=I

Watch a video about the inverse of a matrix to get the basic idea. To get a deeper understanding, check out the 3Blue1Brown channel.

The identity matrix is a matrix where all elements of the main diagonal are ones, and other elements are zeros. Here is an example of a 4, 44,4 identity matrix:


 

The inverse of a matrix can be found using this formula:

A^{-1} = \dfrac{1}{det(A)} \times C^TA 
−1
 = 
det(A)
1
​
 ×C 
T
 

As you can see, it contains a lot of operations you implemented in the previous stages: finding cofactors of all the elements of the matrix, transposition of the matrix, finding the determinant of a matrix, and multiplication of a matrix by a constant.

det(A)det(A) is the determinant of matrix AA, and C^TC 
T
  is the matrix consisting of cofactors of all elements of the matrix AA transposed along the main diagonal. The inverse matrix can’t be found if det(A)det(A) equals zero. You can look up a calculation example.

Objectives
In this stage, your program should support finding the inverse of a matrix. Refer to the example to see how it should be implemented.

Note that in some cases the inverse of a matrix does not exist. In such cases, your program should output a warning message.

Additional improvements
Although it's not required in this stage and we won't check, you can implement a method that prints a matrix in a readable way so that every column is correctly aligned and all elements are rounded to a fixed number of digits.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.
