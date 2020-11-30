#Question 6
class Address ():
    def __init__(self, number, street, city, state, zipcode):
        self.number = number
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
      #define print method to print the address nicely  
    def print(self):
        print(self.number,self.street)
        print(self.city,self.state,self.zipcode)
        #define comebefore method to compare zip
    def getzip(self):
        return self.zipcode
        
    def comesBefore(self,other):
        x = other.getzip()
        if self.zipcode > x:
            print('This address come after')
        elif self.zipcode < x:
            print('This address come before')
        else:
            print('The two address have the same zipcode')
        
    
    
        
    
