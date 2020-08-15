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
# def translate():
#     win32clipboard.OpenClipboard()
#     data = win32clipboard.GetClipboardData()
#     win32clipboard.CloseClipboard()
#     # return translator.translate(data,src='ja').text
#     return translator.translate(data,dest="en").text+'\n'+translator.translate(data,dest="th").text

button_Ckey=0x43
state_Ckey=win32api.GetKeyState(button_Ckey)
def tkloop():
    # global button_c
    # global state_c
    # now_c=win32api.GetKeyState(button_c)
    # if now_c<0 and now_c!=state_c :
        # state_c=now_c
        # time.sleep(0.005)
    global lastdata,lastdatatranslate
    try:
        time.sleep(0.2)
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
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

button_c=0x43
state_c=win32api.GetKeyState(button_c)

root = tk.Tk()
root.attributes("-topmost", True)
root.bind('<Escape>', lambda e: root.quit())
# lmain = tk.Label(root)
# lmain.pack()
text = tk.Text(root,height=10,width=30,font="Sans 20",padx=50,pady=10)
text.pack()
tkloop()
root.mainloop()
