#Készíts egy programot, amely a felhasználótól bekér egy páros számot, majd ennek megfelelően rajzol ki a képernyőre egy pocak szerű alakzatot az alábbiak szerint!

a = int(input("páros szám "))
a = a//2
for i in range (a):
  print("O "*(i+1))

for i in range (a):
  print("O "*(a-i))