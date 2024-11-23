
doc_events = {
    "POS Invoice": {
        "before_save": "scale_integration.scale_integration.scale.process_scale_barcode"
    }
}


fixtures = ["Custom Field", "Custom Script", "Scale Settings"]