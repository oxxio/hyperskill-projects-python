
from bs4 import BeautifulSoup
import requests
import string
import os

if __name__ == '__main__':

    page_number = int(input())
    article_to_find = input()

    url = "https://www.nature.com/nature/articles"
    parent_directory = os.getcwd()

    for i in range(page_number):

        params = {'searchType': 'journalSearch', 'sort': 'PubDate', 'year': '2020', 'page': i + 1}
        response = requests.get(url, params)
        if response.status_code != 200:
            print(f'The URL returned {response.status_code}!')
        else:
            soup = BeautifulSoup(response.content, 'html.parser')
            # directory name
            directory_name = 'Page_' + str(i + 1)
            path = os.path.join(parent_directory, directory_name)
            # create directory
            os.mkdir(path)
            # change directory
            os.chdir(path)
            # find all article
            all_articles = soup.find_all('article')
            for article in all_articles:
                # find article name
                if article.find("span", class_="c-meta__type").text == article_to_find:
                    # find article title
                    title = article.find("a", class_="c-card__link u-link-inherit")
                    stripped = title.text.translate(title.text.maketrans("", "", string.punctuation))
                    # filename
                    file_title = stripped.translate(stripped.maketrans(" ", "_")) + ".txt"
                    # open file
                    file = open(file_title, 'w', encoding='utf-8')
                    # get article content
                    article_url = "https://www.nature.com" + title["href"]
                    response2 = requests.get(article_url)
                    soup2 = BeautifulSoup(response2.content, 'html.parser')
                    body = soup2.find("div", class_="c-article-body").text.strip()
                    file.write(body)
                    file.close()
            # change directory to parent directory
            os.chdir(parent_directory)
    print("Saved all articles.")
