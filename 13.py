import mysql.connector
con_obj=mysql.connector.connect(host='localhost',user='root',password='root')
cur_obj=con_obj.cursor()
try:
    val=("insert into ravi.employee(emp_id,emp_name,emp_age,emp_address,emp_gender,emp_salary,emp_role)values(10,'vijay',22,'mudigere','male',200202,'se')")
    val1=("insert into ravi.employee(emp_id,emp_name,emp_age,emp_address,emp_gender,emp_salary,emp_role)values(11,'chandra',23,'bangalore','male',20202,'de')")
    val2=("insert into ravi.employee(emp_id,emp_name,emp_age,emp_address,emp_gender,emp_salary,emp_role)values(12,'bhoomika',22,'laggere','female',20002,'se')")
    val3=("insert into ravi.employee(emp_id,emp_name,emp_age,emp_address,emp_gender,emp_salary,emp_role)values(13,'ram',25,'bidadi','male',20022,'ts')")
    val4=("insert into ravi.employee(emp_id,emp_name,emp_age,emp_address,emp_gender,emp_salary,emp_role)values(14,'harsha',23,'banavara','male',210202,'test')")

    cur_obj.executemany(val,val1,val2,val3,val4)

    con_obj.commit()
    if cur_obj:
        print('insert data')
    else:
        print('not insert data')
except:
    con_obj.rollback()
con_obj.close()