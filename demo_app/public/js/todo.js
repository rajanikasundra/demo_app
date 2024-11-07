frappe.ui.form.on('ToDo', {
    refresh: function(frm) {
        frappe.msgprint(__(`refresh js event 2`))  
    },

    onload(frm){
        frappe.msgprint("onload event")
    },

    validate(frm){
        frappe.msgprint("validate event")
        // frappe.throw("validate event")
    },

    before_save(frm){
        // frappe.throw("before_save event")
        frappe.msgprint(__("Full name is {0}",[frm.doc.description]))
    },

    after_save(frm){
        frappe.throw("after_save event")

    },

    // before_submit(frm){
    //     frappe.throw("before submit event")
    // },

    // on_submit(frm){
    //     frappe.throw("on submit event")
    // },

    // before_cancle(frm){
    //     frappe.throw("before cancle event")
    // },

    // after_cancle(frm){
    //     frappe.throw("after cancle event")
    // }
});


