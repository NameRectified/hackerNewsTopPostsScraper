# HackerNews+ | Top Stories Scraper

## Overview
This script scrapes **Hacker News** and retrieves posts with **100+ votes**, then sorts them in descending order and generates a **basic HTML file** (Work in Progress) displaying the results.

## How It Works
1. Sends requests to **Hacker News** pages using `requests`.
2. Parses the HTML using `BeautifulSoup`.
3. Extracts **titles, links, and vote counts** for posts with **100+ votes**.
4. Sorts the posts in **descending order** based on votes.
5. **(Work in Progress)** Generates a **simple HTML file** (`hnPlus.html`) with the scraped data.

## Dependencies
- `requests` (for fetching web pages)
- `beautifulsoup4` (for parsing HTML)

## Installation
Run the following command to install the required dependencies:
```bash
pip install requests beautifulsoup4
```

## Usage
Run the script:
```bash
python main.py
```
When prompted enter the number of pages you wish to scrape.

Once the script completes, open **hnPlus.html** in a web browser to view the extracted posts.  
🚧 **Note:** The generated HTML file is a **Work in Progress** and may require further styling improvements.

