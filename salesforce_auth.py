# salesforce_auth.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class SalesforceAuth:
    def __init__(self):
        self.consumer_key = os.getenv("SF_CONSUMER_KEY")
        self.consumer_secret = os.getenv("SF_CONSUMER_SECRET")
        self.access_token = None
        self.instance_url = None
        
        # For production orgs
        self.token_url = "https://absyz-23e-dev-ed.lightning.force.com/services/oauth2/token"
        # For sandbox orgs, use:
        # self.token_url = "https://test.salesforce.com/services/oauth2/token"
    
    def authenticate(self):
        """Authenticate with Salesforce and get access token"""
        params = {
            "grant_type": "client_credentials",
            "client_id": self.consumer_key,
            "client_secret": self.consumer_secret,
        }
        
        response = requests.post(self.token_url, params=params)
        
        if response.status_code == 200:
            auth_data = response.json()
            self.access_token = auth_data.get("access_token")
            self.instance_url = auth_data.get("instance_url")
            return self.access_token
        else:
            raise Exception(f"Authentication failed: {response.text}")
    
    def get_headers(self):
        """Return headers with authentication token"""
        if not self.access_token:
            self.authenticate()
        
        return {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
    
    def query(self, soql_query):
        """Execute a SOQL query"""
        headers = self.get_headers()
        url = f"{self.instance_url}/services/data/v56.0/query?q={soql_query}"
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            # If unauthorized, try to re-authenticate once
            if response.status_code == 401:
                self.authenticate()
                headers = self.get_headers()
                response = requests.get(url, headers=headers)
                
                if response.status_code == 200:
                    return response.json()
            
            raise Exception(f"Query failed: {response.text}")
