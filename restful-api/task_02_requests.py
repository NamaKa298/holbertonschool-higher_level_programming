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
        with open('posts.csv', 'w', newline='') as fichier:
            csvwriter = csv.writer(fichier)
            for donnee in donnees_parsees:
                csvwriter.writerow([donnee.get('userId'), donnee.get('id'),
                                    donnee.get('title')])
    print("Saved the posts to posts.csv")
