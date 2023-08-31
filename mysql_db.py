import pymysql as sqldata
conn = sqldata.connect(host='localhost', user='root',
                       passwd='', database='collage_details')

corsorobj = conn.cursor()
# create database
'''
try:
    db = "create database collage_details"
    corsorobj.execute(db)
    print("data base created")
except:
    print("database does not created...")
'''

# create Database Table
'''try:
    corsorobj.execute(
        "create table information(id INT primary key auto_increment,name varchar(50),department varchar(50),en_no bigint(12),email_id varchar(50))")
    print("data base Table is  created")
except:
    print("database Table is alreay created...")
'''

while True:

    us = int(input('''
    1.INSERT THE DATA BASE
    2.DELETE THE DATA BASE
    3.UPDATE/MODIFY THE DTABASE
    4.SEARCH THE DATA BASE
    5.SHOW THE DATA BASE
    6.END THE THE DATA BASE  
    '''))

    if us == 1 and us < 7:
        try:
            NAME = input("ENTER THE NAME FOR INSERT IN DATABASE:-")
            DEP = input("ENTER THE DEPARTMENT NAME FOR INSERT IN DATABASE:-")
            EN_NO = input(
                "ENTER THE ENROLLMENT NUMBER  FOR INSERT IN DATABASE:-")
            EMAIL = input("ENTER THE EMAIL I'D FOR INSERT IN DATABASE:-")
            ins = "INSERT  INTO information(name,department,en_no,email_id) VALUES(%s,%s,%s,%s)"
            db = (NAME, DEP, EN_NO, EMAIL)
            corsorobj.execute(ins, db)
            conn.commit()
            print(" ----DATA SUCCESFULLU INSERTED----")
        except:
            print(" ----DATA DOES NOT INSERTED----")
    elif us == 2 and us < 7:
        try:
            abc = "DELETE FROM information WHERE id=%s"
            corsorobj.execute(abc, id)
            conn.commit()
            print(" ----DATA SUCCESFULL DELETED----")
        except:
            print(" ----DATA DOES NOT DELETED----")

    elif us == 3 and us < 7:
        try:
            ID = input("ENTER THE ID FOR UPDATE IN DATABASE:-")
            NAME = input("ENTER THE NAME FOR UPDATE IN DATABASE:-")
            DEP = input("ENTER THE DEPARTMENT NAME FOR UPDATE IN DATABASE:-")
            EN_NO = input(
                "ENTER THE ENROLLMENT NUMBER  FOR UPDATE IN DATABASE:-")
            EMAIL = input("ENTER THE EMAIL I'D FOR UPDATE IN DATABASE:-")
            abc = "update information set name=%s,department=%s,en_no=%s,email_id=%s where id=%s"
            db = (NAME, DEP, EN_NO, EMAIL, ID)
            corsorobj.execute(abc, db)
            conn.commit()
            print(" ----DATA SUCCESFULLU UPDATED----")
        except:
            print(" ----DATA DOES NOT  UPDATED----")

    elif us == 4 and us < 7:
        try:
            i_d = input("ENTER THE ID FOR SEARCH DATA:-")

            print("{:<15}{:<20}{:<15}{:<15}{:<30}".format(
                "id", "name", "department", "enrollment_no", "email i'd"))
            abc = "SELECT * FROM information where id='"+i_d+"'"
            corsorobj.execute(abc)
            sdata = corsorobj.fetchall()
            for a in sdata:
                print("{:<15}{:<20}{:<15}{:<15}{:<30}".format(
                    a[0], a[1], a[2], a[3], a[4]))
        except:
            print("YOU SEARCH DATA IS NOT SHOW BECAUSE YOU  ARE WRONG ID ENTER....")
    elif us == 5 and us < 7:
        ord = int(input('''
                  1.NORMAL SHOW DATA
                  2.ASSENDING ORDER  
                  3.DESSENDING ORDER 
                  '''))
        if ord == 1 and ord < 4:
            try:
                print("{:<15}{:<20}{:<15}{:<15}{:<30}".format(
                    "id", "name", "department", "enrollment_no", "email i'd"))
                abc = "SELECT * FROM information "
                corsorobj.execute(abc)
                sdata = corsorobj.fetchall()
                for a in sdata:
                    print("{:<15}{:<20}{:<15}{:<15}{:<30}".format(
                        a[0], a[1], a[2], a[3], a[4]))
            except:
                print("does not found...")

        elif ord == 2 and ord < 4:
            try:
                print("{:<15}{:<20}{:<15}{:<15}{:<30}".format(
                    "id", "name", "department", "enrollment_no", "email i'd"))
                abc = "SELECT * FROM information order by id ASC"
                corsorobj.execute(abc)
                sdata = corsorobj.fetchall()
                for a in sdata:
                    print("{:<15}{:<20}{:<15}{:<15}{:<30}".format(
                        a[0], a[1], a[2], a[3], a[4]))
            except:
                print("does not found...")
        elif ord == 3 and ord < 3:
            try:
                print("{:<15}{:<20}{:<15}{:<15}{:<30}".format(
                    "id", "name", "department", "enrollment_no", "email i'd"))
                abc = "SELECT * FROM information order by id DESC"
                corsorobj.execute(abc)
                sdata = corsorobj.fetchall()
                for a in sdata:
                    print("{:<15}{:<20}{:<15}{:<15}{:<30}".format(
                        a[0], a[1], a[2], a[3], a[4]))
            except:
                print("does not found...")

        else:
            print("PLEASE ENTER THE PERFECT NUMBER FOR SHOW DATA ")
    elif us == 6 and us < 7:
        break
    else:
        print("PLEASE ENTER THE PERFECT NUMBER")
