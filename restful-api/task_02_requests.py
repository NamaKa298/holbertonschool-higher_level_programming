#!/usr/bin/env python3
'''2. Consuming and processing data from an API using Python'''
import requests
import csv

def fetch_and_print_posts():
    '''Fetches posts from the API and prints them'''
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    posts = response.json()
    for post in posts:
        print(post.get('title'))

def fetch_and_save_posts():
    '''Fetches posts from the API and saves them to a CSV file'''
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    posts = response.json()
    with open('posts.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for post in posts:
            writer.writerow([post.get('userId'), post.get('id'), post.get('title')])
if __name__ == '__main__':  
    fetch_and_print_posts()
    fetch_and_save_posts()
