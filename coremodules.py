import random
def login(username, password):
    authplayers = [
    {'username': 'admin', 'password': 'test'},
    {'username': 'mshashmi', 'password': 'test'},
    {'username': 'amen', 'password': 'test'}
    ]

    auth = False

    for item in authplayers:
        if username == item['username'] and password == item['password']:
            print('Login Succesful!')
            auth = True
            return True            
        else:
            continue
    if auth == False:
        return False


def randomgen():
    # generates number between 1 and 6, simulates dice roll.
    val = random.randint(1,6)
    return val

def evenorodd(num):
    # returns true if even, else: its odd
    if num % 2 == 0: return True
    else: return False


    


                    



    


