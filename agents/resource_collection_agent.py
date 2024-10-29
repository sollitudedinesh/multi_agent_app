import requests

def collect_datasets(use_case):
    # Search for relevant datasets on Kaggle
    dataset_search_url = f"https://www.kaggle.com/search?q={use_case.replace(' ', '+')}"
    return dataset_search_url  # Returns link for now; customize if API available

# Collect links for multiple use cases
def collect_resources(use_cases):
    resource_links = []
    for use_case in use_cases:
        link = collect_datasets(use_case)
        resource_links.append(f"- {use_case}: [Dataset Link]({link})")
    return "\n".join(resource_links)

# Test function
if __name__ == "__main__":
    use_cases = ["Predictive Maintenance", "Customer sentiment analysis"]
    print(collect_resources(use_cases))
