import time
import tkinter as tk
import win32api
import googletrans as gt
import win32clipboard
import codecs

translator = gt.Translator()
def getclipboard():
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except Exception as e:
        data=str(e)
    return data
def translt(data):
    en=translator.translate(data,dest="en")
    th=translator.translate(data,dest="th")
    d=en.text+'\n'+th.text
    if en.src=='ja':
        ja=translator.translate(data,dest="ja")
        d=ja.pronunciation+'\n'+d
    return d

lastdata=getclipboard()
lastdatatranslate=translt(lastdata)
def tkloop():
    global lastdata,lastdatatranslate
    if  win32api.GetKeyState(0x43)<0:
        data=getclipboard()
        if data != lastdata:
            d=translt(data)
            lastdatatranslate=d
            lastdata=data
        else:
            d=lastdatatranslate
        text.delete(1.0,tk.END)
        text.insert(1.0,d)
    text.after(50, tkloop)


root = tk.Tk()
root.title("auto translate")
root.attributes("-topmost", True)
root.bind('<Escape>', lambda e: root.quit())
text = tk.Text(root,height=20,width=20,font="Sans 20",padx=50,pady=10)
text.insert(1.0,lastdatatranslate)
text.pack()
tkloop()
root.mainloop()
