import tkinter as tk
from utils.text_name import *


class APP:
    def __init__(self, master):
        frame1 = tk.Frame(master)
        frame2 = tk.Frame(master)
        frame1.pack(anchor="e")
        frame2.pack(side=tk.LEFT, padx=10, pady=10)

        self.hi_there = tk.Button(frame1, text="home", fg="blue", command=self.say_hi)
        self.hi_there.pack()

        self.hi_there2 = tk.Button(frame2, text="home2", fg="blue", command=self.say_hi)
        self.hi_there2.pack()

    def say_hi(self):
        print("test")


class ABOUT:
    def __init__(self, master):
        about = tk.Frame(master)  # .grid(row=0, column=0)
        algorithm = tk.Frame(master)
        local = tk.Frame(master)
        home = tk.Frame(master)
        # input_text = tk.Entry(master)
        # 使用字典的方式设置样式，一次修改多次使用
        label_style = {"anchor": "nw", "side": tk.LEFT, "padx": 30, "pady": 20}
        about.pack(label_style)
        algorithm.pack(label_style)
        local.pack(label_style)
        home.pack(label_style)
        # input_text.pack(side=tk.LEFT)
        # input_text.delete(0, tk.END)
        # input_text.insert(0, "test")

        self.about = tk.Button(about, text=NAME.about, font=("华康少女字体", 24))
        self.algorithm = tk.Label(algorithm, text=NAME.algorithm, fg="blue", font=("华康少女文字W5(P)", 24))
        self.local = tk.Label(local, text=NAME.local, fg="blue", font=("华文楷体", 24))
        self.home = tk.Label(home, text=NAME.home, fg="blue", font=("Arial", 24))
        # self.input_test = tk.Entry(input_text)
        self.about.pack()
        self.algorithm.pack()
        self.local.pack()
        self.home.pack()


root = tk.Tk()
root.title("管理系统")
root.geometry('1000x670+500+200')
app = ABOUT(root)
root.mainloop()
print("vz")
