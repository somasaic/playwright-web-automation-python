from playwright.sync_api import sync_playwright
import json

def scrape_single_site():
    result = {
        "theater_name": "Demo Cinema",
        "movies": []
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://example.com", wait_until="domcontentloaded")

        # Demo logic – simulate extraction
        movie = {
            "movie_name": "Sample Movie",
            "category": "Action",
            "showtimes": [
                {
                    "date": "2025-01-20",
                    "times": [
                        {
                            "time": "18:30",
                            "format": "Standard",
                            "booking_url": "https://example.com/book"
                        }
                    ]
                }
            ]
        }

        result["movies"].append(movie)
        browser.close()

    with open("data/sample_output_events.json", "w") as f:
        json.dump(result, f, indent=4)

if __name__ == "__main__":
    scrape_single_site()
