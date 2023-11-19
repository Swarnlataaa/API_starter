import requests

# Define the API endpoint URL
api_url = "https://jsonplaceholder.typicode.com/posts"

# Send an HTTP GET request to the API endpoint
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Display the first few posts
    for post in data[:5]:
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print()
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
