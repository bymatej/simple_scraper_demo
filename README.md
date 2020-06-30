# Simple Scraper Demo
A simple web scraper used as a demo and for learning purposes.

## About
This is a console application.

Application takes search term as an input from the user, passes it on to Google and retrieves the search results.
The search result is parsed and printed out in the form `search_result_title --> search_result_link`. 

## Usage
The `App.py` needs to be run to run the program. 
To run it, this command needs to be executed in the terminal: `python App.py`

The program takes an input from the user. 
This input represents a search term passed to Google.
This prompt will be displayed: _Please, enter the search term_ 

After the search term is taken from the user, it is passed on to Google. 
Then, the search results are retrieved as a response. 
Search results are then parsed and printed out in the console in form of `search_result_title --> search_result_link`. 

At the top side of the `App.py` file there is one boolean variable called `is_print_response_data`.
It is used to control whether the whole response of the whole page will be printed out in the console or not. 

## Further improvements
Storing the output to a text file.

## Run the application in web browser
The App can be run in web browser on Repl.it

This is the link to the app: https://repl.it/@bymatej/simplescraperdemo#App.py
