import mysql.connector
con_obj=mysql.connector.connect(host='localhost',user='root',password='root')
cur_obj=con_obj.cursor()
try:
    cur_obj.execute('create database ravi')
    if cur_obj:
        print('database created')
    else:
        print('not created')
except:
    con_obj.rollback()
con_obj.close()


