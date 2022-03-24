# memberdb.py

import sqlite3

conn = sqlite3.connect('memberdb.sqlite3') #สร้างไฟล์ฐานข้อมูล
c = conn.cursor()


# สร้างตารางในการจัดเก็บ
c.execute("""CREATE TABLE IF NOT EXISTS member (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				membercode TEXT,
				fullname TEXT,
				tel TEXT,
				usertype TEXT,
				points INTEGER ) """)


def Insert_member(membercode,fullname,tel,usertype,points):
	# CREATE
	with conn:
		command = 'INSERT INTO member VALUES (?,?,?,?,?,?)' # SQL
		c.execute(command,(None,membercode,fullname,tel,usertype,points))
	conn.commit() # SAVE DATABASE
	print('saved')


def View_member():
	# READ
	with conn:
		command = 'SELECT * FROM member'
		c.execute(command)
		result = c.fetchall()
	print(result)
	return result


def Update_member(ID,field,newvalue):
	# UPDATE
	with conn:
		command = 'UPDATE member SET {} = (?) WHERE ID=(?)'.format(field)
		c.execute(command,([newvalue,ID]))
	conn.commit()
	print('updated')


def Delete_member(ID):
	# DELETE
	with conn:
		command = 'DELETE FROM member WHERE ID=(?)'
		c.execute(command,([ID]))
	conn.commit()
	print('deleted')



# res = View_member()
# print(res[1])

#Update_member(2,'fullname','สมศักดิ์ เจริญรุ่งเรือง')

#Delete_member(1)
#View_member()


#Insert_member('MB-1001','สมชาย เก่งมาก','0801234568','general',100)
