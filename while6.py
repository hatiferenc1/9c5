import random
a = 1
while a < 21:
  b = random.randrange(1, 12)
  if b % 3 == 0:
    print(b)
  a += 1
