import frappe

def before_submit(doc,event):
    customer = frappe.db.get_list('Sales Invoice',
                                  fields = ['customer', 'outstanding_amount'],
                                  filters={'customer':['like',doc.customer]}, 
                                  )
    total_outstanding_amount = 0
    for name in customer:
        if name.outstanding_amount > 0:
            total_outstanding_amount += name.outstanding_amount
        
    if total_outstanding_amount > 0 :
        frappe.msgprint(f"Your Total Outstanding Amount Is :: {total_outstanding_amount}")
    else :
        frappe.msgprint("You have no any outstanding amount")
        
        
        print(f"{name.customer}::{name.outstanding_amount}")
        print("\n\n")
        