hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}
#checking in and out of hotel rooms for guests and reservations
check_in_out = input("Will you be \"checking in\" (1) or \"checking out\" (2): ")


floor_number = input("What floor is your room on: ")
room_number =  input("What is your room number: ")

if check_in_out == "1":
    room_occu_in = int(input("How many occupants will reside during your stay: "))
    print(room_occu_in)
    room_names = []
    for name in range(0, room_occu_in):
        room_name_in = input("Enter name of your current/next guest: ")
        room_names.append(room_name_in)
    hotel[floor_number][room_number] = room_names
elif check_in_out == "2":
    floor_num_out = int(input("What is your floor number: "))
    print(floor_num_out)
    room_num_out = int(input("What is your room number: "))
    print(room_num_out)
    hotel[floor_num_out][room_num_out] = ["Vacant"]

# verifying if a room is available
room_vacancy = input("What room would you like to verify: ")

print(hotel)

