"""
Find the number of different ways to climb an n-stage ladder
when each step is either one or two stages.

(For example, a 3-stage ladder can be three ways: 1-1-1, 1-2, and 2-1)
"""

n = input('Enter the number of steps: ')
result = Nth(n)

print(f'Steps: {result}')

def Nth(number):
    if (number == 0 and number == 1):
        return 1
    if (number == 2):
        return 2
    else:
        return Nth(number - 1) + Nth(number - 2) + Nth(number - 3)
