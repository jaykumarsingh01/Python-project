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

