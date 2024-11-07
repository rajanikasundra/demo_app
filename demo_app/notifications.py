

import frappe

def get_notification_config():
    # frappe.log_error("Notification config function called", "Notification Debug")
    
    return {
        "for_doctype": {
            "Property": {
                "conditions": [
                    {"field": "property_type", "value": "condo"},  # Notify when the student gender is Female
                ]
            }
        }
    }



# def get_notification_config():
#     return {
#         "for_doctype": {
#             "Student": {
#                 "conditions": [
#                     {"field": "gender", "value": "Female"},  # Notify when gender is Female
#                     {"field": "date_of_birth", "value": ["<", "today"]}  # Notify if date_of_birth is before today
#                 ]
#             }
#         }
#     }
