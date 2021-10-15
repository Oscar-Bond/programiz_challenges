num = input()

try:
    num_cnvrt = int(num)
except TypeError:
    print('invalid input')
else:
    print(num_cnvrt)