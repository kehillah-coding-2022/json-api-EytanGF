import json
import requests


def main_menu():
    """
    Display a menu of three items, including 'exit'.
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

    if choice == "3":
        for thing in all_pages_list:
	           film = film + [thing['title']]
    else:
        for thing in all_pages_list:
	           not_film = not_film + [thing['name']]

    not_film = sorted(not_film)
    film = sorted(film)

    numb_film = []
    numb_not_film = []

    for y in range(len(film)):
        numb_film = numb_film + [(y + 1)]

    for z in range(len(not_film)):
        numb_not_film = numb_not_film + [(z + 1)]


    for title in range(len(film)):
        print(numb_film[title], "  ", film[title])

    for name in range(len(not_film)):
        print(numb_not_film[name], "  ", not_film[name])






def get_people():
    """
    return a dictionary based on the json response from swapi
    for a given person number
    """

    response = requests.get('http://swapi.co/api/people/%s/' % n) #string format
    json_string = response.text
    data = json.loads(json_string) #convert json string to dictionary
    return data


def get_menudata():
    """
    return a dictionary based on the json response from swapi
    for a given person number
    """

    response = requests.get('https://swapi.dev/api/') #string format
    json_string = response.text
    data = json.loads(json_string) #convert json string to dictionary
    return data

'''
generates 2 different random numbers for game which compares 2 different people's heights or something like that
'''
# a = random.randint()
# b = random.randint()
#
# while a == b:
#     a = random.randint()
