import mysql.connector
con_obj=mysql.connector.connect(host='localhost',user='root',password='root')
cur_obj=con_obj.cursor()
try:
    cur_obj.execute('create table ravi.employee(emp_id int,emp_name varchar(20),emp_age int,emp_address varchar(50),emp_gender varchar(20),emp_salary float,emp_role varchar(20))')

    if cur_obj:
        print('table created')
    else:
        print('not created')

except:
    con_obj.rollback()
con_obj.close()