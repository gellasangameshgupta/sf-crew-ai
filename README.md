# CrewAI + Salesforce Real Estate Lead Management System

An intelligent AI-powered lead management system that integrates CrewAI multi-agent framework with Salesforce CRM to automate real estate lead qualification and management processes.

## 🚀 Features

- **Automated Lead Qualification**: AI agents analyze prospect information to identify high-intent buyers
- **Salesforce Integration**: Seamless CRM integration for lead management and opportunity tracking
- **Multi-Agent System**: Specialized AI agents for different real estate workflows
- **Real-time Data Sync**: Automatic lead creation and updates in Salesforce
- **Intelligent Decision Making**: AI-powered analysis of buying signals and qualification criteria

## 🏗️ Architecture

The system consists of four main components:

### 1. Salesforce Authentication (`salesforce_auth.py`)
- OAuth 2.0 client credentials flow
- Automatic token refresh and session management
- Secure API connection handling

### 2. Custom CrewAI Tools (`salesforce_tools.py`)
- **SearchLeadTool**: Search for existing leads by email
- **CreateLeadTool**: Create new leads with real estate-specific information
- **GetOpportunityTool**: Retrieve and analyze opportunity data

### 3. AI Agent Configuration (`crewai_integration.py`)
- Lead Qualification Specialist agent
- Real estate domain expertise
- Automated workflow execution

### 4. Main Application (`main.py`)
- Authentication testing and validation
- API connection verification

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
- Salesforce Developer account with Connected App
- CrewAI framework
- Required Python packages (see Installation)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/gellasangameshgupta/sf-crew-ai.git
cd sf-crew-ai
```

2. Install required packages:
```bash
pip install crewai python-dotenv requests pydantic
```

3. Create a `.env` file in the root directory:
```env
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# Salesforce Credentials
SF_USERNAME=your_sf_username
SF_PASSWORD=your_sf_password
SF_SECURITY_TOKEN=your_sf_security_token
SF_CONSUMER_KEY=your_sf_consumer_key
SF_CONSUMER_SECRET=your_sf_consumer_secret
SF_INSTANCE_URL=https://your-instance.salesforce.com/
```

## 🔧 Salesforce Setup

1. Create a Connected App in Salesforce:
   - Go to Setup → App Manager → New Connected App
   - Enable OAuth Settings
   - Add OAuth Scopes: `api`, `refresh_token`, `offline_access`
   - Note down Consumer Key and Consumer Secret

2. Configure OAuth Flow:
   - Use Client Credentials flow for server-to-server authentication
   - Ensure proper permissions for Lead and Opportunity objects

## 🚀 Usage

### Basic Authentication Test
```bash
python main.py
```

### Run CrewAI Lead Qualification
```bash
python crewai_integration.py
```

### Example Workflow

The system automatically:
1. Searches for existing leads by email
2. Creates new leads if they don't exist
3. Analyzes lead information for buying intent
4. Retrieves and processes opportunity data
5. Provides detailed qualification reports

## 🔍 Example Output

```
=== Crew Result ===
Lead Qualification Report:

Lead: Jane Jenifer (jane.jenifer@gmail.com)
Status: New lead created successfully (ID: 00Q5f00000X5X5XEAV)
Property Interest: Single Family Home
Buying Intent: HIGH - Active engagement signals detected
Qualification Score: 85/100

Opportunity Analysis:
- Budget alignment: Verified
- Timeline: 3-6 months
- Decision maker: Confirmed
- Next steps: Schedule property viewing
```

## 📁 File Structure

```
sf-crew-ai/
├── crewai_integration.py    # Main CrewAI agent configuration
├── salesforce_auth.py       # Salesforce authentication module
├── salesforce_tools.py      # Custom CrewAI tools for Salesforce
├── main.py                  # Authentication testing
├── .gitignore              # Git ignore patterns
├── .env                    # Environment variables (not tracked)
└── README.md               # This file
```

## 🛡️ Security

- All sensitive credentials are stored in `.env` file (excluded from version control)
- OAuth 2.0 secure authentication flow
- Token refresh and session management
- API request validation and error handling

## 🔄 Workflow

1. **Lead Intake**: System receives lead information
2. **Duplicate Check**: Searches Salesforce for existing leads
3. **Lead Creation**: Creates new lead if not found
4. **Qualification**: AI agent analyzes lead data
5. **Scoring**: Assigns qualification score based on criteria
6. **Reporting**: Generates detailed qualification report

## 🎯 Use Cases

- **Real Estate Agencies**: Automate lead qualification process
- **Property Developers**: Manage prospect pipelines
- **Sales Teams**: Prioritize high-intent leads
- **CRM Optimization**: Enhance Salesforce workflows with AI

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- [CrewAI Documentation](https://docs.crewai.com/)
- [Salesforce API Documentation](https://developer.salesforce.com/docs/api-explorer/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)

## 📞 Support

For questions or issues, please open an issue on GitHub or contact the development team.