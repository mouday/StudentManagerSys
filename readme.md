# 主题：学员管理系统

需求：

用户角色，讲师＼学员， 用户登陆后根据角色不同，能做的事情不同，分别如下

# 讲师视图
```
　　管理班级，可创建班级，根据学员qq号把学员加入班级
　　可创建指定班级的上课纪录，注意一节上课纪录对应多条学员的上课纪录， 即每节课都有整班学员上，
    为了纪录每位学员的学习成绩，需在创建每节上课纪录同时
    为这个班的每位学员创建一条上课纪录
　　为学员批改成绩， 一条一条的手动修改成绩
```
# 学员视图
```
    提交作业
    查看作业成绩
    一个学员可以同时属于多个班级，就像报了Linux的同时也可以报名Python一样，
     所以提交作业时需先选择班级，再选择具体上课的节数
    附加：学员可以查看自己的班级成绩排名
```
# 分析：
```
    数据结构
    teacher（id, name） # 教师
    student(id, name, qq, grades) # 学生
    grade(id, name, students) # 班级
    grade_record(grade_id, student_id, date, task_status, score) # 一对多关系表
    grade2student(grade_id, student_id) # 多对多关系表
```
# 目录结构
```
- bin 
    -main.py        程序入口
-core               核心代码
    -student.py     学生的功能封装
    -teacher.py     教师的功能封装
    -grade.py       班级的功能封装
    -common.py      以上三个对象公共方法
-data               数据管理
    -init_data      数据库，初始数据添加
    -init_database  数据库数据结构的初始化
    -database.db    用sqlite存储数据
```