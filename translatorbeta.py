import time
import tkinter as tk
import win32api
import googletrans as gt
import win32clipboard
import win32api,win32con
import codecs
translator = gt.Translator()

a=translator.translate('สวัสดี').text
print(a)
lastdata=''
lastdatatranslate=''
button_Ckey=0x43
def tkloop():
    global lastdata,lastdatatranslate
    try:
        time.sleep(0.2)
        data=root.clipboard_get()
    except:
        print('error')
        data=' '
        time.sleep(1)
    if data != lastdata:
        en=translator.translate(data,dest="en")
        th=translator.translate(data,dest="th")
        
        d=en.text+th.text
        if en.src=='ja':
            ja=translator.translate(data,dest="ja")
            d=ja.pronunciation+'\n'+d
        lastdatatranslate=d
        print(u"data =\t{}\nenglish =\t{}\nthai =\t{}".format(data,en,th))
        lastdata=data
    else:
        d=lastdatatranslate
    text.delete(1.0,tk.END)
    text.insert(1.0,d)
    text.after(5, tkloop)

root = tk.Tk()
root.attributes("-topmost", True)
root.bind('<Escape>', lambda e: root.quit())
text = tk.Text(root,height=10,width=30,font="Sans 20",padx=50,pady=10)
text.pack()
tkloop()
root.mainloop()
