import mysql.connector
con_obj=mysql.connector.connect(host='localhost',user='root',password='root')
cur_obj=con_obj.cursor()

cur_obj.execute('select emp_id,emp_name,emp_age from ravi.employee')
values=cur_obj.fetchall()
for val in values:
    print(val)
print(('--')*30)
#condition

cur_obj.execute('select * from ravi.employee where emp_id>12 ')
values1=cur_obj.fetchall()
for val in values1:
    print(val)


#update the values
print('*'*50)
cur_obj.execute("update ravi.employee set emp_address='mandya' where emp_address='mudigere'")
cur_obj.execute('select * from ravi.employee where emp_id=10')
values2=cur_obj.fetchall()
for val in values2:
    print(val)
con_obj.close()

