import sys
print(sys.executable)
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image
import random

#ro1_que= round 1 questions
#ro2_que= round 2 questions
#ro3_que= round 3 questions
#ro1_ans_ch= round 1 answers choice
#ro2_ans_ch= round 2 answers choice
#ro3_ans= round 3 answers
#ro1_ans= round 1 answers
#ro2_ans= round 2 answers
#ro1shuff= shuffle ro1 questions
ro1_que= [
    "Who is the author of the book '1984'?",
    "Which of the following keyword is used to create a function in Python ?",
    "To Declare a Global variable in python we use the keyword ?",
    "The lead character in the film 'The Bandit Queen' has been played by",
    "The famous book 'Anandmath' was authored by",
    ]

ro2_que= ['''It was a hot day and 4 couples drank together 44 bottles of cold drink. 
          Anita had 2, Biva 3, Chanchala 4 and Dipti 5 bottles.
          Mr. Panikkar drank just as many bottles as his wife, but each of the 
          other men drank more than his wife- Mr. Dubey twice, Mr. Narayan 
          three times and Mr. Rao four times as many bottles. Then, one of the 
          following sttatements is correct. Which one is it?''',
          
          '''A bag contains coloured balls of which atleast 90% are red. Balls
          are drawn from the bag one by one and their colours are noted. It is found 
          that 49 of the first 50 balls drawn are red. Thereafter, 7 out of every 
          8 balls drawn are red. The number of balls in the bad CAN NOT be''',
          
          '''Let 'a' be the 81-digit number all digits of which are equal to 1. Then
          the number 'a' is ''',
          
          '''The number 2532645918 is divisible by''',
          
          '''The number of solutions of 2sinx+cosx=3 is'''
          
          
          ]

ro3_que= ['''How many ways are there to put one white and one black rook on a chessboard
          so that they do not attack each other?''',
          
          '''The number of different factors of 1800 equals ''',
          
          '''The sum of all the distinct four-digit numbers that can be formed using 
          the digits 1,2,3,4,5 each digit appearing atmost once is ''',
          
          '''The sum of all integers from 1 to 1000 that are divisible by 2 or 5 
          but not divisible by 4 equals ''',
          
          "The number of pairs of integers(m,n)satisfying m*2+n*2+m*n=1 is"
          ]

ro1_ans_ch= [
    ["George Orwell","Thomas Hardy","Emile Zola","Walter Scott"],
    ["function","void","fun","def"],
    ["all","var","let","global"],
    ["Rupa Ganguly","Seema Biswas","Pratibha Sinha","Shabana Azmi"],
    ["Sarojini Naidu","Bankim Chandra Chattopadhyay","Sri Aurobindo","Rabindranath Tagore"]
    ]

ro2_ans_ch= [
    ["Mrs. Panikkar is Chanchala","Anita's husband had 8 bottles","Mr.Narayan had 12 bottles",
     "Mrs.Rao is Dipti"],
    ["170","210","250","194"],
    ["Divisible by 9 but not divisible by 27",
     "Divisible by 27 but not divisible by 81",
     "Divisible by 81 but not divisible by 243",
     "Divisible by 243"],
    ["3 but not 11",
     "11 but not 3",
     "Both 3 and 11",
     "Neither 3 nor 11"],
    ["1","2","infinite","no solution"]
    ]

ro3_ans_= [
    "3136",
    "36",
    "399960",
    "175000",
    "6"
    ]
    
ro1_ans= [0,3,3,1,1]
ro2_ans= [1,2,2,2,3]

user_ans1=[]
user_ans2=[]
user_ans3=[]
indexes1=[]
indexes2=[]
indexes3=[]

def ro1shuff():               #Here, shuffling of ro1 ques is being done using random.
    global indexes1           #Randomisation will occur till the no of que is 5.
    while (len(indexes1)<5):   #Indexes1 will contain the ro1 questions and x1: value of index      
        x1=random.randint(0,4)  #If x1 is already present in the indexes1 list, then that value of x1
        if x1 in indexes1:  #will not be appended and if it's not present, it will be appended.
            continue
        else:
            indexes1.append(x1)
            
def ro2shuff():
    global indexes2
    while (len(indexes2)<5):
        x2=random.randint(0,4)   #Shuffling of ro2 que is being done.
        if x2 in indexes2:
            continue
        else:
            indexes2.append(x2)
            
