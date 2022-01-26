_input= []

for num in open('2_input.txt'):
    data= num.split()
    data[1]= int(data[1])
    _input.append(data)

horizontal= 0
depth= 0
aim= 0

for val in _input:
    if val[0] == 'forward':
        horizontal += val[1]
        depth += aim*val[1]
    elif val[0] == 'up':
        aim -= val[1]
    elif val[0] == 'down':
        aim += val[1]
    else:
        pass

print(horizontal*depth)