# Infinitely Navigatable Menu of Data from the Star Wars API

## Table of Contents

- [Setup](#setup "Goto Setup")
	- [Downloading Requests](#downloading-requests "Goto Downloading Requests")
- [Functions](#functions "Goto Functions")
- [Main Menu](#main-menu "Goto Main Menu")
- [Sub Menu](#sub-menu "Goto Sub Menu")
	- [Loading All the Pages of the Sub Menu](#loading-all-the-pages-of-the-sub-menu "Goto Loading All the Pages of the Sub Menu")
		- [Loading First Page](#loading-first-page "Goto Loading First Page")
		- [Loading Subsequent Pages](#loading-subsequent-pages "Goto Loading Subsequent Pages")
		- [Loading Final Page](#loading-final-page "Goto Loading Final Page")
	- [Generating a List of Titles and Names and URLs](#generating-a-list-of-titles-and-names-and-urls "Goto Generating a List of Titles and Names and URLs")
		- [Generating a List of Titles](#generating-a-list-of-titles "Goto Generating a List of Titles")
		- [Generating a List of Names](#generating-a-list-of-names "Goto Generating a List of Names")
		- [Generating a List of URLs](#generating-a-list-of-urls "Goto Generating a List of URLs")
	- [Generating a List of Numbers which Correspond to the Titles and Names](#generating-a-list-of-numbers-which-correspond-to-the-titles-and-names "Goto Generating a List of Numbers which Correspond to the Titles and Names")
	- [Printing the Sub Menu](#printing-the-sub-menu "Goto Printing the Sub Menu")
	- [Evaluating the Choice of the User Within the Sub Menu](#evaluating-the-choice-of-the-user-within-the-sub-menu "Evaluating the Choice of the User Within the Sub Menu")
- [Page Menu](#page-menu "Goto Page Menu")
	- [If Value is a List](#if-value-is-a-list "Goto If Value is a List")
	- [If Value is not a List but it is a URL](#if-value-is-not-a-list-but-it-is-a-url "Goto If Value is not a List but it is a URL")
	- [If Value is not a URL](#if-value-is-not-a-url "Goto If Value is not a URL")
	- [Printing the Number next to the Item](#printing-the-number-next-to-the-item "Goto Printing the Number next to the Item")
	- [Returning the Name Title Dictionary](#returning-the-name-title-dictionary "Goto Returning the Name Title Dictionary")
- [Infinite Nature of Code](#infinite-nature-of-code "Goto Infinite Nature of Code")
	- [While Loop](#while-loop "Goto While Loop")
- [Files](#files "Goto Files")

## Setup

### Downloading Requests

To install Requests, simply run this simple command in your terminal of choice:

```python
python -m pip install requests
```

JSON is a part of the PSL (**P**ython **S**tandard **L**ibrary) so you do not need to download it
## Functions

Function | Description
------------- | -------------
`main`  | Run main code which calls on a different function and runs an infinately navigatable menu of data from the Star Wars API
`object_menu`  | Generate the interactive menu of a page given an object
`get_dict_from_url`  | Return a dictionary based on the JSON response from SWAPI for a given URL

## Main Menu

I manually made a list of the 6 submenus plus an exit button and then printed each submenu to the right of it's corresponding number:

![Screenshot 2022-01-30 205756](https://user-images.githubusercontent.com/89275837/151741191-268d4393-e3f9-4c26-aa2e-2050c0100e7d.png)


## Sub Menu

### Loading All the Pages of the Sub Menu

#### Loading First Page
I then loaded the data for the entire submenu by loading the first page

```python
    response = requests.get('https://swapi.dev/api/' + (l[int(choice) - 1]) + "/?page=1")
    json_string = response.text
    page_data = json.loads(json_string) 
```

#### Loading Subsequent Pages
Then I used a while loop that ran while ```page_data['next'] != None``` and appended each page by subscripting ```page_data``` at ```'results'```

#### Loading Final Page
I then had to run the for loop one more time to account for the final page:

```python
for result in page_data['results']:
        all_pages_list.append(result)
```

The previous for loop looped through all the pages and appended, and then requested the data for the next page. However, becaused of the while loop, the for loop never appended that last page after loading it and defining it as ```page_data``` so the for loop above appends the last page loaded in the for loop that was never appended.

### Generating a List of Titles and Names and URLs

I then created a blank list for all objects that weren't films (which were defined under a different name; `title` instead of `name`), for all objects that were films, and for urls.

#### Generating a List of Titles

If the user chose 3 in the main menu (meaning they had clicked films to explore), I would run through every object in the list of all the pages, and if that object contained `title` I appended the title to the list of films.

```python
film = []
if choice == "3":
        for object in all_pages_list:
	           film.append(object['title'])
```

#### Generating a List of Names

If the user chose anything other than 3 in the main menu (meaning they had clicked on soemthing other than films), I would run through every object in the list of all the pages, and if that object contained `name` I appended the name to the list of names. 

```python
not_film = []
else:
        for object in all_pages_list:
	           not_film.append(object['name'])
```

#### Generating a List of URLs

I also looped through every object in the list of all the pages and pulled the url out of them which I then put into a list.

```python
url_list = []
for object in all_pages_list:
        url_list.append(object['url'])
```

### Generating a List of Numbers which Correspond to the Titles and Names

I then created a list of numbers which corresponded to the length of the list of films and a list of numbers which corresponded to the length of the list of everything that wasn't a film.

```python
    numb_film = []
    numb_not_film = []


    for y in range(len(film)):
        numb_film.append(y + 1)

    for z in range(len(not_film)):
        numb_not_film.append(z + 1)
```

### Printing the Sub Menu

I then printed the numbers next to all of the names or titles (depending on what they chose in the main menus).

```python
    for i in range(len(film)):
        num = numb_film[i]
        title = film[i]
        print(num, "  ", title)

    for name in range(len(not_film)):
        num = numb_not_film[name]
        name = not_film[name]
        print(num, "  ", name)
```

![Screenshot 2022-01-30 213433](https://user-images.githubusercontent.com/89275837/151743947-07de005d-4059-44ef-b967-3f03f05c0ba1.png)

This worked because the number and title/name were indexed at the same thing.

### Evaluating the Choice of the User Within the Sub Menu

To evaluate the user's choice within the sub menu, I requested data from the url_list indexed at the user's choice minus 1 (as lists start at 0).

```python

    response = requests.get(url_list[(choice2 - 1)])
    json_string = response.text
    object = json.loads(json_string) #convert json string to dictionary

```

## Page Menu

Using the data from the url provided by the sub menu, I used a separate function called `page_menu` which converted the url into a neat menu. I created a blank list called `item_list` which would contain all of the names/titles of the different urls within the page menu. The user wouldn't want to look at a url, but instead the name of the thing that the url contained data on. 

```python
item_list = []
```

I also created a blank dictionary called `name_title_dict` and a variable called `n` which I set at 1. The `name_title_dict` dictionary will later be returned to the `main` function to achieve the infintesmal quality of the code. 

```python
    name_title_dict = {}

    n = 1
```

To do this, I ran through each key in the object and defined value as the object indexed at the key. 

```python
    for key in object:
        value = object[key]
```

### If Value is a List
If the value was a list, that meant it was a list of urls (all of the lists in the page data in this API are lists of urls). I would then generate the data from each of the urls within the list

```python
        if type(value) == list:
            for url in value:
                
                data = get_dict_from_url(url)
```

Then, if the list of urls had come from the 'films' key, I would append the title of the film to `item_list` and if the list of urls had come from any key that wasn't the 'films' key, I would append the name of the object to `item_list`.

```python
                if key == 'films':
                    item_list.append(data['title'])
                    
                else:
                    item_list.append(data['name'])
```

I then added a key/value pair to the `name_title_dict` dictionary and increased n by 1:

```python
name_title_dict[n] = url
```

### If Value is not a List but It Is a URL

If the value was not a list but is still a url, I generated the data from the url.

I would append the title/name (depending on whether the key of the value was 'films') to `item_list`, add a key/value pair to `name_dict_title`, and increase `n` by 1.

```python
        elif type(value) == str and 'https' in value:
            
                data = get_dict_from_url(value)
                
                if key == 'films':
                    item_list.append(data['title'])
                    name_title_dict[n] = value
                    n = n + 1
                    
                elif key != 'url':
                    item_list.append(data['name'])
                    name_title_dict[n] = value
                    n = n + 1
```

### If Value is not a URL

I would print the key next to the value shown below:

![Screenshot 2022-01-30 220458](https://user-images.githubusercontent.com/89275837/151746538-bdbfcb92-7108-4dce-8c16-a3f96487fe62.png)

### Printing the Number Next to the Item

I then reset n at 1 and looped through every item in `item_list`, printing the number next to the item and adding 1 to n each time.

```python
    n = 1
    
    for item in item_list:
        print("%-10s %-20s" % (n, item))
        n = n + 1
```

### Returning the Name Title Dictionary

At the end of the function, I returned `name_title_dict`

## Infinite Nature of Code

Back in the `main` function, I defined `name_title_dict` as the result of putting the url chosen by the user in the sub menu through the `object_menu` function.

### While Loop

I then created a while loop which provides the user with a new input. If the choice of the user is greater then the numbers correlating to the names of the urls in the object menus, I break the code so that instead of a messy stop of code, it cleanly stops. I then load the data from the url of the object that the user selected.

```python
    while(True):
        choice3 = int(input())
        if len(name_title_dict) < choice3:
            break
        response = requests.get(name_title_dict[choice3])
        json_string = response.text
        object = json.loads(json_string) #convert json string to dictionary
        name_title_dict = object_menu(object)
```

## Files

I used a main file ([main.py](https://github.com/kehillah-coding-2022/json-api-EytanGF/blob/main/main.py)) and a module file ([funcs.py](https://github.com/kehillah-coding-2022/json-api-EytanGF/blob/main/funcs.py)) when writing this code.
