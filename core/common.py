
# 教师，学生，课程通用的方法

import sys
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)

from data import init_data
from data import init_database
from data.init_data import session


def get_student_by_qq(student_qq):
    """通过学生qq获取学生信息"""
    student = session.query(init_database.Student).filter(
        init_database.Student.qq == student_qq).first()
    return student


def get_grade(grade_name):
    """通过班级名称获取班级信息"""
    grade = session.query(init_database.Grade).filter(
        init_database.Grade.name == grade_name).first()
    return grade


def get_grade_record(grade_name, student_qq, date):
    """通过班级名称，学生qq，日期获取班级记录"""
    grade = get_grade(grade_name)
    student = get_student_by_qq(student_qq)
    if grade != None and student != None:
        grade_record = session.query(init_database.GradeRecord).filter(
            init_database.GradeRecord.grade == grade,
            init_database.GradeRecord.student == student,
            init_database.GradeRecord.date == date
        ).first()
        return grade_record
    else:
        return None

