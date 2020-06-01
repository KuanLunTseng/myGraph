from copy import deepcopy as cpy
import json 
import random

NAME = ["Aaron", "Baldhere", "Camillia", "Dunstin", "Eulalia", "Francisco", "Gregory", "Hinrick", "Irina", "Jovonnah", "Krystiano", "Lucena", "Martha", "Norris", "Owain", "Pyrena", "Quinn", "Renato", "Salomon", "Toynetta", "Una", "Verlin", "Wythe", "Xena", "York", "Zaza"]
NUM = len(NAME)

class Person(object):
    def __init__(self, name, friend_list):
        self.name = name
        self.friend_list = friend_list

def rand_friend_list(name):
    friend_list = cpy(NAME)
    
    # yourself cannot be your friend 
    friend_list.remove(name)
    n = random.randint(0, len(friend_list))
    random.shuffle(friend_list)
    
    return sorted([friend_list.pop() for i in range(n)])
    
def write_json_file():
    data = {}
    data['people'] = []
    for n in NAME:
        data['people'].append({
            'Name': n,
            'Friends': rand_friend_list(n)
        })

    with open('data.json', 'w') as outfiles:
        json.dump(data, outfiles)

def read_json_file():
    with open('data.json') as json_file:
        data = json.load(json_file)
    
    return [Person(p['Name'], p['Friends']) for p in data['people']]



def main():
    # You should comment out the code below because you only need it once
    #write_json_file()
    
    network = read_json_file()
    for n in network:
        print(n.name)
        print(n.friend_list)
        print('')

if __name__ == '__main__':
   main()
