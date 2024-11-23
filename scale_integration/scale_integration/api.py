
import frappe
from scale_integration.scale_integration.scale import parse_scale_barcode

@frappe.whitelist()
def process_scale_barcode(barcode):
    """
    Process the scanned scale barcode and return item details.
    """
    return parse_scale_barcode(barcode)
