"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    s1 = ""
    s2 = ""
    s3 = ""
    s4 = ""
    for i in range(len(matrix)):
      s1 += str(matrix[i][0]) + " "
      s2 += str(matrix[i][1]) + " "
      s3 += str(matrix[i][2]) + " "
      s4 += str(matrix[i][3]) + " "
    s1 = s1[:-1] + "\n"
    s2 = s2[:-1] + "\n"
    s3 = s3[:-1] + "\n"
    s4 = s4[:-1]
    return s1 + s2 + s3 + s4


#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident(matrix):
  length = len(matrix)
  for i in range(length):
    for x in range(length):
      if i != x: matrix[i][x] = 0
      else: matrix[i][x] = 1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2

#I was unsure of the format for the multiplication
#because the edge matrices are formatted where the
#number of rows in the array is actually the number
#of columns in the matrix it is representing.

#because m1 is usually going to be the transformation
#matrix, I figured that it would be formatted like a
#normal array, without the need to account for this by
#flipping the array.
def matrix_mult( m1, m2 ):
  for i in range(len(m2)):
    temp = [0, 0, 0, 0]
    temp[0] = (m1[0][0] * m2[i][0]) + (m1[0][1] * m2[i][1]) + (m1[0][2] * m2[i][2]) + (m1[0][3] * m2[i][3])
    temp[1] = (m1[1][0] * m2[i][0]) + (m1[1][1] * m2[i][1]) + (m1[1][2] * m2[i][2]) + (m1[1][3] * m2[i][3])
    temp[2] = (m1[2][0] * m2[i][0]) + (m1[2][1] * m2[i][1]) + (m1[2][2] * m2[i][2]) + (m1[2][3] * m2[i][3])
    temp[3] = (m1[3][0] * m2[i][0]) + (m1[3][1] * m2[i][1]) + (m1[3][2] * m2[i][2]) + (m1[3][3] * m2[i][3])
    m2[i] = temp

# m1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# ident(m1)
# m2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
# print(print_matrix(m2))
# print("")
# matrix_mult(m1, m2)
# print(print_matrix(m2))

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
