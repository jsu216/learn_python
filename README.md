# Python Cheatsheet

## Overview

Python is an [interpreted](https://en.wikipedia.org/wiki/Interpreted_language) [dynamically typed](https://en.wikipedia.org/wiki/Dynamic_programming_language) programming Language.

### Versions

- 2.x

    Python 2.x will get to end of life soon. It is only in maintenance mode to support old python programs. Python 3.x is recommended for new python programmers.

- 3.x

-|   Python 2.x  |	Python 3.x
----    |   ----    |   ----
print   |   print is a keyword. e.g. print "hello"  |   print is a function. e.g. print("hello")
exception   |   except Exception e: or except Exception as e:   |   except Exception as e:
PEP 8 consistency   |   Naming of Libraries and API are frequently inconsistent with PEP 8   |   Improved (but still imperfect) consistency with
PEP 8 guidelines
Strings unicode |   ?   |   Strings are all unicode and types type is for unencoded 8 bit values


There is a utility called 2to3.py that can convert Python 2.x code to 3.x.

The features described in this document apply to python 3.x only unless 2.x is explicitly mentioned.

## Language Features

### Indentation

Python does not have curly braces, nor begin and end keywords. No semicolons to end a line of code. The only thing that organizes code into block, function or classes is indentation. Lines of code in the same indentation forms a block until the end of file or a line with less indentation

```python
def function_block():
    # first block
        # second block within first block stuff
        for x in an_iterator:
        # this is the block for the for loop
        print(x)
        # back out to this level ends the for loop
    # and the second block ...
    # more first block stuff ...
def another_function_block():
```

The common standard is 4 spaces per level. If using IDE like PyCharm, this is handled automatically by press the "tab" key.

### Comments

The pound sign (or hashtag) '#' marks a comment from the current location to the end of a line.

For multi lines comments, use a triple quoted (single or double quoted) string.

```python
# Single line of comments starts with #

""" An example of Python script
    Triple quotes allow multi lines of strings as comment.
"""
```

### Keywords

Keywords are reserved words in programming language that cannot be used as a variable, function, or class name.

Keyword |   Usage
----    |   ----
if |   Conditional expression that only executes if True
else |   Used primarily as a catchall. If <expression> is False, then we fall into the else
elif |   Use elif to test multiple conditions.
while |   The while loop only loops while an expression evaluates to True.
break |   Breaks out of a loop
continue |   Ends current iteration of loop and goes back to top of loop
try |   Begins a block to check for exceptions
except |   Followed by Exception type being checked for, begins block of code to handle exception
finally |   Code that will be executed whether exception occurs or not
def |   Define the function
class |   Define a class
del |   Delete a class instance
pass |   class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

## Operators
Common python operators

Operator    |   Action    |   Example
----    |   ----    |   ----
+    |   Adds items together; for strings and sequences concatenates    |   1 + 1 -> 2<br/>"one" + "one" -> "oneone"
-    |   subtraction    |   1 - 1 -> 0
*    |   multiplication, with strings, repeats string    |   2 * 3 -> 6 "one"<br/>* 2 -> "oneone"
/ (//)    |   division, division of integers results in (an integer with truncation in Python 2.x) a float in Python 3.x (// is integer division in Python 3.x)    |   3/2 -> 1 (Python 2.x)<br/>3/2 -> 1.5 (Python 3.x)<br/>4/2 -> 2 (Python 2.x)<br/>4/2 -> 2.0 (Python 3.x)<br/>4//2 -> 2 (Python 3.x) 
**    |   Exponent - raises a number to the given exponent    |   3**2 -> 9
%    |   mod    |   5 % 2 -> 1<br/>100 % 10 -> 0

## Program flows

### Branching

```python
if something_is_true:
    do this block
elif something_else_is true:
    do that block
else:
    do the other block
```

The "something_***_is_true" is called expressions that have either True or False value.

Comparison operators    |   Descriptions
----    |   ----
==    |   Equal to
!=    |   Not equal to
>    |   Greater than
<    |   Less than
>=    |   Greater than or equal to
<=    |   Less than or equal to
is    |   Object identity
is not    |   Negated object identity


### Loops

Python has two types of loops, for and while loops.

```python
for item in ['abc', 'def', 'ghi', 'jkl', 'mno']
    print(item)
```

For loop all items in the given list

```python
counter = 5
while counter > 0
    print(counter)
    counter -= 1
```

While loops until the condition (counter > 0) is False

### Handle Exceptions

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

## Data Objects

### Variables and Types

In Python, __a variable is a reference (or pointer, or label) to a data object in the memory that can be used in program.__

Python is dynamically typed but also __strong typed__ language. A variable could end up referring to different types of objects in one program. But the object it is referring to is strongly typed and must be used in the context matching its type.

```python
x = 1 # x points to an integer object
y = 2 # y also points to an integer object
z = x + y # z points to an integer object: 3
a = y # a points to the same integer object as y
y = "2" # y now points to a different object, a string (text) z = x + y # throws a type mismatch (TypeError) exception since an integer and a string are different types and can't be added.
z = x + a # z now points to an integer (3), since a is pointing to an integer
```

    In Python, things are different. Because the exception handling is strong
    we can just go ahead and try an operation. If the object we are operating
    on has the methods or data members we need, the operation succeeds. If
    not, the operation raises an exception. In other words, in the Python world
    if something walks like a duck and quacks like a duck, we can treat it like a
    duck. This is called “duck typing”.

### Built-in Data Types

The type of the data used in Python. The most commonly used are shown in the following table.

Type    |   Description
----    |   ----
int    |   Since python 3, integer type including both 32 bits, 64 bits integer and long integer in other languages
long    |   Does not exist in python3 (only supported in python 2)
float    |   A floating point number, like a double in C or Java
complex    |   Complex numbers have a real and an imaginary component, each is a float.
boolean    |   True or False

### Built-in Object types

An object in Python is a combination of one or more data in the types above.

Type    |   Description    |   Example
----    |   ----    |   ----
list    |   In a pair of square brackets. Mutable sequence: content can be changed after it was created.    |   [1,2,3]
tuple    |   In a pair of parentheses. Immutable sequeance: content cannot be change after created.    |   (a,b,c)
dict    |   Dictionary lookup map: key and value stored using curly braces    |   {"key1":"value1", "key2":"value2"}
set    |   Collection of unique elements unordered, no duplicates    |   {"apple", "banana", "cherry"}
str    |   String is doube or single quoted a sequence of unicode encoded characters, immutable    |   "abc"

### Sequence indexes and slicing

Sequential collections of items, like list, tuple, and strings allow access by using numeric indexes. Negative index means count back from the end of the sequence.

Notation    |   Returns    |   Example: x = [0, 1, 2, 3]
----    |   ----    |   ----
x[0]    |   First element of a sequence	0
x[1]    |   Second element of a sequence	1
x[-1]    |   Last element of a sequence	3
x[1:]    |   Second element through last element	[1,2,3]
x[:-1]    |   First element up to (but NOT including last element	[0,1,2]
x[:]    |   All elements - returns a copy of list	[0,1,2,3]
x[0:2]    |   Start at first element, then every 2nd element	[0,2]

## Function

### Definition

Functions are defined with the `def` keyword and parenthesis after the function name.

```python
def a_function():
    “”” document function here”””
    print(“something")
```

### Parameters

Parameters of a function can be passed in several ways

- Default parameters

```python
def foo(a=2, b=3):
    print(a)
foo()
```

- By position

```python
foo(1, 2)
```

- By name

```python
foo(b=4)
```

- As a list

```python
def bar(*args):
    print(args)
bar(1, 2, 3)
```

- As a dictionary

```python
def bar(a, b=2, c=3):
    print(a, b, c)
d = {"a":5, "b":6, "c":7}
bar(**d)
```

### Return value

The value returns from a python function can be any data types like, integer, float, list, dict and etc.

```python
return dict("color": "blue")
```

Thanks to tuple packing and unpacking you can also return more than one item a time. Items separated by commas are automatically ‘packed’ into a tuple and can be ‘unpacked’ on the receiving end:

```python
a, b, c = (1, 2, 3)
```

## Classes

### Definition

```python
class MyClass(BaseClass):
    def __init__(self, par):
        # initialize some stuff
        self.foo = “bar”
    def a_method(self):
        # do something
    def another_method(self, parameter):
        # do something with parameter
```

- If inherited from object, the BaseClass can be ommited in class definition.
- Don’t write getters/setters up front, use the @ property instead which lets you add them transparently later.

Self parameter is a reference to the current instance of the class. It is used to access variables that belong to the class.
It does not have to be named self , you can call it whatever you like, but __it has to be the first parameter of any function in the class__:

```python
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()
```

### Instantiating a class

Creating an instance of the a class is called class instantiating.

```python
my_class_object = MyClass()
```

When a class object is instantiated, the classe’s __init__(self) method is called on the instance, usually doing any set up that is needed: initializing variables and the like. If the class __init__() method accepts a parameter, it can be passed in:

```python
my_class_object = MyClass(param)
```

You can delete objects by using the del keyword:

```python
del my_class_object
```

### Inheritance and mixins

Python supports multiple inheritance. This does provide you with more ways to shoot yourself in the foot, but a common pattern for multiple inheritance is to use “mixin” classes.

### Abstract Base Classes, Metaclasses

- Abstract base classes are defined in `PEP 3119`. You can create abstract base classes via the `abc` module, which was added in `Python 2.6`.

- A metaclass is a class for creating classes. You can see examples of this in Python built-ins, such as int, str or type. All of these are metaclasses. You can create a class using a specific metaclass via __metaclass__. If that is
not specified, then type will be used.

## Comprehensions

Python comes with a concept known as comprehensions. There are 3 types:

- list comprehensions

```python
new_list = [x for x in range(5)]
```

This will create a list from 0-5. It is the equivalent of the following for loop:

```python
new_list = []
for x in range(5):
    new_list.append(x)
```

- dict comprehensions

```python
new_dict = {key: str(key) for key in range(5)}
```

- set comprehensions

A set comprehension will create a Python set, which means you will end up with an unordered collection with no duplicates. The syntax for a set comprehension is as follows:

```python
new_set = {x for x in "mississippi"}
```

## The Zen of Python (by Tim Peters)

- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Complex is better than complicated.
- Flat is better than nested.
- Sparse is better than dense.
- Readability counts.
- Special cases aren’t special enough to break the rules.
- Although practicality beats purity.
- Errors should never pass silently.
- Unless explicitly silenced.
- In the face of ambiguity, refuse the temptation to guess.
- There should be one and preferably only one obvious way to do it.
- Although that way may not be obvious at first unless you’re Dutch.
- Now is better than never.
- Although never is often better than *right* now.
- If the implementation is hard to explain, it’s a bad idea.
- If the implementation is easy to explain, it may be a good idea.
- Namespaces are one honking great idea -- let’s do more of those!

Python's coding style is known as `PEP 8`. In order to contribute to Python Code, program must follow `PEP 8`.

## Using libraries

### Importing and using modules and libraries

Using external modules and libraries is as simple as using the import keyword at the top of your code.


Import  |   Explanation
----    |   ----
from lib import x<br/>from lib import x as y    |   Imports single element x from lib, no dot prefix needed<br/>x()<br/>y()
import lib    |   Imports all of lib, dot prefix needed<br/>lib.x()
from lib import *    |   Imports all of lib, no dot prefix needed "NOT FOR" PRODUCTION CODE - POSSIBLE VARIABLE NAME CLASHES!

### Creating modules and libraries

```python
def my_module(foo, bar):
    print foo
    print bar
if __name__ == “__main__”:
    my_module(1, 2)
```

    Any Python script file can be treated like a module and imported. However
    be aware that when a module is imported, its code is executed – that’s the
    reason for the if __name__ == “__main__”: structure in the example above.
    In other words, to be safely used as a module, a script should be organized
    into functions (or classes), with the if statement at the very end.
    Here is an example module.

### The Python standard library - selected library groups

Python comes with a standard library of modules that can do much of what you need to get done.

Library Group   |   Contains libraries for
----    |   ----
File and Directory Access   |   File paths, tempfiles, file comparisons (see the os and tempfile modules)
Numeric and Math   |   Math, decimal, fractions, random numbers/sequences, iterators (see math, decimal, and collections)
Data Persistence   |   Object serialization (pickle), sqlite, database access
File Formats   |   Csv files, config files - see ConfigParser
Generic OS Services   |   Operating system functions, time, command line arguments, logging (see os, logging, time, argparse)
Interprocess   |   Communication with other processes, low-level sockets (see subprocess and the socket module)
Interned Data Handling   |   Handling Internet data, including json, email and mailboxes, mime encoding (see json, email, smtplib and mimetools)
Structured Markup   |   Parsing HTML and XML (see xml.minidom and ElementTree)
Internet Protocols   |   HTTP, FTP, CGI, URL parsing, SMTP, POP, IMAP, Telnet, simple servers (see httplib, urllib, smtplib, imaplib)
Development   |   Documentation, test, Python 2 to Python 3 conversion (see doctest and 2to3)
Debugging   |   Debugging, profiling (see pdb and profile)
Runtime   |   System parameters and settings, builtins, warnings, contexts (see the dir command and the inspect module)
GUI   |   Tkinter GUI libraries, turtle graphics

### Getting other libraries

Use tools like `pip` to install libraries.