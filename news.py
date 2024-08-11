import requests
from news_api_key import *  # Ensure 'key' is defined here

def news():
    # Define the API address and fetch the data
    api_address = "https://newsapi.org/v2/everything?q=keyword&apiKey=" + key
    json_data = requests.get(api_address).json()
    
    # Initialize an empty list for news items
    arr = []

    # Loop through the articles and append the first three
    for i in range(min(3, len(json_data["articles"]))):
        title = json_data["articles"][i]["title"]
        arr.append("number" + str(i+1) + ": " + title + ".")
    
    return arr
