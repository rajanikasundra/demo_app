// Copyright (c) 2024, admin and contributors
// For license information, please see license.txt

frappe.query_reports["Student Script Report"] = {
	"filters": [

		{
			"fieldname":"name",
			"label":__("Student"),
			"fieldtype":"Link",
			"options":"Server Side Scripting",
			"width": 80,
			"reqd": 0,
		},

		{
			"fieldname":"name1",
			"label":__("Name"),
			"fieldtype":"Data",
			"width": 80,
			"reqd": 0,
		},

		{
			"fieldname":"gender",
			"label":__("Gender"),
			"fieldtype":"Link",
			"width": 80,
			"reqd": 0,
		},
		{
			"fieldname":"age",
			"label":__("Age"),
			"fieldtype":"Int",
			"width": 80,
			"reqd": 0,
		},

	]
};
