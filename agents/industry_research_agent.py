import requests
import serpapi

# Replace 'YOUR_SERPER_API_KEY' with your actual Serper API key
SERPER_API_KEY = 'YOUR_SERPER_API_KEY'

def research_industry(company_name):
    search_url = "https://serpapi.com/search"
    params = {
        "q": f"{company_name} industry overview",
        "api_key": SERPER_API_KEY,
        "num": 5  # Number of results
    }
    
    response = requests.get(search_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        # Process the JSON response to extract relevant information
        industry_info = ""
        for result in data.get("organic_results", []):
            industry_info += f"{result['title']}: {result['snippet']}\n"
        return industry_info if industry_info else "No data found."
    else:
        return f"Error fetching industry data: {response.status_code}"

# Test function
if __name__ == "__main__":
    print(research_industry("Nike"))
