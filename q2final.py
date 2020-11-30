class Time: #create time class
    def __init__(self, hour, minute): #create instance variables 
        self._hour = hour
        self._minute = minute
    def resetTime(self): #create reset time method
        self._hour = 00
        self._minute = 00
    def addMinute(self): #create add one minute to the time
        if self._minute == 59: #if minute equal to 59
            self._minute = 0
            self._hour += 1 #add 1 to hour
        elif self._minute != 59: #otherwise just add 1 minute to the time
            self._minute += 1
            
    def printTime(self):
        print("%02d"%self._hour,':',"%02d"%self._minute) #create printTime method
            
            
        
    
    