def ro3shuff():
    global indexes3
    while(len(indexes3)<5):
        x3=random.randint(0,4)   #Shuffling of ro3 que is being done.
        if x3 in indexes3:
            continue
        else:
            indexes3.append(x3)
            
def ro1showresult(score):
    global r2,b6
    #For Round 1
    ro1_lblq.destroy()
    ro1_opt1.destroy()
    ro1_opt2.destroy()
    ro1_opt3.destroy()
    ro1_opt4.destroy()
    
    ro1_resultlbl= Label(
        r2,
        text=("<<Your score for Round 1 is>>"
              ,score),
        font = ("Arial",20),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "blanchedalmond",
    )
    ro1_resultlbl.pack(pady=(200,200))
    
    b6=Button(r2,text="NEXT",font=("Times New Roman",26),bg="steelblue",
              command=roundtwo)
    b6.place(x=290,y=380)
    
def ro2showresult(score):
    global r3,b7
    #For Round 2
    ro2_lblq.destroy()
    ro2_opt1.destroy()
    ro2_opt2.destroy()
    ro2_opt3.destroy()
    ro2_opt4.destroy()
    
    ro2_resultlbl= Label(
        r3,
        text=("<<Your score for Round 2 is>>"
              ,score),
        font = ("Arial",20),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "blanchedalmond",
    )
    ro2_resultlbl.pack(pady=(250,250))
    
    b7=Button(r3,text="NEXT",font=("Times New Roman",26),bg="steelblue",
              command=roundthree)
    b7.place(x=330,y=380)
    

    

#In calc(), 1st x4 and score have been initialised as 0, then for every i in indexes1
#if ro1 ans for that i matches with the index of x4 in user ans1, that means that ans is
#correct and score = score+1
def ro1calc():   
    #For round 1
    global indexes1,user_ans1,ro1_ans
    x4 = 0
    score = 0
    for i in indexes1:
        if user_ans1[x4] == ro1_ans[i]:
            score = score + 1
        x4 += 1
    print(score)
    ro1showresult(score)
    
def ro2calc():   
    #For round 2
    global indexes2,user_ans2,ro2_ans
    x5 = 0
    score = 0
    for i in indexes2:
        if user_ans2[x5] == ro2_ans[i]:
            score = score + 1
        x5 += 1
    print(score)
    ro2showresult(score)
    
#In selectedchoices(), 1st the value of radiobutton the user has chosen is got.
#Then, it is being appended to the user_ans1 list. The structure of 1 que of ro1 has been written in 
#queview(). The structure of 1 radiobutton for that question has also been written there.
#Now, therefore here, a variable ro1ques has been initialised as 1 and will run until it's 5
#that is, 1,2,3,4. According to that, the radiobutton has also been structured to run for those 4 questions.
 
ro1ques =1
ro2ques=1
ro3ques=1
def ro1selectedchoices():
    #For round 1
    global radiovar1,user_ans1
    global ro1_lblq
    global ro1_opt1,ro1_opt2,ro1_opt3,ro1_opt4
    global ro1ques
    getvalue1 = radiovar1.get()
    user_ans1.append(getvalue1)
    radiovar1.set(-1)
    if ro1ques < 5:
        ro1_lblq.config(text= ro1_que[indexes1[ro1ques]])
        ro1_opt1['text'] = ro1_ans_ch[indexes1[ro1ques]][0]
        ro1_opt2['text'] = ro1_ans_ch[indexes1[ro1ques]][1]
        ro1_opt3['text'] = ro1_ans_ch[indexes1[ro1ques]][2]
        ro1_opt4['text'] = ro1_ans_ch[indexes1[ro1ques]][3]
        
        ro1ques += 1
    else:
        ro1calc()
        
def ro2selectedchoices():
    #For round 2
    global radiovar2,user_ans2
    global ro2_lblq
    global ro2_opt1,ro2_opt2,ro2_opt3,ro2_opt4
    global ro2ques
    getvalue2 = radiovar2.get()
    user_ans2.append(getvalue2)
    radiovar2.set(-1)
    if ro2ques < 5:
        ro2_lblq.config(text= ro2_que[indexes2[ro2ques]])
        ro2_opt1['text'] = ro2_ans_ch[indexes2[ro2ques]][0]
        ro2_opt2['text'] = ro2_ans_ch[indexes2[ro2ques]][1]
        ro2_opt3['text'] = ro2_ans_ch[indexes2[ro2ques]][2]
        ro2_opt4['text'] = ro2_ans_ch[indexes2[ro2ques]][3]
        
        ro2ques += 1
    else:
        ro2calc()

          
