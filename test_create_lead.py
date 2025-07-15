# test_create_lead.py
from salesforce_tools import CreateLeadTool

# Create an instance of the tool
create_lead_tool = CreateLeadTool()

# Test data for creating a lead
test_lead = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe.test@example.com",
    "phone": "555-123-4567",
    "company": "Test Company",
    "property_interest": "Single Family Home"
}

try:
    result = create_lead_tool._run(**test_lead)
    print(result)
except Exception as e:
    print(f"Error: {str(e)}")
