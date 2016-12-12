# This is the start of my file.
file = open('file.txt', 'w')

# create the list
for n in range(10):
    file.write(input('Say something to me now. ') + '\n')

# close file
file.close()