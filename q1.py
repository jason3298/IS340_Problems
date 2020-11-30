class Time: #create time class
   def __init__(self, hour, minute): #create instance variables
       self.hour = hour
       self.minute = minute
   def resetTime(self): #create reset time method
       self.hour = 00
       self.minute = 00
   def addMinute(self): #create add one minute to the time
       if self.minute == 59: #if minute equal to 59
           self.minute = 0
           self.hour += 1 #add 1 to hour
       elif self.minute != 59: #otherwise just add 1 minute to the time
           self.minute += 1
           
   def printTime(self):
       print("%02d"%self.hour,':',"%02d"%self.minute) #create printTime method
#main program to run the class
#demonstrate Time class
def main():
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
main()
