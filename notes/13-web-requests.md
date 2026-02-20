# 13: Working with HTTP Endpoints and Web APIs

## Why this matters

Most modern applications communicate with web services and APIs. Understanding HTTP requests and responses is essential for:
- Fetching data from remote servers
- Integrating with third-party services
- Building applications that use external data
- Understanding how the web works

Good HTTP handling gives you:
- Access to vast amounts of data and services
- Real-time information (weather, news, prices)
- Integration with cloud services
- Building distributed applications

---

## 1) Understanding HTTP Requests and Responses

### The HTTP Cycle

Every web interaction follows this pattern:

**Request → Response**

The client sends a **request** to a server, and the server sends back a **response**.

### Components of an HTTP Request

An HTTP request contains:

- **Method**: The action to perform
  - `GET` - Retrieve data (most common)
  - `POST` - Send/create data
  - `PUT` - Update data
  - `PATCH` - Partial update
  - `DELETE` - Remove data

- **URL**: The address of the resource
  - Example: `https://www.bbc.co.uk/news`
  - Example: `https://restcountries.com/v3.1/name/united%20kingdom`

- **Protocol**: Communication protocol
  - `https` - Secure (encrypted)
  - `http` - Insecure (not encrypted)

- **Query Parameters**: Additional data in URL
  - Example: `?search=term&limit=10`
  - Key-value pairs after `?`

- **Headers**: Metadata about the request
  - Content type, authentication tokens, user agent
  - Example: `{"Authorization": "Bearer token123"}`

- **Body**: Data sent with request (for POST/PUT/PATCH)
  - Usually JSON format
  - Example: `{"name": "John", "email": "john@example.com"}`

### Components of an HTTP Response

The server responds with:

- **Status Code**: Numeric code indicating result
  - `200` - Success (OK)
  - `404` - Not Found
  - `400` - Bad Request (user error)
  - `500` - Server Error

- **Status Text**: Human-readable message
  - "OK", "Not Found", "Bad Request"

- **Headers**: Response metadata
  - Content type, caching instructions

- **Body**: The actual data returned
  - Usually JSON, HTML, or XML
  - Contains the information you requested

### Common Error Status Codes

- **400 - Bad Request**: User did something wrong (invalid data, malformed request)
- **404 - Not Found**: The requested resource doesn't exist
- **500 - Internal Server Error**: Server had a problem

---

## 2) Installing and Using the `requests` Library

### What is `requests`?

The `requests` library is the standard Python library for making HTTP requests. It's simple, powerful, and widely used.

### Installation

```bash
pip install requests
```

### Basic GET Request

```python
import requests

# Make a GET request
response = requests.get("https://restcountries.com/v3.1/name/united%20kingdom")

# Check the response
print(response)  # <Response [200]>
print(response.status_code)  # 200
```

### Understanding the Response Object

The `response` object contains:
- `response.status_code` - HTTP status code (200, 404, etc.)
- `response.text` - Response body as text
- `response.json()` - Parse JSON response to Python dict
- `response.headers` - Response headers
- `response.url` - Final URL (after redirects)

---

## 3) Making Your First HTTP Request

### Basic Example

```python
import requests

# Make request to REST Countries API
url = "https://restcountries.com/v3.1/name/united%20kingdom"
response = requests.get(url)

# Check if successful
if response.status_code == 200:
    data = response.json()
    print(f"Country: {data[0]['name']['common']}")
    print(f"Capital: {data[0]['capital'][0]}")
else:
    print(f"Error: {response.status_code}")
```

### Using `raise_for_status()`

Better approach - raises exception for bad status codes:

```python
import requests

try:
    response = requests.get("https://restcountries.com/v3.1/name/france")
    response.raise_for_status()  # Raises exception if status code is 4xx or 5xx
    data = response.json()
    print(f"Country: {data[0]['name']['common']}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")
```

### Key Points:

- `requests.get(url)` makes a GET request
- `response.raise_for_status()` checks for errors
- `response.json()` parses JSON to Python dict
- Always handle exceptions

---

## 4) Working with Query Parameters

### What are Query Parameters?

Query parameters add data to URLs:
- Format: `?key1=value1&key2=value2`
- Used for filtering, searching, pagination

### Using `params` Parameter

The `requests` library handles URL encoding automatically:

