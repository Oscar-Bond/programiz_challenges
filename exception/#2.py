n = int(input())


try:
    if n > 5:
        raise ValueError 
    else:
        print('successful')
except ValueError:
        print('unsuccessful')
    

