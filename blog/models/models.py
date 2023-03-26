import json


def get_articles():
    with open('blog/models/articles.json', 'r') as articles:
        data = json.load(articles)
    return data


def get_users():
    with open('blog/models/users.json', 'r') as users:
        data = json.load(users)
    return data
