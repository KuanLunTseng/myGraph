from copy import deepcopy as cpy
import json 
import random
from name import *

class Person(object):
    def __init__(self, name, friend_list):
        self.name = name
        self.friend_list = friend_list

def rand_friend_list(NAME, name):
    friend_list = cpy(NAME)
    
    # yourself cannot be your friend 
    friend_list.remove(name)
    n = random.randint(0, len(friend_list))
    random.shuffle(friend_list)
    
    return sorted([friend_list.pop() for i in range(n)])
    
def write_json_file(k):
    NAME = k_list(k)
    NUM = len(NAME)
    data = {}
    data['people'] = []
    for n in NAME:
        data['people'].append({
            'Name': n,
            'Friends': rand_friend_list(NAME,n)
        })

    with open('data.json', 'w') as outfiles:
        json.dump(data, outfiles)

def mfriend(k):
    write_json_file(k)
    with open('data.json') as json_file:
        data = json.load(json_file)
    
    return [Person(p['Name'], p['Friends']) for p in data['people']]

