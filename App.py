import html
import re
import urllib.parse
import urllib.request

# Control if whole response should be printed in the console or not
is_print_response_data = False  # Set to True for debugging purposes


def run_google_search():
    # Request input for search term from the user
    search_term = input("Please, enter the search term: ")
    print("\n")
    # Prepare the URL based on user's input
    url = construct_url(search_term)
    # Read the website
    response_data = get_response_data(url)
    # Parse response data and print out the results
    print("GOOGLE SEARCH RESULTS:\n")
    parse_response_data(response_data)


# Constructs the URL based on the search term
def construct_url(search_term):
    base_url = "https://google.com/search"
    parameters = {"q": search_term}
    data = urllib.parse.urlencode(parameters)
    full_url = base_url + "?" + data

    print("Parameters used in URL: " + data)
    print("Full URL with parameters: " + full_url)
    print("\n")

    return full_url


# Reads the data from the website and returns it as string
def get_response_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    request = urllib.request.Request(url, headers=headers, method="GET")
    response = urllib.request.urlopen(request)
    response_data = response.read().decode("UTF-8")  # Decode in UTF-8

    if is_print_response_data:
        print("Full response data: ")
        print(response_data)
        print("\n")

    return response_data


# Parses the response data and prints the title and links from the Google search
def parse_response_data(response_data):
    google_search_results = re.findall(r"<div class=\"r\">(.*?)</div>", str(response_data), flags=re.IGNORECASE)
    for search_result in google_search_results:
        title = parse_search_result_title(str(search_result))
        link = parse_search_result_link(str(search_result))
        print(title + " --> " + link)


# Gets the title from one search result entry
def parse_search_result_title(search_result):
    title = re.findall(r"<h3 class=\"LC20lb DKV0Md\">(.*?)</h3>", str(search_result), flags=re.IGNORECASE)[0]
    return html.unescape(str(title))  # Unescape HTML characters


# Gets the link from one search result entry
def parse_search_result_link(search_result):
    link = re.findall(r"<a href=\"(.*?)\"", search_result, flags=re.IGNORECASE)[0]
    return str(link)


# Run the program
run_google_search()
