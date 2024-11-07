

frappe.ui.form.on('Customer', {
    refresh: function(frm) {
        frm.page.remove_inner_button(__('Get Customer Group Details'), __('Actions'));
        // console.log("\n\nCustom Customer logic loaded\n\n")   
    },
});

