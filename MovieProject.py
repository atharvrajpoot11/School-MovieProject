####################################################################
################### Python SQL Connection ##########################

import pymysql

def insert_Record(tcno,tcname,tmname,no_of_tkt,tstime,dt,sum1):
    con=pymysql.connect(host="localhost",user="root",password="Abc123",db="shows")
    c=con.cursor()
    sql="insert into myshow(cno,cname,mname,no_of_tickets,show_time,sdate,charge) \
values ('%d','%s','%s','%d','%s','%s','%d')"%(tcno,tcname,tmname,no_of_tkt,tstime,dt,sum1)
    try:
        c.execute(sql)
        con.commit()
        print("Record Inserted Successfully . . . ")
        print("\t\t=====================================")
        print("\t\t\t Total Amount is : ",sum1)
        print("\t\t=====================================")
    except:
        con.rollback()
    con.close()
    c.close()
####################################################################
################# View All Customer Details ########################
def All_Record():
    con=pymysql.connect(host="localhost",user="root",password="Abc123",db="shows")
    c=con.cursor()
    sql="select * from myshow"
    try:
        c.execute(sql)
        row=c.fetchall()
        for r in row:
            print(r[0],"\t",r[1],"\t",r[2],"\t",r[3],"\t",r[4],"\t",r[5],"\t",r[6])
    except:
        print("Unable to fetch Record....")
    con.close()
    c.close()

####################################################################
################# View One Customer Details ########################
def One_Record():
    con=pymysql.connect(host="localhost",user="root",password="Abc123",db="shows")
    c=con.cursor()
    cid=int(input("\t\tWhich Customer Details You Want To See? Enter Customer ID : "))
    sql="select * from myshow where cno ="+str(cid)
    try:
        c.execute(sql)
        row=c.fetchall()
        for r in row:
            print("\t\t======================================================")
            print("\t\t\t Personal Information of Customer")
            print("\t\t======================================================")
            print("\t\t\tCustomer Number: ",r[0])
            print("\t\t\tCustomer Name: ",r[1])
            print("\t\t\tMovie Name: ",r[2])
            print("\t\t\tNumber Of Tickets: ",r[3])
            print("\t\t\tShow Time: ",r[4])
            print("\t\t\tShow Date: ",r[5])
            print("\t\t\tCharge: ",r[6])
            
    except:
        print("Unable to fetch Record....")
    con.close()
    c.close()

####################################################################
################# View Many Customer Details ########################

def Many_Record():
    con=pymysql.connect(host="localhost",user="root",password="Abc123",db="shows")
    c=con.cursor()
    rec=int(input("How Many Record Do You Want To See : "))
    sql="select * from myshow"
    try:
        c.execute(sql)
        row=c.fetchmany(rec)
        for r in row:
            print(r[0],"\t",r[1],"\t",r[2],"\t",r[3],"\t",r[4],"\t",r[5],"\t",r[6])
    except:
        print("Unable to fetch Record....")
    con.close()
    c.close()


####################################################################
################# Update Record ####################################

