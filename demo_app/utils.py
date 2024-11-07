# demo_app/utils.py
import frappe
def greet(name):
    return f"Hello, {name}!"

def capitalize_all(value):
    return ' '.join([word.capitalize() for word in value.split()])


def before_request():
    print("\naaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
    # Logic to execute before processing the request
    user = frappe.session.user
    frappe.logger().info(f"Request made by user: {user}")

def after_request(response):
    print("\nbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n")
    # Logic to execute after processing the request
    response_time = ...  # calculate response time
    frappe.logger().info(f"Response sent in {response_time} seconds")
    print(response_time)
    print(response)
    return response  # return the modified or original response

def before_job():
    
    print("\n\nbj\n")

def after_job():
    print("\n\naj\n")