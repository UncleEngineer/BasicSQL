import sqlite3

conn = sqlite3.connect('submarine.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS submarine (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
		brand text,
		price int)""")


def insert_submarine(brand,price):
    ID = None
    with conn:
        c.execute("""INSERT INTO submarine VALUES (?,?,?)""",
                  (ID,brand,price))
    conn.commit()
    print('Data was inserted')

def view_submarine():
    with conn:
        c.execute("SELECT * FROM submarine")
        submarine = c.fetchall()
        print(submarine)

    return submarine


#insert_submarine('China',10000)
#insert_submarine('Russia',30000)

allsubmarine = view_submarine()
print("First Submarine Brand: ",allsubmarine[0][1])

# delete function

def del_submarine(ID):
    with conn:
        c.execute("DELETE FROM submarine WHERE ID=(?)",[(ID)])
    conn.commit()
    print('Data was delete')


def update_submarine(ID,price_change):
    with conn:
        c.execute("UPDATE submarine SET price = (?) WHERE ID=(?)",([price_change,ID]))
    conn.commit()
    print('Data was updated')

# << delete submarine id = 2 >>
#del_submarine(2)

# << update submarine id = 2 change price to 35000 >>
#update_submarine(2,35000)
view_submarine()
