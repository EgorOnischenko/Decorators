from decorator import LogDecorator

print('start people.py')

@LogDecorator()
def get_employees():

    return "people.py"


print('end data.py')