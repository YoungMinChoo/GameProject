#While loops and functions

def counting_function(count, run):

    if count < 5:
        print(count)
    if count >= 5:
        run = False
    count+= 1
    return count, run

run = True
count = 0
while run:
    count, run = counting_function(count, run)