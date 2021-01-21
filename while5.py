#5. Írj egy programot, amely a felhasználótól páros számot kér be. Amennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig, amíg végül páros számot nem ad meg a felhasználó.


a = int(input("Páros szám! "))
while a % 2 == 1:
    a = int(input("Páros szám!"))