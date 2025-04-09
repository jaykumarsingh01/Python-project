from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_start, time_end, userinput):
    time_delay = time_end - time_start
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)

while True:
    ck = input("Ready to test: yes / no: ").lower()

    if ck == "yes":
        test = [
            
            "My Name is Jay Kumar Singh"
         
        ]
        test1 = r.choice(test)
        print("--------- Typing Speed Test -----------")
        print(test1)
        print()
        print()
        time_1 = time()
        testinput = input("Enter: ")
        time_2 = time()

        print('Speed:', speed_time(time_1, time_2, testinput), "w/sec")
        print('Error:', mistake(test1, testinput))

    elif ck == "no":
        print("Thank you!")
        break

    else:
        print("Wrong input, please type 'yes' or 'no'.")

                                                          # Jay Kumar Singh
