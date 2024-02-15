import sqlite3

class Data:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()

        sql="""create table if not exists student(Id integer primary key,Name text,DOB text,Gender text,Age text,
                Department text,Year text,Email text, ContactNo text,Address text )"""

        self.cur.execute(sql)
        self.con.commit()

    def Create(self,name,dob,gender,age,department,year,email,contact,address):
        self.cur.execute("insert into student values(NULL,?,?,?,?,?,?,?,?,?)",
                         (name,dob,gender,age,department,year,email,contact,address))
        self.con.commit()

    def Retrive(self):
        self.cur.execute("select * from student")
        result = self.cur.fetchall()
        return result

    def Update(self,name,dob,gender,age,department,year,email,contact,address,id):
        self.cur.execute("update student set Name=?,DOB=?,Gender=?,Age=?,Department=?,Year=?,Email=?,ContactNo=?,Address=? where Id=?",
                         (name,dob,gender,age,department,year,email,contact,address,id))
        self.con.commit()

    def Delete(self,id):
        self.cur.execute("delete from student where Id=?",(id,))
        self.con.commit()

#o=Data("Student.db")

#o.insert("Abishek","08-01-2002","Male","21","CSE","2022 - 2026",
#         "abishek@gmail.com","7123456786","Nehru road,Bangalore")

#o.update("Abishek","08-01-2002","Male","21","AERO","2022 - 2026",
#         "abishek@gmail.com","7123456786","Nehru road,Bangalore","3")

#o.delete(4)

#o.Retrive()
