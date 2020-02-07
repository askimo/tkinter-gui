from tkinter  import *

class Window(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry('800x600')
        self.master.title('Sudoku')
        self.pack()
        self.createWigdets()

    def createWigdets(self):
        self.button=[ [] for i in range(9)]
        self.fm=[]
        for i in range(9):
            self.fm.append(Frame(self,border=1))
            self.fm[i].pack()
            for j in range(9):
                self.button[i].append(Button(self.fm[i] , text=str(i)+' '+str(j),width=5,height=2))
                self.button[i][j].pack(side=LEFT)

        self.check_area=Frame(self,border=5)
        self.check_area.pack(side=LEFT)
        self.btn_check=Button(self.check_area,  text='检查结果',command=self.btn_check_click)
        self.btn_check.pack(side=LEFT)
        self.btn_test = Button(self.check_area, text=' 测  试 ')
        self.btn_test.pack(side=LEFT)
        self.btn_quit = Button(self.check_area, text=' 退  出 ')
        self.btn_quit.pack(side=LEFT)
    def btn_check_click(self):
        print(type(self.button[4][4]))



app=Window()
app.mainloop()
