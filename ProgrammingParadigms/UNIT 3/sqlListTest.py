from tkinter import *
from tkinter import ttk
import os
import sqlite3

absolute_path = os.path.dirname(__file__)
database_relative_path = "ims.db"
database_full_path = os.path.join(absolute_path, database_relative_path)

if __name__ == "__main__":
    app = Tk()
    app.geometry("640x360+0+0")
    # la parte que importa (inicio)
    connection = sqlite3.connect(database = database_full_path)
    cursor = connection.cursor()
    result = cursor.execute("SELECT name FROM employee")
    dataListTuples = result.fetchall()
    dataList = [data[0] for data in dataListTuples]
    # la parte que importa (final)
    print(dataList)
    connection.close()
    # combobox agregando lo que se saco
    databaseList = ttk.Combobox(app, values=dataList)
    databaseList.pack()
    app.mainloop()
    
