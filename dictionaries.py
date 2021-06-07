#dicitonaries are defined with {}


friend = {
    'name': 'Alan Touring',
    'cell': '1234656',
    'birthday': 'june 23'
}
#empty dictionary
nothing = {}

# values can be anything 
superhero = {
    'name': 'Tony Stark',
    'level': 9,
    'avenger': True,
    'gear': ['happy', "sad", 'mediocre'],
    'vehicle': {
        'make': "audi",
        'model': 'R8'
    },
}

print(superhero['gear'])

for key, value in superhero.items():
    print(f"Superhero's {key} is")
    print(value)