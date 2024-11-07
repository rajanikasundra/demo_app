# Copyright (c) 2024, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime, date


class Student(Document):
	def validate(self):

		# frappe.msgprint("student.py Startsdfghjhgfdfgh")
		# Age setup

		dob = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
		current_date = datetime.today()
		try:
			if dob > current_date :
				frappe.throw("Please enter proper Birth Date")
			age = current_date.year - dob.year - ((current_date.month,current_date.day) < (dob.month,dob.day))
			print(age)
			self.age = int(age)
		except:
			frappe.throw("Enter Birth date")
		

		# Date logic
		if self.date_of_birth >= self.enrollment_date:
			frappe.throw("Enrollment Date not more than or equal Birth Date")


		# Percentage setup
		try:
			count = 0
			total = 0
			for row in self.get("subject_details"):
				if row.mark == None:
					frappe.throw("Please Enter Mark")
				count+=1
				total += row.mark
				# frappe.msgprint("{0}. Subject - {1} & mark - {2}".format(row.idx,row.subject_name,row.mark))
			
			possible_max_mark = count * 100
			percentage = total / count
			self.percentage = percentage
		except:
			frappe.throw("Enter Subject and marks")


		# Print 
		frappe.msgprint(f"Possible Maximal Marks :: {possible_max_mark}")
		frappe.msgprint(f"Total marks :: {total}")
		frappe.msgprint(f"Percentage :: {percentage} ")


	
		# status satup
		# if percentage < 33.00 :
		# 	self.status = 'Fail'
		# elif percentage >=33.00 and percentage < 50.00 :
		# 	self.status = 'Pass'
		# elif percentage >= 50.00 :
		# 	self.status = 'Excellent'
