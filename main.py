from grade_generator import *

# creation
student = Student()

# Introduction
print("让{}同学来讲述一下他的申请经历\n大家好我是来自{}{}的一名学生。".format(randomname(), high_school_location()[0],
                                                   high_school_location()[1]))
# GPA
print("我的GPA是{}/{}。 ".format(student.GPA_limit, student.GPA_limit))
# Toefl Portion
print("我托福最高分是{},阅读{},听力{},口语{},写作{}.拼分最好是{}.当然跟其他知乎大佬是比不了的。".format(student.toefl,
                                                                     student.toefl_r,
                                                                     student.toefl_l,
                                                                     student.toefl_s,
                                                                     student.toefl_w,
                                                                     student.toefl_my_best_score))

# SAT portion
print("关于SAT呢我一共考了{}次，单次最高是{}，阅读{}，语法{}，数学{}，拼分最高是{}。可能是这个回答底下最低吧。".format(student.sat_test_time, student.best_sat,
                                                                           student.one_time_best_sat()[0],
                                                                           student.one_time_best_sat()[1],
                                                                           student.one_time_best_sat()[2],
                                                                           student.best()))

# AP portion
print("我总共考了{}门ap,分别是{}.有些考的不好。因为准备的太仓促了".format(student.ap_count, student.ap))

# Apply
print("我最后决定申请{}所学校,我获得了{}的offer,我被{}脆拒了,以及我被{}放在了waitlist上.我最后决定去我的梦校{}.".format(student.number_of_apply,
                                                                                  student.accept_list,
                                                                                  student.deny_list,
                                                                                  student.waitlist,
                                                                                  student.decision))
# agent
print("最后呢，我十分感谢我的中介{}老师对我文书的不断修改。过程中他对我尽心尽力，如果有需要的同学可以联系他哦。".format(randomname()))
