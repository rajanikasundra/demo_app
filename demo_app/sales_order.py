import frappe
def before_save(doc,event):
    doc.additional_discount_percentage = 5
    # frappe.msgprint(f"yesss {doc}\n {doc.additional_discount_percentage}  \n {doc.customer}")
