import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import make_delivery_note
from frappe.model.mapper import get_mapped_doc
from frappe.utils import flt

@frappe.whitelist()
def make_delivery_note(source_name, target_doc=None):
    def set_missing_values(source, target):
        if not target.get("special_note"):
            target.special_note = "Thank you for your business!"
        target.run_method("set_missing_values")
        target.run_method("set_po_nos")
        target.run_method("calculate_taxes_and_totals")

    def update_item(source_doc, target_doc, source_parent):
        target_doc.qty = flt(source_doc.qty) - flt(source_doc.delivered_qty)
        target_doc.stock_qty = target_doc.qty * flt(source_doc.conversion_factor)

        target_doc.base_amount = target_doc.qty * flt(source_doc.base_rate)
        target_doc.amount = target_doc.qty * flt(source_doc.rate)

    doclist = get_mapped_doc(
        "Sales Invoice",
        source_name,
        {
            "Sales Invoice": {"doctype": "Delivery Note", "validation": {"docstatus": ["=", 1]}},
            "Sales Invoice Item": {
                "doctype": "Delivery Note Item",
                "field_map": {
                    "name": "stei_detail",
                    "parent": "against_sales_invoice",
                    "serial_no": "serial_no",
                    "sales_order": "against_sales_order",
                    "so_detail": "so_detail",
                    "cost_center": "cost_center",
                },
                "postprocess": update_item,
                "condition": lambda doc: doc.delivered_by_supplier != 1,
            },
            "Sales Taxes and Charges": {"doctype": "Sales Taxes and Charges", "add_if_empty": True},
            "Sales Team": {
                "doctype": "Sales Team",
                "field_map": {"incentives": "incentives"},
                "add_if_empty": True,
            },
        },
        target_doc,
        set_missing_values,
    )

    return doclist



