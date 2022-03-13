import sys
import clipboard
import json

SAVED_DATA = 'clipboard.json'

def save_data(filepath, data):
    with open(filepath,"w") as f:
        json.dump(data,f)

def load_data(filepath):
    try:
        with open(filepath,'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv ) == 2:
    command = sys.argv[1].lower()
    data = load_data(SAVED_DATA)
    #save
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA,data)
        print("Data saved!")
    #load
    elif command == "load":
         key = input("Enter a key: ")
         if key in data:
             clipboard.copy(data[key])
             print("Data Copied.")
         else:
             print("Key does not exist.")
    #list
    elif command == "list":
        print(data)
    #remove key
    elif command == 'remove':
        key = input("Enter a key: ")
        if key in data: 
            data.pop(key)
            save_data(SAVED_DATA,data)
        else: print("Key does not exist.")
    #unknown command
    else:
        print("Unkown command. Save, Load, List, and Remove only!")
else: 
    print("Please pass exactly one command.")