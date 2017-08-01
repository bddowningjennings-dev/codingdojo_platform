
import requests

# Set the request parameters
url = 'https://pokeapi.co/api/v2/pokemon/1'

# Fetch url
print "Fetching url.."

# Do the HTTP get request
response = requests.get(url, verify=True) #Verify is check SSL certificate

# Error handling

# Check for HTTP codes other than 200
if response.status_code != 200:
  print 'Status:', response.status_code, 'Problem with the request. Exiting.'
  exit()

# Decode the JSON response into a dictionary and use the data

data = response.json()

# visitors = data[0]['dates'][0]['items'][0]['value']

# print 'nVisitors today:', visitors
print 'This pokemans is: ', data['name'].upper()