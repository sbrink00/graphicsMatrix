from display import *
from matrix import *

#0, 1, 2, 3, 4, 5, 6

def draw_lines(matrix, screen, color):
    length = len(matrix) / 2
    for i in range(length):
      l1 = matrix[i * 2]
      l2 = matrix[i * 2 + 1]
      draw_line(l1[0], l1[1], l2[0], l2[1], screen, color)

def add_edge(matrix, x0, y0, z0, x1, y1, z1):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point(matrix, x, y, z=0):
    matrix.append([x, y, z, 1])




def draw_line(x0, y0, x1, y1, screen, color):
  x1,y1,x0,y0 = int(x1),int(y1),int(x0),int(y0)
  undefined,a,b,m = findABM(x0, y0, x1, y1)
  if 0 <= m and m <= 1:
    if y1 < y0: x0,y0,x1,y1 = x1,y1,x0,y0
    x = x0
    y = y0
    undefined,a,b,m = findABM(x0, y0, x1, y1)
    d = 2 * a + b
    while x <= x1:
      plot(screen, color, x, y)
      if d > 0:
        y += 1
        d += 2 * b
      x += 1
      d += 2 * a
    return
  if m > 1 or undefined:
    if y1 < y0: x0,y0,x1,y1 = x1,y1,x0,y0
    x = x0
    y = y0
    undefined,a,b,m = findABM(x0, y0, x1, y1)
    d = 2 * a + b
    while y <= y1:
      plot(screen, color, x, y)
      if d < 0:
        x += 1
        d += 2 * a
      y += 1
      d += 2 * b
    return
  if m < 0 and m >= -1:
    if y1 > y0: x0,y0,x1,y1 = x1,y1,x0,y0
    x = x0
    y = y0
    undefined,a,b,m = findABM(x0, y0, x1, y1)
    d = 2 * a + b
    while x <= x1:
      plot(screen, color, x, y)
      if d < 0:
        y -= 1
        d -= 2 * b
      x += 1
      d += 2 * a
    return
  if m < -1:
    if y1 > y0: x0,y0,x1,y1 = x1,y1,x0,y0
    x = x0
    y = y0
    undefined,a,b,m = findABM(x0, y0, x1, y1)
    d = 2 * a + b
    while y >= y1:
      plot(screen, color, x, y)
      if d > 0:
        x += 1
        d += 2 * a
      y -= 1
      d -= 2 * b
    return

def findABM(x0, y0, x1, y1):
  undefined = False
  a = y1 - y0
  b = -1 * (x1 - x0)
  if b == 0: return True,a,b,-1
  m = -1.0 * a / b
  return undefined,a,b,m
