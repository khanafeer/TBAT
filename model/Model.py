# -*- coding: utf-8 -*-
import MySQLdb
import datetime
from operator import itemgetter
from random import randint
import barcode
import collections
import threading
def get_ip():
    try:
        f = open("settings")
        x = f.read()
        if not x: x = '127.0.0.1'
        return x
    except:
        return '127.0.0.1'
class Model():
    ID = 0
    IP = get_ip()
    UN = 'root'
    PS = '*-123*-'
    DB = 'tbat_v4'
    def set_id(self,id):
            Model.ID = id
    def __init__(self):
        self.db = MySQLdb.connect(self.IP, self.UN, self.PS, self.DB, charset='utf8')
        self.db.autocommit(True)

        self.db_th = MySQLdb.connect(self.IP, self.UN, self.PS, self.DB, charset='utf8')
        self.db_th.autocommit(True)
        self.db_th_2 = MySQLdb.connect(self.IP, self.UN, self.PS, self.DB, charset='utf8')
        self.db_th_2.autocommit(True)

    def get_user(self):

        curs = self.db.cursor()
        curs.execute("select id from attend ORDER BY date DESC LIMIT 1")
        x = curs.fetchone()
        if x:
            return x[0]
        else:
            return 0
    def check_pass(self,p_id,password):

        curs = self.db.cursor()
        curs.execute("select password from res_pass where id='%s' and used='0'" %(p_id))
        if password == curs.fetchone()[0]:
            return True
        else:
            return False
    def set_pass_unused(self,p):

        curs = self.db.cursor()
        curs.execute("update res_pass set used='1' where id='%s'" %(p))

    def get_pass(self):

        curs = self.db.cursor()
        curs.execute("select id from res_pass WHERE used='0'")
        x = curs.fetchone()
        if x:
            return x[0]
        else:
            return "YOU CAN NOT RESET"
    def check_user_name(self,name):

        curs = self.db.cursor()
        curs.execute("SELECT type FROM permission WHERE uname='%s'" % (name))
        return curs.fetchone()

    def check_name_pass(self,name,password):

        curs = self.db.cursor()
        curs.execute("SELECT * FROM permission WHERE uname='%s' and password='%s'" % (name, password))
        return curs.fetchone()
    def get_user_time(self,uid):

        curs = self.db.cursor()
        curs.execute("select * from user_time where user_id='%d'" %(uid))
        return curs.fetchone()
    def get_users_access(self,uid):
        pass

        curs = self.db.cursor()
        curs.execute("select * from user_access where user_id='%d'" %(uid))
        x = []
        for i in curs.fetchall():
            if i[2] == 1:
                x.append(i[1])
        return x
    def set_user_time(self,t1,t2,working,uid):
        try:

            curs = self.db.cursor()
            curs.execute("insert into user_time VALUES ('%d','%s','%s','%s')" %(uid,t1,t2,working))

        except:

            curs = self.db.cursor()
            curs.execute("update user_time set st_dt='%s', end_dt='%s',working='%s' where user_id='%d'" %(t1,t2,working,uid))

    def set_user_access(self,uid,widget,TF):

        curs = self.db.cursor()
        curs.execute("select access from user_access where user_id='%d' and widget='%s'" %(uid,widget))
        if curs.fetchone():
            curs.execute("update user_access set access='%s' WHERE user_id='%d' and widget='%s'" %(TF,uid,widget))

        else:
            curs.execute("insert into user_access VALUES ('%d','%s','%s')" % (uid, widget,TF))

    def get_user_info(self,id):

        curs = self.db.cursor()
        curs.execute("select * from permission where id = '%s'" %(int(id)))
        return curs.fetchone()
    def get_all_users(self):

        curs = self.db.cursor()
        curs.execute("select name from permission")
        cc = [item[0] for item in curs.fetchall()]
        return cc
    def get_users_name(self):

        curs = self.db.cursor()
        curs.execute("select uname from permission")
        cc = [item[0] for item in curs.fetchall()]
        return cc
    def add_user(self,name,uname,passw,type):
        try:

            curs = self.db.cursor()
            curs.execute("insert into permission (name,uname,password,type) VALUES ('%s','%s','%s','%s')" % (
            name, uname, passw, type))

            return True
        except:
            return False
    def delete_user(self,ufname):
        try:

            curs = self.db.cursor()
            curs.execute("delete from permission WHERE name = '%s'" %(ufname))

            return True
        except:
            return False
    def update_user(self,name,uname,password,type,uid):
        try:

            curs = self.db.cursor()
            curs.execute("update permission set name = '%s', uname='%s',password='%s',type='%s' WHERE id='%d'" %(name,uname,password,type,int(uid)))

            return True
        except:
            return False
    def get_last_date_exp(self, ph):

        curs = self.db.cursor()
        curs.execute("select date from buy_orders WHERE exp_phone='%s' ORDER BY date DESC" % (ph))
        return curs.fetchall()
    def get_exp_dept(self, ph):

        curs = self.db.cursor()
        curs.execute("select tottal,paid,tasded from buy_orders WHERE exp_phone='%s' and retrieve='0'" % (ph))
        x = curs.fetchall()
        dept = 0
        if x:
            for i in x:
                dept += (i[0] - i[1]) - i[2]
        return dept
    def get_user_id(self,uname):

        curs = self.db.cursor()
        curs.execute("select id from permission WHERE name='%s'" %(uname))
        x = curs.fetchone()
        if x:
            return int(x[0])
        else:
            return 0
    def get_user_name(self,id):

        curs = self.db.cursor()
        sql ="select name from permission WHERE id='%d'" %(id)
        curs.execute(sql)
        x = curs.fetchone()
        if x:
            return x[0]
        else:
            return u'تم مسح المستخدم من البرنامج'
    #add, update, delete and search course
    def add_course(self,name,days,hours,price,inst,details,t , absence , allow ,allow_defore):
        try:

            curs = self.db.cursor()
            curs.execute("insert into course (name,days,hours,price,inst,details,bill_method,absence,allow , allow_defore) VALUES ('%s','%d','%f','%f' , '%s','%s','%s','%d','%f' , '%f')" % (
                name, days , hours , price , inst , details , t , absence , allow , allow_defore))
            return True
        except Exception as ex:
            return False
    def edite_course(self,id,name,days,hours,price,inst,details,t,absence , allow , allow_before):
        try:

            curs = self.db.cursor()
            curs.execute("update course set name='%s' ,days='%d', hours='%f',price='%f',inst='%s',details='%s',bill_method='%s' , absence = '%d' , allow = '%f' , allow_defore = '%f' where name='%s'" %(name,days,hours,price,inst,details,t,absence,allow,allow_before,id))

            return True
        except:
            return False
    def get_course_price(self,gp_id):

        curs = self.db.cursor()
        curs.execute("select price from course where name='%s'" % (gp_id))
        x = curs.fetchone()
        if x:
            return x[0]
        else:
            return 0
    def get_course_bill(self,gp_id):

        curs = self.db.cursor()
        curs.execute("select bill_method from course where name='%s'" %(gp_id))
        x = curs.fetchone()
        if x:
            return x[0]
        else:
            return None

    def delete_course(self,name):
        try:

            curs = self.db.cursor()
            curs.execute("delete from course where name='%s'" %(name))

            return True
        except Exception as ex:
            return False
    def get_course_by_name(self,name):

        curs = self.db.cursor()
        curs.execute("select * from course where name='%s'" %(name))
        return curs.fetchone()
    def get_groups(self):

        curs = self.db.cursor()
        curs.execute("select name from course")
        return [item[0] for item in curs.fetchall()]
    def get_groups_st(self,bc):

        curs = self.db.cursor()
        curs.execute("select gp_name from student_course where bc='%s'" %(bc))
        return [item[0] for item in curs.fetchall()]
    def get_st_gp(self,phone):

        curs = self.db.cursor()
        curs.execute("select course.name,course.hours,course.days from course inner join student_course on course.name = student_course.gp_name where student_course.bc='%s'" %(phone))
        return curs.fetchall()
    def st_gp_not_exist(self,st,gp):

        curs = self.db.cursor()
        curs.execute("select * from student_course where bc='%s' and gp_name='%s'" %(st,gp))
        if curs.fetchall():
            return False
        else:
            return True
    def add_st_gp(self,bc,gp,price):
        #try:

            curs = self.db.cursor()
            curs.execute("insert into student_course values('%s','%s','%s')"%(bc,gp,price))

            return True
        #except:
            #return False
    def del_st_course(self,st,gp):
        try:

            curs = self.db.cursor()
            curs.execute("delete from student_course where bc='%s' and gp_name='%s'" %(st,gp))

            return True
        except:
            return False
    def add_course_time_structure(self,course,day,st,end):
        try:

            curs = self.db.cursor()
            curs.execute("insert into course_time_structure values('%s','%s','%s','%s')" %(course,day,st,end))

            return True
        except:
            return False
    def add_course_time(self, course,date, day, st, end):
        try:

            curs = self.db.cursor()
            curs.execute("insert into course_time(c_name, date, day, st_time, end_time) values('%s','%s','%s','%s','%s')" % (course,date, day, st, end))

            return True
        except:
            return False
    def get_course_structure(self,course):

        curs = self.db.cursor()
        curs.execute("select * from course_time_structure where c_name='%s'" %(course))
        return curs.fetchall()
    def get_course(self,course):
        curs = self.db.cursor()
        curs.execute("select * from course_time where c_name='%s' order by date,st_time" %(course))
        return curs.fetchall()
    def del_course_time_st(self,course,day,t1,t2):
        try:
            curs = self.db.cursor()
            curs.execute("delete from course_time_structure where c_name='%s' and day='%s' and st_time='%s' and end_time='%s'" %(course,day,t1,t2))

            return True
        except:
            return False
    def del_course_time(self, course,date,t1,t2):
            try:

                curs = self.db.cursor()
                curs.execute("delete from course_time where c_name='%s' and date='%s' and st_time='%s' and end_time='%s'" % (course,date,t1,t2))

                return True
            except:
                return False
    def del_course_time_all(self, course):
            try:

                curs = self.db.cursor()
                curs.execute("delete from course_time where c_name='%s'" % (course))

                return True
            except:
                return False
    def get_st_exams(self,bc):

        curs = self.db.cursor()
        curs.execute("select distinct x.name from exam x inner join gp_exam gp on x.name = gp.exam_name inner join student_course st_gp on st_gp.gp_name = gp.gp_name where st_gp.bc='%s'" %(bc))
        return curs.fetchall()
    def get_st_course_times(self,phone):
        curs = self.db.cursor()
        curs.execute( "select student_course.gp_name,course_time.st_time,course_time.end_time,course_time.id,course_time.date from student_course inner join course_time on student_course.gp_name = course_time.c_name where student_course.bc='%s' and course_time.date = '%s' order by course_time.st_time" %(phone,datetime.date.today()))
        out =  curs.fetchall()
        return out
    def get_course_times(self):

        curs = self.db.cursor()
        curs.execute("select student_course.gp_name,course_time.st_time,course_time.end_time,course_time.id,course_time.date from student_course inner join course_time on student_course.gp_name = course_time.c_name where course_time.date = '%s' order by course_time.st_time" %(datetime.date.today()))
        now_cs = curs.fetchall()
        return now_cs

    def attend_exam(self, st, attend_id, degree):
        '''check if attend_id exist return 2 if not add to attend table and return 1'''
        curs = self.db.cursor()
        curs.execute("select * from exam_time where id='%d'" % (attend_id))
        x = curs.fetchone()
        if x:
            if self.get_st_exam_status(st, attend_id) == u'حضور':
                return 2
            self.attend_st_exam(st, x[1], x[2], x[4], x[5], u'حضور')
            return 1
        else:
            return 3
    def attend_course(self,st,attend_id,date):
        '''check if attend_id exist return 2 if not add to attend table and return 1'''
        curs = self.db.cursor()
        curs.execute("select * from course_time where id='%d'" %(attend_id))
        x = curs.fetchone()
        if x:
            gpid = self.get_course_by_name(x[1])[0]
            if self.get_st_gp_status(st,attend_id) == u'حضور':
                return 2
            self.attend_st_gp(st,gpid,x[2],x[4],x[5],u'حضور')
            return 1
        else:
            return 3
    def get_st_gp_status(self,st,attend_id):
        curs = self.db.cursor()
        curs.execute("select * from course_time where id='%d'" % (attend_id))
        x = curs.fetchone()
        if x:
            curs = self.db.cursor()
            curs.execute("select status from attend_course where st_name='%s' and date='%s' and start='%s' and end='%s'" % (st,x[2],x[4],x[5]))
            x = curs.fetchone()
            if x:
                return x[0]
        return None
    def get_st_exam_status(self,st,attend_id):
        curs = self.db.cursor()
        curs.execute("select * from exam_time where id='%d'" % (attend_id))
        x = curs.fetchone()
        if x:
            curs = self.db.cursor()
            curs.execute("select status from attend_exam where st_name='%s' and date='%s' and start='%s' and end='%s'" % (st,x[2],x[4],x[5]))
            x = curs.fetchone()
            if x:
                return x[0]
        return None
    def get_date_course(self , id , cs):

        curs = self.db.cursor()
        curs.execute("select date from course_time where id = '%d' and c_name = '%s'" %(id , cs))
        return curs.fetchone()
    def get_baid_mony(self,course , phone , mony_id , time_month):

        curs = self.db.cursor()
        curs.execute("select baid , gp_type , mony_id from course_mony where st_bc ='%s' and gp_name ='%s' "%(phone,course))
        out = curs.fetchall()
        if out:
            for i in out:
                if unicode(i[1]) == u'بالحصة':
                    if str(mony_id) in str(i[2]):
                        return True ,i[0]
                elif unicode(i[1]) == u'بالشهر' :
                    if str(time_month) in str(i[2]):
                        return True, i[0]
                else:
                    return True,i[0]
            return  False , 0
        return False , 0


    def get_course_mony(self, name):

        curs = self.db.cursor()
        curs.execute("select price , bill_method from course where name = '%s'" % (name))
        return curs.fetchall()
    def get_students(self, model):

        curs = self.db.cursor()
        curs.execute("SELECT name FROM students")
        cc = [item[0] for item in curs.fetchall()]
        curs.execute("SELECT sphone FROM students")
        cc += [item[0] for item in curs.fetchall()]
        curs.execute("SELECT bc FROM students")
        cc += [item[0] for item in curs.fetchall()]
        model.setStringList(cc)

    def get_courses(self, model):

        curs = self.db.cursor()
        curs.execute("SELECT name FROM course")
        cc = [item[0] for item in curs.fetchall()]
        model.setStringList(cc)
    def get_course_rest_time(self,course):

        curs = self.db.cursor()
        curs.execute("select st_time,end_time from course_time where c_name='%s'" %(course))
        x = curs.fetchall()
        time = 0
        for i in x:
            time += (i[1] - i[0]).total_seconds()
        return time
    #add, update, delete and search student
    def get_bc(self,st):

        curs = self.db.cursor()
        curs.execute("select bc from students where name='%s'" %(st))
        x = curs.fetchone()
        if x:
            return x[0]
        curs.execute("select bc from students where sphone='%s'" % (st))
        x = curs.fetchone()
        if x:
            return x[0]
        curs.execute("select bc from students where bc='%s'" % (st))
        x = curs.fetchone()
        if x:
            return x[0]
        return x
    def add_student(self,bc,name,school,sphone,fphone,mail,add,details):
        try:

            curs = self.db.cursor()
            curs.execute("insert into students values('%s','%s','%s','%s','%s','%s','%s','%s')" %(bc,name,school,sphone,fphone,mail,add,details))

            return True
        except:
            return False
    def edite_student(self,oldbc,bc,name,school,sphone,fphone,mail,add,details):
        try:

            curs = self.db.cursor()
            sql = "update students set bc='%s',name='%s',school='%s', sphone='%s',fphone='%s' , mail='%s',students.add='%s',details='%s' where bc='%s'" %(bc,name,school,sphone,fphone,mail,add,details,oldbc)
            curs.execute(sql)

            return True
        except Exception as ex:
            return False
    def delete_student(self,bc):
        try:

            curs = self.db.cursor()
            curs.execute("delete from students where bc='%s'" %(bc))

            curs.close()
            return True
        except:
            return False
    def get_course_by_name(self,name):

        curs = self.db.cursor()
        curs.execute("select * from course where name='%s'" %(name))
        return curs.fetchone()
    def get_student(self,bc):

        curs = self.db.cursor()
        curs.execute("select * from students where bc='%s'" %(bc))
        x = curs.fetchone()
        if x:
            return x
        else:
            curs.execute("select * from students where sphone='%s'" % (bc))
            x = curs.fetchone()
            if x:
                return x
            else:
                curs.execute("select * from students where name='%s'" % (bc))
                return curs.fetchone()
    def get_st_cs(self,course):

        curs = self.db.cursor()
        curs.execute("select students.name,students.sphone,students.bc,student_course.price from student_course inner join students on student_course.bc = students.bc where gp_name='%s'" %(course))
        return curs.fetchall()
    def del_st_cs(self,ph,cs):
        try:

            curs = self.db.cursor()
            curs.execute("delete from student_course where bc='%s' and gp_name='%s'" %(ph,cs))

            return True
        except:
            return False
    def get_course_dates(self,name):
        gpid = self.get_course_by_name(name)[0]
        curs = self.db.cursor()
        curs.execute("select distinct date,start,end from attend_course where gp_id='%s' order by date" %(gpid))
        return curs.fetchall()

    def get_course_dates_before(self,course):
        curs = self.db.cursor()
        curs.execute(
            "select distinct course_time.id from course_time left join attend_course on course_time.date = attend_course.date and course_time.st_time = attend_course.start and course_time.end_time = attend_course.end  where course_time.c_name='%s' and course_time.date < NOW() order by course_time.date,course_time.day" % (course))
        return curs.fetchall()
    def get_attend(self , st_name):

        curs = self.db.cursor()
        curs.execute("select date from attend_course where date < NOW() and st_name = '%s' and status='%s'" %(st_name,u'حضور') )
        return curs.fetchall()
    def del_att_st(self,st,att_id):
        try:

            curs = self.db.cursor()
            curs.execute(
                "delete from attend_course where st_name='%s' and attend_id='%d'" % (st, int(att_id)))
            return True
        except:
            return False
    def check_attend(self,st,date,start,end):
        curs = self.db.cursor()
        curs.execute(
            "select status from attend_course where st_name='%s' and date='%s' and start='%s' and end='%s'" % (st,date,start,end))
        x = curs.fetchone()
        if x:
            if x[0] == u'حضور':
                return True
        return False
    def put_st_mony(self,st_bc,gp_name,gp_type,mony_id,amount):

        curs = self.db.cursor()
        curs.execute("select baid from course_mony where st_bc='%s' and gp_name='%s' and mony_id='%s'" % (
        st_bc, gp_name, mony_id))
        baid = curs.fetchone()
        if baid:
            try:
                curs.execute(
                    "update course_mony set baid='%d' where st_bc='%s' and gp_name='%s' and mony_id='%s'" % (
                    baid[0] + amount, st_bc, gp_name, mony_id))

                return True
            except:
                return False
        else:
            try:
                curs.execute("insert into course_mony values('%s','%s','%s','%s','%f','%s','%s')" % (
                st_bc, gp_name, gp_type, mony_id, amount, datetime.datetime.now(), Model.ID))

                return True
            except:
                return False
    def get_st_mony(self,st_bc,gp_name,mony_id):

        curs = self.db.cursor()
        curs.execute("select baid from course_mony where st_bc='%s' and gp_name='%s' and mony_id='%s'" %(st_bc,gp_name,mony_id))
        x = curs.fetchone()
        if x:
            return x[0]
        else:
            return 0
    def get_st_degree(self,st_bc,date,start,end):

        curs = self.db.cursor()
        curs.execute("select degree from attend_exam where st_name='%s' and date='%s' and start='%s' and end='%s'" % (st_bc,date,start,end))
        x = curs.fetchone()
        if x:
            return x[0]
        else:
            return 0
    def put_st_degree(self,st, attend_id,degree):
        try:
            curs = self.db.cursor()
            curs.execute(
                "select degree from attend_exam where st_name='%s' and attend_id='%d'" % (st, int(attend_id)))
            baid = curs.fetchone()
            if baid:
                curs.execute("update attend_exam set degree='%f' where st_name='%s' and attend_id='%d'" %(degree,st,int(attend_id)))

                return True
            else:
                curs.execute("insert into attend_exam values('%s','%d','%s','%f')" % (st, int(attend_id), datetime.datetime.now(), degree))

                return True
        except:
            return False
    def get_course_months(self,name):

        "show the date as  month and year only   such as (4-2018)  but 4 refer to month  not day  "

        curs = self.db.cursor()
        curs.execute(
            "select distinct course_time.date from course_time where course_time.c_name='%s' order by course_time.date" % (
            name))
        x= curs.fetchall()
        v= []
        for i in x:
            x = str(i[0].month) + " - " + str(i[0].year)
            if x not in v:
                v.append(str(i[0].month) + " - " + str(i[0].year))
        return v
    def get_course_days(self,name):

        curs = self.db.cursor()
        curs.execute(
            "select distinct course_time.id,course_time.date,course_time.day from course_time where course_time.c_name='%s' order by course_time.date,course_time.day" % (
            name))
        return curs.fetchall()
    def get_course_num_days(self,name):

        curs = self.db.cursor()
        curs.execute("select days from course where name ='%s'"%(name))
        x = curs.fetchone()
        if x:
            return x[0]
        else:
            return 0
    def random_with_N_digits(self,n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)
    def generate_barcode(self):
        try:
            right_bc = str(datetime.date.today().day) + str(datetime.date.today().month) + str(datetime.date.today().year)
            rest_bc = str(self.random_with_N_digits(12-len(right_bc)))
            bc_test = right_bc+rest_bc
            obj = barcode.get('ean13',bc_test)
            bc = obj.get_fullcode()
            if self.get_student(bc):
                self.generate_barcode()
            else:
                return bc
        except:
            return '0000000000000'
    def get_exam_num_days(self,name):

        curs = self.db.cursor()
        curs.execute("select days from exam where name ='%s'"%(name))
        x = curs.fetchone()
        if x:
            return x[0]
        else:
            return 0
    def get_method_price(self,cname):

        curs = self.db.cursor()
        curs.execute("select bill_method,price from course where name='%s'" %(cname))
        return curs.fetchone()
    #for exams
    def add_exam(self, name, days, hours, max_degree, details , type ):
        try:

            curs = self.db.cursor()
            curs.execute("insert into exam values('%s','%d','%f','%f','%s', '%s' )" % (
            name, days, hours, max_degree, details , type ))

            return True
        except:
            return False

    def edite_exam(self, oldname,name, days, hours, max_degree, details , type ):
        try:

            curs = self.db.cursor()
            curs.execute(
                "update exam set name='%s' ,days='%d', hours='%f',max_degree='%f',details='%s' , type = '%s' where name='%s'" % (
                name, days, hours, max_degree, details,type  ,oldname))

            return True
        except:
            return False

    def delete_exam(self, name):
        try:

            curs = self.db.cursor()
            curs.execute("delete from exam where name='%s'" % (name))

            return True
        except:
            return False

    def get_exam_by_name(self, name):

        curs = self.db.cursor()
        curs.execute("select * from exam where name='%s'" % (name))
        return curs.fetchone()
    def get_exam_type(self,exam):

        curs = self.db.cursor()
        curs.execute("select exam.type from exam where name='%s'" % (exam))
        x = curs.fetchone()
        if x:
            return x[0]
        else:
            return None
    def get_exams_st(self, bc):
        curs = self.db.cursor()
        curs.execute("select * from gp_exam where exam_name='%s'" % (bc))
        return  curs.fetchall()

    def gp_exam_not_exist(self, gp, ex):

        curs = self.db.cursor()
        curs.execute("select * from gp_exam where gp_name='%s' and exam_name='%s'" % (gp, ex))
        if curs.fetchall():
            return False
        else:
            return True

    def add_gp_ex(self, gp, ex):
        try:

            curs = self.db.cursor()
            curs.execute("insert into gp_exam values('%s','%s')" % (gp, ex))

            return True
        except:
            return False

    def del_gp_ex(self, gp, ex):
        try:

            curs = self.db.cursor()
            curs.execute("delete from gp_exam where gp_name='%s' and exam_name='%s'" % (gp, ex))

            return True
        except:
            return False

    def add_exam_time_structure(self, exam, day, st, end):
        try:

            curs = self.db.cursor()
            curs.execute("insert into exam_time_structure values('%s','%s','%s','%s')" % (exam, day, st, end))

            return True
        except:
            return False

    def add_exam_time(self ,exam, date, day, st, end , gp):
        try:

            curs = self.db.cursor()
            curs.execute(
                "insert into exam_time ( c_name, date, day, st_time, end_time , gp) values('%s','%s','%s','%s','%s' , '%s')" % (
                     exam, date, day, st, end , gp))

            return True
        except:
            return False

    def get_exam_structure(self, exam):

        curs = self.db.cursor()
        curs.execute("select * from exam_time_structure where c_name='%s'" % (exam))
        return curs.fetchall()

    def get_exam(self, exam):

        curs = self.db.cursor()
        curs.execute("select * from exam_time where c_name='%s' order by date,st_time" % (exam))
        return curs.fetchall()

    def del_exam_time_st(self, exam, day, t1, t2):
        try:

            curs = self.db.cursor()
            curs.execute(
                "delete from exam_time_structure where c_name='%s' and day='%s' and st_time='%s' and end_time='%s'" % (
                    exam, day, t1, t2))

            return True
        except:
            return False

    def del_exam_time(self, exam, date, t1, t2):
        try:

            curs = self.db.cursor()
            curs.execute(
                "delete from exam_time where c_name='%s' and date='%s' and st_time='%s' and end_time='%s'" % (
                    exam, date, t1, t2))

            return True
        except:
            return False

    def del_exam_time_all(self, exam):
        try:

            curs = self.db.cursor()
            curs.execute("delete from exam_time where c_name='%s'" % (exam))

            return True
        except:
            return False
    def get_st_exam_times(self, exam):

        curs = self.db.cursor()
        sql = "select st_time,end_time,id from exam_time where c_name ='%s' and exam_time.date = '%s' order by exam_time.st_time" % (
        exam, datetime.date.today())
        curs.execute(sql)
        return curs.fetchone()

    def get_exams(self, model):

        curs = self.db.cursor()
        curs.execute("SELECT name FROM exam")
        cc = [item[0] for item in curs.fetchall()]
        model.setStringList(cc)
    def get_exam_rest_time(self, exam):

        curs = self.db.cursor()
        curs.execute("select st_time,end_time from exam_time where c_name='%s'" % (exam))
        x = curs.fetchall()
        time = 0
        for i in x:
            time += (i[1] - i[0]).total_seconds()
        return time
    def get_exam_gps(self,exam):
        curs = self.db.cursor()
        curs.execute("select gp_name from gp_exam where exam_name='%s'" %(exam))
        return curs.fetchall()
    def get_all_gp(self ):

        curs = self.db.cursor()
        curs.execute('select name from course')
        return curs.fetchall()
    def check_attend_ex(self,st,date,start,end):
        curs = self.db.cursor()
        curs.execute("select status,degree from attend_exam where st_name='%s' and date='%s' and start='%s' and end='%s'" % (st,date,start,end))
        x = curs.fetchone()
        if x:
            if x[0] == u'حضور':
                return True,x[1]
        return False,0
    def student_exist(self,bc,nm):

        curs = self.db.cursor()
        curs.execute("select * from students where bc='%s'" % (bc))
        if curs.fetchone():
            return 2
        else:
                curs.execute("select * from students where name='%s'" % (nm))
                if curs.fetchone():
                    return 3
                else:
                    return 1
    def get_exam_dates(self, name ):

        curs = self.db.cursor()
        curs.execute(
                "select distinct exam_time.id,exam_time.date,exam_time.day from exam_time left join attend_exam on exam_time.id = attend_exam.attend_id where exam_time.c_name='%s' order by exam_time.date,exam_time.day" % (
               name))
        return curs.fetchall()
    def get_exam_max(self,exam):
        curs = self.db.cursor()
        curs.execute("select max_degree from exam where name='%s'" %(exam))
        return curs.fetchone()[0]
    def get_exam_dates_2(self, name):

        curs = self.db.cursor()
        curs.execute("select distinct date , start,end from attend_exam where exam_name = '%s'"%(name))
        return curs.fetchall()
    def get_all_students(self):

        curs = self.db.cursor()
        curs.execute("select * from students")
        tbs = []
        for i in curs.fetchall():
            x = list(i)
            x.extend([u'تعديل - حذف',u'طباعة'])
            tbs.append(x)
        return tbs

    def get_all_courses(self):
        curs = self.db.cursor()
        curs.execute("select * from course")
        tbs = []
        for i in curs.fetchall():
            x = list(i)
            x.append(u"حذف - تعديل")
            tbs.append(x)
        return tbs
    def get_all_exams(self):

        curs = self.db.cursor()
        curs.execute("select * from exam")
        tbs = []
        for i in curs.fetchall():
            x = list(i)
            x.append(u"حذف - تعديل")
            tbs.append(x)
        return tbs
    def get_all_mony(self,st,end):
        curs = self.db.cursor()
        curs.execute("select st_cs.bc,st.name,st_cs.gp_name,cs_m.gp_type,cs_m.mony_id,st_cs.price,cs_m.baid,cs_m.date from student_course st_cs inner join students st on st_cs.bc = st.bc left join course_mony cs_m on st_cs.bc = cs_m.st_bc and st_cs.gp_name = cs_m.gp_name  WHERE cs_m.date BETWEEN '%s' and '%s'" %(st,end))
        print "this is result",curs.fetchall()

        return curs.fetchall()
    #for report page
    def get_course_dates_bydates(self,bc,name,d1,d2):
        try:
            gpid = self.get_course_by_name(name)[0]
        except:
            gpid = 0
        curs = self.db.cursor()
        curs.execute("select * from attend_course where gp_id='%s' and st_name = '%s' and date between '%s' and '%s'" %(gpid,bc,d1,d2))
        return curs.fetchall()
    def get_exam_dates_rep(self, name,d1,d2):
        curs = self.db.cursor()
        curs.execute("select exam_name from gp_exam where gp_name ='%s'" %(name))
        x = curs.fetchall()
        lst = []
        for i in x:
            curs.execute("select * from attend_exam where exam_name='%s' and date between '%s' and '%s'" % (i[0], d1, d2))
            lst.extend([list(i) for i in curs.fetchall()])
        return lst
    def get_st_rep_att(self,st,end,gp,bc):
        v = self.get_course_dates_bydates(bc,gp,st,end)
        att = 0
        aps = 0
        for i in v:
            if i[5] == u'حضور':
                att += 1
            else:
                aps += 1
        return str(att) + "/" + str(att+aps)
    def get_st_rep_mony(self,d1,d2,gp_name,st_bc):

        curs = self.db.cursor()
        curs.execute("select baid from course_mony where st_bc='%s' and gp_name='%s' and date BETWEEN '%s' and '%s'" %(st_bc,gp_name,d1,d2))
        x = curs.fetchall()
        b = 0
        for i in x:
            b += i[0]
        return str(b)
    def get_st_rep_ex_deg(self,st,end,gp,bc):
        v = self.get_exam_dates_rep(gp,st,end)
        max_v = 0
        value = 0
        for i in v:
                max_v += i[8]
                value += i[7]
        return str(value) + "/" + str(max_v)
    def get_st_rep_ex(self,st,end,gp,bc):
        v = self.get_exam_dates_rep(gp,st,end)
        att = 0
        aps = 0
        for i in v:
            if i[5] == u'حضور':
                att += 1
            else:
                aps += 1
        return str(att) + "/" + str(att + aps)
    def get_allow(self,course):

        curs = self.db.cursor()
        curs.execute("select allow from course where name = '%s'" %(course))
        return curs.fetchone()
    def get_allow_before(self,course):

        curs = self.db.cursor()
        curs.execute("select allow_defore from course where name = '%s'" %(course))
        return curs.fetchone()
    def get_time_gp(self , gp):

        curs = self.db.cursor()
        curs.execute("select * from course_time where c_name = '%s'" %(gp))
        out = curs.fetchall()
        return out
    def get_time_by_id(self , dt_id):
        curs = self.db.cursor()
        curs.execute("select * from course_time where id = '%s'" %(dt_id))
        out = curs.fetchone()
        return out
    def get_exam_time_by_id(self , dt_id):

        curs = self.db.cursor()
        curs.execute("select * from exam_time where id = '%s'" %(dt_id))
        out = curs.fetchone()
        return out
    def edt_time_course(self,dt_id,date,t1,t2):

        curs = self.db.cursor()
        curs.execute("update course_time set date='%s' , st_time='%s' , end_time='%s' where id='%s'" %(date,t1,t2,dt_id))

    def get_exam_type(self,name):
        curs = self.db.cursor()
        curs.execute("select type from exam where name='%s'" %(name))
        x = curs.fetchone()
        if x:
            return x[0]
        return None
    def edt_time_exam(self,dt_id,date,t1,t2):

        curs = self.db.cursor()
        curs.execute("update exam_time set date='%s' , st_time='%s' , end_time='%s' where id='%s'" %(date,t1,t2,dt_id))



    def get_times(self , gp):

        curs = self.db.cursor()
        curs.execute("select absence from course where name = '%s'" %(gp))
        return  curs.fetchone()
    def get_all_stu(self , gp):
        curs = self.db.cursor()
        curs.execute("select bc from student_course where gp_name ='%s'" %(gp))
        return curs.fetchall()
    def get_name(self , bc):

        curs = self.db.cursor()
        curs.execute("select name from students where bc = '%s'" %(bc))
        return curs.fetchone()
    def get_allow_times(self , ph , gp):

        curs = self.db.cursor()
        curs.execute("select flage from allow_times where ph = '%s' and gp = '%s'" %(ph , gp))
        return curs.fetchone()
    def put_allow_times(self , ph , gp , flage):

        curs = self.db.cursor()
        curs.execute("select flage from allow_times where ph = '%s' and gp = '%s'" % (ph, gp))
        out = curs.fetchone()
        if out :
            curs.execute("update allow_times set flage = '%d' where ph = '%s' and gp = '%s' " %(int(flage) , ph , gp))

        else:
            curs.execute("insert into allow_times values ( '%s' , '%s' , '%d' ) " %(ph , gp , int(flage)))
    def get_last_course_date(self,student,course_id,course_name):
        curs = self.db.cursor()
        curs.execute("select date,start,end from attend_course where st_name ='%s' and gp_id='%s' order by date desc limit 1" %(student,course_id))
        d = curs.fetchone()

        if d:
            return d
        else:
            curs.execute("select date,st_time,end_time from course_time where c_name ='%s' order by date limit 1" % (course_name))
            d = curs.fetchone()
            if d:
                return d
        return None
    def get_last_exam_date(self,student,course,gp=None):
        curs = self.db.cursor()
        curs.execute("select date,start,end from attend_exam where st_name ='%s' and exam_name='%s'" %(student,course))
        d = curs.fetchone()
        if d:
            return d
        else:
            if gp:
                curs.execute("select date,st_time,end_time from course_time where c_name ='%s'" % (gp))
                d = curs.fetchone()
                if d:
                    return d
            else:
                curs.execute("select date,st_time,end_time from exam_time where c_name ='%s'" % (course))
                d = curs.fetchone()
                if d:
                    return d
        return None
    def get_course_dates_next(self,course,last_date):
        curs = self.db.cursor()
        if last_date:
            curs.execute(
                "select id from course_time where c_name ='%s' and date = '%s' and st_time='%s' and end_time='%s'" % (
                course, last_date[0], last_date[1], last_date[2]))
            d = curs.fetchone()
            if d:
                curs.execute("select date,st_time,end_time from course_time where id >= '%s' and date <= '%s'" % (d[0],datetime.datetime.now()))
                return curs.fetchall()
        curs.execute("select date,st_time,end_time from course_time where date <= '%s'" % (datetime.datetime.now()))
        return curs.fetchall()
    def get_exam_dates_next(self,course,last_date):
        curs = self.db.cursor()
        if last_date:
            curs.execute(
                "select id from exam_time where c_name ='%s' and date = '%s' and st_time='%s' and end_time='%s'" % (
                course, last_date[0], last_date[1], last_date[2]))
            d = curs.fetchone()
            if d:
                curs.execute("select date,st_time,end_time from exam_time where id >= '%s' and date <= '%s'" % (d[0],datetime.datetime.now()))
                return curs.fetchall()
        curs.execute("select date,st_time,end_time from exam_time where date <= '%s'" % (datetime.datetime.now()))
        return curs.fetchall()

    def insert_st_course_attend(self,st,gp,date,start,end,status):
        curs = self.db.cursor()
        curs.execute("select * from attend_course where st_name = '%s' and gp_id='%s' and date='%s' and start='%s' and end='%s'" %(st,gp,date,start,end))
        if not curs.fetchone():
            curs.execute("insert into attend_course values('%s','%s','%s','%s','%s','%s','%s')" %(st,gp,date,start,end,status,datetime.datetime.now()))
    def insert_st_exam_attend(self,st,gp,date,start,end,status):
        curs = self.db.cursor()
        curs.execute("select * from attend_exam where st_name = '%s' and exam_name='%s' and date='%s' and start='%s' and end='%s'" %(st,gp,date,start,end))
        x = curs.fetchone()
        if not x:
            max_deg = self.get_exam_max(gp)
            curs.execute("insert into attend_exam values('%s','%s','%s','%s','%s','%s','%s','0','%f')" %(st,gp,date,start,end,status,datetime.datetime.now(),max_deg))

    def attend_st_gp(self,st,gp,date,start,end,status):
        curs = self.db.cursor()
        curs.execute(
            "update attend_course set status='%s' , datetime='%s' where st_name = '%s' and gp_id='%s' and date='%s' and start='%s' and end='%s'" % (
            status, datetime.datetime.now(), st, gp, date, start, end))
        return True
    def attend_st_exam(self,st,gp,date,start,end,status,degree=0):
        curs = self.db.cursor()
        max_deg = self.get_exam_max(gp)
        sql =  "update attend_exam set status='%s' , datetime='%s',degree='%s',max_degree='%f' where st_name = '%s' and exam_name='%s' and date='%s' and start='%s' and end='%s'" % (
            status, datetime.datetime.now(),degree,max_deg, st, gp, date, start, end)
        curs.execute(sql)
        return True
    def insert_absent_days(self):
        for cs in self.get_all_courses():
            gp = cs[0]
            gp_name = cs[1]
            students = self.get_all_stu(cs[1])
            for st in students:
                last = self.get_last_course_date(st[0], gp,gp_name)
                for i in self.get_course_dates_next(gp, last):
                    self.insert_st_course_attend(st[0], gp, i[0], i[1], i[2], u'غياب')

    def insert_exam_absent_days(self):
        for cs in self.get_all_exams():
            for exgp in self.get_exams_st(cs[0]):
                gp = self.get_course_by_name(exgp[0])[0]
                students = self.get_all_stu(exgp[0])
                for st in students:
                    if self.get_exam_type(exgp[1]) == u'دورى':
                        last = self.get_last_exam_date(st[0], gp,exgp[0])
                        for i in self.get_course_dates_next(gp, last):
                            self.insert_st_exam_attend(st[0], exgp[1], i[0], i[1], i[2], u'غياب')
                    else:
                        last = self.get_last_exam_date(st[0], exgp[1])
                        for i in self.get_exam_dates_next(exgp[1], last):
                            self.insert_st_exam_attend(st[0], exgp[1], i[0], i[1], i[2], u'غياب')

    def student_group_swift(self,st_bc,old_gp,new_gp):
        ngp_id = self.get_course_by_name(new_gp)[0]
        ogp_id = self.get_course_by_name(old_gp)[0]
        curs = self.db.cursor()
        curs.execute("select * from student_course where bc='%s' and gp_name='%s'" %(st_bc,new_gp))
        if not curs.fetchall():
            curs.execute("update student_course set gp_name='%s' where bc='%s' and gp_name='%s'" %(new_gp,st_bc,old_gp))
            curs.execute(
                "update course_mony set gp_name='%s' where st_bc='%s' and gp_name='%s'" % (new_gp, st_bc, old_gp))
            curs.execute(
                "update attend_course set gp_id='%s' where st_name='%s' and gp_id='%s'" % (ngp_id, st_bc, ogp_id))
            return True
        else:
            return False

    def get_group_list(self):
        curs = self.db.cursor()
        curs.execute("select name from course")
        tbl = []
        gps = curs.fetchall()
        for i in gps:
            curs.execute("select * from student_course where gp_name ='%s'" %(i[0]))
            tbl.append([i[0],len(curs.fetchall())])
        return tbl

    def get_exam_list(self):
        curs = self.db.cursor()
        curs.execute("select name from exam")
        tbl = []
        xm = curs.fetchall()
        for i in xm:
            curs.execute("select gp_name from gp_exam where exam_name='%s'" %(i[0]))
            v = curs.fetchall()
            for j in v:
                curs.execute("select * from student_course where gp_name ='%s'" %(j[0]))
                tbl.append([i[0],len(curs.fetchall())])
        return tbl
    def get_gp_att_abs(self,gp,d1,d2):
        st = {}
        gpid= self.get_course_by_name(gp)[0]
        curs = self.db.cursor()
        curs.execute("select * from attend_course where gp_id='%s'and date between '%s' and '%s'" %(gpid,d1,d2))
        x = curs.fetchall()
        for i in x:
            st.setdefault(i[0], []).append(i[5])
        for k,v in st.iteritems():
            a = v.count(u'حضور')
            l = v.count(u'غياب')
            try:
                st[k] = [a,l,(a / float(a+l))*100]
            except Exception as ex:
                st[k] = [a,l,0]
        return st
    def get_ex_att_abs(self,gps,d1,d2):
        st = {}
        dg = {}
        curs = self.db.cursor()
        for gp in gps:
            curs.execute("select * from attend_exam where exam_name='%s' and date between '%s' and '%s'" %(gp,d1,d2))
            x = curs.fetchall()
            for i in x:
                st.setdefault(i[0], []).append(i[5])
                try:
                    dg.setdefault(i[0], []).append(((i[7]/i[8])*100))
                except:
                    dg.setdefault(i[0], []).append(0)

        for k,v in st.iteritems():
            a = v.count(u'حضور')
            l = v.count(u'غياب')

            mx = 0
            for i in dg[k]:
                mx += i
            try:
                mx = mx / len(dg[k])
            except:
                mx = 0
            try:
                st[k] = [a,l,(a / float(a+l))*100,mx]
            except Exception as ex:
                st[k] = [a,l,0,0]
        return st

    def th_course(self):
        t=threading.Thread(target=self.insert_absent_days)
        t.setDaemon(True)
        t.start()
    def th_exam(self):
        t2=threading.Thread(target=self.insert_exam_absent_days)
        t2.setDaemon(True)
        t2.start()

    def get_exams_of_course(self,gb):
        curs = self.db.cursor()
        curs.execute("select exam_name from gp_exam where gp_name='%s'"%(gb))
        xm = curs.fetchall()
        x=[i[0] for i in xm]
        return x


    def edite_price(self,price, gp_name,bc ):
        try:

            curs = self.db.cursor()
            curs.execute("update student_course set price='%s' where gp_name='%s' and bc='%s' " % (
                price,gp_name,bc))

            return True
        except:
            return False

    def get_course_price_by_name(self,gp_name,br):
        curs = self.db.cursor()
        curs.execute("select price from student_course where gp_name='%s' and bc='%s' " % (gp_name,br))
        x = curs.fetchone()
        if x:
            return x[0]
        else:
            return 0

    def get_students_name(self):
        curs=self.db.cursor()
        curs.execute("select name from students")
        studetns=[]
        for i in curs.fetchall():
            studetns.append(i[0])
        return studetns


    def get_student_report_info(self,st_name):
        curs=self.db.cursor()
        curs.execute("select st.bc,st.name,st_cs.gp_name,st_cs.price,cs.bill_method from student_course st_cs inner join students st on st.bc = st_cs.bc inner join course cs on cs.name = st_cs.gp_name where st.name = '%s' "%(st_name))
        return curs.fetchall()

    def get_specific_course_days(self,name,d1,d2):
        curs = self.db.cursor()
        curs.execute(
            "select distinct course_time.id,course_time.date,course_time.day from course_time where course_time.c_name='%s' and course_time.date BETWEEN '%s' and '%s'" % (
            name,d1,d2))
        return len(curs.fetchall())

    def get_specific_course_months(self,name,d1,d2):

        "show the date as  month and year only   such as (4-2018)  but 4 refer to month  not day  "

        curs = self.db.cursor()
        curs.execute("select distinct course_time.date from course_time where course_time.c_name='%s' and course_time.date BETWEEN '%s' and '%s' " % (name,d1,d2))
        x= curs.fetchall()
        v= []
        for i in x:
            x = str(i[0].month) + " - " + str(i[0].year)
            if x not in v:
                v.append(str(i[0].month) + " - " + str(i[0].year))
        return v

    def get_paid_date(self,st_bc,gp_name):
        curs=self.db.cursor()
        curs.execute("select baid,date from course_mony where st_bc='%s' and gp_name='%s' "%(st_bc,gp_name))
        for i in curs.fetchall():
            print "thi",list(i)
            return list(i)
