#Question 5
def find(text,string):
    char_num = 0 #save the positon of character in char_num
    y = len(text)-len(string) #save the last potition of character in y
    x = text[char_num:len(string)]
    #if the first characters in text equal to string then end the recursion
    if x == string:
        return True
    else:
        while char_num <= y:
            char_num +=1
            x = text[char_num:char_num+len(string)]
            if x == string:
                char_num = y+1
                #end the process and return True when x = string
                return True
            elif char_num == y and x != string:
                #end the process and return false after the last x
                return False
                
        
            
            
            
def main():
    #demonstrate the find function
    print(find("Mississippi","sip"))
    print(find("Mississippi","pip"))
main()
    
    
