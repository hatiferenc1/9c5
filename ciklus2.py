"""
 2. Feladat Készíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 5 x 5-ös mezőben az alábbi alakzatot!

    O . . . . 
    . O . . . 
    . . O . . 
    . . . O . 
    . . . . O   
 """
n = 5
sor = 0
while sor < n:
    oszlop = 0
    while oszlop < n:
        if oszlop == sor:   
            print("O " , end='')        
        else:
            print(". " , end='')
        oszlop = oszlop + 1    
    print()
    sor = sor + 1
  