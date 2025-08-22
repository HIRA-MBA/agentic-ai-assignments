from agents import function_tool



    
# FAQ lookup
faqs = {
    "return policy": "We offer a 30‑day return policy for all items.",
    "track my order": "You can track your order by giving valid order number.",
    "shipping policy": "Free shipping over $100; under $100 costs $10.",
    "payment policy": "We accept credit cards and PayPal; 10% off on orders over $100.",
    "customer service policy": "Our team is available 24/7 to assist you."
}

@function_tool
def faq_lookup_tool(question: str) -> str:
    key = question.lower().strip()
    return faqs.get(key, "Sorry, I don't have an answer for that.")