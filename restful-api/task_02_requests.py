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
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Parser les données récupérées en objet JSON
        posts = response.json()
        
        # Structurer les données en une liste de dictionnaires
        post_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        # Utiliser le module csv pour écrire les données dans un fichier CSV
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            # Définir les noms des colonnes
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Écrire l'en-tête
            writer.writeheader()
            
            # Écrire les données des posts
            for post in post_data:
                writer.writerow(post)
                
        print("Posts have been saved to posts.csv")
    else:
        print("Failed to fetch posts")