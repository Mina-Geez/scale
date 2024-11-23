
import frappe

def parse_scale_barcode(barcode):
    """
    Parse a scale barcode and return item details.

    Barcode format: Prefix (2 digits) + Item Code (5 digits) + Weight (6 digits)
    Example: 2030001010003 -> Prefix: 20, Item Code: 30001, Weight: 1.0003 kg
    """
    try:
        prefix_length = 2
        item_code_length = 5
        weight_length = 6

        # Extract parts of the barcode
        prefix = barcode[:prefix_length]
        item_code = barcode[prefix_length:prefix_length + item_code_length]
        weight_raw = barcode[prefix_length + item_code_length:]

        # Convert weight (e.g., 010003 -> 1.0003 kg)
        weight = float(weight_raw) / 10000

        # Check prefix validity
        if prefix != "20":
            frappe.throw(f"Invalid barcode prefix: {prefix}")

        # Fetch item details
        item = frappe.get_doc("Item", {"item_code": item_code})
        if not item:
            frappe.throw(f"Item with code {item_code} not found!")

        return {
            "item_code": item_code,
            "item_name": item.item_name,
            "qty": weight,
            "rate": item.standard_rate or 0,
        }
    except Exception as e:
        frappe.throw(f"Error parsing barcode: {str(e)}")
