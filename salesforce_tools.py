# salesforce_tools.py
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json

import requests
from salesforce_auth import SalesforceAuth

# Initialize Salesforce authentication
sf_auth = SalesforceAuth()

class LeadSearchInput(BaseModel):
    email: str = Field(..., description="Email address to search for")

class SearchLeadTool(BaseTool):
    name: str = "search_salesforce_lead"
    description: str = "Searches for a lead in Salesforce by email address"
    args_schema: Type[BaseModel] = LeadSearchInput
    
    def _run(self, email: str) -> str:
        """Search for a lead by email address"""
        try:
            # Escape single quotes in the email
            safe_email = email.replace("'", "\\'")
            
            # Query Salesforce for the lead
            query = f"SELECT Id, FirstName, LastName, Email, Phone, Company FROM Lead WHERE Email = '{safe_email}'"
            result = sf_auth.query(query)
            
            if result['totalSize'] > 0:
                # Format the lead information
                leads = []
                for record in result['records']:
                    lead = {
                        'id': record['Id'],
                        'name': f"{record.get('FirstName', '')} {record.get('LastName', '')}",
                        'email': record['Email'],
                        'phone': record.get('Phone', 'Not provided'),
                        'company': record.get('Company', 'Not provided')
                    }
                    leads.append(lead)
                
                return json.dumps(leads)
            else:
                return "No leads found with that email address."
                
        except Exception as e:
            return f"Error searching for lead: {str(e)}"

class LeadInput(BaseModel):
    first_name: str = Field(..., description="First name of the lead")
    last_name: str = Field(..., description="Last name of the lead")
    email: str = Field(..., description="Email address of the lead")
    phone: str = Field(None, description="Phone number of the lead")
    company: str = Field(None, description="Company name")
    property_interest: str = Field(None, description="Type of property the lead is interested in")

class OpportunityInput(BaseModel):
    opportunity_id: str = Field(..., description="ID of the opportunity")

class CreateLeadTool(BaseTool):
    name: str = "create_salesforce_lead"
    description: str = "Creates a new lead in Salesforce with real estate specific information"
    args_schema: Type[BaseModel] = LeadInput
    
    def _run(self, first_name: str, last_name: str, email: str, phone: str = None, 
             company: str = None, property_interest: str = None) -> str:
        """Create a new lead in Salesforce"""
        try:
            headers = sf_auth.get_headers()
            
            # Prepare lead data
            lead_data = {
                'FirstName': first_name,
                'LastName': last_name,
                'Email': email,
                'Company': company if company else f"{first_name} {last_name}",  # Company is required
                'Phone': phone,
                'Industry': 'Real Estate',
                'Description': f'Interested in {property_interest}' if property_interest else None
            }
            
            # Remove None values
            lead_data = {k: v for k, v in lead_data.items() if v is not None}
            
            # Create the lead in Salesforce
            url = f"{sf_auth.instance_url}/services/data/v56.0/sobjects/Lead"
            response = requests.post(url, headers=headers, json=lead_data)
            
            if response.status_code == 201:
                lead_id = response.json()['id']
                return f"Lead created successfully with ID: {lead_id}"
            else:
                return f"Failed to create lead: {response.text}"
                
        except Exception as e:
            return f"Error creating lead: {str(e)}"

class GetOpportunityTool(BaseTool):
    name: str = "get_salesforce_opportunity"
    description: str = "Retrieves an opportunity from Salesforce by ID"
    args_schema: Type[BaseModel] = OpportunityInput

    def _run(self, opportunity_id: str) -> str:
        """Retrieve an opportunity by ID"""
        try:
            headers = sf_auth.get_headers()
            url = f"{sf_auth.instance_url}/services/data/v56.0/sobjects/Opportunity/{opportunity_id}"
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                opportunity = response.json()
                return json.dumps(opportunity)
            else:
                return f"Failed to retrieve opportunity: {response.text}"
                
        except Exception as e:
            return f"Error retrieving opportunity: {str(e)}"