```python
import requests

# Method 1: Using params (recommended)
response = requests.get(
    "https://restcountries.com/v3.1/name/united",
    params={"fullText": "false"}  # Adds ?fullText=false
)

# Method 2: Building URL manually (not recommended)
url = "https://restcountries.com/v3.1/name/united?fullText=false"
response = requests.get(url)
```

### Multiple Parameters

```python
import requests

# Multiple query parameters
response = requests.get(
    "https://restcountries.com/v3.1/all",
    params={
        "fields": "name,capital,population",
        "limit": 10
    }
)
# URL becomes: https://restcountries.com/v3.1/all?fields=name,capital,population&limit=10

data = response.json()
for country in data[:5]:  # First 5 countries
    print(f"{country['name']['common']}: {country.get('capital', ['N/A'])[0]}")
```

### Key Points:

- Use `params` dictionary for query parameters
- `requests` handles URL encoding automatically
- Multiple parameters separated by `&`
- Check API documentation for available parameters

---

## 5) Parsing JSON Responses

### Understanding JSON

JSON (JavaScript Object Notation) is the standard format for API responses:
- Looks like Python dictionaries
- Easy to parse and work with

### Parsing JSON

```python
import requests
import json

response = requests.get("https://restcountries.com/v3.1/name/germany")
response.raise_for_status()

# Parse JSON to Python dict
data = response.json()

# Access nested data
country_name = data[0]['name']['common']
capital = data[0]['capital'][0]
population = data[0]['population']

print(f"{country_name}: {capital} (Population: {population:,})")
```

### Working with Nested Data

```python
import requests

response = requests.get("https://restcountries.com/v3.1/name/japan")
data = response.json()

country = data[0]

# Nested access
name = country['name']['common']  # Nested dict
languages = list(country['languages'].values())  # Convert dict values to list
currencies = list(country['currencies'].keys())  # Get currency codes

print(f"Country: {name}")
print(f"Languages: {', '.join(languages)}")
print(f"Currencies: {', '.join(currencies)}")
```

### Safe Access with `.get()`

Always use `.get()` to avoid KeyError:

```python
import requests

response = requests.get("https://restcountries.com/v3.1/name/monaco")
data = response.json()

country = data[0]

# Safe access with default values
capital = country.get('capital', ['Unknown'])[0]  # Default if missing
region = country.get('region', 'Unknown')
population = country.get('population', 0)

print(f"Capital: {capital}")
print(f"Region: {region}")
print(f"Population: {population:,}")
```

---

## 6) Error Handling

### Common HTTP Errors

Different errors require different handling:

```python
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError

def fetch_country(name):
    """Fetch country data with comprehensive error handling."""
    url = "https://restcountries.com/v3.1/name/" + name
    
    try:
        response = requests.get(url, timeout=10)
        
        # Check status code
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("Country not found")
            return None
        else:
            print(f"Unexpected status code: {response.status_code}")
            return None
            
    except Timeout:
        print("Request timed out - server took too long")
        return None
    except ConnectionError:
        print("Connection error - check your internet connection")
        return None
    except RequestException as e:
        print(f"Request error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Usage
data = fetch_country("france")
if data:
    print(f"Found: {data[0]['name']['common']}")
```

### Exception Types

- **`requests.exceptions.Timeout`**: Request took too long
- **`requests.exceptions.ConnectionError`**: Can't connect to server
- **`requests.exceptions.HTTPError`**: Bad HTTP status code (4xx, 5xx)
- **`requests.exceptions.RequestException`**: Base class for all request errors

### Adding Timeouts

Always add timeouts to prevent hanging:

```python
import requests

# Timeout after 10 seconds
response = requests.get("https://restcountries.com/v3.1/name/spain", timeout=10)

# Separate connect and read timeouts
response = requests.get(
    "https://restcountries.com/v3.1/name/italy",
    timeout=(5, 10)  # (connect timeout, read timeout)
)
```

---

## 7) Working with Request Headers

### What are Headers?

Headers provide metadata about requests:
- Authentication tokens
- Content type
- User agent
- Custom headers

### Setting Headers

```python
import requests

headers = {
    "User-Agent": "MyApp/1.0",
    "Accept": "application/json",
    "Authorization": "Bearer your-token-here"
}

response = requests.get(
    "https://api.example.com/data",
    headers=headers
)
```

### Common Headers

- **`User-Agent`**: Identifies your application
- **`Authorization`**: Authentication token
- **`Content-Type`**: Type of data being sent
- **`Accept`**: What response format you want

