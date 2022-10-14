import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random


def window1():
    class Application(Frame):

        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.createWidget()

        def createWidget(self):
            # 创建提醒选择难度按钮
            self.btn01 = Button(root, text="准备游戏",
                                width=8, height=1, bg="grey", fg="black",
                                anchor=N, command=self.startgametips)
            self.btn01.pack()

            # 创建画布标题插入图片
            self.canvas = Canvas(self, width=300, height=200, bg="white")
            self.canvas.pack()
            global photo1
            photo1 = PhotoImage(file="title.gif")
            self.canvas.create_image(150, 170, image=photo1)

            # 创建登录界面
            self.label01 = Label(self, text="用户名")
            self.label01.pack()
            # StringVar变量绑定到指定的组件。
            # StringVar变量的值发生变化，组件内容也变化；
            # 组件内容发生变化，StringVar变量的值也发生变化。
            v1 = StringVar()
            self.entry01 = Entry(self, textvariable=v1)
            self.entry01.pack()
            v1.set("用户名默认为学号")

            # 创建密码框
            self.label02 = Label(self, text="密码")
            self.label02.pack()
            v2 = StringVar()
            v2.set("密码默认为123456")
            self.entry02 = Entry(self, textvariable=v2)
            self.entry02.pack()
            Button(self, text="登陆账号", command=self.login).pack()

            # 创建画布背景插入图片
            self.canvas = Canvas(self, width=650, height=300, bg="white")
            self.canvas.pack()
            global photo2
            photo2 = PhotoImage(file="background.gif")
            self.canvas.create_image(150, 170, image=photo2)

            # 创建难度选择按钮
            self.v = StringVar();
            self.v.set("E")

            self.r1 = Radiobutton(self, text="简单", value="E", variable=self.v)
            self.r2 = Radiobutton(self, text="中等", value="M", variable=self.v)
            self.r3 = Radiobutton(self, text="困难", value="D", variable=self.v)

            self.r1.pack(side="left");
            self.r2.pack(side="left")
            self.r3.pack(side="left")

            Button(self, text="确定", width=4, height=1, bg="grey", fg="black",
                   anchor=N,command=window2).pack(side="left")

        def startgametips(e):
            messagebox.showinfo("提醒", "请选择难度后开启游戏")

        def login(self):
            username = self.entry01.get()
            pwd = self.entry02.get()

            if pwd == "123456":
                messagebox.showinfo("《逍遥骰》————小组《算法佬与小白》", "登录成功！开始游戏！")
            else:
                messagebox.showinfo("《逍遥骰》————小组《算法佬与小白》", "登录失败！用户名或密码错误！")
    tk=tkinter
    root = tk.Tk()
    root.title("《逍遥骰》————小组《算法佬与小白》")
    root.geometry("1200x800+200+100")
    app = Application(master=root)
    root.mainloop()

