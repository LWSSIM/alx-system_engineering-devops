# Let's delve deeper into using APIs with Python.

- This README provides an overview of APIs, REST APIs, microservices, data formats (CSV and JSON), and Python coding conventions relevant to implementing APIs in a Python web application.
---

## API Glossary

-Terms and concepts you will need along da waaaay!!

### What is an API?

An API (Application Programming Interface) defines a set of rules and protocols that allows different software applications to communicate with each other. It specifies how software components should interact.


### Bash Scripting Limitations

Bash scripting is powerful for automating tasks in a Unix-like environment. However, it's not suitable for complex applications or tasks requiring platform independence, advanced data processing, or extensive error handling. For web applications, Python or other high-level languages are more appropriate.


### What are Microservices?

Microservices is an architectural style where an application is composed of small, independently deployable services that work together. Each microservice focuses on a specific business function and communicates with others via APIs.


### CSV Format

CSV (Comma-Separated Values) is a plain text format used for storing tabular data. Each line in a CSV file represents a row, and columns are separated by commas.
```csv
Name, Age, City
John, 30, New York
Alice, 25, London
```

### JSON Format

JSON (JavaScript Object Notation) is a lightweight data interchange format. It is easy for humans to read and write and easy for machines to parse and generate. JSON represents data as key-value pairs and arrays.
```json
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```


### Pythonic Naming Conventions

Python follows PEP 8 conventions for naming:

Package and module names: lowercase_with_underscores
Class names: CapWords or CamelCase
Variable names: lowercase_with_underscores
Function names: lowercase_with_underscores
Constant names: UPPERCASE_WITH_UNDERSCORES
The use of CapWords or CamelCase for class names helps distinguish them from variables and functions.
[Python's PEP8](https://www.python.org/dev/peps/pep-0008/)


---


## Using REST APIs with Python

### 1. Requests Library

Python's `requests` library is commonly used for making HTTP requests, including interacting with REST APIs. You can install it via pip:

```bash
pip install requests
```

Here's a basic example of making a GET request to an API endpoint:

```python
import requests

url = 'https://api.example.com/data'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)
```

### 2. Authentication

Many APIs require authentication. You can include authentication credentials in your requests using various methods like basic authentication, API keys, OAuth, etc.

Example with API key:

```python
import requests

url = 'https://api.example.com/data'
headers = {'Authorization': 'Bearer YOUR_API_KEY'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)
```

### 3. Handling POST Requests

To send data to an API using POST requests, you can use the `post()` method:

```python
import requests

url = 'https://api.example.com/data'
data = {'key': 'value'}
response = requests.post(url, json=data)

if response.status_code == 200:
    print('Data posted successfully.')
else:
    print('Error:', response.status_code)
```

### 4. Error Handling

Always handle errors gracefully. Check the response status code and handle errors accordingly to prevent unexpected behavior in your application.

### 5. Using REST Frameworks

Frameworks like Flask or Django provide tools to easily create REST APIs in Python. Flask-RESTful and Django REST Framework are popular choices for building RESTful APIs with Python.

Example using Flask-RESTful:

```python
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
```

### 6. Documentation

Always refer to the API documentation for specific usage instructions, available endpoints, required parameters, authentication methods, and response formats.

### 7. Rate Limiting and Best Practices

Respect rate limits set by the API provider to avoid getting blocked. Follow best practices outlined in the API documentation to ensure efficient and reliable communication with the API.

### 8. Testing

Test your API requests thoroughly to ensure they behave as expected under different scenarios. Use tools like Postman or Swagger for manual testing and automated testing frameworks for regression testing.

### Resources

- [Requests Library Documentation](https://docs.python-requests.org/en/latest/)
- [Flask-RESTful Documentation](https://flask-restful.readthedocs.io/en/latest/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)

These are just some basic examples to get you started with using REST APIs in Python. Experiment with different APIs and explore more advanced features as you become more comfortable with the concepts.



