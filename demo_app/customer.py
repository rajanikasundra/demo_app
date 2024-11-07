
import frappe
def on_update(doc,event):
    print(f"\n{doc}\n{event}\n")
    customer_group = doc.customer_group
    data = frappe.db.get_list('Customer', filters={'customer_group': ['like', customer_group ]},pluck='name')
    print(f"\n\n{data}\n\n")
    count = len(data)

    for name in data:
        frappe.db.set_value('Customer', name, 'customer_group_count', count)

    doc.customer_group_count = count
		



# // Remove action button


def before_save(doc,event):
    
    
    doc1 = frappe.get_doc('Server Side Scripting','try4 ')
    # frappe.msgprint(f"{doc}")
    # frappe.msgprint(f"{doc1}")
    if doc is doc1:
        print("same")
    else :
        print("not same")
        
    doc1.append("family_members",{
        "name1":"riya",
        "relation":"bhabhi",
        "age":22
    })
    doc1.db_insert()
		
    
    
    
    
    # frappe.msgprint(f"\n{doc.first_name}\n\n")
    # price_changed = doc.has_value_changed("bod")
    # frappe.msgprint(f"\n{price_changed}\n\n")
    # if price_changed:
    #     frappe.msgprint("yes")
    
    
        
        
	
