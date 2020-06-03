
import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

# Build a chache for every math function
pow_cache = {}
fac_cache = {}
div_cache = {}
mod_cache = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Use x, y as the key
    i = (x,y)
    # Declare v outside of the if statements
    v = 0

    # If we have this key in the respective cache, 
    # use that key's value for v

    # Pow
    if i in pow_cache:
        v = pow_cache[i]
    else:
        pow_cache[i] = math.pow(x, y)
        v = pow_cache[i] 

    # factorial
    if i in fac_cache:
        v = fac_cache[i]
    else:
        fac_cache[i] = math.factorial(v)
        v = fac_cache[i]

    # Division
    if i in div_cache:
        v = div_cache[i]
    else:
        div_cache[i] = v // (x + y)
        v = div_cache[i]

    # Modulo
    if i in mod_cache:
        v = mod_cache[i]
    else:
        mod_cache[i] = v % 982451653
        v = mod_cache[i]

    # Return result
    return v


"""
x = 3
y = 4

slowfun(x, y)
"""

# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

