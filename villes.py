from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuration du service ChromeDriver avec WebDriver Manager et Options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Mode headless (sans interface graphique)
chrome_options.add_argument("--no-sandbox")  # Pour les environnements limités
chrome_options.add_argument("--disable-dev-shm-usage")  # Éviter les problèmes de mémoire partagée
chrome_options.add_argument("--disable-gpu")  # Désactiver l'accélération GPU (facultatif)
chrome_options.add_argument("--log-level=3")  # Réduire les logs pour rendre la console plus lisible

service = Service(ChromeDriverManager().install())

# Initialisation du navigateur
print("Initialisation du navigateur en mode headless...")
driver = webdriver.Chrome(service=service, options=chrome_options)
print("Navigateur lancé avec succès ! (Mode headless)")

# URL cible
url = "https://www.lefrenchguide.com/campings/"
driver.get(url)

# Attendre que la page charge les éléments dynamiques
wait = WebDriverWait(driver, 10)

# Fichier pour enregistrer les propositions
output_file = "propositions.txt"

# Ensemble pour éviter les doublons
found_proposals = set()

# Propositions à ignorer
ignored_proposals = {
    "Votre position",
    "Paris",
    "Marseille",
    "Lyon",
    "Toulouse",
    "Nice",
    "Nantes",
    "Montpellier",
    "Strasbourg",
    "Bordeaux",
    "Lille"
}

try:
    # Ouvrir le fichier en mode écriture
    with open(output_file, "w", encoding="utf-8") as file:
        for postal_code in range(1000, 102000):  # Boucle de 01000 à 101999
            postal_code_str = f"{postal_code:05d}"  # Formater en 5 chiffres
            print(f"Test du code postal : {postal_code_str}")

            # Remplir le champ "Ville ou code postal"
            city_input = driver.find_element(By.ID, "home-form-search-input-city")
            city_input.clear()
            city_input.send_keys(postal_code_str)
            time.sleep(1)  # Pause courte pour laisser le menu déroulant apparaître

            # Attendre que la liste des suggestions soit visible
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sef_input-list")))
                suggestions = driver.find_elements(By.CSS_SELECTOR, ".sef_input-list li")

                for suggestion in suggestions:
                    suggestion_text = suggestion.text.strip()
                    if (
                        suggestion_text not in found_proposals
                        and suggestion_text not in ignored_proposals
                        and suggestion_text  # S'assurer que le texte n'est pas vide
                    ):
                        found_proposals.add(suggestion_text)
                        file.write(suggestion_text + "\n")  # Enregistrer dans le fichier
                        file.flush()  # Forcer l'écriture
                        print(f"Nouvelle proposition trouvée : {suggestion_text}")
            except Exception as e:
                print(f"Aucune suggestion trouvée pour le code postal {postal_code_str}. Erreur : {e}")

except Exception as e:
    print(f"Erreur : {e}")

# Fermer le navigateur
driver.quit()