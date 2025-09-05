# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Environment Setup
```bash
# Install Python 3.13.0 and activate
pyenv install 3.13.0
pyenv shell 3.13.0

# Install Poetry and dependencies
curl -sSL https://install.python-poetry.org | python3
poetry env use ~/.pyenv/versions/3.13.0/bin/python
poetry install
```

### Testing
```bash
# Run all tests
poetry run pytest

# Check test discovery
poetry run pytest --collect-only

# Run specific test files
poetry run pytest tests/test_auth.py
poetry run pytest tests/device/test_get_device.py
```

### Code Quality
```bash
# Run linter
poetry run ruff check

# Format code
poetry run ruff format
```

### Build and Package
```bash
# Build the package
poetry build

# Publish to test PyPI (requires token setup)
poetry build
poetry publish --repository test-pypi
```

## Architecture Overview

This is a Python library that wraps the SOTI MobiControl REST API for managing mobile devices, profiles, and packages.

### Core Components

- **`SotiApiClient`** (`soti_mobicontrol_python/SotiApiClient.py`): Main API client class that handles HTTP requests (GET, POST, PUT, DELETE) to the SOTI MobiControl API
- **`Auth`** (`soti_mobicontrol_python/auth.py`): Manages OAuth2 authentication with automatic token refresh using client credentials and user password
- **`SotiMobiControlServerConfig`** (`soti_mobicontrol_python/soti_mobicontrol_config.py`): Configuration dataclass for server connection details (FQDN, clientId, clientSecret, username, password)

### API Endpoint Structure

Endpoints are organized by functionality in the `endpoints/` directory:
- **Device Management**: `endpoints/device/` - Device operations, attributes, certificates, users, actions, rename
- **Device Groups**: `endpoints/devicegroups/` - Group membership and management
- **Security**: `endpoints/security/` - User management  
- **Servers**: `endpoints/servers/` - Health checks and server info

### Key Patterns

1. **Async HTTP Client**: Uses `httpx.AsyncClient` for all API communications
2. **Authentication Flow**: Client credentials + password grant type with automatic token refresh
3. **Base URL Construction**: `https://{FQDN}/MobiControl/api` + endpoint
4. **Error Handling**: Uses `response.raise_for_status()` for HTTP error handling
5. **Headers**: All requests include `Authorization: Bearer {token}` and `accept: application/json`

### Testing Structure

- Tests mirror the endpoint structure under `tests/`
- Uses `pytest` with `@pytest.mark.vcr()` for API interaction recording
- Integration tests require live SOTI MobiControl server credentials
- Test configuration handled via `tests/helper/config.py`

### Helper Modules

- **`helper/device_id.py`**: Device ID utilities and parsing
- **`helper/path.py`**: Path handling for API endpoints

### Dependencies

- **httpx**: Async HTTP client for API requests  
- **anyio**: Async I/O support
- **pytest + pytest-asyncio**: Testing framework with async support
- **ruff**: Linting and code formatting