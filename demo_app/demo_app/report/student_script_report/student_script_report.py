# Copyright (c) 2024, admin and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []

	columns = get_columns()
	cs_data = get_cs_data(filters)

	if not cs_data:
		frappe.msgprint('No records found')
		print(f"\n\n\n\n1...{columns,cs_data}\n\n\n")
		return columns, cs_data

	data = []

	for d in cs_data:
		row = frappe._dict({
			'name1': d.name1,
			'date_of_birth': d.date_of_birth,
			'percentage': d.percentage,
			'age': d.age,
			'subject_name':d.subject_name,
			'mark':d.mark
		})
		data.append(row)

	chart = get_chart_data(data)
	report_summary = get_report_summary(data)
	return columns, data, None, chart, report_summary




def get_columns():
	return[
	
		{
			"fieldname":"name1",
			"label":("Name"),
			"fieldtype":"Data",
			"width": 80,
			
		},
		{
			"fieldname":"age",
			"label":("Age"),
			"fieldtype":"Int",
			"width": 100,
		},
		{
			"fieldname":"date_of_birth",
			"label":("DOB"),
			"fieldtype":"Date",
			"width": 80,
		},
		{
			"fieldname":"percentage",
			"label":("Percent"),
			"fieldtype":"Percent",
			"width": 100,
		},
		{
			"fieldname":"subject_name",
			"label":("Subject Name"),
			"fieldtype":"data",
			"width": 80,
		},
		{
			"fieldname":"mark",
			"label":("Marks"),
			"fieldtype":"Int",
			"width": 80,
		},
		
	]


def get_cs_data(filters):
	conditions = get_conditions(filters)
	print(f"2....\n\n\n\n\n\n\n{conditions}\n\n\n{filters}\n\n\n\n")
	data = frappe.get_all(
		doctype = 'Student',
		fields = ['name1','date_of_birth','percentage', 'age', 'subject_details.subject_name','subject_details.mark'],
		filters = conditions,
		order_by = 'name1 desc' 
	)
	return data


def get_conditions(filters):
	print(f"\n\n3..{filters}\n\n")
	conditions = {}
	for key,value in filters.items():
		if filters.get(key):
			conditions[key]= value
	return conditions



def get_chart_data(data):
	if not data :
		return None

	labels = ['mark <= 50', 'mark > 50']

	mark_data = {
		'mark <= 50' : 0,
		'mark > 50' : 0,
	}

	datasets = []

	for entry in data:
		# print(f"\n\n{type(entry.age, data)}\n\n")
		if entry.mark <= 50:
			mark_data['mark <= 50'] += 1
		else :
			mark_data['mark > 50'] += 1
	# a=10
	# b=5
	datasets.append({
		'name' : 'Mark Status',
		'values' : [mark_data.get('mark <= 50'), mark_data.get('mark > 50')]
		# 'values' : [a,b]
	})
	print(f"\n\n\n\n\n\n\n\n5... datasets :: {datasets}\n\n\n\n\n")
	chart = {
		'data' : {
			'labels':labels,
			'datasets':datasets
		},
		'type' : 'line',
		'height' : 300
	}
	print(f"\n\n\n\n\n\n\n\n6.... chart :: {chart}\n\n\n\n\n")

	return chart




def get_report_summary(data):
	if not data :
		return None
	print(f"\n{data}\n")
	below_60, above_60 = 0,0

	for entry in data:
		if entry.percentage <= 60:
			below_60 += 1
		else :
			above_60 += 1


	return[
		{
			'value' : below_60,
			'indicator' : 'Green',
			'label' : 'Percentage Below 60',
			'datatype' : 'Int'
		},
		{
			'value' : above_60,
			'indicator' : 'Blue',
			'label' : 'Percentage Above 60',
			'datatype' : 'Int'
		},
	]


