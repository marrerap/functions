# Global scope
global_vairable = "place variable outside of function or loops etc for global scope"

# Local scope
def greet():
    phrase = 'hello'
    print(phrase)

greet()

#from this point and before, i cannot use the phrase variable outside of the greet function.
#from this point and below you still cannot acccess the internal variables of the def function
def greet2(name):
    phrase2 = "Hey"
    print(phrase2, name)

greet2()

