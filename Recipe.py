# -*- coding:UTF-8 -*-
#
import tkinter
import time
import tkinter.messagebox
import tkinter.ttk
import datetime
import io

root=tkinter.Tk()
root.title("BIT-Recipe Plan")  #窗口标题
root.geometry('800x500+250+80')  #设置窗口的大小宽x高+偏移量
root.iconbitmap('Notes_128px_1184310_easyicon.net.ico')  #设置窗口图标
menu=tkinter.Menu(root)                                #生成菜单
welcome=tkinter.messagebox.showinfo(parent=root,title=u'欢迎',message='Welcome to BIT-Recipe Plan!')


#*************************************************************************************************
#下拉菜单模块
submenu=tkinter.Menu(menu,tearoff=0)                   #生成下拉菜单
submenu.add_command(label="Open")                      #向下拉菜单中添加Open、Save，Close命令
submenu.add_command(label="Save")
submenu.add_command(label="Close")
menu.add_cascade(label="File",menu=submenu)            #将下拉菜单添加到菜单中，主菜单中名字为File
submenu=tkinter.Menu(menu,tearoff=0)
submenu.add_command(label='Read')
submenu.add_command(label='Edit')
menu.add_cascade(label='Edit',menu=submenu)

def Contact():
    tkinter.messagebox.showinfo(title='Contact',message='Author:Leibniz.Wang\nContact:leibnizwang@163.com\n')

def About():
    tkinter.messagebox.showinfo(title='About',message='Version:1.1.0')

def Help():
    tkinter.messagebox.showinfo(title='Help',message='This is a recipe-note application.You can note your recipe everyday!')

submenu=tkinter.Menu(menu,tearoff=0)
submenu.add_command(label='About',command=About)
submenu.add_command(label="Contact",command=Contact)
submenu.add_command(label='Help',command=Help)
menu.add_cascade(label="Help",menu=submenu)
root.config(menu=menu)
#*************************************************************************************************
#timenow是显示时间变量
timenow=datetime.datetime.now()
chose_time=tkinter.Label(text='选择时间')
chose_time.grid(row=0,column=7)
choose_year=tkinter.IntVar()
choose_month=tkinter.IntVar()
choose_day=tkinter.IntVar()
time_chosen01=tkinter.ttk.Combobox(root,width=4,textvariable=choose_year)
time_chosen02=tkinter.ttk.Combobox(root,width=2,textvariable=choose_month)
time_chosen03=tkinter.ttk.Combobox(root,width=3,textvariable=choose_day)
time_chosen01['values']=('2016','2017','2018','2019','2020')
time_chosen02['values']=('01','02','03','04','05','06','07','08','09','10','11','12')
time_chosen03['values']=('01','02','03','04','05','06','07','08','09','10',
                         '11','12','13','14','15','16','17','18','19','20',
                         '21','22','23','24','25','26','27','28','29','30',
                         '31')
time_chosen01.grid(row=0,column=8)
time_chosen02.grid(row=0,column=9)
time_chosen03.grid(row=0,column=10)
time_chosen01.set(timenow.year)
time_chosen02.set(timenow.month)
time_chosen03.set(timenow.day)

#*************************************************************************************************
#标签设定模块
label_timenow=tkinter.Label(root,text=u'当前日期：')
label_timenow.grid(row=0,column=0)
#label_showtime=tkinter.Label(root,text=str(timenow.year)+'/'+str(timenow.month)+'/'+str(timenow.day))
label_showtime=tkinter.Label(root,text=time.strftime("%Y/%m/%d"))
label_showtime.grid(row=0,column=1)
#label_canming=tkinter.Label(root,text=u'用餐')
label_time=tkinter.Label(root,text=u'时间')
label_place=tkinter.Label(root,text=u'地点')
label_food=tkinter.Label(root,text=u'食物')
#label_softdrinks=tkinter.Label(root,text=u'饮料')
#label_canming.grid(row=2,column=0)
label_time.grid(row=2,column=4)
label_place.grid(row=2,column=7)
label_food.grid(row=2,column=1)
#label_softdrinks.grid(row=2,column=12)
label_breakfast=tkinter.Label(root,text=u'早餐')
label_lunch=tkinter.Label(root,text=u'中餐')
label_dinner=tkinter.Label(root,text=u'晚餐')
label_night=tkinter.Label(root,text=u'夜宵')
label_breakfast.grid(row=3,column=0)
label_lunch.grid(row=4,column=0)
label_dinner.grid(row=5,column=0)
label_night.grid(row=6,column=0)

