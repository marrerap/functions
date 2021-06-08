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

# retrieve the email address only
ramit_add = ramit['email']
#retieve the first interest in the interest list
ramit_first_int = ramit["interests"][0]
# retrieve jas from a nested list and display her email
jas_email = ramit['friends'][0]['email']
# retrieve jan's second interest 
jan_interests = ramit['friends'][1]['interests'][1]




print(ramit_add , ramit_first_int, jas_email, jan_interests)