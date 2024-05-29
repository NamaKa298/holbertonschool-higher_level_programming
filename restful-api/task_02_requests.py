#!/usr/bin/env python3
'''2. Consuming and processing data from an API using Python'''
import requests
import csv


def fetch_and_print_posts():
    '''fetches all post from JSONPlaceholder'''
    url_JSONPlaceholder = https: // jsonplaceholder.typicode.com/
    reponse = requests.get(url_JSONPlaceholder)
    print("Status code: {}".format(reponse.status_code))
    if reponse.status_code == 200:
        donnees_parsees = reponse.json()
        for donnee in donnees_parsees:
            print(donnee.get('title'))


def fetch_and_save_posts():
    '''fetches all post from JSONPlaceholder'''
    url_JSONPlaceholder = https: // jsonplaceholder.typicode.com/
    reponse = requests.get(url_JSONPlaceholder)
    print("Status code: {}".format(reponse.status_code))
    if reponse.status_code == 200:
        donnees_parsees = reponse.json()
        with open('posts.csv', 'w', newline='') as fichier_csv:
            csv_writer = csv.writer(fichier_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for donnee in donnees_parsees:
                csv_writer.writerow([donnee.get('userId'), donnee.get('id'), donnee.get('title')])
    print("Données enregistrées dans posts.csv")