#*************************************************************************************************
'''
canming=tkinter.StringVar()
canming.set(u'早餐')
canmingChosen=tkinter.OptionMenu(root,canming,u'早餐',u'中餐',u'晚餐',u'夜宵')
canmingChosen.grid(row=3,column=0)
'''
#*******************************************************************************************
#时间选择模块
time_hour_start1= tkinter.IntVar()
time_min_start1=tkinter.IntVar()
time_hour_last1=tkinter.IntVar()
time_min_last1=tkinter.IntVar()
timeChosen11=tkinter.ttk.Combobox(root, width=2, textvariable=time_hour_start1)
timeChosen12=tkinter.ttk.Combobox(root, width=2, textvariable=time_min_start1)
timeChosen13=tkinter.ttk.Combobox(root, width=2, textvariable=time_hour_last1)
timeChosen14=tkinter.ttk.Combobox(root, width=2, textvariable=time_min_last1)
timeChosen11['values']= ('00','01','02','03','04','05','06','07','08','09','10','11','12')     # 设置下拉列表的值
timeChosen12['values']=('00','05','10','15','20','25','30','35','40','45','50','55')
timeChosen13['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12')
timeChosen14['values']=('00','05','10','15','20','25','30','35','40','45','50','55')
timeChosen11.grid(column=2, row=3)      # 设置其在界面中出现的位置  column代表列   row 代表行
timeChosen12.grid(column=3, row=3)
timeChosen13.grid(column=5, row=3)
timeChosen14.grid(column=6, row=3)
timeChosen11.current('00')    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
timeChosen12.current('00')
timeChosen13.current('00')
timeChosen14.current('00')

time_hour_start2= tkinter.IntVar()
time_min_start2=tkinter.IntVar()
time_hour_last2=tkinter.IntVar()
time_min_last2=tkinter.IntVar()
timeChosen21=tkinter.ttk.Combobox(root, width=2, textvariable=time_hour_start2)
timeChosen22=tkinter.ttk.Combobox(root, width=2, textvariable=time_min_start2)
timeChosen23=tkinter.ttk.Combobox(root, width=2, textvariable=time_hour_last2)
timeChosen24=tkinter.ttk.Combobox(root, width=2, textvariable=time_min_last2)
timeChosen21['values']= ('00','01','02','03','04','05','06','07','08','09','10','11','12')     # 设置下拉列表的值
timeChosen22['values']=('00','05','10','15','20','25','30','35','40','45','50','55')
timeChosen23['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12')
timeChosen24['values']=('00','05','10','15','20','25','30','35','40','45','50','55')
timeChosen21.grid(column=2, row=4)      # 设置其在界面中出现的位置  column代表列   row 代表行
timeChosen22.grid(column=3, row=4)
timeChosen23.grid(column=5, row=4)
timeChosen24.grid(column=6, row=4)
timeChosen21.current('00')    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
timeChosen22.current('00')
timeChosen23.current('00')
timeChosen24.current('00')

time_hour_start3= tkinter.IntVar()
time_min_start3=tkinter.IntVar()
time_hour_last3=tkinter.IntVar()
time_min_last3=tkinter.IntVar()
timeChosen31=tkinter.ttk.Combobox(root, width=2, textvariable=time_hour_start3)
timeChosen32=tkinter.ttk.Combobox(root, width=2, textvariable=time_min_start3)
timeChosen33=tkinter.ttk.Combobox(root, width=2, textvariable=time_hour_last3)
timeChosen34=tkinter.ttk.Combobox(root, width=2, textvariable=time_min_last3)
timeChosen31['values']= ('00','01','02','03','04','05','06','07','08','09','10','11','12')     # 设置下拉列表的值
timeChosen32['values']=('00','05','10','15','20','25','30','35','40','45','50','55')
timeChosen33['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12')
timeChosen34['values']=('00','05','10','15','20','25','30','35','40','45','50','55')
timeChosen31.grid(column=2, row=5)      # 设置其在界面中出现的位置  column代表列   row 代表行
timeChosen32.grid(column=3, row=5)
timeChosen33.grid(column=5, row=5)
timeChosen34.grid(column=6, row=5)
timeChosen31.current('00')    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
timeChosen32.current('00')
timeChosen33.current('00')
timeChosen34.current('00')

