questions = [
          
           [
         "Which planet is known as the Red Planet?" ,
        
            "Venus","jupiter","Mars", "Saturn",3
           ],
          
           [
               "Who was the first President of India?", " Dr. Rajendra Prasad ","Sardar Vallabhbhai Patel"," Jawaharlal Nehru",
            "B. R. Ambedkar",1
            ],

           [
               "What is the capital of Australia ?"," Sydney","Canberra" , "Melbourne" ,"Perth" ,2
               ],

           [
               "Which is the largest continent in the world?", "Africa","North America","Asia ","Antarctica",3
               ],

           [
               "Which is the longest river in the world?",  "Amazon","Nile ","Yangtze","Mississipp",2
               ],

           [
               "Who discovered gravity?","Isaac Newton","Albert Einstein","Galileo Galilei","Nikola Tesla",1 
               ],

           [
               "In which year did India gain independence?", "1945","1946", "1947" ,"1974",3
               ],

           [
               "Who was the first Prime Minister of India?"," Jawaharlal Nehru","Lal Bahadur Shastri","Indira Gandhi"," Rajiv Gandhi",1
               ],

           [
               "Which movement was led by Mahatma Gandhi in 1942?","Quit India Movement","Civil Disobedience Movement","Non-Cooperation Movement"," Dandi March",1
               ],

           [
               "Who was the last Mughal emperor of India?"," Akbar","Aurangzeb", "Bahadur Shah Zafar","Shah Jahan",3
               ],


           [
               "The Jallianwala Bagh massacre took place in which year?","1919","1920","1931","1942",1
               ],

           [
               "Which is the longest river in India?","Yamuna","Brahmaputra","Ganga"," Godavari",3
           ],

           [
               "Which is the highest mountain peak in India?","Kangchenjunga", "Mount Everest","Nanda Devi","K2",1
               ],

           [
               "Which is the largest state in India by area?","Rajasthan","Maharashtra","Uttar Pradesh","Madhya Pradesh",1
               ],
           
           [
               "What is the capital of Kerala?"," Kochi","Thiruvananthapuram"," Kozhikode","Ernakulam",2
               ],
           
           [
               "The Sundarbans, famous for Royal Bengal Tigers, is located in which state?","Odisha","West Bengal ","Assam","Jharkhand",2
               ],

            ["What is the chemical symbol of Gold?","Ag","Au"," Pb","Pt",2
               ],

            ] 


levels = [
    1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 
          10000000, 50000000, 700000000 
 ] 

# Welcome message

print("\n🔵 Welcome to 'Kaun Banega Crorepati'! 🔵\n")
print("Answer the questions correctly to win the grand prize of Rs. 7 Crore!\n")


for i in range (0, len(questions)):
    question=questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"{question[0]}")
    print(f"a. {question[1]}                   b. {question[2]}")
    print(f"c. {question[3]}                   d. {question[4]}")
    reply= int(input("enter your answer (1-4) : "))
    if (reply==question[-1]):
     print(f"correct answer, you have won Rs.{levels[i]}")
     if (i==4):
            money=10000
     elif(i==9):
            money=320000
     elif(i==14):
            money=10000000


     elif(i==16):
            money=70000000
    else:
        print("wrong answer !")
        break
else:
    print("Congratulations! You have won the game.")
    

print(f"you can take money for home is: {money}")





        # que=que1[i]
# print(f"which language was used to create Fb {que[i]}")
# print(f"Who was the first President of India? {que[i]}")
# print(f"What is the capital of Australia {que[i]}")
# print(f"Which is the largest continent in the world? {que[i]}")
# print(f"Which is the longest river in the world{que[i]}")
# print(f"Who discovered gravity? {que[i]}")
# print(f"In which year did India gain independence? {que[i]}")
# print(f"Who was the first Prime Minister of India? {que[i]}")
# print(f"Which movement was led by Mahatma Gandhi in 1942 {que[i]}")
# print(f"Who was the last Mughal emperor of India? {que[i]}")
# print(f"The Jallianwala Bagh massacre took place in which year? {que[i]}")
# print(f"Which is the longest river in India? {que[i]}")
# print(f"Which is the highest mountain peak in India? {que[i]}")
# print(f"Which is the largest state in India by area? {que[i]}")
# print(f"What is the capital of Kerala? {que[i]}")
# print(f"The Sundarbans, famous for Royal Bengal Tigers, is located in which state? {que[i]}")
 


