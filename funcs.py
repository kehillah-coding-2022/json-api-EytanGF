import json
import requests


def main():
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
    url_list = []

    if choice == "3":
        for object in all_pages_list:
	           film.append(object['title'])
    else:
        for object in all_pages_list:
	           not_film.append(object['name'])

    for object in all_pages_list:
        url_list.append(object['url'])

    # TODO: if extra time, menus

    numb_film = []
    numb_not_film = []


    for y in range(len(film)):
        numb_film.append(y + 1)

    for z in range(len(not_film)):
        numb_not_film.append(z + 1)


    for i in range(len(film)):
        num = numb_film[i]
        title = film[i]
        print(num, "  ", title)

    for name in range(len(not_film)):
        print(numb_not_film[name], "  ", not_film[name])

    choice2 = int(input())

    response = requests.get(url_list[(choice2 - 1)])
    json_string = response.text
    object = json.loads(json_string) #convert json string to dictionary

    name_title_dict = page_menu(object)

    while(True):
        choice3 = int(input())
        if len(name_title_dict) < choice3:
            break
        response = requests.get(name_title_dict[choice3])
        json_string = response.text
        object = json.loads(json_string) #convert json string to dictionary
        name_title_dict = page_menu(object)


def page_menu(object):
    spc = " "

    #name_list = []
    #title_list = []
    item_list = []

    name_title_dict = {}

    n = 1
#    print(object)
    for key in object:
        # modify field width and justification
        value = object[key]
        #print(key)
        #print(value)

        if type(value) == list:
            for url in value:
                data = get_dict_from_url(url)
                if key == 'films':
                    item_list.append(data['title'])
                else:
                    item_list.append(data['name'])
                #go to list and each link in list and get name/title from each url
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

        #     for item in name_list:
#             print("%-10s %-20s" % (n, item))
        #     #get url and print object of name unlesss film, then print title

        else:
            print("%-10s %-10s %-20s" % (spc, key, value))

    n = 1
    for item in item_list:
        print("%-10s %-20s" % (n, item))
        n = n + 1
#    for item in name_list:
#        print("%-10s %-20s" % (n, item))
#        n = n + 1

    return(name_title_dict)



    #people objects that have urls:
    #homeworld, films, species, vehicles,
    #check type using type() function and do 2 values, one for urls which are strings, and others which are strings inside lists, check if https is in the strings
    #if "https" in string









#add somevalue at the end of each input value to go back and to quit using [-1]


def get_people():
    """
    return a dictionary based on the json response from swapi
    for a given person number
    """

    response = requests.get('http://swapi.co/api/people/%s/' % n) #string format
    json_string = response.text
    data = json.loads(json_string) #convert json string to dictionary
    return data


def get_dict_from_url(x):

    """
    return a dictionary based on the json response from swapi
    for a given url
    """

    response = requests.get(x) #string format
    json_string = response.text
    data = json.loads(json_string) #convert json string to dictionary
    return data

'''
generates 2 different random numbers for game which compares 2 different people's heights or somevalue like that
'''
# a = random.randint()
# b = random.randint()
#
# while a == b:
#     a = random.randint()
