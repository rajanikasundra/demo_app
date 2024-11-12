

frappe.ui.form.on('Customer', {
    refresh: function(frm) {
        frm.page.remove_inner_button(__('Get Customer Group Details'), __('Actions'));
        // console.log("\n\nCustom Customer logic loaded\n\n")  
        
        


        
        frappe.call({
            method: "demo_app.customer.get_outstanding_amount",
            args: {
                customer: frm.doc.name
            },
            callback: function(r) {console.log("[[[[[",r.message)
                if (r.message) {
                    frappe.msgprint(__('Total Outstanding Amount: {0}', [r.message]));
                }
            }
        });
    },
});

