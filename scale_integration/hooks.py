
doc_events = {
    "POS Invoice": {
        "before_save": "scale_integration.scale_integration.scale.process_scale_barcode"
    }
}


fixtures = ["Custom Field", "Custom Script", "Scale Settings"]
app_include_js = "/assets/scale_integration/js/scale_integration.js"
app_include_css = "/assets/scale_integration/css/scale_integration.css"
