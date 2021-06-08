import pickle
# pickle allows us to serialize/deserialize 


with open('todo.pickle', 'rb') as file_handle:
    todos = pickle.load(file_handle)
    #print(todos)
    for i in todos:
        if i['completed']:
            print(f"Done: {i['title']}")
        else:
            print(f"Todo: {i['title']}")