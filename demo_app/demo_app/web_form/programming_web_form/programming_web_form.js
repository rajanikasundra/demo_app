// frappe.web_form.after_load = () => {

// }

frappe.ready(function() {
	// This code will run after the web form is fully loaded
	frappe.msgprint("Please fill all values carefully");
	frappe.web_form.on('name1',(field,value)=>{
		console.log(value)
		frappe.web_form.set_value('student_id', value+'11');
		frappe.web_form.set_value('grade', 'A');

	});
	
	frappe.web_form.validate = () => {
		let enrollment = frappe.web_form.get_value('enrollment_date');
		if (!enrollment){
			frappe.msgprint("Enter enrollment date");
			return false;
			
		}
		
	}

	frappe.web_form.on('date_of_birth', (field, value) => {
		console.log("value")
		if (value) {
		frappe.web_form.set_df_property('date_of_birth', 'hidden', 1);
		}
		frappe.web_form.set_value('grade', 'B');
	});
	   
	// let field_value = frappe.web_form.get_value('name1');  
	// console.log("Field Value:", field_value);


	
});
