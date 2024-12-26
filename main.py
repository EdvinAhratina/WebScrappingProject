import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import unidecode
from datetime import datetime

# URL de base
BASE_URL = "https://www.lefrenchguide.com/"

# Fonction pour scraper une page donnée
def scrape_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'accès à {url} : {e}")
        return None

# Fonction pour extraire les données d'une catégorie (festivals, concerts, musées, etc.)
def extract_category_data(category_url, category_name,ville,cp):
    compteur = 1
    #print(f"Scraping de la catégorie : {category_name}")
    items = []
    page_number = 1

    while True:
        #print(f"Scraping de la page {page_number} pour {category_name}")
        soup = scrape_page(category_url)
        if not soup:
            break

        if category_name == "Festivals":
            item_list = soup.find_all('div', class_='sef_list-badges')[0]
            for item in item_list:
                #print(f'{compteur} / {item}')
                name = item.select_one('span.font-bold.text-secondary-500').text.strip() if item.select_one(
                    'span.font-bold.text-secondary-500') else "Non spécifié"
                description = item.select_one('span.text-white.px-2.py-0\\.5.text-xs.rounded-md').text
                location = item.select_one('svg.fa-location-arrow + span').text if item.select_one(
                    'svg.fa-location-arrow + span') else "Non spécifié"
                # Si item est déjà un élément <a>
                href = item['href'] if item.name == 'a' else item.find_parent('a')['href']
                items.append({
                    "Ville de Recherche": ville,
                    "Code Postal": cp,
                    "Catégorie": category_name,
                    "Nom": name,
                    "Description": description,
                    "Localisation": location,
                    "Complément d'URL": href
                })
                compteur+=1
        elif category_name=="Monuments" :
            item_list = soup.find_all('div',class_='sef_list-badges')[0]
            for item in item_list:
                name = item.select_one('span.font-bold.text-secondary-500').text.strip() if item.select_one(
                    'span.font-bold.text-secondary-500') else "Non spécifié"
                location = item.select_one('svg.fa-location-arrow + span').text if item.select_one(
                    'svg.fa-location-arrow + span') else "Non spécifié"
                # Si item est déjà un élément <a>
                href = item['href'] if item.name == 'a' else item.find_parent('a')['href']
                items.append({
                    "Ville de Recherche": ville,
                    "Code Postal": cp,
                    "Catégorie": category_name,
                    "Nom": name,
                    "Localisation": location,
                    "Complément d'URL": href
                })
        elif category_name=="Restaurants" :
            item_list = soup.find_all('div',class_='sef_list-badges')[0]
            for item in item_list:
                name = item.select_one('span.font-bold.text-secondary-500').text.strip() if item.select_one(
                    'span.font-bold.text-secondary-500') else "Non spécifié"
                location = item.select_one('svg.fa-location-arrow + span').text if item.select_one(
                    'svg.fa-location-arrow + span') else "Non spécifié"
                # Si item est déjà un élément <a>
                href = item['href'] if item.name == 'a' else item.find_parent('a')['href']
                items.append({
                    "Ville de Recherche": ville,
                    "Code Postal": cp,
                    "Catégorie": category_name,
                    "Nom": name,
                    "Localisation": location,
                    "Complément d'URL": href
                })
        elif category_name=="Hôtels" :
            item_list = soup.find_all('div',class_='sef_list-badges')[0]
            for item in item_list:
                name = item.select_one('span.font-bold.text-secondary-500').text.strip() if item.select_one(
                    'span.font-bold.text-secondary-500') else "Non spécifié"
                location = item.select_one('svg.fa-location-arrow + span').text if item.select_one(
                    'svg.fa-location-arrow + span') else "Non spécifié"
                # Si item est déjà un élément <a>
                href = item['href'] if item.name == 'a' else item.find_parent('a')['href']
                items.append({
                    "Ville de Recherche": ville,
                    "Code Postal": cp,
                    "Catégorie": category_name,
                    "Nom": name,
                    "Localisation": location,
                    "Complément d'URL": href
                })
        elif category_name=="Musées" :
            item_list = soup.find_all('div',class_='sef_list-badges')[0]
            for item in item_list:
                name = item.select_one('span.font-bold.text-secondary-500').text.strip() if item.select_one(
                    'span.font-bold.text-secondary-500') else "Non spécifié"
                location = item.select_one('svg.fa-location-arrow + span').text if item.select_one(
                    'svg.fa-location-arrow + span') else "Non spécifié"
                # Si item est déjà un élément <a>
                href = item['href'] if item.name == 'a' else item.find_parent('a')['href']
                items.append({
                    "Ville de Recherche": ville,
                    "Code Postal": cp,
                    "Catégorie": category_name,
                    "Nom": name,
                    "Localisation": location,
                    "Complément d'URL": href
                })
        elif category_name=="Parcs et Jardins" :
            item_list = soup.find_all('div',class_='sef_list-badges')[0]
            for item in item_list:
                name = item.select_one('span.font-bold.text-secondary-500').text.strip() if item.select_one(
                    'span.font-bold.text-secondary-500') else "Non spécifié"
                location = item.select_one('svg.fa-location-arrow + span').text if item.select_one(
                    'svg.fa-location-arrow + span') else "Non spécifié"
                # Si item est déjà un élément <a>
                href = item['href'] if item.name == 'a' else item.find_parent('a')['href']
                items.append({
                    "Ville de Recherche": ville,
                    "Code Postal": cp,
                    "Catégorie": category_name,
                    "Nom": name,
                    "Localisation": location,
                    "Complément d'URL": href
                })
        elif category_name=="Cinemas" :
            item_list = soup.find_all('div', class_='sef_list-badges')[0]
            for item in item_list:
                name = item.select_one('span.font-bold.text-secondary-500').text.strip() if item.select_one(
                    'span.font-bold.text-secondary-500') else "Non spécifié"
                location = item.select_one('svg.fa-location-arrow + span').text if item.select_one(
                    'svg.fa-location-arrow + span') else "Non spécifié"
                # Si item est déjà un élément <a>
                href = item['href'] if item.name == 'a' else item.find_parent('a')['href']
                items.append({
                    "Ville de Recherche": ville,
                    "Code Postal": cp,
                    "Catégorie": category_name,
                    "Nom": name,
                    "Localisation": location,
                    "Complément d'URL": href
                })
        elif category_name=="Campings" :
            item_list = soup.find_all('div',class_='sef_list-badges')[0]
            for item in item_list:
                name = item.select_one('span.font-bold.text-secondary-500').text.strip() if item.select_one(
                    'span.font-bold.text-secondary-500') else "Non spécifié"
                location = item.select_one('svg.fa-location-arrow + span').text if item.select_one(
                    'svg.fa-location-arrow + span') else "Non spécifié"
                # Si item est déjà un élément <a>
                href = item['href'] if item.name == 'a' else item.find_parent('a')['href']
                items.append({
                    "Ville de Recherche": ville,
                    "Code Postal": cp,
                    "Catégorie": category_name,
                    "Nom": name,
                    "Localisation": location,
                    "Complément d'URL": href
                })
        else :
            print(f"Catégorie introuvable : {category_name}")
        # Vérifier si une pagination existe pour continuer
        next_page = soup.select_one('a.next-page')  # Modifier selon la classe CSS du bouton "Page suivante"
        if next_page and 'href' in next_page.attrs:
            category_url = next_page['href']
            page_number += 1
            time.sleep(1)  # Pause pour éviter de surcharger le serveur
        else:
            break

    return items

