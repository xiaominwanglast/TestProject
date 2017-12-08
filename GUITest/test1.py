#coding:utf-8
from Tkinter import *
root = Tk()
root.title(u"TestLink csv文件转为xml")
root.geometry('1000x800')
root.resizable(width=False, height=False)
top_frame=Frame(root)
Label(root, text=u"TestLin CSV用例转XML文件", font=('Arial', 15)).pack()
top_next_frame=Frame(root)

# Label(root, text=u"说明文档", font=('Arial', 13)).pack()
# Label(root, text=u"1.选中二级目录并且导出二级目录下的xml文件(非根目录)",bg = 'yellow', font=('Arial', 13),wraplength = 600,justify = 'left').pack()
# Label(root, text=u"2.查看xml文件记录二级目录testsuite id的值",bg = 'yellow', font=('Arial', 13),justify = 'left').pack()
#\n2.查看xml文件记录二级目录testsuite id的值,\n3.若导入用例在三级目录，则记录xml"
root.mainloop()

