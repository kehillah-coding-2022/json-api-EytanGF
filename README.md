# json-api Overview

### Requests
[HTTP requests](http://www.w3schools.com/tags/ref_httpmethods.asp) can be made from within python!

```python
import requests
response = requests.get('https://www.wikipedia.org/')
print(response.text)
```
The code above is an example of getting the HTML returned by a web server.

#### Requirements
In order to use the `requests` module, we must first install it. You can install it via:
```bash
$ pip3 install requests
```
You should probably leave out the `3` if you are on Windows.

### JSON
HTML is not the only way to organize data. We can represent structured data with JSON documents

```json
{
  "firstname": "spongebob",
  "lastname": "squarepants",
  "location": "bikini bottom",
  "occupation": "fry cook",
  "friends": ["sandy", "patrick", "squidward"]
}
```

We could make a similarly structured JSON string that represents a different set of data
```json
{
  "firstname": "sandy",
  "lastname": "cheeks",
  "location": "bikini bottom",
  "occupation": "scientist",
  "friends": ["spongebob", "patrick", "squidward"]
}
```

The nice thing about JSON is that it can be interpreted by a whole host of programming languages.
These JSON strings can be parsed with the `json` module in Python in order to create dictionary objects:
```python
import json

json_string = """
  {
    "firstname": "sandy",
    "lastname": "cheeks",
    "location": "bikini bottom",
    "occupation": "scientist",
    "friends": ["spongebob", "patrick", "squidward"]
  }
"""
print(type(json_string))

data = json.loads(json_string)
print(type(data), data['friends'][2])
```

### JSON APIs
For this project use the [Star Wars](https://swapi.dev/)API.

Use a [get request](http://www.w3schools.com/tags/ref_httpmethods.asp) to get the data from the api:
```python
import requests
resp = requests.get('http://swapi.dev/api/people/1/')
data = json.loads(resp.text)
print(data['name'])
resp = requests.get(data['homeworld'])
home = json.loads(resp.text)
```

## Hints
Some helpful hints for this project which may prove useful:

#### Catching errors
```python
#this program throws an error
'a' + 1
print('hello')
```

```python
#this program catches the error
try:
    'a' + 1
except:
    print('there was an error')
print('hello')
```

```python
#this program is more specific about what kind of error it will catch
try:
    'a' + 1
except TypeError:
    print('there was an error')
print('hello')
```
If you change `TypeError` to `IndexError` above, the program will crash.

### String Formats
One way to put python variables together into strings is with something called string formats:

```python
bags = [10, 15, 4]
fruit = ['oranges', 'apples', 'cherries']
for x in range(len(fruit)):
    n = bags[i]
    f = fruit[i]
    print('I have %s bags of %s' % (n, f))
```

## Assignment
Your task is to create an interactive program using the JSON api of your choice.
Your first task, in order to help you get a grasp on things, could be to create a loop
that explores all of the characters in your universe. From there, decide if you want to create a game,
or an interactive explorer that can traverse the data models, or something else.
Your code should showcase your skills in writing loops, functions, and modules, as well as
indexing data structures and working with strings.

#### Level 1
The program has a menu and allows the user to get and view data from an api.

#### Level 2
The code is abstracted into a module and a main file. Output text is somehow processed
from its original form. Specific values from the data are accessed and presented to
the user (i.e., not just printing the whole dictionary)

### Level 3
The program is abstracted enough to allow the user to visit another part of the api (this means
the api itself must return urls to other parts of the api). For example, while viewing a person's
info from the Star Wars API, the user could jump to the homeworld of that user and view data about it.

### Level 4
The program is abstracted enough to allow the user to fully explore/access all parts of the api
until they choose to quit from a menu. This is similar to Level 3, but goes indefinitely, possibly circularly,
etc.
