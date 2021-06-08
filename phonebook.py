phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

phone_list = phonebook_dict
#print only Elizabeth's phone number not name.
print(phonebook_dict["Elizabeth"])

#add a new key and value to the dictionary
phonebook_dict["Kareem"] = "938-489-1234"

#print the changes made
print(phone_list)

#del a key and value from a dictionary
del phonebook_dict["Alice"]

# change the value for a key in a dictionary
phonebook_dict['Bob'] = '968-345-2345'
print(phone_list)
