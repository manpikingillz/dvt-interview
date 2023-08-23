# Given username and limit values, return an array of names of articles authored by the user with the given username
# orderd by the number of comments they have, descedning. limit the list to limit records.
# If articles have the same number of comments, order them by name asc

import requests


def topArticles(username, limit):
    response = requests.get(
        f'https://jsonmock.hackerrank.com/api/articles?author={username}&limit={limit}')

    if response.status_code == 200:
        data = response.json()

        articles_data = data['data']
        sorted_articles = sorted(
            articles_data,
            key=lambda article: (-article['num_comments'], article['title']))

        article_names = [item['title'] for item in sorted_articles]
        return article_names
    else:
        print("Error Occured: ", response.status_code)


if __name__ == "__main__":
    username = "epaga"
    limit = 5

    print('article names: ', topArticles(username, limit))
