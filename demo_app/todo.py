import frappe

def validates(doc,event):
    print("\nabc\n")
    frappe.msgprint(f"validate event for doc event {doc}\n{event}")


def on_update(doc,event):
    # super().on_update()
    frappe.msgprint("i am on update")


def before_save(doc,event):
    frappe.msgprint(f"before_save events")


def before_insert(doc,event):
    frappe.msgprint(f"before_insert events ")


def after_insert(doc,event):
    frappe.msgprint("after_insert( events")


# def before_submit(doc,event:
#     frappe.msgprint("before_submit events")


# def on_submit(doc,event):
# 	frappe.msgprint("on_submit events")


# def on_cancel(doc,event):
# 	frappe.msgprint("on_cancle events")


def on_trash(doc,event):
    frappe.msgprint("on_trash events")


def after_delete(doc,event):
    frappe.msgprint("after_delete events")
    

def OverrideNew_todo(description):
    frappe.msgprint("1111111111111")