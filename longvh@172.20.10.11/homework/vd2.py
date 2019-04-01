#them thu vien
import pymysql
	
#mo ket noi den mysql
db = pymysql.connect("localhost","root","huynam","wsn")

#su dung mot doi tuong cursor de truy cap
cursor = db.cursor()

#Xoa table neu table da ton tai
cursor.execute("DROP TABLE IF EXISTS sensors")

#tao 1 bang
sql = """create table sensors(
                id int(10) primary key auto_increment,
                temperature int(3) not null,
                humidity int(3) not null,
                time datetime not null ) """

#thuc thi
cursor.execute(sql)

#dong ket noi
db.close()

