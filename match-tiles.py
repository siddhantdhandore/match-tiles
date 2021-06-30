from tkinter import *
import random

#========ROOT CONFIGURATION=====================================================
root = Tk()
width = root.winfo_screenwidth()//2
height = root.winfo_screenheight()//2
root.geometry(f'500x500+{width - 250}+{height-250}')
#==========********************************************==============================


#============FRAME FOR 20 BUTTONS=====================================================
buttonFrame=Frame(root,width=395,height = 400,bd="8",relief = "ridge",bg="#959595")
buttonFrame.place(x=50,y=40)
#===**********************END 20 BUTTON FRAME*************************=================

#BUTTON DEFINITIONS=========================

#newList CONTAINS RANDOMLY MIXED 25 NUMBERS
textList=['1','2','3','4','5','6','7','8','9','10','11','12','13']
numList=random.sample(textList,12)
numList+=random.sample(textList,13)

numberOfClicks=0
prev=[]
def setText(button,index):
    global prev,numberOfClicks
    numberOfClicks+=1
    if prev == []:
        prev += [button]
        button['text']=numList[index]
    elif prev != []:
        if prev[0] == button:
            return
        elif prev[0]['text'] == numList[index]:
            prev[0]['text']=numList[index]
            button['text']=numList[index]
            prev[0]['state']=DISABLED
            button['state']=DISABLED
            prev =[]
        else:
            prev[0]['text'] =""
            prev[0]=button
            button['text']=numList[index]
            
def printClicks():
    print(numberOfClicks)



#===============ALL 2O BUTTONS============================================================
#=======ROW ONE===================================
b00=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b00,0))
b00.place(x=0,y=0,relwidth=0.2,relheight=0.2)

b01=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b01,1))
b01.place(x=76,y=0,relwidth=0.2,relheight=0.2)

b02=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b02,2))
b02.place(x=152,y=0,relwidth=0.2,relheight=0.2)

b03=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b03,3))
b03.place(x=228,y=0,relwidth=0.2,relheight=0.2)

b04=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b04,4))
b04.place(x=304,y=0,relwidth=0.2,relheight=0.2)
#======***********************************************
#=======ROW TWO===================================
b10=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b10,5))
b10.place(x=0,y=77,relwidth=0.2,relheight=0.2)

b11=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b11,6))
b11.place(x=76,y=77,relwidth=0.2,relheight=0.2)

b12=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b12,7))
b12.place(x=152,y=77,relwidth=0.2,relheight=0.2)

b13=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b13,8))
b13.place(x=228,y=77,relwidth=0.2,relheight=0.2)

b14=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b14,9))
b14.place(x=304,y=77,relwidth=0.2,relheight=0.2)
#======***********************************************
#=======ROW THREE===================================
b20=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b20,10))
b20.place(x=0,y=154,relwidth=0.2,relheight=0.2)

b21=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b21,11))
b21.place(x=76,y=154,relwidth=0.2,relheight=0.2)

b22=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b22,12))
b22.place(x=152,y=154,relwidth=0.2,relheight=0.2)

b23=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b23,13))
b23.place(x=228,y=154,relwidth=0.2,relheight=0.2)

b24=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b24,14))
b24.place(x=304,y=154,relwidth=0.2,relheight=0.2)
#======***********************************************

#=======ROW FOUR===================================
b30=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b30,15))
b30.place(x=0,y=231,relwidth=0.2,relheight=0.2)

b31=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b31,16))
b31.place(x=76,y=231,relwidth=0.2,relheight=0.2)

b32=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b32,17))
b32.place(x=152,y=231,relwidth=0.2,relheight=0.2)

b33=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b33,18))
b33.place(x=228,y=231,relwidth=0.2,relheight=0.2)

b34=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b34,19))
b34.place(x=304,y=231,relwidth=0.2,relheight=0.2)
#======***********************************************

#=======ROW FIVE===================================
b40=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b40,20))
b40.place(x=0,y=308,relwidth=0.2,relheight=0.2)

b41=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b41,21))
b41.place(x=76,y=308,relwidth=0.2,relheight=0.2)

b42=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b42,22))
b42.place(x=152,y=308,relwidth=0.2,relheight=0.2)

b43=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b43,23))
b43.place(x=228,y=308,relwidth=0.2,relheight=0.2)

b44=Button(buttonFrame,text="",font="Times 36 bold",width = 1,height=1,command=lambda:setText(b44,24))
b44.place(x=304,y=308,relwidth=0.2,relheight=0.2)

bNumberOfClicks=Button(root,text='click',command=printClicks)
bNumberOfClicks.pack()
#======***********************************************
#====***************************END ALL 2O BUTTONS*******************************=======


    
root.mainloop()

