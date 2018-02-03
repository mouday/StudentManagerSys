
# 增加虚拟的老师，学生，课程，课程记录的初始数据

import datetime
import random
import sys
import os
import string

BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)

from sqlalchemy.orm import sessionmaker
from data import init_database


Session = sessionmaker(init_database.engine)
session = Session()

def get_qq():
    # 随机获取6位qq号
    nums = string.digits  # 0123456789
    qq = "".join(random.sample(nums, 6))  # 获取6位QQ号
    return qq

def get_time():
    # return time.strftime("%Y-%m-%d", time.localtime()) # 不支持
    return datetime.datetime.now()  # 支持

def get_date_from_str(string):
    # 通过字符串获取日期对象
    return datetime.date(string)

def init_data():
    # 初始化数据库
    student1 = init_database.Student(name="Tom", qq=get_qq())
    student2 = init_database.Student(name="Jack", qq=get_qq())
    student3 = init_database.Student(name="Jimi", qq=get_qq())
    student4 = init_database.Student(name="Ben", qq=get_qq())
    student5 = init_database.Student(name="Jone", qq=get_qq())

    teacher1 = init_database.Teacher(name="李老师")
    teacher2 = init_database.Teacher(name="王老师")
    teacher3 = init_database.Teacher(name="白老师")

    grade1 = init_database.Grade(name="语文")
    grade2 = init_database.Grade(name="数学")
    grade3 = init_database.Grade(name="英语")

    grade_record1 = init_database.GradeRecord(
        grade= grade1, student =student1, date=get_time())
    grade_record2 = init_database.GradeRecord(
        grade= grade1, student =student2, date=get_time())
    grade_record3 = init_database.GradeRecord(
        grade= grade3, student =student3, date=get_time())

    session.add_all([student1, student2, student3, student4, student5])
    session.add_all([teacher1, teacher2, teacher3])
    session.add_all([grade1, grade2, grade3])
    session.add_all([grade_record1, grade_record2, grade_record3])

    session.commit()
    print("数据初始化成功！")

if __name__ == "__main__":

    init_data()
    session.close()

