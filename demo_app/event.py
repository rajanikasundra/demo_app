from demo_app.demo_app.doctype.student.student import Student
from frappe.model.document import Document
from datetime import datetime, date
import frappe

class OverrideStudent(Student):
	
	def validate(self):
		super().validate()

		# status satup
		if self.percentage < 33.00 :
			self.status = 'Fail'
		elif self.percentage >=33.00 and self.percentage < 50.00 :
			self.status = 'Pass'
		elif self.percentage >= 50.00 :
			self.status = 'Excellent'


# todo class override method
from frappe.desk.doctype.todo.todo import ToDo
class OverrideToDo(ToDo):
	# def validate(self):
	# 	data = self.priority
	# 	frappe.msgprint(f'Hello notty....{data}')

	# def on_update(self):
	# 	# super().on_update()
	# 	frappe.msgprint("i am on update")

	# def before_save(self):
	# 	data = self.priority
	# 	frappe.msgprint(f"before_save events {data}")
	
	# def before_insert(self):
	# 	data = self.description
	# 	frappe.msgprint(f"before_insert events  {data}")

	# def after_insert(self):
	# 	frappe.msgprint("after_insert( events")
	

	# def before_submit(self):
	# 	frappe.msgprint("before_submit events")

	# # def on_submit(self):
	# 	frappe.msgprint("on_submit events")

	# def on_cancel(self):
	# 	frappe.msgprint("on_cancle events")

	def on_trash(self):
		frappe.msgprint("on_trash events")

	def after_delete(self):
		frappe.msgprint("after_delete events")





from erpnext.buying.doctype.purchase_order.purchase_order import PurchaseOrder
class OverridePurchaseOrder(PurchaseOrder):
	def before_save(self):
		print("\n\n")
		print(self.schedule_date)
		self.status = "On Hold"
		print(self.status)

	# def validate(self):
	# 	print("\n\n")
	# 	print(self.schedule_date)
	# 	self.status = "On Hold"
	# 	print(self.status)



		# if not self.schedule_date:
		# 		frappe.throw("enter required date")

		# items_data = self.items
		# for data in items_data:
		# 	print(data.schedule_date)
			
		# 	if not data.schedule_date:
		# 		frappe.throw("enter required date")
			
		# 	frappe.msgprint("done")
		



@frappe.whitelist()
def get_events(self):
	frappe.msgprint("asd")


@frappe.whitelist()
def Myfrappe_call(msg):
	frappe.msgprint("My hello ...................")
	return " this is from event.py"





	


