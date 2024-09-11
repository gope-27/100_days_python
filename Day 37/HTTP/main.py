import requests
from datetime import datetime

USERNAME = "gopinath27"
TOKEN = "asdfghjkl"
GRAPH_ID = "studychart"  # You need to define your GRAPH_ID

# Define the endpoint
pixela_endpoint = "https://pixe.la/v1/users"

# User creation (already commented out)
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create Graph Endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Study Tracker",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Graph creation (already commented out)
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Pixel creation endpoint
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

# Get input from user (make sure it is a numerical value)
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many study commits did you complete today? "),  # Input should be numerical
}

# Make sure the input is a valid integer before sending the request
if pixel_data["quantity"].isdigit():
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    print(response.text)
else:
    print("Invalid quantity. Please enter a valid number.")

# Update pixel data endpoint
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "5"  # Update the quantity with the correct number (not 'yes')
}

# Pixel update (commented out)
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Delete pixel data endpoint
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# Pixel deletion (commented out)
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
