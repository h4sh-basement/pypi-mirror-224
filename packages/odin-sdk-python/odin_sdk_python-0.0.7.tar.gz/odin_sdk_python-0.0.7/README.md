# Odin SDK for Python

Odin offers precise internet insights to infosec teams, enhancing security by proactively spotting threats in their attack surface. It scans the entire IPv4, identifying 100+ public services and creating a comprehensive inventory of hosts, domains, certificates, and more. With in-depth scanning of sensitive ports and detailed service analysis, Odin provides unparalleled understanding of an organization's online presence.


The Odin SDK for Python allows you to easily interact with the [Odin API](https://getodin.com/docs/api) and access various cybersecurity services, certificate information, and more.

## Installation

To use the Odin SDK in your Python project, you need to install it using pip:

```bash
pip install odin-sdk-python
```

## Examples

In the "example.py", you can find various usage examples demonstrating how to interact with the Odin API using the `odin-sdk-python` package.

Each example is a standalone Python program that showcases specific functionalities of the SDK.

```python
from odin import OdinClient, APIException

client = OdinClient("https://api.getodin.com/v1", "<APIKey>")

def ex_hosts_count():
    # Example for using get_hosts_count
    try:
        response = client.get_hosts_count("string")
        print(response.success)
        print(response.data.count)
        
    except APIException as e:
        print(e.status_code)
        print(e.message)
```

Make sure to replace `<APIKey>` with your actual Odin API key. 


Thank you for using the Odin SDK for Go. If you encounter any issues, find a bug, or want to contribute, feel free to open an issue or submit a pull request. Your feedback and contributions are highly appreciated!

For more information about our other projects and services, visit our website at https://www.getodin.com.