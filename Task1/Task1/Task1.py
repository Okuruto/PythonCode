import math
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier
print('�������� ����������� ������� �� ������: ��������, ���������, ���������, �������, �������, �������, ����������.')
Cal = input()
if Cal == '��������':
   print('������� ������ ���������')
   sum1 = int(input())
   print ('������� ������ ���������')
   sum2 = int(input())
   print('�����')
   print( sum1 + sum2 )
elif Cal == '���������':
   print('������� �����������')
   sub1 = int(input())
   print ('������� ����������')
   sub2 = int(input())
   print('��������')
   print( sub1 - sub2 )
elif Cal == '���������':
   print('������� ������ ���������')
   mul1 = int(input())
   print ('������� ������ ���������')
   mul2 = int(input())
   print('������������')
   print( mul1 * mul2 )
elif Cal == '�������':
   print('������� �������')
   div1 = int(input())
   print ('������� �������� �������� �� ����')
   div2 = int(input())
   print('�������')
   print( div1 / div2 )
elif Cal == '�������':
   print('������� �����')
   num = int(input())
   print ('������� �������')
   Pow = int(input())
   print('�������')
   print( num ** Pow )
elif Cal == '�������':
    print('������� �����')
    numl = int(input())
    print('������� ���������')
    base = int(input())
    print ('�������')
    print (math.log(numl,base))
elif Cal == '����������':
    print('������� �����')
    numr = float(input())
    print('�� ������ ����� ���������?')
    nroun = int(input())
    print('� ������� ��� �������?')
    Pal = input()
    if Pal =='�������':
         print (round_up(numr, nroun))
    if Pal =='�������':
         print (round_down(numr, nroun))
