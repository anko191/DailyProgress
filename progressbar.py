from PIL import ImageTk
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageGrab as ImageGrab
import re

def done(arr, name = "defalut", maxw = 500, maxh = 100):
    root = tk.Tk()
    sw = str(maxw + 40)
    sh = str(maxh)
    root.geometry(sw+"x"+sh)

    tit = tk.Label(root, text = name, relief = tk.RIDGE, bg = "snow")

    name = name.replace('/','_')
    tit.grid(row = 0, column = 1, ipadx = 20)
    for i, ar in enumerate(arr):
        label = tk.Label(root, text = ar[0] + " ", bg = "white")
        label.grid(row = i+1, column = 0, ipadx = 10, sticky=tk.W)
        progressbar = ttk.Progressbar(root,
                                      orient="horizontal",

                                      length = maxw//2,
                                      mode = "determinate")


        progressbar.grid(row = i+1, column = 1, sticky=tk.EW)

        maximum_bar = 24
        value_bar = ar[1]
        percentage = "%.1f"%((value_bar / maximum_bar) * 24)
        progressbar.configure(maximum=maximum_bar, value=value_bar)
        per = tk.Label(root, text = str(percentage) + "時間/日", bg = "white")
        per.grid(row = i+1, column = 2, sticky=tk.E)

    def save_canvas():
        x = root.winfo_rootx()
        y = root.winfo_rooty()
        xx = x + root.winfo_width()
        yy = y + root.winfo_height()
        ImageGrab.grab(bbox=(x,y,xx,yy)).save(name + ".png",quarity = 100)
        print(name + ".png", "に出力しました。")
    root.after(1000, save_canvas)
    root.configure(bg = "white")
    root.mainloop()



name = input("タイトル名を入力してください：")
if len(name) == 0:
    print('正式な名前を入力してください。1/3の様なスラッシュは自動的に_に変換されます')
    exit()
N = int(input("入力するデータ数を入力してください："))
arr = []
for i in range(N):
    print(f" - {i+1}番目の入力です - ")
    tag = input("名前：")
    tim = input("時間：")
    if len(tim) == 0:
        tim = 0
    else:
        tim = float((tim))
    arr.append([tag,tim])
maxl = 0
flag = False
balcheck = re.compile('[A-Z0-9a-z]+')
for a in arr:
    if len(a[0]) > 10:
        a[0] = a[0][:10]
    if balcheck.fullmatch(a[0]) == None:
        flag = True
    maxl = max(maxl, len(a[0]))
# print(flag)
done(arr, name = name, maxw = (200 + maxl*11) if flag else (200 + maxl * 5),maxh = len(arr)*22 + 40)
