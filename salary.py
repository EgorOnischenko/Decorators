from decorator import LogDecorator


print('start salary.py')


@LogDecorator()
def calculate_salary():

    return "salary.py"






print('end salary.py')