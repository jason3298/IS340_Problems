class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
    def resetTime(self):
        self.hour = 00
        self.minute = 00
    def addMinute(self):
        if self.minute == 59:
            self.minute = 0
            self.hour += 1
        elif self.minute != 59:
            self.minute += 1
            self.hour += 1
    def printTime(self):
        print("%02d"%self.hour,':',"%02d"%self.minute)
            
            
        
    
    
