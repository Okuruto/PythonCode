import math
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier
print('Выберете необходимую функцию из списка: сложение, вычитание, умножение, деление, степень, логариф, округление.')
Cal = input()
if Cal == 'сложение':
   print('Введите первое слогаемое')
   sum1 = int(input())
   print ('Введите второе слогаемое')
   sum2 = int(input())
   print('Сумма')
   print( sum1 + sum2 )
elif Cal == 'вычитание':
   print('Введите уменьшаемое')
   sub1 = int(input())
   print ('Введите вычитаемое')
   sub2 = int(input())
   print('Разность')
   print( sub1 - sub2 )
elif Cal == 'умножение':
   print('Введите первый множитель')
   mul1 = int(input())
   print ('Введите второй множитель')
   mul2 = int(input())
   print('Произведение')
   print( mul1 * mul2 )
elif Cal == 'деление':
   print('Введите делимое')
   div1 = int(input())
   print ('Введите делитель отличный от нуля')
   div2 = int(input())
   print('Частное')
   print( div1 / div2 )
elif Cal == 'степень':
   print('Введите число')
   num = int(input())
   print ('Введите степень')
   Pow = int(input())
   print('Степень')
   print( num ** Pow )
elif Cal == 'логариф':
    print('Введите число')
    numl = int(input())
    print('Введите основание')
    base = int(input())
    print ('Логариф')
    print (math.log(numl,base))
elif Cal == 'округление':
    print('Введите число')
    numr = float(input())
    print('До какого знака округлять?')
    nroun = int(input())
    print('В большую или меньшую?')
    Pal = input()
    if Pal =='большую':
         print (round_up(numr, nroun))
    if Pal =='меньшую':
         print (round_down(numr, nroun))
