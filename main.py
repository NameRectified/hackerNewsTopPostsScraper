'''
    The goal is to scrape the posts from hackernews with score greated than 100
    look at soup.select in the documentation, it could have made the work a lot easier
    Enumerate is used in lists when we want the elements of the list as well as the index of those items.
'''
import requests
from bs4 import BeautifulSoup
import pprint # for better printing

response = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(response.text,'html.parser')

# for title in soup.find_all('span',class_="titleline"):
#     for link in title.find_all('a'):
#         print(link.get('href'),link.text,sep='\n',end='\n\n')
#     # print(title.find_all('a').get('href'),end="\n\n")

# for elem in soup.find_all('tr',class_='athing'):
    # print(elem.get('id'),end='\n\n')

posts = []
for score_elem in  soup.find_all('span',class_='score'):
    # print(score_elem)
    score =int(score_elem.text.split(' ')[0]) # tyou can use .replace(' points','') like on the website the score is stored as eg 100 points and replace points with empty string and then convert to integer
    if score>100:
        # print(score,score_elem.get('id').split('_')[1])
        print(score)
        id_ = int(score_elem.get('id').split('_')[1])
        row_with_score_greater_than_100 = soup.find(id=id_)
        for titleline in row_with_score_greater_than_100.find_all('span',class_="titleline"):
            for link in titleline.find_all('a',recursive=False): # we want only the direct anchor children and not all anchor tags
            # for link in titleline.select('a:first-of-type'):
                # print(link)
                # print(link.get('href'),link.text,sep='\n',end='\n\n')
                posts.append({'title':link.text,'link':link.get('href',None),'votes':score})
                # posts.append({'title':link.text,'link':link.get('href',None)})
                # posts.append({title:link.text})
    pprint.pprint(posts)
            # print(title.find_all('a').get('href'),end="\n\n")
