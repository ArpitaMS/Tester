from time import *
import random
def mistake(partest,usertest):
    error = 0
    for i in range (len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error +1
        except:
            #for blank test
            error= error+1
    return error

def speed_time(time_start,time_end,userinput):
    time_delay = time_end - time_start
    time_round= round(time_delay,2)
    speed = len(userinput)/time_round
    return round(speed)

test=["This is a test for calculating your typing speed","Paragraph can contain two to ten sentences connected to eachother",
      "Para is self contained unit of discourse dealing with a particular point"]

test1=random.choice(test)
print("    ^^^^^  Typing Speed   ^^^^^    ")
print(test1)
print()
print()
time_1=time()
testinput=input('Enter :')
time_2=time()

print('Speed:', speed_time(time_1,time_2,testinput),"w/sec")
print('Error:',mistake(test1,testinput))
