import json
import requests


def main():
    """
    Run main code which calls on a different function and runs an infinately navigatable menu of data from the Star Wars API
    """
    l = ["people", "planets", "films", "species", "vehicles", "starships", "exit"]

    for x in range(len(l)):
        print(x+1, "  ", l[x])

    choice = input()
    if choice == "7":
        quit()

    all_pages_list = []

    response = requests.get('https://swapi.dev/api/' + (l[int(choice) - 1]) + "/?page=1")
    json_string = response.text
    page_data = json.loads(json_string) #convert json string to dictionary


    while page_data['next'] != None:
        for result in page_data['results']:
            all_pages_list.append(result)

        response = requests.get(page_data['next'])
        json_string = response.text
        page_data = json.loads(json_string)

    for result in page_data['results']:
        all_pages_list.append(result)

    not_film = []
    film = []
    url_list = []

    if choice == "3":
        for object in all_pages_list:
	           film.append(object['title'])
    else:
        for object in all_pages_list:
	           not_film.append(object['name'])

    for object in all_pages_list:
        url_list.append(object['url'])

    numb_film = []
    numb_not_film = []


    for y in range(len(film)):
        numb_film.append(y + 1)

    for z in range(len(not_film)):
        numb_not_film.append(z + 1)


    for title in range(len(film)):
        num = numb_film[title]
        title = film[title]
        print(num, "  ", title)

    for name in range(len(not_film)):
        num = numb_not_film[name]
        name = not_film[name]
        print(num, "  ", name)

    choice2 = int(input())

    response = requests.get(url_list[(choice2 - 1)])
    json_string = response.text
    object = json.loads(json_string) #convert json string to dictionary

    name_title_dict = object_menu(object)

    while(True):
        choice3 = int(input())
        if len(name_title_dict) < choice3:
            break
        response = requests.get(name_title_dict[choice3])
        json_string = response.text
        object = json.loads(json_string) #convert json string to dictionary
        name_title_dict = object_menu(object)


def object_menu(object):
    '''
    Generate the interactive menu of a page given an object
    '''
    spc = " "

    item_list = []

    name_title_dict = {}

    n = 1

    for key in object:
        value = object[key]


        if type(value) == list:
            for url in value:

                data = get_dict_from_url(url)

                if key == 'films':
                    item_list.append(data['title'])

                else:
                    item_list.append(data['name'])

                name_title_dict[n] = url
                n = n + 1

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

        else:
            print("%-10s %-10s %-20s" % (spc, key, value))

    n = 1

    for item in item_list:
        print("%-10s %-20s" % (n, item))
        n = n + 1

    return(name_title_dict)


def get_dict_from_url(x):

    """
    return a dictionary based on the json response from swapi
    for a given url
    """

    response = requests.get(x) #string format
    json_string = response.text
    data = json.loads(json_string) #convert json string to dictionary
    return data
