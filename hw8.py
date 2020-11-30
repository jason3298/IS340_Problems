#Question 6
wordcounts={'and': 2, 'make': 1, 'everything': 1, 'become': 1, 'better': 1, 'the': 2, 'second': 1, 'one': 1, 'is': 1, 'called': 1, 'life': 1, 'liberty': 1, 'pursuit': 1, 'of': 1, 'paper': 1, 'which': 1, 'was': 1, 'choreographed': 1, 'by': 1, 'Radhanath': 1, 'Thialan\n': 1}
#the dictionary from last file
cache = {"q5hw8.txt":"wordcounts"}
filename=input('Please enter your file name,enter ! to quit:')
while filename !=  '!': #while not sentinel
    
    if filename in cache:
        print ('Your file name has been entered!') 
        x=cache.get(filename)
        print('Please look up for this dictionary:',x)
        #Show the name of the dictionary when filename already in cache
        filename=input('Please enter your file name:') 
    else:
        


        infile=open(filename,'r')#open file
        counts={}
        list0=[]

        for line in infile:
            
            list1 = line.split(" ") #split word in file
            list0=list0+list1
        for element in list1:
            if element not in counts: #if word not in the dictionary,add it with key = 1
                counts[element] = 1
            elif element in counts:
                counts[element] += 1
                #if word in the dictionary, the key plus 1
        cache[filename]='counts'
        print(counts) #print the dictionary
        print('This is the list of the file you"ve entered',cache)
        filename=input('Please enter your file name:')
        infile.close
