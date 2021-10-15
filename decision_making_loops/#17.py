my_list = []

ft = int(input())
md = int(input())
ls = int(input())

my_list.append(ft)
my_list.append(md)
my_list.append(ls)

if my_list[0] == my_list[-1]:
    print('True')
else:
    print('False')