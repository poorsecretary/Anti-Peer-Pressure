import random
import json


def high_school_location(a=random.randint(0, 1)):
	with open("Data", "r", encoding="utf-8") as d:
		data = json.loads(d.read())
		# 如果美高
		if a == 0:
			location = random.choice(data["State"])
			school_type = random.choice(data["school_type_us"])
		# 如果大陆高中

		else:
			location = random.choice(data["Province"])
			school_type = random.choice(data["school_type_china"])

		return [location, school_type]


def randomname(a=random.randint(0, 480)):
	with open("Data", "r", encoding="utf-8") as d:
		sumname = json.loads(d.read())["sumname"]
		return sumname[a]


def ap_score(n=random.randint(1, 38)):
	with open("Data", "r", encoding="utf-8") as d:
		ap_subject = random.choices(json.loads(d.read())["ap_tests"], k=n)
		for n in range(0, len(ap_subject)):
			ap_subject[n] = ap_subject[n] + " {}分".format(random.randint(3, 5))
		string = ""
		for ap in ap_subject:
			string += ap + ", "
			if ap == ap_subject[len(ap_subject) - 1]:
				string += ap + "。"
		return [string, len(ap_subject)]


class Student:
	sat_test_time = random.randint(1, 5)

	def __init__(self, toefl=None, best_sat=None, sat=None, best_one_time=None, best_over_all=None, location=None,
	             toefl_r=None, toefl_l=None, toefl_s=None, toefl_w=None, toefl_my_best_score=None, ap=None,
	             ap_count=None, accept_list=None, deny_list=None, waitlist=None, decison=None, number_of_apply=None,
	             gpa_limit=random.choice([4.0, 4.5, 5.0]), gpa=None):
		self.GPA_limit = gpa_limit
		self.GPA = None
		if location is None:
			location = high_school_location()
		if best_over_all is None:
			best_over_all = []
		if sat is None:
			sat = []
		self.toefl = toefl
		self.best_sat = best_sat
		self.sat = sat
		self.best_one_time = best_one_time
		self.best_over_all = best_over_all
		self.location = location
		self.toefl_r = toefl_r
		self.toefl_l = toefl_l
		self.toefl_s = toefl_s
		self.toefl_w = toefl_w
		self.toefl_my_best_score = toefl_my_best_score
		self.toefl_test()
		self.ap = ap
		self.ap_count = ap_count
		self.accept_list = accept_list
		self.deny_list = deny_list
		self.waitlist = waitlist
		self.decision = decison
		self.number_of_apply = number_of_apply
		self.test()

	def test(self):
		self.gpa()
		self.toefl_test()
		self.sat_test()
		self.ap_test()
		self.apply()

	def gpa(self):
		self.GPA = round(random.uniform(3.0 + (self.GPA_limit - 4.0), self.GPA_limit),2)

	def best(self):
		return self.best_over_all[0] + self.best_over_all[1] + self.best_over_all[2]

	def one_time_best_sat(self):
		return self.sat[self.best_one_time]

	def toefl_test(self):
		n = random.randint(1, 7)
		grade_list = [random.randint(20, 30) for x in range(0, 4)]
		best_r, best_h, best_s, best_w, = grade_list[0], grade_list[1], grade_list[2], grade_list[3]
		best_all = best_r + best_h + best_w + best_w

		for n in range(0, n):
			r, best_r = best_grade(best_r)
			h, best_h = best_grade(best_h)
			s, best_s = best_grade(best_s)
			w, best_w = best_grade(best_w)
			if r + h + s + w > best_all:
				best_all = r + h + s + w
				grade_list = [r, h, s, w]
		self.toefl = best_all
		self.toefl_r = grade_list[0]
		self.toefl_l = grade_list[1]
		self.toefl_s = grade_list[2]
		self.toefl_w = grade_list[3]
		self.toefl_my_best_score = best_h + best_r + best_s + best_w

	def ap_test(self):
		n = random.randint(1, 28)
		with open("Data", "r", encoding="utf-8") as d:
			ap_subject = random.choices(json.loads(d.read())["ap_tests"], k=n)
			for n in range(0, len(ap_subject)):
				ap_subject[n] = ap_subject[n] + " {}分".format(random.randint(3, 5))
			string = ""
			for ap in ap_subject:
				string += ap + ", "
				if ap == ap_subject[len(ap_subject) - 1]:
					string += ap + "。"
			self.ap = string
			self.ap_count = len(ap_subject)

	def sat_test(self):
		for n in range(0, Student.sat_test_time):
			if n == 0:
				grade = random_sat()
				self.best_sat = grade[0] + grade[1] + grade[2]
				self.best_over_all = list(grade)
				self.best_one_time = n
			else:
				g_list = self.sat[n - 1]
				grade = random_sat(g_list[0], g_list[1], g_list[2])
				for x in range(0, 3):
					if grade[x] > self.best_over_all[x]:
						self.best_over_all[x] = int(grade[x])
				if grade[0] + grade[1] + grade[2] > self.best_sat:
					self.best_sat = grade[0] + grade[1] + grade[2]
					self.best_one_time = n
			self.sat.append(grade)

	def apply(self):
		n = random.randint(5, 20)
		self.number_of_apply = n
		with open("Data", "r", encoding="utf-8") as d:
			university = random.sample(json.loads(d.read())["University"], n)
			accept = round(n * 4 / 13)
			accept_list = random.sample(university, accept)
			self.accept_list = l2s(accept_list)
			deny = round(n * 5 / 13)
			deny_list = random.sample(list(set(university) - set(accept_list)), deny)
			self.deny_list = l2s(deny_list)
			wl = n - accept - deny
			waitlist = random.sample(list(set(university) - set(accept_list) - set(deny_list)), wl)
			self.waitlist = l2s(waitlist)
			decision = random.choice(accept_list)
			self.decision = str(decision)


def l2s(n):
	string = ""
	for x in n:
		if x == n[len(n) - 1]:
			string += x
		else:
			string += x + "、"

	return string


def random_sat(r=None, g=None, m=None):
	if r == g == m is None:
		return [random.randint(20, 30) * 10, random.randint(20, 30) * 10, random.randint(70, 80) * 10]
	else:
		r, g, m = r / 10, g / 10, m / 10
		upper_limit = r + 10 if r < 30 else 40
		lower_limit = r - 3 if r > 5 else 5
		reading = random.randint(lower_limit, upper_limit)
		upper_limit = g + 10 if g < 30 else 40
		lower_limit = g - 3 if g > 5 else 5
		grammar = random.randint(lower_limit, upper_limit)
		upper_limit = m + 20 if m < 60 else 80
		lower_limit = m - 5 if m > 10 else 10
		math = random.randint(lower_limit, upper_limit)
		return [reading * 10, grammar * 10, math * 10]


def best_grade(b):
	a = random.randint(b - 5 if b >= 5 else 5, b + 5 if b <= 25 else 30)
	if a > b:
		b = a
	return a, b
