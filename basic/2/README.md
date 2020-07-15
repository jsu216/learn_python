# Class 2

## Calculation

Type `python3` in terminal console and get into python console, then try the following

```console
>>> 6 * 123.45
740.7
```

```console
>>> 4 + 20 * 30 / 10
64.0
```

## Variables

Variable in programming language is a place to store the information such as number, text and etc.

```console
>>> jason = 11
>>> print(jason)
```

Variable names can be made up of letters, numbers, and the underscore character (`_`), but they can’t start with a number.
You can use anything from single letters (such as a ) to long sentences for variable names.
__A variable can’t contain a space, so use an underscore to separate words.__
It is highly recommend to meaningful words as the variable name, but not too long.

### Variable without value

```console
>>> myval = None
>>> print(myval)
None
```

Try the `variables.py`

The followings are different data types of variables

### String

```python
var1 = "Hello World"
var2 = 'Foo Bar'
```

- Embedding Values in Strings

```console
>>> myscore = 1000
>>> message = 'I scored %s points'
>>> print(message % myscore)
I scored 1000 points
```

```console
>>> joke_text = '%s: a device for finding furniture in the dark'
>>> bodypart1 = 'Knee'
>>> bodypart2 = 'Shin'
>>> print(joke_text % bodypart1)
Knee: a device for finding furniture in the dark
>>> print(joke_text % bodypart2)
Shin: a device for finding furniture in the dark
```

```console
>>> nums = 'What did the number %s say to the number %s? Nice belt!!'
>>> print(nums % (0, 8))
What did the number 0 say to the number 8? Nice belt!!
```

- Multiplying Strings

```console
>>> print(10 * 'a')
aaaaaaaaaa
```

Try the `stringmultiply.py`

### Number

`var2 = 123` is different than `var2 = '123'` although they appear the same with print them

```python
var2 = 123
print(var2)
var2 = '123'
print(var2)
```

- Convert string to int

```console
>>> age = '10'
>>> converted_age = int(age)
```

- Convert int to string

```console
>>> age = 10
>>> converted_age = str(age)
```

### Bool

```python
var3 = True
```

### List

```console
>>> wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']
>>> print(wizard_list)
['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']
```

- Access by index

```console
>>> print(wizard_list[2])
eye of newt
```

the first item in a list is 0, the second is 1, and the third is 2.

```console
>>> wizard_list[2] = 'snail tongue'
>>> print(wizard_list)
['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'snake dandruff']
```

- Get the subset

```console
>>> print(wizard_list[2:5])
['snail tongue', 'bat wing', 'slug butter']
```

- list element types

```console
>>> some_numbers = [1, 2, 5, 10, 20]
>>> some_strings = ['Which', 'Witch', 'Is', 'Which']
numbers_and_strings = ['Why', 'was', 6, 'afraid', 'of', 7, 'because', 7, 8, 9]
>>> print(numbers_and_strings)
['Why', 'was', 6, 'afraid', 'of', 7, 'because', 7, 8, 9]
```

List might have another list as element

```console
>>> numbers = [1, 2, 3, 4]
>>> strings = ['I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'sore']
>>> mylist = [numbers, strings]
>>> print(mylist)
[[1, 2, 3, 4], ['I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'sore']]
```

- Add items to list

```console
>>> wizard_list.append('bear burp')
>>> print(wizard_list)
['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'snake dandruff', 'bear burp']
>>> wizard_list.append('mandrake')
>>> wizard_list.append('hemlock')
>>> wizard_list.append('swamp gas')
>>> print(wizard_list)
['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'snake dandruff', 'bear burp', 'mandrake', 'hemlock', swamp gas']
```

- Removing Items from a List

```console
>>> del wizard_list[5]
>>> print(wizard_list)
['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'bear burp', 'mandrake', 'hemlock', 'swamp gas']
```

- List Arithmetic

concatenate

```console
>>> list1 = [1, 2, 3, 4]
>>> list2 = ['I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
print(list1 + list2)
[1, 2, 3, 4, 'I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
```

multiply

```console
>>> list1 = [1, 2]
>>> print(list1 * 5)
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
```

division ( / ) and subtraction ( - ) give only errors, as in these examples:

```console
>>> list1 / 20
Traceback (most recent call last):
File "<pyshell>", line 1, in <module>
list1 / 20
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> list1 - 20
Traceback (most recent call last):
File "<pyshell>", line 1, in <module>
list1 - 20
TypeError: unsupported operand type(s) for -: 'list' and 'int'
```

### Tuple

A tuple is like a list that uses parentheses, as in this example:

```console
>>> fibs = (0, 1, 1, 2, 3)
>>> print(fibs[3])
2
```

The main difference between a tuple and a list is that a tuple cannot change once you’ve created it.
For example, if we try to replace the first value in the tuple fibs with the number 4 ( just as
we replaced values in our wizard_list ), we get an error message:

```console
>>> fibs[0] = 4
Traceback (most recent call last):
File "<pyshell>", line 1, in <module>
fibs[0] = 4
TypeError: 'tuple' object does not support item assignment
```

### Map

A map (also referred to as a dict, short for dictionary) is a collection of things, like lists and tuples.
The difference between maps and lists or tuples is that each item in a map has a key and a corresponding value.

```console
>>> favorite_sports = {'Ralph Williams': 'Football', 'Michael Tippett': 'Basketball', 'Edward Elgar': 'Baseball', 'Rebecca Clarke': 'Volleyball', 'Ethel Smyth': 'Badminton', 'Frank Bridge': 'Rugby'}
```

Key |   Value
----    |   ----
Ralph Williams    |   Football
Michael Tippett    |   Basketball
Edward Elgar    |   Baseball
Rebecca Clarke    |   Volleyball
Ethel Smyth    |   Badminton
Frank Bridge    |   Rugby


- Search by `key`

```console
>>> print(favorite_sports['Rebecca Clarke'])
Volleyball
```

- Delete

```console
>>> del favorite_sports['Ethel Smyth']
>>> print(favorite_sports)
{'Rebecca Clarke': 'Volleyball', 'Michael Tippett': 'Basketball', 'Ralph Williams': 'Football', 'Edward Elgar': 'Baseball', 'Frank Bridge': 'Rugby'}
```

- Replace

```console
>>> favorite_sports['Ralph Williams'] = 'Ice Hockey'
>>> print(favorite_sports)
{'Rebecca Clarke': 'Volleyball', 'Michael Tippett': 'Basketball', 'Ralph Williams': 'Ice Hockey', 'Edward Elgar': 'Baseball', 'Frank Bridge': 'Rugby'}
```

You can’t join maps with the plus operator ( + ).
