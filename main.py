import pyodbc
from tkinter import *
import configparser

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings.ini")  # читаем конфиг

server = config["MSSQL"]["server"]
database = config["MSSQL"]["database"]
username = config["MSSQL"]["username"]
password = config["MSSQL"]["password"]
fontsize = config["WINDOW"]["fontsize"]


cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


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
window.attributes("-topmost", True)
lbl = Label(window, font=("Arial Bold", fontsize))
lbl.grid(column=0, row=0)

getcnt()
window.mainloop()
