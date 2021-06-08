ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
#name the function 
def count_friends(ramit):
    #get the loop going for each item in the list
    for i in ramit:
        # this will check if each instance in "friends" is a list 
        # to count each friend because each friend has thier
        # own list. if i was counting strings i would relpace
        # list with string
        if isinstance(ramit['friends'], list):
            #define the count for the loop
            count = 0
            # this will add the number of list instances to the
            #  counter above
            count += len(ramit['friends'])
        #be sure to return a value to the function 
        return(count)

#create a variable to dislay the results of the function
friend_counter = count_friends(ramit)
# add the counter to the list
ramit['friends_count'] = friend_counter
# display the new list
print(ramit)


