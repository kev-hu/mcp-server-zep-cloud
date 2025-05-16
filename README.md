# MCP Server for Zep Cloud

[![smithery badge](https://smithery.ai/badge/mcp-server-zep-cloud)](https://smithery.ai/protocol/mcp-server-zep-cloud)

MCP Server for Zep Cloud provides a bridge between LLM clients and the Zep Cloud API, enabling memory management for AI assistants.

## Overview

An MCP server for storing and retrieving user memories, preferences, procedures, and factual relationships through the Zep Cloud API. It acts as a semantic memory layer that enables AI assistants to maintain context about users across conversations.

## Tools

1. **User Management**:
   - `create_user`: Create a new user in Zep Cloud
   - `get_user`: Get details of a user
   - `update_user`: Update a user's metadata
   - `delete_user`: Delete a user
   - `list_users`: List all users

2. **Graph Operations**:
   - `search_graph`: Search a user's memory graph
   - `add_graph_data`: Add data to a user's memory graph

3. **Connectivity**:
   - `check_connection`: Check connection status with the Zep Cloud API

## Environment Variables

| Name | Description | Default Value |
|------|-------------|---------------|
| `ZEP_API_KEY` | API key for the Zep Cloud service | None |
| `MCP_HOST` | Host to bind the server to | `0.0.0.0` |
| `MCP_PORT` | Port to run the server on | `8080` |

## Installation

### Using Smithery

```bash
npx @smithery/cli install mcp-server-zep-cloud --client claude
```

### Manual Installation with Claude Desktop

1. Clone this repository:
```bash
git clone https://github.com/yourusername/mcp-server-zep-cloud.git
cd mcp-server-zep-cloud
```

2. Install dependencies:
```bash
pip install -r config/requirements.txt
```

3. Configure Claude Desktop by adding to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "zep-cloud": {
      "command": "python",
      "args": ["/path/to/mcp-server-zep-cloud/core/run_server.py"],
      "env": {
        "ZEP_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

The configuration file is located at:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

### Using Docker

A Dockerfile is available for building and running the MCP server:

```bash
# Build the container
docker build -t mcp-server-zep-cloud .

# Run the container
docker run -p 8080:8080 \
  -e ZEP_API_KEY="your-api-key" \
  mcp-server-zep-cloud
```

## Fallback Mode

If the server cannot connect to the Zep Cloud API, it automatically starts in fallback mode:

- All API operations are simulated and return success
- No actual data is sent to or received from the Zep Cloud API
- The server remains operational, allowing client integration to function
- Warning messages are logged to indicate fallback mode

## Repository Structure

- **core/**: Core functionality files
  - `zep_cloud_client.py`: Client implementation for the Zep Cloud API
  - `zep_cloud_server.py`: MCP server providing tools for API access
  - `run_server.py`: Standalone script to run the server directly

- **scripts/**: Utility scripts for operations and testing
  - `check_user_exists.py`: Utility to check if a user exists
  - `create_specific_user.py`: Script to create test users
  - `run_server.sh` / `run_server.bat`: Shell scripts to run the server

- **tests/**: Test scripts
  - `test_zep_cloud_client.py`: Unit tests for the Zep Cloud client
  - `test_server_initialization_fixes.py`: Tests for server initialization

- **config/**: Configuration files
  - `.env.example`: Template for environment configuration
  - `requirements.txt`: Package dependencies

## Security Considerations

- **API Key Protection**: Never commit your API key to version control
- **Environment Variables**: Use environment variables for sensitive data
- **Restricted Access**: Limit the server to trusted networks

## Support for Other Clients

This MCP server is designed to work with any MCP-compatible client. It has been tested with:

- Claude Desktop
- Claude in web browser

## Development

### Running Tests

```bash
cd tests
python test_zep_cloud_client.py
python test_server_initialization_fixes.py
```

### Running in Development Mode

```bash
cd scripts
./run_server.sh
```

## License

This MCP server is licensed under the MIT License.