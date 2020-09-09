# Class 5

## Function

You need to reuse your code as much as possible. Function provides a way to reuse your code in different places.

### Built in functions

You have already use the following functions:

- print()
- quit()
- range()

```python
abs(-123)

bool(0)

bool(3)

help(print)

len('this is a test string')
```

- The `dir` function (short for directory) returns information about any 
value. Basically, it tells you the functions that can be used with 
that value in alphabetical order. 
For example, to display the functions that are available for a 
list value, enter this: 

```python
myvar=123
dir(myvar)
```

```text
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

- The `eval` function is often used to turn user input into Python 
expressions. For example, you could write a simple calculator pro-
gram that reads equations entered into Python and then calculates 
(evaluates) the answers. 

```python
eval('12*52+30/2-5')
```

- `float` and `int` function
The `float` function converts a string or a number into a floating-point number, which is a number with a decimal place (also called a real number). For example, the number 10 is an integer (also called a whole number), but 10.0, 
10.1, and 10.253 are all floating-point numbers (also called floats).

```text
>>> float('123.456789')
123.456789
```

The `int` function converts a string or a number into a whole number (or integer), which basically means that everything after the decimal point is dropped. For example, here’s how to convert a floating-point number into a plain integer:

```text
>>> int(123.456)
123
```

- `len` function
The len function returns the length of an object or, in the case of a string, the number of characters in the string. For example, to get the length of this is a test string, you would do this:

```text
>>> len('this is a test string')
21
```

```text
>>> creature_list = ['unicorn', 'cyclops', 'fairy', 'elf', 'dragon', 'troll']
>>> print(len(creature_list))
6
```

```text
>>> enemies_map = {'Batman' : 'Joker', 'Superman' : 'Lex Luthor', 'Spiderman' : 'Green Goblin'}
>>> print(len(enemies_map))
3
```

- max and min functions
The max function returns the largest item in a list, tuple, or string. For example, here’s how to use it with a list of numbers:

```text
>>> numbers = [5, 4, 10, 30, 22]
>>> print(max(numbers))
30
```

```text
>>> strings = 's,t,r,i,n,g,S,T,R,I,N,G'
>>> print(max(strings))
t
```

```text
>>> print(max(10, 300, 450, 50, 90))
450
```

```text
>>> numbers = [5, 4, 10, 30, 22]
>>> print(min(numbers))
4
```

- range function
The range function, as we’ve seen before, is mainly used in for loops, to loop through a section of code a
specific number of times. The first two parameters given to range are called the start and the stop.
You saw range with these two parameters in the earlier example of using the len funcion to work with a loop.
The numbers that range generates begin with the number given as the first parameter and end with the number that’s one less than the second parameter.
For example, the following shows what happens when we print the numbers that range creates between 0 and 5:

```text
>>> for x in range(0, 5):
        print(x)
0
1
2
3
4
```

The range function actually returns a special object called an `iterator` that repeats an action a number of times.
In this case, it returns the next highest number each time it is called.
You can convert the iterator into a list (using the function list).
If you then print the returned value when calling range, you’ll see the numbers it contains as well:

```text
>>> print(list(range(0, 5)))
[0, 1, 2, 3, 4]
```
You can also add a third parameter to range, called step.
If the step value is not included, the number 1 is used as the step by default.
But what happens when we pass in the number 2 as the step? Here’s the result:

```text
>>> count_by_twos = list(range(0, 30, 2))
>>> print(count_by_twos)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
```

- sum function
The `sum` function adds items in a list and returns the total. Here’s an example:

```text
>>> my_list_of_numbers = list(range(0, 500, 50))
>>> print(my_list_of_numbers)
[0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
>>> print(sum(my_list_of_numbers))
2250
```

- round function
The `round` function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
The default number of decimals is 0, meaning that the function will return the nearest integer.

__A interesting behavior__
try the following and see if the results match your expectation

```python
round(1.4)
round(1.5)
round(2.4)
round(2.5)
round(2.6)

round(2.51)
round(2.501)
```

### Create a function

```python
def myfunc(myname):
    print('hello %s' % myname)

myfunc('Kid')
```

```shell script
python3 myfunc.py
```

## Variable scopes

A variable that’s inside the body of a function can’t be used again when the function has finished running because it exists only
inside the function. In the world of programming, this is called scope.

Do you still remember the term `block`?

```shell script
python3 scope.py
```

## Working with files

Files on your computer are documents, pictures, music, games, and etc. Everything on your computer is stored as files.
 
Let’s look at how to open and work with files in Python by using the built-in function open.
But first we need to create a new file to play with, say `myfile.txt`

### Read files

```text
>>> test_file = open('.\\myfile.txt')
>>> text = test_file.read()
>>> print(text)
```

### Write files

```text
>>> test_file = open('c:\\myfile2.txt', 'w')test_file.write('this is my test file')
test_file.write('this is my second text file!')

```


## Handle exceptions

Exceptions are the errors happened while program running. If the errors are not handled in Python program, it will be thrown to the system (OS).

```python
try:
    item = x[0]
except TypeError:
    #this will print only on a TypeError exception
    print “x isn’t a list!”
else:
    # executes if the code in the “try” does NOT
    # raise an exception
    print “You didn’t raise an exception!”
finally:
    #this will always print
    print “processing complete”
```

```shell script
python3 tryexcept.py
```

## Module

Modules are used to group functions, variables, and other things together into larger, more powerful programs.
Some modules are built in to Python, and you can download other modules separately.

You’ll find modules to help you write games (such as tkinter , which is built in, and PyGame , which is not),

### Use module

```python
import time

print(time.asctime())
```

```shell script
python3 module.py
```