# Fonction principale pour scraper toutes les catégories
def scrape_all_categories(complement_url,ville,cp):
    categories = {
        "Festivals": f"https://www.lefrenchguide.com/festivals/{complement_url}/",
        "Monuments": f"https://www.lefrenchguide.com/monuments/{complement_url}/",
        "Musées": f"https://www.lefrenchguide.com/musees/{complement_url}/",
        "Hôtels": f"https://www.lefrenchguide.com/hotels/{complement_url}/",
        "Campings": f"https://www.lefrenchguide.com/campings/{complement_url}/",
        "Restaurants": f"https://www.lefrenchguide.com/restaurants/{complement_url}/",
        "Parcs et Jardins": f"https://www.lefrenchguide.com/parcs-jardins/{complement_url}/",
        "Cinemas": f"https://www.lefrenchguide.com/cinemas/{complement_url}/"
    }

    all_data = []
    for category_name, category_url in categories.items():
        category_data = extract_category_data(category_url, category_name,ville,cp)
        all_data.extend(category_data)

    return all_data

def create_df_for_one_city(complement_url,ville,cp):
    # Lancer le scraping
    data = scrape_all_categories(complement_url,ville,cp)

    # Sauvegarder les données dans un fichier CSV avec horodatage
    if data:
        #timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        #file_name = f"lefrenchguide_data_{timestamp}.csv"
        file_name = f"lefrenchguide_data.csv"
        df = pd.DataFrame(data)
        df.to_csv(file_name, index=False, encoding='utf-8')
        print(f"Les données ont été sauvegardées dans {file_name}")
    else:
        print("Aucune donnée n'a été récupérée.")


def create_df_for_all_cities():
    villes = []
    datas=[]
    compteur = 1
    with open('propositions.txt', 'r', encoding='utf-8') as file:
        for line in file:
            value = unidecode.unidecode(line.replace(' ','-').replace('\n','').lower().replace('saint-','st-').replace('\'','-').replace('sainte-','ste-'))
            villes.append([value,line.replace('\n','')[0:-6],line.replace('\n','')[-6:]])
    print(villes)

    for ville in villes :
        print(f"{compteur}/ Ville : {ville[0]}")
        data = scrape_all_categories(ville[0],ville[1],ville[2])
        for row in data :
            datas.append(row)
        if compteur == 100 :
            break
        else :
            compteur += 1
    if data:
        #timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        #file_name = f"lefrenchguide_data_{timestamp}.csv"
        file_name = f"lefrenchguide_all_data.csv"
        df = pd.DataFrame(datas)
        df.to_csv(file_name, index=False, encoding='utf-8')
        print(f"Les données ont été sauvegardées dans {file_name}")
    else:
        print("Aucune donnée n'a été récupérée.")

create_df_for_all_cities()