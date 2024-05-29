#!/usr/bin/env python3
'''2. Consuming and processing data from an API using Python'''
import requests
import csv

def fetch_and_print_posts():
    '''fetches all post from JSONPlaceholder'''
    url_JSONPlaceholder = "https://jsonplaceholder.typicode.com/"
    reponse = requests.get(url_JSONPlaceholder)
    print("Status code: {}".format(reponse.status_code))
    if reponse.status_code == 200:
        donnees_parsees = reponse.json()
        for donnee in donnees_parsees:
            print(donnee.get('title'))

def fetch_and_save_posts():
    '''fetches all post from JSONPlaceholder'''
    url_JSONPlaceholder = "https://jsonplaceholder.typicode.com/"
    reponse = requests.get(url_JSONPlaceholder)
    if reponse.status_code == 200:
        donnees_parsees = reponse.json()
        for donnee in donnees_parsees:
            post_data = [{'id': donnee['id'], 'title': donnee['title'], 'body': donnee['body']}]
            with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Écrire l'en-tête
            writer.writeheader()
            
            # Écrire les données des posts
            for post in post_data:
                writer.writerow(post)
