print('Перемножение матриц, число Армстронга, извлечение буквы из слова, прекращение записи слова на букве')
Prog = input()
if Prog == 'Перемножение матриц':
     X = [[12,7,3],
         [4 ,5,6],
         [7 ,8,9]]

     Y = [[5,8,1,2],
         [6,7,3,0],
         [4,5,9,1]]

     result = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]

     for i in range(len(X)):
 
         for j in range(len(Y[0])):
       
             for k in range(len(Y)):
                 result[i][j] += X[i][k] * Y[k][j]

     for r in result:
         print(r)
if Prog == 'число Армстронга':
    num = int(input("Введи число: "))
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

    if num == sum:
        print(num,"Это чилсо Армстронга")
    else:
        print(num,"Это не число Армстронга")
if Prog == 'извлечение буквы из слова':
    for val in "Мясная лавка":
        if val == "а":
            continue
        print(val)
if Prog == 'прекращение записи слова на букве':
    for val in "Василий":
        if val == "л":
             break
        print(val)

