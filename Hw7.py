#Question 6:
inputfilename = input('Enter file name:')
infile = open(inputfilename,'r') #input and open file
catlist=[] #Create a list to save the data 
total_dinner=0 #initialize total for both services
total_lodging=0
for line in infile: #loop through each lines
    catlist = line.split(';') #split by ;
    service=catlist[1] #save the name of the service in a variable
    amt=float(catlist[2]) #save the amt
    if service == "Dinner": #compare the service and add up the total
        total_dinner = total_dinner+amt
    if service == "Lodging":
        total_lodging= total_lodging + amt
infile.close()
print('The total revenue from dinner is:',total_dinner) #Print the result
print('The total revenue from lodging is:',total_lodging)
