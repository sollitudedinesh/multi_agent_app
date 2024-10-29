from agents.industry_research_agent import research_industry
from agents.use_case_generation_agent import generate_use_cases
from agents.resource_collection_agent import collect_resources

def run_workflow(company_name):
    industry_info = research_industry(company_name)
    use_cases = generate_use_cases(industry_info)
    resources = collect_resources(use_cases)
    
    # Save results
    with open("resources/dataset_links.md", "w") as f:
        f.write(resources)
    return industry_info, use_cases, resources

if __name__ == "__main__":
    company_name = "TATA Motors"
    industry_info, use_cases, resources = run_workflow(company_name)
    print("Industry Info:\n", industry_info)
    print("\nUse Cases:\n", use_cases)
    print("\nResource Links:\n", resources)
