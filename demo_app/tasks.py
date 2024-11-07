import frappe
import string
import random
import time

# def cron():
#     letter = string.ascii_letters
#     note = " ".join(random.choice(letter) for i in range(20))

#     print(letter)
#     print("\n\n")
#     print(note)

#     new_note = frappe.get_doc({
#         "doctype" : "Note",
#         "title": note
#     })
#     new_note.insert()
#     frappe.db.commit()
#     print("abcfjdsn")
#     print("\n inserted note in note\n")
#     frappe.msgprint("success")

# # def all():
# #     print("\nabc\n")
# #     frappe.msgprint("ABC")


# def long_running_job(param1, param2):
#     try :
#         frappe.log('Starting long running job')
#         time.sleep(10)
#         frappe.log(f"param1 : {param1} and param2 : {param2}")
#         print("\n\n done \n\n")
#     except Exception as e:
#         frappe.log(f"Error in long running job : {str(e)}")
#         print("\n\n error \n\n")
#         raise


# def enqueue_job():
#     print("\n\n  \n\entern")
#     # frappe.enqueue(long_running_job, queue='default', is_async=False, now=False, timeout=500, param1 = 'A', param2='B')
#     # frappe.enqueue(long_running_job, queue='default', is_async=True, now=False, timeout=500, param1 = 'A', param2='B')
#     frappe.enqueue(long_running_job, queue='short', is_async=False, timeout=500, param1 = 'A', param2='B')









def get_dashboard_data(data):
    frappe.msgprint("aaaaaaaaaaaaa")
    print("\n\nasdfg\n")
    print(data)
    # Custom logic to gather data for the Task dashboard
    data = {
        "total_tasks": frappe.db.count('Task'),
        "completed_tasks": frappe.db.count('Task', filters={'status': 'Completed'}),
        # Add more custom metrics as needed
    }
    print("\n\n")
    print(data)
    return data