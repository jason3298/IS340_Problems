#demonstrate Time class
from q2final import Time #demonstrate Time class
t = Time(20,58) #Create current time
print('The current time is:') 
t.printTime() #print the current time
t.addMinute()
t.addMinute()
t.addMinute() #add 3 minutes
print('The time after three minute is:')
t.printTime() #print the time after adding 3 minutes
t.resetTime() #reset time
print('The reset time is:')
t.printTime() #print the reset time

