import json

def classify_customer_case(case_text):
    """
    Función que simula la clasificación automática de etiquetas y categorías
    para optimizar la anotación de datos y triaje de casos de soporte.
    """
    case_text_lower = case_text.lower()
    
    if "charge" in case_text_lower or "refund" in case_text_lower or "dispute" in case_text_lower:
        category = "Payment Dispute"
        priority = "High"
    elif "bug" in case_text_lower or "error" in case_text_lower or "app" in case_text_lower:
        category = "Technical Bug"
        priority = "Medium"
    else:
        category = "General Inquiry"
        priority = "Low"

    result = {
        "case_content": case_text,
        "predicted_category": category,
        "priority_level": priority,
        "annotation_status": "Auto-Labeled"
    }
    
    return json.dumps(result, indent=2)

if __name__ == "__main__":
    sample_case = "I was double charged for my transaction yesterday and I need an immediate refund."
    print("--- AI Case Classification Output ---")
    print(classify_customer_case(sample_case))
