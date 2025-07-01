# **HackerNews+ | Top Stories Scraper**  

## **Overview**  
**HackerNews+** is a Python-based web scraper that extracts **top-voted stories** (100+ points) from **Hacker News** and generates a webpage displaying the results.  

## **Features**  
Scrapes multiple pages of Hacker News  
Filters stories with **100+ votes**  
Sorts stories in **descending order** by vote count  
Generates a **styled HTML file** (`output.html`)  
Automatically opens the generated page in a browser  

---

## **How It Works**  
1. Sends requests to **Hacker News** pages using `requests`.  
2. Parses the HTML using `BeautifulSoup`.  
3. Extracts **titles, links, and vote counts** for posts with **100+ votes**.  
4. Sorts the posts in **descending order** based on votes.  
5. Uses **Jinja2** templating to dynamically create an HTML page.  
6. Applies **CSS styling** for better readability.  
7. Opens the generated webpage automatically after execution.  

---

## **Installation**  
Ensure you have Python **3.x** installed.  
Then, install the required dependencies:  

```bash
pip install requests beautifulsoup4 jinja2
```

---

## **Usage**  
Run the script by executing the following command:  

```bash
python main.py
```

When prompted, enter the **number of pages** you wish to scrape.  

- The script will fetch and process the Hacker News posts.  
- A new file, **output.html**, will be created with the extracted stories.  
- The file will **automatically open** in your default web browser.  

---

## **Customization**  
You can modify the **HTML template** (`templates/index.html`) and **CSS styles** (`static/style.css`) to enhance the appearance of the generated page.  

---
  

