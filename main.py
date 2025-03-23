'''
Notes:
    The goal is to scrape the posts from hackernews with score greated than 100
    look at soup.select in the documentation, it could have made the work a lot easier
    Enumerate is used in lists when we want the elements of the list as well as the index of those items.
'''
import requests
from bs4 import BeautifulSoup
import sys
from jinja2 import Environment,FileSystemLoader,select_autoescape
import webbrowser
import os

class HNScraper():
    def __init__(self,pageCount):
        self.posts = []
        try:
            with requests.Session() as session:
                for page in range(1,pageCount+1):
                    response = session.get(f"https://news.ycombinator.com/?p={page}")
                    soup = BeautifulSoup(response.text,'html.parser')
                    self.posts.extend(self.scrape_stories(soup))
        except requests.exceptions.RequestException:
            sys.exit("Could not connect to hacker news. Please try again later.")


    def sort_stories(self):
        return sorted(self.posts,key=lambda key:key['votes'],reverse=True)

    def scrape_stories(self,soup):
        posts = []
        for vote_elem in soup.find_all('span',class_='score'):
            vote =int(vote_elem.text.split(' ')[0])
            if vote>=100:
                id_ = int(vote_elem.get('id').split('_')[1])
                row_with_score_greater_than_100 = soup.find(id=id_)
                for titleline in row_with_score_greater_than_100.find_all('span',class_="titleline"):
                    # to get only direct anchor children
                    for link in titleline.find_all('a',recursive=False):
                        posts.append({'title':link.text,'link':link.get('href',None),'votes':vote})
        return posts
    def create_webpage(self,links):
        env = Environment(
        loader=FileSystemLoader("./templates"),
        autoescape=select_autoescape()
        )
        template = env.get_template("index.html")
        rendered_html = template.render(links=links)
        with open("output.html","w",encoding="utf-8") as file:
            file.write(rendered_html)

if __name__=="__main__":
    page_count = int(input("Enter the number of pages you wish to scrape:"))
    scraper = HNScraper(page_count)
    posts = scraper.posts
    sorted_stories = scraper.sort_stories()
    scraper.create_webpage(sorted_stories)
    webbrowser.open("output.html")
