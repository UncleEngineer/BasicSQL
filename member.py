# member.py

import sqlite3
from tkinter import *
from tkinter import ttk

conn = sqlite3.connect('member.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS memberinfo (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				memberid TEXT,
				first_name TEXT,
				last_name TEXT,
				tel TEXT,
				points INTEGER,
				note TEXT ) """)

def Insert_NewMember(memberid,first_name,last_name,tel,points,note):
	with conn:
		command = 'INSERT INTO memberinfo VALUES (?,?,?,?,?,?,?)'
		c.execute(command,(None,memberid,first_name,last_name,tel,points,note))
	conn.commit()
	print('Saved')

def View_Member():
	with conn:
		command = 'SELECT * FROM memberinfo'
		c.execute(command)
		result = c.fetchall() # c.fetchone() , c.fetchmany(5)
	print(result)
	return result

def View_OneMember(memberid):
	with conn:
		command = 'SELECT * FROM memberinfo WHERE memberid=(?)'
		c.execute(command,([memberid]))
		result = c.fetchall() # c.fetchone() , c.fetchmany(5)
	print(result)
	return result


def Delete_Member(ID):
	with conn:
		command = 'DELETE FROM memberinfo WHERE ID=(?)'
		c.execute(command,([ID]))
	conn.commit()
	print('{}: deleted'.format(ID))


def Update_Member(ID,field,data):
	with conn:
		command = 'UPDATE memberinfo SET {} = (?) WHERE ID=(?)'.format(field)
		c.execute(command,([data,ID]))
	conn.commit()
	print('{}: {}={} updated'.format(ID,field,data))


# Insert_NewMember('C1003','สมศรี','ดีจัง','0809876543',50,'สมาชิกขาประจำ')
# Delete_Member(1)
# Update_Member(2,'first_name','สมหญิง')
# View_Member()
# View_OneMember('C1003')

GUI = Tk()
GUI.geometry('900x600')
GUI.title('โปรแกรมบันทึก member')

v_search = StringVar()
v_search.set('C1001')
search = ttk.Entry(GUI,textvariable=v_search,font=(None,20),width=15)
search.place(x=50,y=50)

from tkinter import messagebox

def SearchMember():
	search = v_search.get() # ดึงข้อมูล
	data = View_OneMember(search)
	if len(data) >= 1:
		data = data[0]
		v_memberid.set(data[1])
		v_first_name.set(data[2])
		v_last_name.set(data[3])
		v_tel.set(data[4])
		v_points.set(data[5])
		v_note.set(data[6])
	else:
		messagebox.showwarning('Not found','ไม่มีสมาชิกคนนี้ กรุณาตรวจสอบรหัสสมาชิกให้ถูกต้อง')


FB1 = Frame(GUI)
FB1.place(x=90,y=100)
bsearch = ttk.Button(FB1,text='ค้นหาชื่อสมาชิก',command=SearchMember)
bsearch.pack(ipadx=30,ipady=20)

##########RIGHT############
F2 = Frame(GUI)
F2.place(x=400,y=100)


v_memberid = StringVar()
L = Label(F2,text='รหัสสมาชิก',font=(None,15)).pack()
E1 = ttk.Entry(F2,textvariable=v_memberid,font=(None,20),width=25)
E1.pack()

v_first_name = StringVar()
L = Label(F2,text='ชื่อ',font=(None,15)).pack()
E2 = ttk.Entry(F2,textvariable=v_first_name,font=(None,20),width=25)
E2.pack()

v_last_name = StringVar()
L = Label(F2,text='นามสกุล',font=(None,15)).pack()
E3 = ttk.Entry(F2,textvariable=v_last_name,font=(None,20),width=25)
E3.pack()

v_tel = StringVar()
L = Label(F2,text='เบอร์โทร',font=(None,15)).pack()
E4 = ttk.Entry(F2,textvariable=v_tel,font=(None,20),width=25)
E4.pack()

v_points = StringVar()
L = Label(F2,text='Points',font=(None,15)).pack()
E5 = ttk.Entry(F2,textvariable=v_points,font=(None,20),width=25)
E5.pack()

v_note = StringVar()
L = Label(F2,text='อื่นๆ',font=(None,15)).pack()
E6 = ttk.Entry(F2,textvariable=v_note,font=(None,20),width=25)
E6.pack()

FB2 = Frame(GUI)
FB2.place(x=520,y=520)
bsave = ttk.Button(FB2,text='บันทึก/อัพเดต')
bsave.pack(ipadx=30,ipady=20)


GUI.mainloop()