---

## 8) Sending Data with POST Requests

### POST vs GET

- **GET**: Retrieve data (no body, parameters in URL)
- **POST**: Send/create data (has body, data in request)

### Sending JSON Data

```python
import requests

# Data to send
data = {
    "name": "John Doe",
    "email": "john@example.com"
}

# POST request with JSON body
response = requests.post(
    "https://httpbin.org/post",
    json=data  # Automatically sets Content-Type and serializes JSON
)

print(response.status_code)  # 200
result = response.json()
print(result['json'])  # Shows the data we sent
```

### Alternative: Manual JSON

```python
import requests
import json

data = {"name": "Jane", "email": "jane@example.com"}

response = requests.post(
    "https://httpbin.org/post",
    data=json.dumps(data),  # Manual JSON string
    headers={"Content-Type": "application/json"}
)
```

### Key Points:

- Use `json=` parameter for automatic JSON handling
- `requests` sets `Content-Type: application/json` automatically
- POST requests have a body (unlike GET)

---

## 9) Processing API Responses

### Extracting and Transforming Data

```python
import requests

def get_country_info(country_name):
    """Fetch and process country information."""
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if not data:
            return None
        
        country = data[0]
        
        # Extract and format data
        info = {
            "name": country['name']['common'],
            "capital": country.get('capital', ['Unknown'])[0],
            "population": country.get('population', 0),
            "region": country.get('region', 'Unknown'),
            "area": country.get('area', 0)
        }
        
        return info
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Usage
info = get_country_info("canada")
if info:
    print(f"Name: {info['name']}")
    print(f"Capital: {info['capital']}")
    print(f"Population: {info['population']:,}")
```

### Working with Lists

Many APIs return lists of results:

```python
import requests

def list_european_countries():
    """Get all European countries."""
    url = "https://restcountries.com/v3.1/region/europe"
    
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    countries = response.json()
    
    # Process list
    for country in countries[:10]:  # First 10
        name = country['name']['common']
        capital = country.get('capital', ['N/A'])[0]
        print(f"{name}: {capital}")

list_european_countries()
```

---

## 10) Building an API Client Class

### Organizing API Code

Create a class to encapsulate API functionality:

```python
import requests
from requests.exceptions import RequestException

class CountryAPIClient:
    """Client for REST Countries API."""
    
    def __init__(self):
        """Initialize the API client."""
        self.base_url = "https://restcountries.com/v3.1"
    
    def get_country(self, name):
        """Get country by name."""
        url = f"{self.base_url}/name/{name}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data[0] if data else None
        except RequestException as e:
            print(f"Error: {e}")
            return None
    
    def search_by_region(self, region):
        """Get all countries in a region."""
        url = f"{self.base_url}/region/{region}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error: {e}")
            return []
    
    def get_capital(self, country_name):
        """Get capital city of a country."""
        country = self.get_country(country_name)
        if country:
            capitals = country.get('capital', [])
            return capitals[0] if capitals else None
        return None

# Usage
client = CountryAPIClient()

france = client.get_country("france")
if france:
    print(f"Country: {france['name']['common']}")

capital = client.get_capital("japan")
print(f"Capital: {capital}")

european_countries = client.search_by_region("europe")
print(f"Found {len(european_countries)} European countries")
```

### Benefits of a Client Class:

- **Organization**: All API code in one place
- **Reusability**: Methods can be called multiple times
- **Maintainability**: Easy to update if API changes
- **Encapsulation**: Hides implementation details

---

## 11) Saving API Responses to Files

### Caching API Responses

Save responses to avoid repeated requests:

```python
import requests
import json
from pathlib import Path

def get_country_data(country_name, cache_dir="cache"):
    """Fetch country data, using cache if available."""
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(exist_ok=True)
    
    cache_file = cache_dir / f"{country_name}.json"
    
    # Check cache first
    if cache_file.exists():
        print(f"Loading from cache: {country_name}")
        with open(cache_file) as f:
            return json.load(f)
    
    # Fetch from API
    print(f"Fetching from API: {country_name}")
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    
    # Save to cache
    with open(cache_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    return data

# Usage
data = get_country_data("brazil")
print(f"Country: {data[0]['name']['common']}")

# Second call uses cache
data = get_country_data("brazil")
```

### Downloading Files

