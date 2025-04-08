from time import *
import random as r


# print(time())

def mistake(partest,usertest):
  error = 0
  for i in range (len(partest)):
    try:
      if partest[i] != usertest[i]:
        error = error + 1
      
    except:
        error = error + 1
  return error
         
def speed_time (time_start, time_end, userinput):
 time_delay = time_end-time_start
 time_R =round(time_delay,2)
 speed = len(userinput)/ time_R
 return round(speed) 
       

 
 test =[
    "A paragraph is a series of sentences that are organized and coherent,"
" and are all related to a single topic. "
"Almost every piece of writing you do that is longer than a few sentences should be organized into paragraphs. "
"This is because paragraphs show a reader where the subdivisions of an essay begin and end,"
" and thus help the reader see the organization of the essay and grasp its main points.", 
"my name is jay kumar singh",
"welcome to our family"
]
test1 =r.choice(test)
print("---------typing speed -----------")
print(test1)

print()
print()
time_1 =time()
testinput=input("Enter: ")
time_2 = time()


print('Speed : ',speed_time (time_1, time_2, testinput), "w/sec")
print('Error : ',  mistake(test1,testinput))



