import sys
from googlesearch import search

def google_search(query, num_results=5):
    try:
        results = search(query, num_results=num_results, stop=num_results)
        for i, result in enumerate(results, start=1):
            print(f"{i}. {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python googlesearch.py <query>")
        sys.exit(1)

    query = ' '.join(sys.argv[1:])
    google_search(query)

