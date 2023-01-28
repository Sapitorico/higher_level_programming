<div><h1 align="center">Python - if/else, loops, functions</h1></div>

<details>
<summary><h2>if Statements</h2></summary>

most well-known statement type is the if statement

```py
x = int(input("Please enter an integer: "))
Please enter an integer: 42
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```

There may be zero or more elif parts, and the other parts are optional.
If you compare equal values in multiple constants, or examine a specific type or attribute, you can also find the coincidence statements useful.

</details>

<details>
<summary><h2>for Statements</h2></summary>

The state statement in Python is a bit different from what is accustomed to C. instead deducting to the user the ability to specify the iteration passstring), in the order in which they appear in the order.

```py
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

cat 3
window 6
defenestrate 12
```
The code that modifies collections while repeating the same collection can be difficult to succeed.

```py
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```

## The range() Function

The Range Incorporated Function is useful when it needs to iterate on a set of numbers.

```py
for i in range(5):
    print(i)

0
1
2
3
4
```

The specified end point is never part of the generated sequence;Range (10) generates 10 values, legal indices for elements of a sequence of length 10.

```py
list(range(5, 10))
[5, 6, 7, 8, 9]

list(range(0, 10, 3))
[0, 3, 6, 9]

list(range(-10, -100, -30))
[-10, -40, -70]
```
To iterate over the indices of a sequence, you can combine range() and len() as follows:

```py
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

0 Mary
1 had
2 a
3 little
4 lamb
```
A strange thing happens if you just print a range:

```py
range(10)
range (0, 10)
```
In many ways, the object returned by Range () behaves as if it were a list, but in reality it is not.

Hemos visto que la declaración for es una construcción, mientras que una función de ejemplo que usa iterable es sum():

```py
sum(range(4))  # 0 + 1 + 2 + 3
6
```
Más adelante veremos más funciones que devuelven iterables y toman iterables como argumentos.

</details>

<details>
<summary><h2> break and continue Statements, and else Clauses on Loops</h2></summary>

Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the iterable or when the condition becomes false , but not when the loop is terminated by a break statement.

```py
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

The continue statement, also borrowed from C, continues with the next iteration of the loop:

```py
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
```

## pass Statements

The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:

```py
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)
```
This is commonly used for creating minimal classes:
```py
class MyEmptyClass:
    pass
```
</details>


<details>
<summary><h2>Defining Functions</h2></summary>

We can create a function that writes the Fibonacci series to an arbitrary boundary:

```py
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```

The keyword def introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next line, and must be indented.
The execution of a function introduces a new symbol table used for the local variables of the function. More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. 1 When a function calls another function, or calls itself recursively, a new local symbol table is created for that call.
A function definition associates the function name with the function object in the current symbol table.

```py
fib
<function fib at 10042ed0>
f = fib
f(100)
0 1 1 2 3 5 8 13 21 34 55 89
```
Coming from other languages, you might object that fib is not a function but a procedure since it doesn’t return a value. This value is called None .

```py
fib(0)
print(fib(0))
None
```
It is simple to write a function that returns a list of the numbers of the Fibonacci series, instead of printing it:

```py
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```
This example, as usual, demonstrates some new Python features:

* The return statement returns with a value from a function. return without an expression argument returns None. Falling off the end of a function also returns None.

* Append calls a method of the list object result. A method is a function that ‘belongs’ to an object and is named obj. Methodname, where obj is some object , and methodname is the name of a method that is defined by the object’s type.

</details>

<details>
<summary><h1>String Formatters in Python 3</h1>
Python’s str.format method of the string class allows you to do variable substitutions and value formatting.
</summary>

## Using Formatters

Formatters work by putting in one or more replacement fields or placeholders — defined by a pair of curly braces {} — into a string and calling the str.format() method.
You’ll pass into the method the value you want to concatenate with the string. This value will be passed through in the same place that your placeholder is positioned when you run the program.

Let’s print out a string that uses a formatter:

```py
print("Sammy has {} balloons.".format(5))

Output
Sammy has 5 balloons.
```

We can also assign a variable to be equal to the value of a string that has formatter placeholders:

```py
open_string = "Sammy loves {}."
print(open_string.format("open source"))

Output
Sammy loves open source.
```

* You can use multiple pairs of curly braces when using formatters. If we’d like to add another variable substitution to the sentence above, we can do so by adding a second pair of curly braces and passing a second value into the method, we passed two strings into the str.format() method, separating them by a comma.
* We can pass these index numbers into the curly braces that serve as the placeholders in the original string:
* But, if we reverse the index numbers with the parameters of the placeholders we can reverse the values being passed into the string:
```py
print("Sammy the {1} has a pet {0}!".format("shark", "pilot fish"))

Output
Sammy the pilot fish has a pet shark!
```

for more information on how to use str.format: [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
</details>