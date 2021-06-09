import pyodbc
from tkinter import *
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'DESKTOP-67EPKQ2\\SQLEXPRESS'
database = 'RusGuardDB'
username = 'sa'
password = '123456'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Sample select query
# cursor.execute('''
# SELECT      COUNT(*) AS Expr1
# FROM        [Log]
# WHERE       (DateTime >= DATEADD(day, DATEDIFF(day, 0, GETDATE()), 0)) AND
#             (DateTime < DATEADD(day, DATEDIFF(day, - 1, GETDATE()), 0)) AND
#             (Message = N'Вход по лицу')
# ''')


def getcnt():
    cursor.execute('''
SELECT      COUNT(*) AS Expr1
FROM        [Log]
WHERE       (DateTime >= DATEADD(day, DATEDIFF(day, 0, GETDATE()), 0)) AND
            (DateTime < DATEADD(day, DATEDIFF(day, - 1, GETDATE()), 0)) AND
            (Message = N'Вход по лицу')
        ''')
    message = str(cursor.fetchone()[0]).zfill(3)
    lbl.config(text=message)
    lbl.after(1000, getcnt)
# row = cursor.fetchone()
# print(row)
window = Tk()
window.title("Счётчик посетителей")
lbl = Label(window, font=("Arial Bold", 100))
lbl.grid(column=0, row=0)

getcnt()
window.mainloop()
