def make_bricks(small, big, goal):
  res = goal//5
  
  if (small >= goal) or (goal % 5 ==0 and big *5 >= goal):
    print("hello")
    return True
  elif (goal - res*5) <= small:
    print("world")
    return True
  else:
    return False
print(make_bricks(3, 1, 7))
print(make_bricks(1, 4, 12))
print(make_bricks(1, 7, 7))
print(make_bricks(7, 1, 11))
