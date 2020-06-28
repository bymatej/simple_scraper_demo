import urllib.request
import urllib.parse

url = "https://google.com/search"
parameters = {"q": "python"}
data = urllib.parse.urlencode(parameters)
requested_data = data.encode("utf-8")
request = urllib.request.Request(url, requested_data)
response = urllib.request.urlopen(request)
response_data = response.read()
print(response_data)
