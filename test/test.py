import requests

# Open the file in binary mode
with open('Tes.pdf', 'rb') as file:
    # Send a POST request with the file
    resp = requests.post("https://transtableextractor.vercel.app", files={'file': file})

# Print the response status code
print("Status Code:", resp.status_code)

# Check if the response is in JSON format
try:
    # Attempt to parse the response as JSON
    response_data = resp.json()
    print("Response JSON:", response_data)
except ValueError:
    # If response is not JSON, print the raw text
    print("Response Text:", resp.text)



