'''
    The goal is to scrape the posts from hackernews with score greated than 100
    look at soup.select in the documentation, it could have made the work a lot easier
    Enumerate is used in lists when we want the elements of the list as well as the index of those items.
'''
import requests
from bs4 import BeautifulSoup
import pprint # for better printing

def sort_stories(dict):
    return sorted(dict,key=lambda key:key['votes'],reverse=True)
    # return sorted(dict,key=lambda key:key[1]['votes'])
    # return dict[votes]
posts = []
def story_scraper():
    for score_elem in  soup.find_all('span',class_='score'):
        score =int(score_elem.text.split(' ')[0]) # you can use .replace(' points','') like on the website the score is stored as eg 100 points and replace points with empty string and then convert to integer
        if score>=100:
            # print(score)
            id_ = int(score_elem.get('id').split('_')[1])
            row_with_score_greater_than_100 = soup.find(id=id_)
            for titleline in row_with_score_greater_than_100.find_all('span',class_="titleline"):
                for link in titleline.find_all('a',recursive=False): # we want only the direct anchor children and not all anchor tags
                    posts.append({'title':link.text,'link':link.get('href',None),'votes':score})
        # mega_dict.append({count:posts})
        # pprint.pprint(mega_dict)


# page_count = int(input("Enter the number of pages you wish to scrape:"))
page_count = 5
for count in range(1,page_count+1):
    response = requests.get(f"https://news.ycombinator.com/?p={count}")
    soup = BeautifulSoup(response.text,'html.parser')
    # print(f"This is for page {count} ")
    story_scraper()

pprint.pprint(sort_stories(posts))
