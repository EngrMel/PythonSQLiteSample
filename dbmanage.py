import sqlite3

conn = sqlite3.connect('test1.db') #connecting to sqlitedb, this will create a new one if there's no existing db.

'''
Creating table/s, you need to structure your database first before implementing CRUD.
'''
def create_table():
    try:
        conn = sqlite3.connect('test1.db')
        conn.execute('''CREATE TABLE "ITEM_TABLE" (
                "BARCODE"	TEXT,
                "ITEM_NAME"	TEXT,
                "QUANTITY"	INTEGER,
                PRIMARY KEY("BARCODE")
            );''')
        conn.close()
    except sqlite3.OperationalError:
        print("Table exists")

'''
Basic CRUD examples using parameter and qmark styling
'''        
        
def create_record(barcode, item_name, qty):
    try:
        conn = sqlite3.connect('test1.db')
        cur = conn.cursor()
        cur.execute(("INSERT INTO ITEM_TABLE VALUES (?,?,?)"), (barcode,item_name,qty))
        conn.commit()
    except:
        print("error creating record")
    conn.close()

def read_all():
    try:
        conn = sqlite3.connect('test1.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM ITEM_TABLE")
        records = cur.fetchall()
        print(records)
        #for record in records:
            #print(record)
    except:
        print("error in reading all")
    conn.close()

def delete_record(barcode):
    try:
        conn = sqlite3.connect('test1.db')
        cur = conn.cursor()
        cur.execute(("DELETE FROM ITEM_TABLE WHERE BARCODE = ?"), (barcode,))
        conn.commit()
    except:
        print("error deleting record")
    conn.close()

def update_record(barcode,new_name,new_qty):
    try:
        conn = sqlite3.connect('test1.db')
        cur = conn.cursor()
        cur.execute(("UPDATE ITEM_TABLE SET ITEM_NAME= ?, QUANTITY=? WHERE BARCODE =?"), (new_name,new_qty,barcode))
        conn.commit()
    except:
        print("error updating record")
    conn.close()



