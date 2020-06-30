import urllib.request
import urllib.parse
import re

url = "https://ut.abfackeln.com/asu.html"
parameters = {"page": "install"}
data = urllib.parse.urlencode(parameters)
# requested_data = data.encode("utf-8")
print(data)
full_url = url + "?" + data
print(full_url)

request = urllib.request.Request(full_url)
response = urllib.request.urlopen(request)
response_data = response.read()
print(response_data)

text_in_li_tags = re.findall(r"", str(response_data), re.IGNORECASE)
print(text_in_li_tags)
