print('请输入总金额')
z = float(input())

print('主压得赔率')
p1 = float(input())
print('副压的赔率')
p2 = float(input())
print('请输入压的场次1（主）2（副）')
age = input()
if age == 1:
    p2 = p2 - 1
    x = z / p2
else:
    p1 = p2 - 1
    x = z / p1
print(x)