import json
import webbrowser


# Function to read URLs from a JSON file
def read_urls_from_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


# Function to open URLs using the webbrowser module
def open_urls(urls_by_group):
    for group_name, urls in urls_by_group.items():
        for url in urls:
            webbrowser.open_new_tab(url)


# JSON file path
json_file_path = "urls.json"

# Reading URLs from JSON file
urls_by_group = read_urls_from_json(json_file_path)

# Opening URLs using the webbrowser module
open_urls(urls_by_group)
