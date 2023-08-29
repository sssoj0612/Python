from tkinter import *

window = Tk()

# btn1 = Button(window, text="버튼1")
# btn2 = Button(window, text="버튼2")
# btn3 = Button(window, text="버튼3")
#
# btn1.pack(side=LEFT)
# btn2.pack(side=LEFT)
# btn3.pack(side=LEFT)

# for문
btnList = [None] * 3

for i in range(0, 3) :
    btnList[i] = Button(window, text="버튼" + str(i+1))

for btn in btnList :
    btn.pack(side=RIGHT)

window.mainloop()