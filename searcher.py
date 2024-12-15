import requests
import csv

# Google Custom Search API credentials
API_KEY = "your_api_key"
SEARCH_ENGINE_ID = "your_search_engine_id"

def search_google(query, api_key, search_engine_id, num_results=10):
    """
    Query Google Custom Search API.
    """
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": search_engine_id,
        "num": num_results,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def save_to_csv(data, filename="safety_websites.csv"):
    """
    Save the search results to a CSV file.
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "URL", "Description"])  # Header
        for entry in data:
            writer.writerow([entry["title"], entry["url"], entry["description"]])

def main():
    # Keywords to search
    queries = ["safety regulations", "fire safety", "workplace safety"]
    all_results = []

    for query in queries:
        print(f"Searching for: {query}")
        results = search_google(query, API_KEY, SEARCH_ENGINE_ID)
        if results and "items" in results:
            for item in results["items"]:
                all_results.append({
                    "title": item.get("title"),
                    "url": item.get("link"),
                    "description": item.get("snippet", "")
                })
    
    if all_results:
        print("Saving results to CSV...")
        save_to_csv(all_results)
        print(f"CSV file created with {len(all_results)} entries.")
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