time_hour_start4= tkinter.IntVar()
time_min_start4=tkinter.IntVar()
time_hour_last4=tkinter.IntVar()
time_min_last4=tkinter.IntVar()
timeChosen41=tkinter.ttk.Combobox(root, width=2, textvariable=time_hour_start4)
timeChosen42=tkinter.ttk.Combobox(root, width=2, textvariable=time_min_start4)
timeChosen43=tkinter.ttk.Combobox(root, width=2, textvariable=time_hour_last4)
timeChosen44=tkinter.ttk.Combobox(root, width=2, textvariable=time_min_last4)
timeChosen41['values']= ('00','01','02','03','04','05','06','07','08','09','10','11','12')     # 设置下拉列表的值
timeChosen42['values']=('00','05','10','15','20','25','30','35','40','45','50','55')
timeChosen43['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12')
timeChosen44['values']=('00','05','10','15','20','25','30','35','40','45','50','55')
timeChosen41.grid(column=2, row=6)      # 设置其在界面中出现的位置  column代表列   row 代表行
timeChosen42.grid(column=3, row=6)
timeChosen43.grid(column=5, row=6)
timeChosen44.grid(column=6, row=6)
timeChosen41.current('00')    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
timeChosen42.current('00')
timeChosen43.current('00')
timeChosen44.current('00')

label_blank=tkinter.Label(root,text='--')
label_blank.grid(row=3,column=4)
label_blank=tkinter.Label(root,text='--')
label_blank.grid(row=4,column=4)
label_blank=tkinter.Label(root,text='--')
label_blank.grid(row=5,column=4)
label_blank=tkinter.Label(root,text='--')
label_blank.grid(row=6,column=4)
#************************************************************************************************

#**********************************************************************************************
#地点选择模块
place1= tkinter.StringVar()
place1.set('北食堂一层')
placeChosen1=tkinter.OptionMenu(root, place1, "北食堂一层","北食堂二层","北食堂三层",
                               "南食堂一层","南食堂二层" ,"南食堂三层", "清真食堂","中食堂","其他")
placeChosen1.grid(row=3,column=7)

place2= tkinter.StringVar()
place2.set('北食堂一层')
placeChosen2=tkinter.OptionMenu(root, place2, "北食堂一层","北食堂二层","北食堂三层",
                               "南食堂一层","南食堂二层" ,"南食堂三层", "清真食堂","中食堂","其他")
placeChosen2.grid(row=4,column=7)

place3= tkinter.StringVar()
place3.set('北食堂一层')
placeChosen3=tkinter.OptionMenu(root, place3, "北食堂一层","北食堂二层","北食堂三层",
                               "南食堂一层","南食堂二层" ,"南食堂三层", "清真食堂","中食堂","其他")
placeChosen3.grid(row=5,column=7)

place4= tkinter.StringVar()
place4.set('北食堂一层')
placeChosen4=tkinter.OptionMenu(root, place4, "北食堂一层","北食堂二层","北食堂三层",
                               "南食堂一层","南食堂二层" ,"南食堂三层", "清真食堂","中食堂","其他")
placeChosen4.grid(row=6,column=7)
#***********************************************************************************************

#*************************************************************************************
#食物填充模块
breakfast_food=tkinter.StringVar()
lunch_food=tkinter.StringVar()
dinner_food=tkinter.StringVar()
night_food=tkinter.StringVar()
text_food1=tkinter.Text(root,width=20,height=3)
text_food1.grid(row=3,column=1)
text_food2=tkinter.Text(root,width=20,height=3)
text_food2.grid(row=4,column=1)

text_food3=tkinter.Text(root,width=20,height=3)
text_food3.grid(row=5,column=1)

text_food4=tkinter.Text(root,width=20,height=3)
text_food4.grid(row=6,column=1)

#*************************************************************************************
lingshi_text=tkinter.Text(root,width=20,height=2)#单行，可用于零食
lingshi_text.grid(row=7,column=1)
lingshi=tkinter.IntVar()
lingshi.set(1)
check1=tkinter.Checkbutton(root,text=u'零食',variable=lingshi,
                           onvalue=1,offvalue=0)
check1.grid(row=7,column=0)

