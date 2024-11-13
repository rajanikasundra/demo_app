# Copyright (c) 2024, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime, timedelta


class SystemLog(Document):
	def validate(self):
		
		limit_date = datetime.today() - timedelta(days=1)

		data = frappe.db.get_all("System Log", {"timestamp":('<',limit_date)},pluck="name")
		print(f"\n\n\n\n{data}\n{limit_date}\n\n\n")
  
		for item in data:
			print(item)
			# frappe.db.delete("System Log",item)
			# frappe.delete_doc("System Log",item)
