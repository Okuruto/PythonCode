print('������������ ������, ����� ����������, ���������� ����� �� �����, ����������� ������ ����� �� �����')
Prog = input()
if Prog == '������������ ������':
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
if Prog == '����� ����������':
    num = int(input("����� �����: "))
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

    if num == sum:
        print(num,"��� ����� ����������")
    else:
        print(num,"��� �� ����� ����������")
if Prog == '���������� ����� �� �����':
    for val in "������ �����":
        if val == "�":
            continue
        print(val)
if Prog == '����������� ������ ����� �� �����':
    for val in "�������":
        if val == "�":
             break
        print(val)

