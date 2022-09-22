import random
numbers = []
def numinput(gennumbers):
    gennumbers = []
    numlen = int(input('how many numbers do you want to generate?'))
    for i in range(numlen):
        numin = random.randint(1,100)
        gennumbers.append(numin)
    print(gennumbers)
    return(gennumbers)
def Bub_sort(numbers,numlen):
    templist = numbers
    sorted = 0
    pos = 0
    sorts = 0
    while sorted == 0:
        for x in range(numlen-1):
            for i in range(numlen-1):
                #print('pos',pos)
                temp1 = templist[pos]
                temp2 = templist[pos+1]
                #print('temp 1 & 2: ',temp1,temp2)
                if temp1 > temp2:
                    temptemp = temp1
                    temp1 = temp2
                    temp2 = temptemp
                    #print(temp1,temp2,temptemp)
                    templist[pos] = temp1
                    templist[pos+1] = temp2
                pos = pos+1
                sorts = sorts+1
            pos=0
        sorted=1
    return(numbers)

numbers = numinput(numbers,)
numbers = Bub_sort(numbers,len(numbers))
print(numbers)