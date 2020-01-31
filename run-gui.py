# -*- coding:utf-8 -*-
from tkinter  import *
import os

def btn_click():
    #print("btn is clicked")
    #txt.insert(1.0,"开始执行PING命令\n")   #在文本区第一行插入
    txt.insert(END, "开始执行PING命令\n")  #在文本区最后一行插入
    cmd='ping 127.0.0.1'
    tmp=os.popen(cmd)
    for i in tmp:
        txt.insert(END,i)
def btn_show_click():
    content=txt.get(0.0,END)
    print(content)

def btn3_click():
    from tkinter.filedialog import askopenfilename as openfile
    path=openfile()
    txt.insert(END, '选择了文件：'+path)
    pass


    #lable1.config(image=img)

root=Tk()#生成一个窗口
root.geometry('800x600')#窗口尺寸设置，注意当中的是字母X
root.title("tkinter windows")#窗口名称

#窗口布局说明
#每个元件的对齐方式只能选择LEFT,RIGHT，TOP,BUTTOM，
#选择同样对齐方式的按照pack的顺序依次堆叠
#本代码中的对齐方式简单说明下
#fm1上对齐，里面装了2个元件，TEXT和SCOLLBAR，分别是左对齐和右边对齐
#fm2上对齐，紧跟着fm1。fm2里面装个2个BUTTON，左对齐
#fm1.pack_propagate(0)用于固定FRAME的尺寸，否则会根据里面的元件自动缩放
#fm1=Frame(root,width=750,height=500,bg='red',border=3) 通过设置FRAME的背景颜色，可便于观察对齐方式

fm1=Frame(root,width=750,height=500,border=3)
fm1.pack_propagate(0)
fm1.pack(side=TOP)

txt=Text(fm1,width=100,height=40)
txt.pack(side=LEFT)

scl=Scrollbar(fm1)
scl.pack(side=RIGHT,fill=Y)
#关联滚动条和文本联动
scl.config(command=txt.yview)
txt.config(yscrollcommand=scl.set)




fm2=Frame(root,width=750,height=50,border=3)
fm2.pack_propagate(0)
fm2.pack(side=TOP)

btn=Button(fm2,text=' 开始测试 ',command=btn_click)
btn.pack(side=LEFT)
btn_show=Button(fm2,text='获取文本框内容',command=btn_show_click)
btn_show.pack(side=LEFT)

btn3=Button(fm2,text='打开文件...',command=btn3_click)
btn3.pack(side=LEFT)

img=PhotoImage(file=r'.\loading-lazy.gif')
#img.zoom(2,2)
lable1=Label(fm2,image=img)
lable1.pack(side=RIGHT)

root.mainloop()
