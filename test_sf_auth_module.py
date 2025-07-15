# test_sf_auth_module.py
from salesforce_auth import SalesforceAuth

# Create an instance of the SalesforceAuth class
sf_auth = SalesforceAuth()

try:
    # Test authentication
    token = sf_auth.authenticate()
    print("Authentication successful!")
    print(f"Access Token: {token[:10]}...")
    print(f"Instance URL: {sf_auth.instance_url}")
    
    # Test query functionality
    result = sf_auth.query("SELECT Id, Name FROM Account LIMIT 5")
    print("\nQuery successful!")
    print(f"Found {result['totalSize']} records")
    
    # Display the records
    for record in result['records']:
        print(f"Account: {record['Name']} (ID: {record['Id']})")
        
except Exception as e:
    print(f"Error: {str(e)}")
