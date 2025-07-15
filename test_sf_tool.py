# test_sf_tool.py
from salesforce_tools import SearchLeadTool
import json

# Create an instance of the tool
search_lead_tool = SearchLeadTool()

# Test the tool with an email address
# Replace with an email that exists in your Salesforce org
test_email = "rick@stripe.com"

try:
    result = search_lead_tool._run(test_email)
    print(f"Search result for {test_email}:")
    
    # Try to parse the result as JSON
    try:
        leads = json.loads(result)
        if isinstance(leads, list):
            for lead in leads:
                print(f"\nName: {lead['name']}")
                print(f"Email: {lead['email']}")
                print(f"Phone: {lead['phone']}")
                print(f"Company: {lead['company']}")
                print(f"ID: {lead['id']}")
        else:
            print(result)
    except json.JSONDecodeError:
        # If not JSON, just print the string result
        print(result)
        
except Exception as e:
    print(f"Error: {str(e)}")
