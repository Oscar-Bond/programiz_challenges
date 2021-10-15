num = int(input())

class InvalidNum(Exception):
    def __init__(self, value):
        self.value = value
 
    def __str__(self):
        return(repr(self.value))

try:
    if num > 5:
        print('valid')
    else:
        raise InvalidNum("invalid")
except InvalidNum as error:
    print(error.value)
    