def window2():

    class Application(Frame):

        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.createWidget()

        def createWidget(self):

            #创建提示标识
            self.label01 = Label(self,text="开始进行游戏，请投掷骰子", width=23,height=1,
                             fg="black", bg="grey").grid(row=0, column=3)
            self.label02 = Label(self, text="玩家", width=4, height=1,
                                 fg="black", bg="grey").grid(row=0, column=0)
            self.label03 = Label(self, text="电脑", width=4, height=1,
                                 fg="black", bg="grey").grid(row=0, column=6)
            #创建3/1/3的标签架构
            #填入数据

            label01Text = ((6,6,6),
                         (2,5,1),
                         (4,4,3,))
            label02Text =((5,1,1),
                          (5,6,6),
                          (0,1,0))
            #中间那行白色的
            for rindex in range(0,3):
                Label(self, text="", width=8, height=4, bg="white") \
                    .grid(row=rindex + 1, column=3, sticky=NSEW)
            #player
            for rindex, r in enumerate(label01Text):
                for cindex, c in enumerate(r):

                        Label(self, text=c, width=8,height=4,fg="black", bg="white") \
                            .grid(row=rindex + 1, column=cindex, sticky=NSEW)
            #AI
            for rindex, r in enumerate(label02Text):
                for cindex, c in enumerate(r):
                    Label(self, text=c, width=8,height=4,fg="black", bg="white") \
                            .grid(row=rindex + 1, column=cindex+4, sticky=NSEW)


            #创建投掷结果显示
            self.label04 = Label(self, text="本轮投出**\n请选择将填入三行空位\n选第一行请敲击K\n"
                                            "选第二行请敲击E\n选第三行请敲击X\n", width=23, height=6,
                                 fg="black", bg="white").grid(row=6, column=3)
            #创建投掷按钮
            self.button02 = Button(self, text="点击投掷\n进入下一轮", width=10, height=2,
                                 fg="black", bg="white").grid(row=7, column=3, sticky=NSEW)
            # 创建得分栏显示
            self.label04 = Label(self, text="最终的得分结果为  ", width=23, height=1,
                                 fg="black", bg="grey").grid(row=8, column=3, sticky=NSEW)
            self.label05 = Label(self, text="**", width=3, height=1,
                                 fg="black", bg="grey").grid(row=9, column=0, sticky=NSEW)
            self.label06 = Label(self, text="**", width=3, height=1,
                                 fg="black", bg="grey").grid(row=9, column=6, sticky=NSEW)
            self.label07 = Label(self, text="恭喜玩家，游戏胜利！", width=3, height=1,
                                 fg="black", bg="white").grid(row=9, column=3, sticky=NSEW)

            # 将选择移动改为键盘输入引导移动
            def k_move(event):
                self.r1.grid(row=4, column=0, sticky=NSEW)
                self.r2.grid(row=4, column=1, sticky=NSEW)
                self.r3.grid(row=4, column=2, sticky=NSEW)

            def k_moveover(event):
                self.r1.grid(row=4, column=0, sticky=NSEW)
                self.r2.grid(row=4, column=1, sticky=NSEW)
                self.r3.grid(row=4, column=2, sticky=NSEW)

            def e_move(event):
                self.r1.grid(row=4, column=0, sticky=NSEW)
                self.r2.grid(row=4, column=1, sticky=NSEW)
                self.r3.grid(row=4, column=2, sticky=NSEW)

            def e_moveover(event):
                self.r1.grid(row=4, column=0, sticky=NSEW)
                self.r2.grid(row=4, column=1, sticky=NSEW)
                self.r3.grid(row=4, column=2, sticky=NSEW)

            def x_move(event):
                self.r1.grid(row=4, column=0, sticky=NSEW)
                self.r2.grid(row=4, column=1, sticky=NSEW)
                self.r3.grid(row=4, column=2, sticky=NSEW)

            def x_moveover(event):
                self.r1.grid(row=4, column=0, sticky=NSEW)
                self.r2.grid(row=4, column=1, sticky=NSEW)
                self.r3.grid(row=4, column=2, sticky=NSEW)

            root.bind("<KeyPress-K>", k_move)
            root.bind("<KeyRelease-K>", k_moveover)
            root.bind("<KeyPress-K>", e_move)
            root.bind("<KeyRelease-K>", e_moveover)
            root.bind("<KeyPress-K>", x_move)
            root.bind("<KeyRelease-K>", x_moveover)
            #创建目标行选择按钮
            # self.v = StringVar();
            # self.v.set("K")
            #
            # self.r1 = Radiobutton(self, text="第一行", value="K", variable=self.v)
            # self.r2 = Radiobutton(self, text="第二行", value="E", variable=self.v)
            # self.r3 = Radiobutton(self, text="第三行", value="X", variable=self.v)
            #
            #
            # self.r1.grid(row=4, column=0, sticky=NSEW)
            # self.r2.grid(row=4, column=1, sticky=NSEW)
            # self.r3.grid(row=4, column=2, sticky=NSEW)
            #
            # Button(self, text="确定").grid(row=4, column=5, sticky=NSEW)
    tk = tkinter
    root = tk.Tk()
    root.title("《逍遥骰》————小组《算法佬与小白》")
    root.geometry("800x700+400+200")
    app = Application(master=root)
    root.mainloop()


if __name__ == '__main__':
    window1()