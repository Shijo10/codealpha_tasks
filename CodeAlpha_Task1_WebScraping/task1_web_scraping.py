# ============================================================
# CODEALPHA INTERNSHIP — TASK 1: Web Scraping
# Target: https://books.toscrape.com (legal practice site)
# Scrapes: Book titles, prices, ratings, availability
# Author: CodeAlpha Intern
# ============================================================

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# ─────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────
BASE_URL = "https://books.toscrape.com/catalogue/"
START_URL = "https://books.toscrape.com/catalogue/page-1.html"
MAX_PAGES = 5          # Scrape first 5 pages (50 books)
OUTPUT_FILE = "scraped_books.csv"

RATING_MAP = {
    "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

# ─────────────────────────────────────────
# SCRAPER FUNCTIONS
# ─────────────────────────────────────────

def get_page(url):
    """Fetch a page and return BeautifulSoup object."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as e:
        print(f"  ⚠️  Error fetching {url}: {e}")
        return None


def parse_books(soup):
    """Extract book data from a single page."""
    books = []
    articles = soup.find_all("article", class_="product_pod")

    for article in articles:
        # Title
        title = article.find("h3").find("a")["title"]

        # Price
        price = article.find("p", class_="price_color").text.strip()
        price_clean = float(price.replace("£", "").replace("Â", "").strip())

        # Star rating
        rating_word = article.find("p", class_="star-rating")["class"][1]
        rating = RATING_MAP.get(rating_word, 0)

        # Availability
        availability = article.find("p", class_="instock availability")
        in_stock = "In Stock" if availability and "In stock" in availability.text else "Out of Stock"

        # Book URL
        book_url = BASE_URL + article.find("h3").find("a")["href"].replace("../", "")

        books.append({
            "Title": title,
            "Price (£)": price_clean,
            "Rating (1-5)": rating,
            "Availability": in_stock,
            "URL": book_url
        })

    return books


def get_next_page(soup):
    """Get URL of the next page if it exists."""
    next_btn = soup.find("li", class_="next")
    if next_btn:
        return BASE_URL + next_btn.find("a")["href"]
    return None


# ─────────────────────────────────────────
# MAIN SCRAPER
# ─────────────────────────────────────────

def main():
    print("=" * 55)
    print("   CODEALPHA — TASK 1: Web Scraping")
    print("   Target: books.toscrape.com")
    print("=" * 55)

    all_books = []
    url = START_URL
    page_num = 1

    while url and page_num <= MAX_PAGES:
        print(f"\n📄 Scraping page {page_num}/{MAX_PAGES} — {url}")
        soup = get_page(url)

        if not soup:
            print("  ⚠️  Skipping page due to error.")
            break

        books = parse_books(soup)
        all_books.extend(books)
        print(f"  ✅ Collected {len(books)} books (Total: {len(all_books)})")

        url = get_next_page(soup)
        page_num += 1
        time.sleep(1)   # Be polite — don't hammer the server

    # ─────────────────────────────────────
    # SAVE TO CSV
    # ─────────────────────────────────────
    df = pd.DataFrame(all_books)

    print("\n" + "=" * 55)
    print("📊 SCRAPED DATA SUMMARY")
    print("=" * 55)
    print(f"\n  Total books scraped : {len(df)}")
    print(f"  Pages scraped       : {page_num - 1}")
    print(f"  Avg price           : £{df['Price (£)'].mean():.2f}")
    print(f"  Cheapest book       : £{df['Price (£)'].min():.2f}")
    print(f"  Most expensive      : £{df['Price (£)'].max():.2f}")
    print(f"  Avg rating          : {df['Rating (1-5)'].mean():.1f} / 5")
    print(f"  In stock            : {(df['Availability'] == 'In Stock').sum()} books")

    print("\n📌 Rating Distribution:")
    print(df['Rating (1-5)'].value_counts().sort_index().to_string())

    print("\n📌 Top 5 Highest Rated Books:")
    top = df.sort_values(['Rating (1-5)', 'Price (£)'], ascending=[False, True]).head(5)
    for _, row in top.iterrows():
        print(f"  ⭐ {row['Rating (1-5)']} | £{row['Price (£)']:.2f} | {row['Title'][:50]}")

    print("\n📌 Top 5 Cheapest Books:")
    cheap = df.sort_values('Price (£)').head(5)
    for _, row in cheap.iterrows():
        print(f"  💰 £{row['Price (£)']:.2f} | ⭐{row['Rating (1-5)']} | {row['Title'][:50]}")

    # Save CSV
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n✅ Data saved to: {OUTPUT_FILE}")
    print("\n✅ Task 1 — Web Scraping Complete!\n")

    return df


if __name__ == "__main__":
    main()
