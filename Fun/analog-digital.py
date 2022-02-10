import random

def send(data):
    returned= convert(data)
    if returned == 0:
        print("received signal!")
    

def convert(data):
    if data%2 == 0:
        return 0
    else:
        return 1

for i in range(10):
    x = random.randrange(0, 10)
    send(x)

