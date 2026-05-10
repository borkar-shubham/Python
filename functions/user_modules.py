import arithmetic  #This is the custom module that we created locally in arithmetic.py file.

a = 9
b = 6

result = arithmetic.add(a, b)
print(result)

out = arithmetic.square_root(a)
print(out)

from arithmetic import square

out2 = square(b)
print(out2)