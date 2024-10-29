def generate_use_cases(industry_info):
    # Example use cases based on industry
    if "Automotive" in industry_info:
        return [
            "Predictive Maintenance with ML for vehicle health monitoring",
            "Customer sentiment analysis using NLP on feedback",
            "Supply chain optimization with AI-driven logistics"
        ]
    elif "Retail" in industry_info:
        return [
            "Personalized product recommendations using GenAI",
            "Automated inventory management",
            "Customer service chatbot for enhanced support"
        ]
    else:
        return ["General AI use cases in the specified industry."]

# Test function
if __name__ == "__main__":
    industry_info = "Automotive industry with a focus on vehicle maintenance."
    print(generate_use_cases(industry_info))