def queview1():
    #For Round 1
    global ro1_lblq,ro1_opt1,ro1_opt2,ro1_opt3,ro1_opt4
    global r2
    ro1_lblq=Label(
        r2,
        text = ro1_que[indexes1[0]],
        font = ("Arial", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "blanchedalmond",
    )
    ro1_lblq.pack(pady=(100,30))
    
    global radiovar1
    radiovar1 = IntVar()
    radiovar1.set(-1)
    
    ro1_opt1 = Radiobutton(
        r2,
        text = ro1_ans_ch[indexes1[0]][0],
        font = ("Times", 12),
        value = 0,
        variable = radiovar1,
        command = ro1selectedchoices,
        background = "blanchedalmond",
    )
    ro1_opt1.pack(pady=5)
    
    
    ro1_opt2 = Radiobutton(
        r2,
        text = ro1_ans_ch[indexes1[0]][1],
        font = ("Times", 12),
        value = 1,
        variable = radiovar1,
        command = ro1selectedchoices,
        background = "blanchedalmond",
    )
    ro1_opt2.pack(pady=5)
    
    
    ro1_opt3 = Radiobutton(
        r2,
        text = ro1_ans_ch[indexes1[0]][2],
        font = ("Times", 12),
        value = 2,
        variable = radiovar1,
        command = ro1selectedchoices,
        background = "blanchedalmond",
    )
    ro1_opt3.pack(pady=5)
    
    
    ro1_opt4 = Radiobutton(
        r2,
        text = ro1_ans_ch[indexes1[0]][3],
        font = ("Times", 12),
        value = 3,
        variable = radiovar1,
        command = ro1selectedchoices,
        background = "blanchedalmond",
    )
    ro1_opt4.pack(pady=5)
    
def queview2():
    #For Round 2
    global ro2_lblq,ro2_opt1,ro2_opt2,ro2_opt3,ro2_opt4
    global r3
    ro2_lblq=Label(
        r3,
        text = ro2_que[indexes2[0]],
        font = ("Arial", 16),
        width = 500,
        justify = "center",
        wraplength = 800,
        background = "blanchedalmond",
    )
    ro2_lblq.pack(pady=(100,30))
    
    global radiovar2
    radiovar2 = IntVar()
    radiovar2.set(-1)
    
    ro2_opt1 = Radiobutton(
        r3,
        text = ro2_ans_ch[indexes2[0]][0],
        font = ("Times", 12),
        value = 0,
        variable = radiovar2,
        command = ro2selectedchoices,
        background = "blanchedalmond",
    )
    ro2_opt1.pack(pady=5)
    
    
    ro2_opt2 = Radiobutton(
        r3,
        text = ro2_ans_ch[indexes2[0]][1],
        font = ("Times", 12),
        value = 1,
        variable = radiovar2,
        command = ro2selectedchoices,
        background = "blanchedalmond",
    )
    ro2_opt2.pack(pady=5)
    
    
    ro2_opt3 = Radiobutton(
        r3,
        text = ro2_ans_ch[indexes2[0]][2],
        font = ("Times", 12),
        value = 2,
        variable = radiovar2,
        command = ro2selectedchoices,
        background = "blanchedalmond",
    )
    ro2_opt3.pack(pady=5)
    
    
    ro2_opt4 = Radiobutton(
        r3,
        text = ro2_ans_ch[indexes2[0]][3],
        font = ("Times", 12),
        value = 3,
        variable = radiovar2,
        command = ro2selectedchoices,
        background = "blanchedalmond",
    )
    ro2_opt4.pack(pady=5)
        
           
    
def quizstarted():
    global r1
    global r2
    r1.destroy()
    r2=Tk()  #3rd WINDOW 
    r2.title("WELCOME TO SIGMA")
    r2.geometry('700x500')
    r2.config(bg="blanchedalmond")
    r2.resizable(0,0)
    
    global l15
    global b4
    l15=Label(r2,text="LET'S START")
    l15.config(bg="blanchedalmond",font=("Times New Roman",26))
    l15.pack(pady=200)
    b4=Button(r2,text="Round 1>>",font=("Times New Roman",26),bg="steelblue",
              command=round1started)
    b4.place(x=240,y=380)
    
def roundtwo():
    global r2,b6,r3
    r2.destroy()
    r3=Tk() #4th Window
    r3.title("WELCOME TO SIGMA")
    r3.geometry('800x700')
    r3.config(bg="blanchedalmond")
    r3.resizable(0,0)
    
    global l16
    global b5
    l16=Label(r3,text="LET'S START")
    l16.config(bg="blanchedalmond",font=("Times New Roman",26))
    l16.pack(pady=200)
    
    b5=Button(r3,text="Round 2>>",font=("Times New Roman",26),bg="steelblue",
              command=round2started)
    b5.place(x=300,y=380)
    
def roundthree():
    global r3,b7,r4
    r3.destroy()
    r4=Tk() #4th Window
    r4.title("WELCOME TO SIGMA")
    r4.geometry('800x700')
    r4.config(bg="blanchedalmond")
    r4.resizable(0,0)
    
    global l17
    global b8
    l17=Label(r4,text="LET'S START")
    l17.config(bg="blanchedalmond",font=("Times New Roman",26))
    l17.pack(pady=200)
    
    b8=Button(r4,text="Round 3>>",font=("Times New Roman",26),bg="steelblue",
              command=round3started)
    b8.place(x=300,y=380)
    
def round1started():
    global l15
    global b4
    global r2
    global r3
    l15.destroy()
    b4.destroy()
    ro1shuff()
    queview1()

def round2started():
    global l16
    global b5
    l16.destroy()
    b5.destroy() 
    ro2shuff()
    queview2()
    
def round3started():
    global l17
    global b8
    l17.destroy()
    b8.destroy()


def ok():
    global r2
    global r7
    r1.destroy()
    r7.destroy()
    r2=Tk()  #3rd WINDOW 
    r2.title("WELCOME TO SIGMA")
    r2.geometry('700x500')
    r2.config(bg="blanchedalmond")
    r2.resizable(0,0)
    
    global l15
    global b4
    l15=Label(r2,text="LET'S START")
    l15.config(bg="blanchedalmond",font=("Times New Roman",26))
    l15.pack(pady=200)
    b4=Button(r2,text="Round 1>>",font=("Times New Roman",26),bg="steelblue",
              command=round1started)
    b4.place(x=240,y=380)


def quizstarted():
    global r1
    global e1
    global e5
    global r7
    if len(e1.get())==0 or len(e5.get())==0:
        messagebox.showwarning("Error","REQUIRED FIELDS")
        
    
    else:
        nm=e5.get()
        r7=Tk()   
        r7.title("LOGIN ID")
        r7.geometry('300x200')
        r7.config(bg="blanchedalmond")
        r7.resizable(0,0)
        l20=Label(r7,text=("YOUR ID IS : ",nm),font=("Arial Rounded MT",10),bg="blanchedalmond")
        l20.pack(pady=20)
        
        b10=Button(r7,text="OK",font=("Times New Roman",20),bg="black",fg="white",
                  command=ok)
        b10.place(x=230,y=130)
        


def personalinfo():
    global r1 
    r1=Tk()  #2nd WINDOW (PERSONAL INFORMATION)
    r1.title("WELCOME TO SIGMA")
    r1.geometry('700x500')
    r1.config(bg="blanchedalmond")
    r1.resizable(0,0)
    
    l14=Label(text="PLEASE FILL UP THE DETAILS",)
    l14.config(bg="blanchedalmond",font=("Times New Roman",26))
    l14.pack(pady=30)
    
    
    #name
    global e1
    Label(r1,text="ENTER NAME  **",bg="blanchedalmond",font=("Snap ITC",22)).place(x=25,y=130)
    e1=Entry(r1,width=40)
    e1.place(x=400,y=140)
    

    #class
    Label(r1,text="ENTER CLASS",bg="blanchedalmond",font=("Snap ITC",22)).place(x=25,y=200)
    e2=ttk.Combobox(r1)
    e2['values']=('IX','X','XI','XII')
    e2.current()
    e2.place(x=400,y=210)
    
             

    #roll no.
    global e3
    global e4
    Label(r1,text="ENTER ROLL NO.",bg="blanchedalmond",font=("Snap ITC",22)).place(x=25,y=270)
    e3=ttk.Combobox(r1)
    e3['values']=('0','1','2','3','4','5','6','7','8','9')
    e3.place(x=400,y=280)
    
    e4=ttk.Combobox(r1)
    e4['values']=('0','1','2','3','4','5','6','7','8','9')
    e4.place(x=550,y=280)

    #EMAIL ID
    global e5
    Label(r1,text="ENTER EMAIL ID **",bg="blanchedalmond",font=("Snap ITC",22)).place(x=25,y=340)
    e5=Entry(r1,width=20)
    e5.place(x=400,y=350)
    e6=ttk.Combobox(r1)
    e6['values']=('@gmail.com','@yahoo.com','@icloud.com')
    e6.current(0)
    e6.place(x=550,y=350)

    b3=Button(r1,text="START THE QUIZ",font=("Microsoft Sans Serif",18),bg="steelblue",
              command=quizstarted)
    b3.place(x=230,y=420)
    
    
    
    
    

def startispressed():
    r.destroy()
    personalinfo()
    
    
    

def instructions():
    l2=Label(r,text="READ THE INSTRUCTIONS CAREFULLY : ")
    l2.config(font=("Modern No. 20",20),bg="beige")
    l2.pack(pady=40)
    
    l3=Label(r,text="1. There are three rounds                                          ")
    l3.config(font=("Lucida Sans",18),bg="beige")
    l3.pack(pady=2)
    
    l4=Label(r,text="2. 1st Round : General Knowledge And Current Affairs")
    l4.config(font=("Lucida Sans",18),bg="beige")
    l4.pack()
    
    l5=Label(r,text="               2nd Round : Mathematics(MCQ)                                          ")
    l5.config(font=("Lucida Sans",18),bg="beige")
    l5.pack()
    
    l6=Label(r,text="    3rd Round : Mathematics(INTEGER TYPE)                  ")
    l6.config(font=("Lucida Sans",18),bg="beige")
    l6.pack()
    
    
    l7=Label(r,text=" 3. Each round has five questions.                                 ")
    l7.config(font=("Lucida Sans",18),bg="beige")
    l7.pack()
    
    l8=Label(r,text="    ROUND 1 & ROUND 2 : Each question has 4 options.")
    l8.config(font=("Lucida Sans",18),bg="beige")
    l8.pack()
    
    l9=Label(r,text="                                      Out of which ONE is correct.")
    l9.config(font=("Lucida Sans",18),bg="beige")
    l9.pack()
    
    l10=Label(r,text="                                    Each question is of 1 mark.")
    l10.config(font=("Lucida Sans",18),bg="beige")
    l10.pack()
    
    l11=Label(r,text="   ROUND 3 : Consists of INTEGER TYPE QUESTIONS.   ")
    l11.config(font=("Lucida Sans",18),bg="beige")
    l11.pack()
    
    l12=Label(r,text="Each question is of 2 mark.")
    l12.config(font=("Lucida Sans",18),bg="beige")
    l12.pack()
    
    l13=Label(r,text="CLICK ON START BUTTON TO START THE QUIZ")
    l13.config(font=("Algerian",20),bg="black",fg="white")
    l13.pack(pady=20)
    
    b2=Button(r,text="START",
              command = startispressed)
    b2.config(font=("Microsoft Sans Serif",24),bg="steelblue")
    b2.pack(pady=20)
    
def nextispressed():
    img1.destroy()
    img2.destroy()
    l1.destroy()
    b1.destroy()   
    instructions()
     
 
r=Tk()  #MAIN WINDOW FOR GUI
r.title("WELCOME TO SIGMA")
r.geometry('800x700')
r.config(bg="beige")
r.resizable(0,0)



a1= PhotoImage(file='new1.png')
img1= Label(r,image = a1)
img1.place(x =0,y = 0)
a2=PhotoImage(file='woodenbg5.png')
img2=Label(r,image=a2)
img2.place(x=0,y=220)


l1=Label(r,text="TO READ INSTRUCTIONS, CLICK NEXT")
l1.config(font=("Comic Sans MS",24),bg="antiquewhite")
l1.place(x=95,y=350)

b1=Button(r,text="NEXT",
          command = nextispressed, )
b1.config(font=("Microsoft Sans Serif",28),bg="sienna")
b1.place(x=340,y=550)








r.mainloop()