def Update_Record():
    con=pymysql.connect(host='localhost',user='root',password='ujjwal',database='school')
    c=con.cursor()
    print("\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\t+\t UPDATE Customer INFORMATION                    +")
    print("\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\t+\t\t1. Update Customer Name               +")
    print("\t+\t\t2. Update Movie Name                  +")
    print("\t+\t\t3. Update Number Of Ticket            +")
    print("\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    q=int(input("\t\tWhat do you want to update? Select a Choice : "))
    rno=int(input("\t\tCustomer Number of Student :"))
    if q==1:
        cont=int(input("Please Give me your Updated Name : "))
        sql="update myshow set cname ="+"'"+str(cont)+"'"+"where cno ="+str(rno)
        try:
            c.execute(sql)
            con.commit()
            print("Successfully Updated . . . ")
        except:
            con.rollback()

    if q==2:
        add=input("Please Give me your New Movie Name : ")
        sql="update students set mname ="+"'"+add+"'"+"where cno ="+str(rno)
        try:
            c.execute(sql)
            con.commit()
            print("Successfully Updated . . . ")
        except:
            con.rollback()

    if q==3:
        adr=int(input("Please Give me your Updated Number Of Ticket : "))
        sql="update students set no_of_tickets ="+"'"+str(adr)+"'"+"where cno ="+str(rno)
        try:
            c.execute(sql)
            con.commit()
            print("Successfully Updated . . . ")
        except:
            con.rollback()
    con.close()
    c.close()

############################ Main Menu #############################
while True:
    print("\t\t==================================================")
    print("\t\t\t\t INOX THEATRE")
    print("\t\t==================================================")
    print("\t\t+\t1. Book Show                              +")
    print("\t\t+\t2. View Movies                            +")
    print("\t\t+\t3. View Customer Information              +")
    print("\t\t+\t4. Update Customer Information            +")
    print("\t\t==================================================")
    ch=int(input("Which Option Do  You Want To perfrom. Enter Your Choice = "))
    total=0
    sum1=0
    if ch==1:
        
        tcno=int(input("\t\tCustomer Number : "))
        tcname=input("\t\tCustomer Name : ")
        tmname=input("\t\tMovie Name : ")
        no_of_tkt=int(input("\t\tHow Many Tickets do You Want : "))
        
        tstime=input("\t\tTiming of the Show : ")
        dt=input("\t\tToday Date : ")
        tch=int(input("\t\tCost of One Ticket : "))
        total=total+(no_of_tkt*tch)
        q1=input("\t\tDo You Want to Prefer Snacks Y/N : ")
        t=0
        if q1.upper()=='Y':
            while True:
                print("\t\t+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("\t\t+\t1. Soft Drink                         (650ml)             130/-      \t+")
                print("\t\t+\t2. Swiss Chocolate Can                (200ml)             150/-      \t+")
                print("\t\t+\t3. Cafe Mocha Can                     (200ml)             150/-      \t+")
                print("\t\t+\t4. Cheese Popcorn                     (70gms)             270/-      \t+")
                print("\t\t+\t5. Caramel Popcorn                    (70gms)             270/-      \t+")
                print("\t\t+\t6. Fried Samosa                       (140gms)            60/-       \t+")
                print("\t\t+\t7. Veg Pizza                          (8 inch)            135/-      \t+")
                print("\t\t+\t8. Veg Cheese Sandwich                (140gms)            90/-       \t+")
                print("\t\t+\t9. Nachos                             (100gms)            340/-      \t+")
                print("\t\t+\t10. Icecream                          (100gms)            150/-      \t+")
                print("\t\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            
                q2=int(input("\t\t Choose Your Snacks : "))
                if q2==1:
                    cost=130
                elif q2==2:
                    cost=150
                elif q2==3:
                    cost=150
                elif q2==4:
                    cost=270
                elif q2==5:
                    cost=270
                elif q2==6:
                    cost=60
                elif q2==7:
                    cost=135
                elif q2==8:
                    cost=90
                elif q2==9:
                    cost=340
                elif q2==10:
                    cost=150
                quan=int(input("How Many Quantity Do You Want : "))
                t=t+(cost*quan)
                q3=input("Do you Want to choose Another snack : Y/N : ")
                if q3.upper()=='N':
                    break
            
            sum1=total+t
            insert_Record(tcno,tcname,tmname,no_of_tkt,tstime,dt,sum1)

    if ch==2:
        q4=input("\t\tDo You Want To See Movies In Theater Y/N : ")
        if q4.upper()=='Y':
            print("\t\t+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\t\t+\t1. Avatar 2                 Screen 1             100/-      \t+")
            print("\t\t+\t2. Black Panther 2          Screen 2             230/-      \t+")
            print("\t\t+\t3. The Batman               Screen 3             180/-      \t+")
            print("\t\t+\t4. Kantra                   Screen 4             120/-      \t+")
            print("\t\t+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    elif ch==3:
        print()
        print()
        print("\t\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("\t\t+\t\t Details of the customer                 +")
        print("\t\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("\t\t+\t\t1. View All Customer Details             +")
        print("\t\t+\t\t2. View One Customer Details             +")
        print("\t\t+\t\t3. View Many Customer Details            +")
        print("\t\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        q=int(input("\t\t Enter your Choice = "))
        if q==1:
            All_Record()
        elif q==2:
            One_Record()
        elif q==3:
            Many_Record()

    elif ch==4:
        Update_Record()
        
            
