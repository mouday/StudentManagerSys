
# 教师视图，实现教师具体功能
"""
讲师视图
　　管理班级，可创建班级，根据学员qq号把学员加入班级
　　可创建指定班级的上课纪录，注意一节上课纪录对应多条学员的上课纪录，
    即每节课都有整班学员上，
    为了纪录每位学员的学习成绩，需在创建每节上课纪录同时
    为这个班的每位学员创建一条上课纪录
　　为学员批改成绩， 一条一条的手动修改成绩
"""
import sys
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)

from data import init_data
from data import init_database
from data.init_data import session
from core import common

class Teacher(object):
    def __init__(self, name):
        self.name = name

    def add_grade(self, grade_name):
        # 增加课程 成功True， 失败False
        try:
            grade = init_database.Grade(name=grade_name)
            session.add(grade)
            session.commit()
            return True
        except:
            return False

    def add_student_to_grade(self, student_qq, grade_name):
        # 把学生增加到课程
        try:
            student =common.get_student_by_qq(student_qq)
            grade = common.get_grade(grade_name)
            grade.students.append(student)
            session.commit()
        except:
            return False
        return True

    def add_grade_record(self, grade_name):
        # 增加课程记录
        try:
            grade=common.get_grade(grade_name)
            students = grade.students
            records = []
            for student in students:
                grade_record =common.get_grade_record(
                    grade_name,student.qq,init_data.get_time())

                if grade_record == None:  # 记录为空再添加
                    grade_record = init_database.GradeRecord(
                        grade=grade, student=student, date =init_data.get_time())
                    records.append(grade_record)
            session.add_all(records)
            session.commit()
        except:
            return False
        return True

    def modify_score(self, grade_name, student_qq, date, score):
        # 修改成绩
        grade_record = common.get_grade_record(grade_name, student_qq, date)
        if grade_record != None:
            grade_record.score = score
            session.commit()
            return True
        else:
            return False



if __name__  == "__main__":
    t = Teacher("王老师")
    # ret = t.get_grade("地理")
    ret = t.modify_score("数学", "012465", "2018-02-04", 12)
    print(ret)

