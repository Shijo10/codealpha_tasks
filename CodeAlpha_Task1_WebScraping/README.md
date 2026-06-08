# 🕸️ Task 1 — Web Scraping

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Scraping-green?style=flat-square)
![Requests](https://img.shields.io/badge/Requests-HTTP-orange?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Storage-150458?style=flat-square&logo=pandas)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

> **CodeAlpha Data Analytics Internship — Task 1**

---

## 📌 Objective

Build a web scraper using **Python + BeautifulSoup** to extract book data from [books.toscrape.com](https://books.toscrape.com) — a legal, public practice site designed for scraping exercises.

The scraper collects:
- 📖 Book titles
- 💰 Prices
- ⭐ Star ratings
- 📦 Availability (In Stock / Out of Stock)
- 🔗 Book URLs

---

## 📂 Files

| File | Description |
|---|---|
| `task1_web_scraping.py` | Main scraper script |
| `scraped_books.csv` | Output dataset (generated on run) |
| `README.md` | Task documentation |

---

## 🌐 Target Website

| Detail | Value |
|---|---|
| **URL** | https://books.toscrape.com |
| **Type** | Public practice site (legal to scrape) |
| **Pages scraped** | 5 pages (50 books) |
| **Data points** | Title, Price, Rating, Availability, URL |

---

## ⚙️ How to Run

```bash
# Install dependencies
pip install requests beautifulsoup4 pandas

# Run the scraper
python task1_web_scraping.py
```

The script will:
1. Scrape 5 pages of books (50 books total)
2. Print a full summary in the terminal
3. Save all data to `scraped_books.csv`

---

## 📊 Sample Output

```
Total books scraped : 50
Pages scraped       : 5
Avg price           : £35.24
Cheapest book       : £10.00
Most expensive      : £59.69
Avg rating          : 3.0 / 5
In stock            : 50 books
```

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `requests` | HTTP GET requests to fetch web pages |
| `BeautifulSoup4` | Parse HTML and extract data |
| `pandas` | Store and export data to CSV |
| `time` | Polite delay between requests |

---

## 🔍 How It Works

```
Start URL
   ↓
Fetch page HTML (requests)
   ↓
Parse HTML (BeautifulSoup)
   ↓
Extract: title, price, rating, availability
   ↓
Follow "next page" link
   ↓
Repeat for 5 pages
   ↓
Save to CSV (pandas)
```

---

## 📋 CSV Output Columns

| Column | Type | Description |
|---|---|---|
| Title | str | Full book title |
| Price (£) | float | Price in GBP |
| Rating (1-5) | int | Star rating |
| Availability | str | In Stock / Out of Stock |
| URL | str | Direct link to book page |

---

> 📁 Part of [CodeAlpha_DataAnalytics](../README.md) repository
