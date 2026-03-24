
# importing the pyttsx library 
import pyttsx3 
#inlistion
 
x= pyttsx3.init() 
print("welcome to robo speker created by Gaurav")
while True:
    y=input("enter here what you want to speak:")    
    if y == "thankyou":
            x.say("thankyou   for   using     robospeker " ) 
    else:
            x.say(y)
    x.runAndWait()