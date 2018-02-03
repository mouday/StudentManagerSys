
# 存储老师，学生，班级的数据库

# 此处使用简单的数据库，sqlite3
import sys
import os

from  sqlalchemy import Integer, String, DATE, Column, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import  declarative_base

BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 注意数据库需要些绝对路径
engine = create_engine("sqlite:///%s/data/database.db"%(BaseDir))
# engine = create_engine("mysql+pymysql://root:123456@127.0.0.1/test?charset=utf8")

Base = declarative_base()


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))

    def __repr__(self):
        return "%s | %s"%(self.id, self.name)


class GradeRecord(Base):
    __tablename__ = "grade_records"
    id = Column(Integer, primary_key=True, autoincrement=True)
    grade_id = Column(Integer, ForeignKey("grades.id"))
    stu_id =  Column(Integer, ForeignKey("students.id"))
    date = Column(DATE)
    task_status = Column(Integer, default=0)
    score = Column(Integer, default=0)

    # 1对多的关系表
    grade = relationship("Grade", foreign_keys=[grade_id], backref="grade_records")
    student = relationship("Student", foreign_keys=[stu_id], backref="grade_records")

    def __repr__(self):
        return "%s | %s | %s | %s | %s | %s"%(
            self.id, self.grade.name, self.student.name,
            self.date, self.task_status, self.score)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    qq = Column(String(32))

    def __repr__(self):
        return "%s | %s | %s" % (self.id, self.name, self.qq)

# 创建关系表，第三张表连接grade和stuent
grade2student = Table("grade2student", Base.metadata,
                    Column("grade_id", Integer, ForeignKey("grades.id")),
                    Column("student_id", Integer, ForeignKey("students.id"))
                    )

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), unique=True)

    # 增加多对多的关系表
    students = relationship("Student", secondary=grade2student, backref="grades")

    def __repr__(self):
        return "%s | %s" % (self.id, self.name)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("数据库初始化成功")



