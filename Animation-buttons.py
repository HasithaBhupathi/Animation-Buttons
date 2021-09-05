from tkinter import*

window = Tk()
window.geometry('800x600+350+50')
window.title('Window')
window['bg'] = 'gray'


count = 0
size = 12


def command_1_1():
    global count,size
 
    if count <= 10 and count > 0:
        size -=2
        button1.config(font = ('arial',size,'bold italic'))
        count -=1
        window.after(10,command_1_1)

def command_1():
    global count,size

    if count < 10:
        size +=2
        button1.config(font = ('arial',size,'bold italic'))
        count += 1
        window.after(10,command_1)

    
    elif count ==10:

        command_1_1()


button1 = Button(window,text = 'Click Me_1',fg = 'red',font = ('arial',12,'bold italic'),command = command_1)
button1.pack(pady = 100)


count1 = 0
size1 = 0
fo = 12

def command_1_2():
    global count1,size1,fo
    if (count1 <= 20) and (count1 > 0):
        size1 -=5
        fo -=2
        button2.pack_configure(pady = size1)
        button2.config(font = ('arial',fo,'bold italic'))
        count1 -=1
        window.after(10,command_1_2)


def command_2():
    global count1,size1,fo
    if count1 < 20:
        size1 +=5
        fo += 2
        button2.pack_configure(pady = size1)
        button2.config(font = ('arial',fo,'bold italic'))
        count1 +=1
        window.after(10,command_2)

    elif count1 == 20:

        command_1_2()    


button2 = Button(window,text = 'Click me_2',fg = 'blue',font = ('arial',12,'bold italic'),command = command_2)
button2.pack()



window.mainloop()
