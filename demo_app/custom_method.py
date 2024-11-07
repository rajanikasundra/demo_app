import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def add_special_note():
    # Check if the custom field already exists to avoid duplication
    if not frappe.db.exists('Custom Field', {"dt":'Delivery Note','fieldname': 'special_note'}):
        custom_field = frappe.get_doc({
            'doctype': 'Custom Field',
            'dt': 'Delivery Note',
            'fieldname': 'special_note',
            'label': 'Special Note',
            'fieldtype': 'Text',
            'insert_after': 'customer',
            'default': "Thank you for your business",
           
        })
        
        # Insert the custom field into the database
        custom_field.insert()
        frappe.db.commit()

add_special_note()

# from demo_app.custom_method import add_delivery_note




# in demo_app/custom_employee.py

def custom_get_employee_email(employee_doc):
    print("\n\n\n aaaaaaaabbbbbbbbbbbbbbccccccccccc  \n\n")
    # Custom logic here if needed, or just modify the existing function
    return (
        employee_doc.get("user_id") or 
        employee_doc.get("personal_email") or 
        employee_doc.get("company_email")
    )
