# Class 5

You need to reuse you code as much as possible. Function provides a way to reuse your code in different places.

You have already use the following functions:

- print()
- quit()
- range()

## Create a function

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