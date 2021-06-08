#request what the user wants for christmas


list_of_wants = []
num_of_wants = int(input("How many gifts do you want for Christmas? "))

for i in range(0, num_of_wants):
  wants = input("What do you want for Christmas? ")
  list_of_wants.append(wants)  

#request if user has been good or bad
attitude = input("Have you been \"good\" or \"bad\" this year? ")

# determine what is printed based on the attitude variable
if attitude == "good":
    print(list_of_wants)
elif attitude == "bad":
    print("Really.... get ready for a lump of coal!!!")
else:
    print("Please enter either \"good\" or \"bad\"!!!")