softdrinks=tkinter.IntVar()
softdrinks.set(1)
check2=tkinter.Checkbutton(root,text=u'饮料',variable=softdrinks,onvalue=1,offvalue=0)
check2.grid(row=8,column=0)

softdrinks_text=tkinter.Text(root,width=20,height=2)
softdrinks_text.grid(row=8,column=1)

fruit=tkinter.IntVar()
fruit.set(1)
check3=tkinter.Checkbutton(root,text='水果',variable=fruit,onvalue=1,offvalue=0)
check3.grid(row=9,column=0)

fruit_text=tkinter.Text(root,width=20,height=2)
fruit_text.grid(row=9,column=1)

#******************************************************************************
#核心函数模块
name=time_chosen01.get()+time_chosen02.get()+time_chosen03.get()+'.txt'
#f=open(name,mode='w',encoding='utf-8')
#f.close()
#def read(breakfast_read):

def save():
    if int(time_chosen01.get())==2017 and int(time_chosen02.get())==int(timenow.month)and int(timenow.day)-int(time_chosen03.get())<=7:

        breakfast_read = tkinter.StringVar()
        lunch_read = tkinter.StringVar()
        dinner_read = tkinter.StringVar()
        night_read = tkinter.StringVar()
        lingshi_read=tkinter.StringVar()
        softdrinks_read=tkinter.StringVar()
        fruit_read=tkinter.StringVar()
        breakfast_read.set(text_food1.get("1.0", 'end-1c'))  # breakfast_read是写入文件引入的变量，breakfast是文本框变量
        lunch_read.set(text_food2.get("1.0", 'end-1c'))
        dinner_read.set(text_food3.get("1.0", 'end-1c'))
        night_read.set(text_food4.get("1.0", 'end-1c'))
        lingshi_read.set(lingshi_text.get("1.0",'end-1c'))
        softdrinks_read.set(softdrinks_text.get("1.0",'end-1c'))
        fruit_read.set(fruit_text.get("1.0",'end-1c'))
        f=open(name,mode='wt',encoding='utf-8')
        f.write('日期：'+time.strftime("%Y/%m/%d")+'\n')
        f.write('早餐：'+breakfast_read.get()+'\n')
        f.write('地点：'+place1.get()+'\n')
        f.write('时间：' + str(time_hour_start1.get()) + ':' + str(time_min_start1.get()) + '-'+str(time_hour_last1.get()) + ':' + str(time_min_last1.get()) + '\n')
        f.write('午餐：'+lunch_read.get()+'\n')
        f.write('地点：'+place2.get()+'\n')
        f.write('时间：' + str(time_hour_start2.get()) + ':' + str(time_min_start2.get()) + '-'+str(time_hour_last2.get()) + ':' + str(time_min_last2.get()) + '\n')
        f.write('晚餐：'+dinner_read.get()+'\n')
        f.write('地点：'+place3.get()+'\n')
        f.write('时间：' + str(time_hour_start3.get()) + ':' + str(time_min_start3.get()) + '-' + str(time_hour_last3.get()) + ':' + str(time_min_last3.get()) + '\n')
        f.write('夜宵：'+night_read.get()+'\n')
        f.write('地点：'+place4.get()+'\n')
        f.write('时间：' + str(time_hour_start4.get()) + ':' + str(time_min_start4.get()) + '-' + str(time_hour_last4.get()) + ':' + str(time_min_last4.get()) + '\n')
        if lingshi.get()==1:
            f.write('零食：'+lingshi_read.get()+'\n')
        else:
            f.write('零食：NULL'+'\n')
        if softdrinks.get()==1:
            f.write('饮料：'+softdrinks_read.get()+'\n')
        else:
            f.write('饮料：NULL'+'\n')
        if fruit.get()==1:
            f.write('水果：'+fruit_read.get()+'\n')
        else:
            f.write('水果：NULL'+'\n')
        f.close()
    else:
        warning = tkinter.messagebox.showinfo(parent=root, title='警告', message='超过一星期无法保存！')
#******************************************************************************
button1=tkinter.Button(root,text=u'编辑')
button2=tkinter.Button(root,text=u'查看')
button3=tkinter.Button(root,text="保存",command=save)
button1.grid(row=1,column=8)
button2.grid(row=1,column=9)
button3.grid(row=1,column=10)
root.mainloop()
