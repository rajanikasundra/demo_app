import frappe

def validate(doc,event):
    pass
    # print(f"\n\n\n\n\n\n{doc.first_name,doc.last_name},{event}")
    # frappe.msgprint(f"Error occured {doc.name}")


def on_update(doc,event):
    pass
    # print(f"\n\n\n\n\n\n{doc.first_name,doc.last_name},{event}")
    # frappe.msgprint(f"{doc.name} has been updated by {doc.owner}")

def before_submit(doc,event):
    pass
    # frappe.msgprint(f"Error occured {doc.name1}")
   
    # script1 = frappe.get_doc({
    #     'doctype':'Student',
    #     'name':f"{doc.name} added",
    #     'name1': f"{doc.name1} Added",
    #     'public': True
    # })
  
    # script1.insert()
    # frappe.db.commit()
    

