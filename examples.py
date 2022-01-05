import requests
import json

def get_person(n):
    """
    return a dictionary based on the json response from swapi
    for a given person number
    """

    response = requests.get('http://swapi.co/api/people/%s/' % n) #string format
    json_string = response.text
    data = json.loads(json_string) #convert json string to dictionary
    return data


def menu():
    """
    Display a menu of three items, including 'exit'.
    """
    exit = False
    while not exit:
        print('1. Apples')
        print('2. Oranges')
        print('3. Exit')
        choice = input('Make a selection')
        if choice ==  '1':
            print('applesauce')
        elif choice == '2':
            print('orange julius')
        elif choice == '3':
            print('exiting...')
            exit = True
        else:
            print('Unrecognized input: ' + choice)