```python
import requests

def download_file(url, filename):
    """Download a file from URL."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Write binary data
        with open(filename, 'wb') as f:  # 'wb' for binary
            f.write(response.content)
        
        print(f"Downloaded: {filename}")
        return True
    except RequestException as e:
        print(f"Download error: {e}")
        return False

# Usage
download_file(
    "https://example.com/data.csv",
    "data.csv"
)
```

---

## 12) What We Covered

1. **HTTP basics** - Request/response cycle, components
2. **`requests` library** - Making HTTP requests in Python
3. **GET requests** - Fetching data from APIs
4. **Query parameters** - Filtering and searching
5. **JSON parsing** - Working with API responses
6. **Error handling** - Handling timeouts, connection errors, status codes
7. **Headers** - Setting request metadata
8. **POST requests** - Sending data to APIs
9. **Data processing** - Extracting and transforming API data
10. **API client classes** - Organizing API code
11. **File operations** - Caching and downloading

---

## 13) Key Takeaways

1. **HTTP is request/response** - Client sends request, server sends response
2. **Use `requests` library** - Standard Python library for HTTP
3. **GET for retrieving** - Most common, no body
4. **POST for sending** - Has body, sends data
5. **Query parameters** - Use `params` dictionary
6. **Parse JSON** - Use `response.json()` to get Python dict
7. **Handle errors** - Timeouts, connection errors, status codes
8. **Add timeouts** - Prevent hanging requests
9. **Use `.get()`** - Safe dictionary access
10. **Organize with classes** - Create API client classes

---

## 14) Practice Exercises

1. Fetch data from REST Countries API for 5 different countries
2. Create a function that searches countries by region
3. Build an API client class for a different API (e.g., BoredAPI)
4. Add error handling with timeouts and retries
5. Cache API responses to files

---

## Summary

HTTP requests let you interact with web APIs and services. The `requests` library makes this simple:
- **GET requests** retrieve data
- **POST requests** send data
- **Query parameters** filter results
- **JSON responses** parse to Python dicts
- **Error handling** ensures robustness

Remember: Always handle errors, add timeouts, and use `.get()` for safe dictionary access!

---

## 60-Second Recap

- **HTTP is request/response** - Client requests, server responds
- **`requests` library** - Standard Python HTTP library
- **GET retrieves data** - Most common request type
- **POST sends data** - Has body with JSON
- **Query parameters** - Use `params` dictionary
- **Parse JSON** - `response.json()` gives Python dict
- **Handle errors** - Timeouts, connection errors, status codes
- **Add timeouts** - Prevent hanging requests
- **Status codes matter** - 200=OK, 404=Not Found, 400=Bad Request
- **Use `.get()` safely** - Avoid KeyError exceptions

---

## Mini Q&A

**Q: What is HTTP?**  
A: Hypertext Transfer Protocol - the standard way clients and servers communicate on the web.

**Q: What's the difference between GET and POST?**  
A: GET retrieves data (no body), POST sends data (has body). GET is for reading, POST is for creating/sending.

**Q: How do I add query parameters?**  
A: Use the `params` dictionary: `requests.get(url, params={"key": "value"})`

**Q: What does `response.json()` do?**  
A: Parses the JSON response body into a Python dictionary.

**Q: How do I handle errors?**  
A: Use try/except with `requests.exceptions.RequestException`, check `response.status_code`, and use `response.raise_for_status()`.

**Q: What is a timeout?**  
A: Maximum time to wait for a response. Prevents requests from hanging indefinitely.

**Q: Why use `.get()` instead of `[]` for dictionaries?**  
A: `.get()` returns `None` if key doesn't exist, `[]` raises `KeyError`. Safer for API data.

**Q: What are HTTP status codes?**  
A: Numeric codes indicating request result: 200=OK, 404=Not Found, 400=Bad Request, 500=Server Error.

**Q: Can I send data with GET requests?**  
A: Only via query parameters in the URL. For larger data, use POST with a JSON body.

**Q: How do I set request headers?**  
A: Use `headers` parameter: `requests.get(url, headers={"Header-Name": "value"})`

**Q: What is JSON?**  
A: JavaScript Object Notation - a text format for data exchange. Looks like Python dictionaries.

**Q: Should I cache API responses?**  
A: Yes, if you make repeated requests. Saves time and reduces server load.

**Q: How do I download files?**  
A: Use `response.content` (binary data) and write with `'wb'` mode: `file.write(response.content)`
