# -*- coding:utf-8 -*-
from tkinter  import *
import os

class Window:
    def btn_click(self):
        # print("btn is clicked")
        # txt.insert(1.0,"开始执行PING命令\n")   #在文本区第一行插入
        self.txt.insert(END, "开始执行PING命令\n")  # 在文本区最后一行插入
        cmd = 'ping 127.0.0.1'
        tmp = os.popen(cmd)
        for i in tmp:
            self.txt.insert(END, i)

    def btn_show_click(self):
        content = self.txt.get(0.0, END)
        print(content)

    def btn3_click(self):
        from tkinter.filedialog import askopenfilename as openfile
        path = openfile()
        self.txt.insert(END, '选择了文件：' + path)
        pass

    def __init__(self,root):
        print('构建窗体')
        root.geometry('800x600')  # 窗口尺寸设置，注意当中的是字母X
        root.title("tkinter windows")  # 窗口名称

        self.fm1 = Frame(root, width=750, height=500, border=3)
        self.fm1.pack_propagate(0)
        self.fm1.pack(side=TOP)
        self.txt = Text(self.fm1, width=100, height=40)
        self.txt.pack(side=LEFT)
        self.scl = Scrollbar(self.fm1)
        self.scl.pack(side=RIGHT, fill=Y)
        # 关联滚动条和文本联动
        self.scl.config(command=self.txt.yview)
        self.txt.config(yscrollcommand=self.scl.set)

        self.fm2 = Frame(root, width=750, height=50, border=3)
        self.fm2.pack_propagate(0)
        self.fm2.pack(side=TOP)
        self.btn = Button(self.fm2, text=' 开始测试 ', command=self.btn_click)
        self.btn.pack(side=LEFT)
        self.btn_show = Button(self.fm2, text='获取文本框内容', command=self.btn_show_click)
        self.btn_show.pack(side=LEFT)
        self.btn3 = Button(self.fm2, text='打开文件...', command=self.btn3_click)
        self.btn3.pack(side=LEFT)
        self.img = PhotoImage(file=r'.\loading-lazy.gif')
        # img.zoom(2,2)
        self.lable1 = Label(self.fm2, image=self.img)
        self.lable1.pack(side=RIGHT)

    def __del__(self):
        print('解构窗体')

root = Tk()  # 生成一个窗口
win=Window(root)
root.mainloop()