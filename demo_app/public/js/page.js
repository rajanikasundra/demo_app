console.log("page_js called")

frappe.pages['programming-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Demo Page',
		single_column: true
	});

	frappe.msgprint("programing page")
	console.log("pageeee")
	page.set_title('your Page')
	page.set_indicator('Done','blue')
	let $btn = page.set_primary_action('New',() =>frappe.msgprint("Clicked New"),'octicon octicon-plus')
	let $btn2 = page.set_secondary_action('Refresh',() =>frappe.msgprint("Clicked Refresh"),'octicon octicon-plus')
	
	page.add_menu_item('send Email',() =>frappe.msgprint("Clicked send email"))

	page.add_action_item('Delete',() =>frappe.msgprint("Clicked Deleted"))


	// let field = page.add_field({
	// 	label : 'Status',
	// 	fieldtype : 'Select',
	// 	fieldname : 'Status',
	// 	options : [
	// 		'Open','Closed','Cancelled'
	// 	],
	// 	change(){
	// 		frappe.msgprint(field.get_value());
	// 	}
	// });


	//$(frappe.render_template("programming_page", {})).appendTo(page.body);

	$(frappe.render_template("programming_page",{
		data:"Hi Frappe"
	})).appendTo(page.body);
}