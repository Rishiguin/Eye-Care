from win10toast import ToastNotifier
import time
import tkinter
from playsound import playsound
window = tkinter.Tk()
window.title("Eye Care")

window.iconbitmap(r'C:\Python programs\eye care\eyeico3.ico')


def tim():
    t1 = inp.get()
    interv=inp2.get()
    window.destroy()
    t2='0'+t1
    t=int(t2)
    t3=float(interv)
    print(t)
    no_of_iter2=int(t*60/t3)
    no_of_iter=int((((no_of_iter2)*20)+(t*60))/t3)
    print(no_of_iter)
    for i in range(no_of_iter):
      toaster = ToastNotifier()
      toaster.show_toast("Eye rest",
                   "Go look around for 20 seconds",
                   icon_path='C:\Python programs\eye care\eyeico3.ico',
                   duration=10)
      time.sleep(20)
      playsound('C:\Python programs\eye care\jingle.mp3')
      toaster.show_toast("Eye rest",
                   "Back to Work",
                   icon_path='C:\Python programs\eye care\eyeico3.ico',
                   duration=5)
      
      time.sleep(t3*60-20)


lbl = tkinter.Label(window,text='ENTER TIME IN HOUR : ',font = 'arial')
inp = tkinter.Entry(window)
submit= tkinter.Button(window,text='submit',font='arial',command=tim)
lbl2 = tkinter.Label(window,text='ENTER INTERVAL BETWEEN NOTIFICATIONS(in min) : ',font = 'arial')
inp2 = tkinter.Entry(window)

lbl.grid(row=1,column=1)
inp.grid(row=1,column=2)
lbl2.grid(row=2,column=1)
inp2.grid(row=2,column=2)
submit.grid(row=3,column=1,columnspan=2)

window.mainloop()



