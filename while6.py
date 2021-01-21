#6. Írj egy programot, amely [1;12] intervallumon állít elő 20 darab véletlenszámot! A képernyőre kizárólag csak a 3-mal oszthatóakat írja ki, és a végén informálja a felhasználót arról is, hány darab ilyen szám volt.
import random
a = 1
while a < 21:
  b = random.randrange(1, 12)
  if b % 3 == 0:
    print(b)
  a += 1
