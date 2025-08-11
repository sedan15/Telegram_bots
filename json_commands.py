import json

def read_json(filename): 
    with open(f'data/{filename}','r') as f:
        file = json.load(f)
    return file

def write_json(filename,users):
    with open(f'data/{filename}','w') as f:
        json.dump(users,f)
