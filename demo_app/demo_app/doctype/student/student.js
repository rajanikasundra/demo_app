// Copyright (c) 2024, admin and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Student", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on('Subject', {
  
    mark: function (frm, cdt, cdn) {
        let child = locals[cdt][cdn];
    
        if (child.mark < 0) {
            child.mark = 0    
            frappe.throw(__('Marks cannot be negative.'));
        }
        if(child.mark > 100){
            child.mark = 0
            frappe.throw(__('Marks not valid more than 100.'))
        }
        frm.refresh_field('mark');
        
    }
    
});