import json
import requests


def main_menu():
    """
    Display a menu of three items, including 'exit'.
    """
    l = ["people", "planets", "films", "species", "vehicles", "starships", "exit"]
    for x in range(len(l)):
        print(x+1, "  ", l[x])
    # z = get_menudata()
    choice = input()
    if choice == "7":
        quit()
    response = requests.get('https://swapi.dev/api/' + l[int(choice) - 1])
    json_string = response.text
    data = json.loads(json_string) #convert json string to dictionary
    exit = False
    while not exit:
        if choice == "3":
            for thing in data['results']:
    	           print(thing['title'])
        else:
            for thing in data['results']:
    	           print(thing['name'])
            choice1 = input('Make a selection')
        if choice ==  '1':
            print('applesauce')
        elif choice == '2':
            print('orange julius')
        elif choice == '3':
            print('exiting...')
            exit = True
        else:
            print('Unrecognized input: ' + choice)
    # return data

# def sub_menu():
#     '''
#     get a navigatable list of names that will return the data
#     '''
#     if

# def sub_menu():
#
# def



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
