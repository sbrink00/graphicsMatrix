from display import *
from draw import *
from matrix import *
import math

screen = new_screen()
color = [ 255, 255, 255 ]
matrix = new_matrix()
#print(print_matrix(matrix))
#250 lines

#test cases
m1 = new_matrix()
print("New Matris: ")
print(print_matrix(m1))
print("")
print("Adding edge: ")
add_edge(m1, 1, 1, 0, 2, 2, 0)
print(print_matrix(m1))
print("")
print("Adding two points: ")
add_point(m1, 3, 3, 0)
add_point(m1, 4, 4, 0)
print(print_matrix(m1))
print("")
print("Turning square matrix into identity matrix: ")
print("Original matrix: ")
ary = []
for i in range(7):
  ary.append([7] * 7)
print("note that print matrix doesn't work because of the difference between transformation matrices and edge matrices")
print(ary)
ident(ary)
print("Identity matrix: ")
print(ary)
transform = [[3, 0, 0, 0], [0, 3, 0, 0], [0, 0, 3, 0], [0, 0, 0, 3]]
print("")
print("Testing matrix multiplication. Should multiply everything by 3")
print(matrix_mult(transform, m1))
print(print_matrix(m1))
print("success")
print("")
print("Image file name: output.png")

x = 0
for i in range(250):
  if i <= 125: degree = i
  else: degree = 250 - i
  degree = degree % 90
  sin = math.sin(math.radians(degree))
  height = YRES * sin
  add_edge(matrix, x, 0, 0, x, height, 0)
  add_edge(matrix, x + 1, 0, 0, x + 1, height, 0)
  x += 4

draw_lines( matrix, screen, color )
save_ppm_ascii(screen, "output.ppm")
#display(screen)
