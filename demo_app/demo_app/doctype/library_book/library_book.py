# Copyright (c) 2024, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime

class LibraryBook(Document):
	def validate(self):
		self.check_isbnNo_unique()
		self.past_publication_year()
  
	def check_isbnNo_unique(self):
		no = self.isbn_number
		exists_no = frappe.db.exists("Library Book",{"isbn_number": no})
		if exists_no :
			frappe.throw("Enter unique <b>Isbn Number</b>")
  
	def past_publication_year(self):
		year = self.publication_year
		current_year = datetime.now().year
  
		if year > current_year:
			frappe.throw("Enter publication year less than current year")
		

     


