<div><h1 align="center">Python - Hello, World</h1>

<h2>Python Programming</h2>

It is a powerful and easy language to learn, tine high -level structures, efficient and with a simple but effective approach to object -oriented programming.
The elegant syntax and Python's dynamic typification, along with its interpreted nature, makes it an ideal language for command sequences and rapid applying development in many areas.
Python is easy to use, but it is a language real, it offers structures and support for large Software.
It also offers much more error verification, than C, being a very high -level language, it has high -level integrated data types, such as flexible matrices and dictionaries.
It allows to divide its program into modules that can be used in other Software, in addition to a large amount of standard modules
It is an interpreted language does not need to compile or in them.The interpreter could be used interactively, which facilitates experimentation with the characteristics of the language

Allows you to write compact and readable

* Data types allows to express complex operations in a single line

* Sequence grouping is performed through instead of brackets.

* It is not necessary to declare variables or arguments

Python is extendable: if you know program in C it is easy to add a new function or module incorporated into the interpret, You can also link Python's interpreter to an application written in C and be used it as extensions
</div>

<details>
<summary><h3>Invoking the Interpreter</h3></summary>

The interpreter works very similar to the Unix Shell: when invoked with a standard input connected to a TTY device, read and run commands interactively;When invoked with an argument of file name or with a file like standard input, read a script of that file and execute it.

A second way to start the interpreter is Python -C Command [ARG] ... that executes the statements in the command, analogous to the shell option.

These can be invoked with Python -M Module [ARG] ... which will execute the module source file as if you had written your full name in the command line.

By using a command sequence file, it is sometimes useful to execute the command sequence and then change to interactive mode.

## Argument Passing

When the interpreter knows them, the name of the script and the additional arguments become a list of chains and are assigned to the ARGV variable in the SYS module.The length of the list is at least one;When no command sequence or arguments is provided, Sys.argv [0] is the empty chain.When the name of the script is given as '-' (which means standard input), Sys.argv [0] is established in '-'.When used -M, Sys.argv [0] is established in the full name of the module in which it resides.

## Interactive Mode

In this way, the following command is requested in the main indicator, usually three signs of greater than (>>>).For the continuation lines, the default value is a second three -point indicator (...).The interpreter prints a welcome message with the version number and the copyright notice before printing the first notice.
</details>

<details>
<summary><h3>An Informal Introduction to Python</h3></summary>

In the following examples, the entrance and exit are distinguished by the presence or absence of a notice (>>> and ...): To repeat the example, you must write everything after the notice, when the notice appears;The lines that do not start with an indicator are broadcast from the interpreter.Note that the secondary notice in a single line in the example means that you must write a blank line;This is used to finish a command of several lines.

You can change the visualization of the instructions and the exit by clicking >>> in the upper right corner of the sample box.If you hide the instructions and exit of the examples, you can easily copy and paste the entry lines into your interpreter.

Python comments begin with the hash character, #, and extend until the end of the physical line.

```py
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
```

## Numbers

The integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional part (e.g. 5.0, 1.6) have type float. We will see more about numeric types later in the tutorial.

## Strings

Besides numbers, Python can also manipulate strings, which can be expressed in several ways. They can be enclosed in single quotes ('...') or double quotes ("...") with the same result 2. \ can be used to escape quotes:

```py
'spam eggs'  # single quotes
'spam eggs'
'doesn\'t'  # use \' to escape the single quote...
"doesn't"
"doesn't"  # ...or use double quotes instead
"doesn't"
'"Yes," they said.'
'"Yes," they said.'
"\"Yes,\" they said."
'"Yes," they said.'
'"Isn\'t," they said.'
'"Isn\'t," they said.'
```

In the interactive interpreter, the exit chain is in double quotes and the special characters escape with inverted bars.The chain is locked in double quotes if the chain contains a simple quote and does not contain double quotes;Otherwise, it is locked in single quotes.

```py
'"Isn\'t," they said.'
'"Isn\'t," they said.'
print('"Isn\'t," they said.')
"Isn't," they said.
s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output
'First line.\nSecond line.'
print(s)  # with print(), \n produces a new line
First line.
Second line.
```

If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:

```py
print('C:\some\name')  # here \n means newline!
C:\some
ame
print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. The following example:

```py
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

output:

Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect 
```

Strings can be concatenated (glued together) with the + operator, and repeated with *:

```py
# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'
'unununium'
```

Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

```py
'Py' 'thon'
'Python'
```

This feature is particularly useful when you want to break long strings:

```py
text = ('Put several strings within parentheses '
        'to have them joined together.')
text
'Put several strings within parentheses to have them joined together.'
```

This only works with two literals though, not with variables or expressions

Indices may also be negative numbers, to start counting from the right:

```py
word[-1]  # last character
'n'
word[-2]  # second-last character
'o'
word[-6]
'P'
```

Note that since -0 is the same as 0, negative indices start from -1.
In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring:
Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
The built-in function len() returns the length of a string:
</details>

<details>
<summary><h2>f-Strings:</h2></summary>

Also called “formatted string literals,” f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values. The expressions are evaluated at runtime and then formatted using the __format__ protocol.


## Simple Syntax

The syntax is similar to the one you used with str.format() but less verbose. Look at how easily readable this is:

```py
>>> name = "Eric"
>>> age = 74
>>> f"Hello, {name}. You are {age}."
'Hello, Eric. You are 74.'
```
It would also be valid to use a capital letter F

## Arbitrary Expressions

Because f-strings are evaluated at runtime, you can put any and all valid Python expressions in them. This allows you to do some nifty things.

You could do something pretty straightforward, like this:

```py
>>> f"{2 * 37}"
'74'
```

But you could also call functions. Here’s an example:

```py
>>> def to_lowercase(input):
...     return input.lower()

>>> name = "Eric Idle"
>>> f"{to_lowercase(name)} is funny."
'eric idle is funny.'
```
</details>