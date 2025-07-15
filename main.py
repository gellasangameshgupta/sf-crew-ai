import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_salesforce_auth():
    # Authentication parameters
    params = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("SF_CONSUMER_KEY"),      # Consumer Key
        "client_secret": os.getenv("SF_CONSUMER_SECRET"), # Consumer Secret
    }
    
    # For production orgs
    token_url = "https://absyz-23e-dev-ed.lightning.force.com/services/oauth2/token"
    # For sandbox orgs, use:
    # token_url = "https://test.salesforce.com/services/oauth2/token"
    
    # Make the authentication request
    response = requests.post(token_url, params=params)
    
    # Check if authentication was successful
    if response.status_code == 200:
        # Extract the access token and instance URL
        auth_data = response.json()
        access_token = auth_data.get("access_token")
        instance_url = auth_data.get("instance_url")
        
        print("Authentication successful!")
        print(f"Access Token: {access_token[:10]}...")  # Print first 10 chars for security
        print(f"Instance URL: {instance_url}")
        
        # Test the connection with a simple query
        test_api_connection(access_token, instance_url)
    else:
        print(f"Authentication failed: {response.status_code}")
        print(response.text)

def test_api_connection(access_token, instance_url):
    # Set up the headers with the access token
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    # Simple query to test the connection - get one Account record
    query = "SELECT Id FROM Account LIMIT 1"
    url = f"{instance_url}/services/data/v56.0/query?q={query}"
    
    # Make the request
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("\nAPI connection test successful!")
        print(response.json())
    else:
        print(f"\nAPI connection test failed: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    test_salesforce_auth()
