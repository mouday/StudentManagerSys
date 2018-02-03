"""
主题：学员管理系统

需求：

用户角色，讲师＼学员， 用户登陆后根据角色不同，能做的事情不同，分别如下

讲师视图
　　管理班级，可创建班级，根据学员qq号把学员加入班级
　　可创建指定班级的上课纪录，注意一节上课纪录对应多条学员的上课纪录， 即每节课都有整班学员上，
    为了纪录每位学员的学习成绩，需在创建每节上课纪录同时
    为这个班的每位学员创建一条上课纪录
　　为学员批改成绩， 一条一条的手动修改成绩

学员视图
    提交作业
    查看作业成绩
    一个学员可以同时属于多个班级，就像报了Linux的同时也可以报名Python一样，
     所以提交作业时需先选择班级，再选择具体上课的节数
    附加：学员可以查看自己的班级成绩排名
"""
import sys
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)

from core.student import Student
from core.teacher import Teacher

def student_view():
    """学生视图"""
    qq = input("请输入学生qq号：")
    student = Student(qq)
    while True:
        choice = input("1.交作业，2.查成绩，3.看排名")
        if choice == "1":
            grade_name = input("课程名称:")
            grade_date = input("上课日期（2018-02-03）：")
            ret = student.submit_task(grade_name, grade_date)
            print(ret)
        elif choice =="2" :
            grade_name = input("课程名称:")
            ret=student.get_score(grade_name)
            print(ret)
        elif choice == "3":
            grade_name = input("课程名称:")
            ret = student.get_rank(grade_name)
            print(ret)
        else:
            print("请输入正确的选项")

def teacher_view():
    """教师视图"""
    teacher_name = input("输入老师姓名:")
    teacher = Teacher(teacher_name)
    while True:
        choice = input("1.增加课程，2.增加上课记录，3.把学生增加到班级，4.修改学生成绩")
        if choice == "1":
            grade_name = input("课程名称:")
            ret = teacher.add_grade(grade_name)
            print(ret)
        elif choice == "2":
            grade_name = input("课程名称:")
            ret = teacher.add_grade_record(grade_name)
            print(ret)
        elif choice == "3":
            qq = input("请输入学生qq号：")
            grade_name = input("课程名称:")
            ret = teacher.add_student_to_grade(qq, grade_name)
            print(ret)
        elif choice=="4":
            qq = input("请输入学生qq号：")
            grade_name = input("课程名称:")
            date = input("上课时间：")
            score = input("成绩:")
            ret = teacher.modify_score(grade_name, qq, date, score)
            print(ret)
        else:
            print("请输入正确的选项")

def main():
    role = input("选择角色：1.教师，2.学生：")
    if role == "1":
        teacher_view()
    elif role == "2":
        student_view()
    else:
        print("输入错误，退出程序")

if __name__ == "__main__":
    main()

