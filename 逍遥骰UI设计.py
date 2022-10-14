"""逍遥骰的界面设计
update by yiting and xingyuan
       in 2022.10
"""
import tkinter
from tkinter import *
from tkinter import messagebox

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()


    def createWidget(self):
        #创建提醒选择难度按钮
        self.btn01 = Button(root, text="准备游戏",
                            width=8,height=1,bg="grey",fg="black",
                            anchor=N,command=self.startgametips)
        self.btn01.pack()


        #创建画布标题插入图片
        self.canvas = Canvas(self, width=300, height=200, bg="white")
        self.canvas.pack()
        global photo1
        photo1 = PhotoImage(file="title.gif")
        self.canvas.create_image(150, 170, image=photo1)


        #创建登录界面
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


        #创建难度选择按钮
        self.v = StringVar();
        self.v.set("E")

        self.r1 = Radiobutton(self, text="简单", value="E", variable=self.v)
        self.r2 = Radiobutton(self, text="中等", value="M", variable=self.v)
        self.r3 = Radiobutton(self, text="困难", value="D", variable=self.v)

        self.r1.pack(side="left");
        self.r2.pack(side="left")
        self.r3.pack(side="left")

        Button(self, text="确定", width=4, height=1, bg="grey", fg="black",
               anchor=N).pack(side="left")

    def startgametips(e):
        messagebox.showinfo("提醒", "请选择难度后开启游戏")

    def login(self):
        username = self.entry01.get()
        pwd = self.entry02.get()

        if pwd=="123456":
            messagebox.showinfo("逍遥骰", "登录成功！开始游戏！")
        else:
         messagebox.showinfo("逍遥骰","登录失败！用户名或密码错误！")



if __name__ == '__main__':
    root = Tk()
    root.title("《逍遥骰》————小组作业")
    root.geometry("1200x800+200+100")
    app = Application(master=root)
    root.mainloop()







