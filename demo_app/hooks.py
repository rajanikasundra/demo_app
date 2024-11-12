app_name = "demo_app"
app_title = "Demo App"
app_publisher = "admin"
app_description = "app for demo app"
app_email = "test@site.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/demo_app/assets/css/demo_app.css"
# app_include_js = [ "/assets/demo_app/js/demo_app.js" , "/assets/demo_app/assets/js/demo_app.js"]

# include js, css files in header of web template
# web_include_css = "/assets/demo_app/css/app-web.css"
# web_include_js = "/assets/demo_app/js/app-web.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "demo_app/public/scss/website"

# include js, css files in header of web form
# dout!!!!
# webform_include_js = {"Programming Web-Form": "public/js/web-form.js"}
# webform_include_css = {"Programming Web-Form ": "public/css/web-form.css"}

# include js in page
# page_js = {"programming-page" : "public/js/page.js"}

# include js in doctype views
doctype_js = {
			# "doctype" : "public/js/doctype.js",
			"Customer" : "public/js/customer.js",
			# "ToDo": "public/js/todo.js"
}
# doctype_list_js = {
# 	"Dixit" : "public/js/student_list.js"
# }

doctype_tree_js = {"Student" : "public/js/student_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# dout!!!!!!!!
# app_include_icons = "demo_app/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Administrator": "index"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Student"]

# Jinja
# ----------

# add methods and filters to jinja environment
jinja = {
	"methods": "demo_app.utils.greet",
	"filters": "demo_app.utils.capitalize_all"
}

# Installation
# ------------

# before_install = "demo_app.install.before_install"
# after_install = "demo_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "demo_app.uninstall.before_uninstall"
# after_uninstall = "demo_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "demo_app.utils.before_app_install"
# after_app_install = "demo_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "demo_app.utils.before_app_uninstall"
# after_app_uninstall = "demo_app.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# dout!!!!!!!
# notification_config = "demo_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	# "ToDo": "demo_app.event.OverrideToDo",
	"Student": "demo_app.event.OverrideStudent",
	# "Customer": "demo_app.customer.customCustomer",
	# "Purchase Order": "demo_app.event.OverridePurchaseOrder",
	
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }

	'Student':{
		"validate":"demo_app.demo_app.doctype.student.events.validate",
		# "on_update":"erpnext.my_module.doctype.server_side_scripting.events.on_update",
		"before_submit":"demo_app.demo_app.doctype.student.events.before_submit",
	},
	'Customer':{
		"on_update":"demo_app.customer.on_update",
	},
	'ToDo':{
		"validate":"demo_app.todo.validates",
		"on_update":"demo_app.todo.on_update",
		"before_save":"demo_app.todo.before_save",
		"before_insert":"demo_app.todo.before_insert",
		"after_insert":"demo_app.todo.after_insert",
		"on_trash":"demo_app.todo.on_trash",
		"after_delete":"demo_app.todo.after_delete"

	},
	'Server Side Scripting':{
		"before_save":"demo_app.customer.before_save"
	},

	'Sales Order':{
		"before_save":"demo_app.sales_order.before_save"
	},
 
	# 'Sales Invoice':{
	# 	'before_submit':"demo_app.sales_invoice.before_submit"
	# }
 
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	# "cron": {
    #     "* * * * *":[
    #         # "demo_app.tasks.cron",
	# 		# "erpnext.tasks.enqueue_job"
    #     ],
	# }
	# "all": [
    #     "demo_app.tasks.cron"
    # ],
	"daily": [
		"demo_app.tasks.daily"
	],
	# "hourly": [
	# 	"demo_app.tasks.hourly"
	# ],
	# "weekly": [
	# 	"demo_app.tasks.weekly"
	# ],
	# "monthly": [
	# 	"demo_app.tasks.monthly"
	# ],
}

# Testing
# -------

# before_tests = "demo_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
	# "frappe.desk.doctype.todo.todo.new_todo": "demo_app.todo.OverrideNew_todo",
	# "frappe.desk.doctype.event.event.get_events": "demo_app.event.get_events",
	"erpnext.my_module.doctype.client_side_scripting.client_side_scripting.frappe_call" : "demo_app.event.Myfrappe_call",
	"erpnext.accounts.doctype.sales_invoice.sales_invoice.make_delivery_note" : "demo_app.whitelist_override.make_delivery_note",
	
}
#



# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
override_doctype_dashboards = {
	"Task": "demo_app.tasks.get_dashboard_data"
}

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Grade"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Student"]


# Request Events
# ----------------
# before_request = ["demo_app.utils.before_request"]
# after_request = ["demo_app.utils.after_request"]

# Job Events
# ----------
before_job = ["demo_app.utils.before_job"]
# after_job = ["demo_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]
user_data_fields = [
    {
        "doctype": "Student",
        "filter_by": "name",  # Field used to identify the student (e.g., user ID or email)
        "redact_fields": ["date_of_birth", "status"],  # Fields with sensitive data to redact
        "partial": 1,  # Partially redact the data, not a full deletion
    },
    # {
    #     "doctype": "Grade",
    #     "filter_by": "student_id",  # Field in `Grade` DocType to identify records linked to the student
    #     "partial": 1  # Partial redaction for records in the `Grade` DocType
    # }
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"demo_app.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


from erpnext.setup.doctype.employee import employee
from demo_app.custom_method import custom_get_employee_email

employee.get_employee_email = custom_get_employee_email