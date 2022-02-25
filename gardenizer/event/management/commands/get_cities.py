from django.core.management.base import BaseCommand
import requests
from tqdm import tqdm

from event.models import Category, City

class Command(BaseCommand):
    """
    This command enable the population of the database for Category and City tables.
    """
    help = "Populate database with all city names and corresponding zipcodes"
    
    def handle(self,*args,**kwargs):
        self._fill_cities()
        self._add_categories()
        
    def _get_cities_data(self):
        """
        Get all french cities with corresponding zipcodes 
        from https://geo.api.gouv.fr/
        """
        all_cities = []
        response = requests.get(
            "https://geo.api.gouv.fr/communes?fields=nom,codesPostaux"
        )
        data = response.json()
        for each_city in tqdm(data):
            if each_city["codesPostaux"] != []:
                one_city = (each_city['nom'],each_city["codesPostaux"][0])
                all_cities.append(one_city)
        
        return all_cities
    
    def _fill_cities(self):
        """
        Fill the Db with cities data (name and zipcode)
        """
        cities = self._get_cities_data()
        for each_city in tqdm(cities):
            obj, created = City.objects.get_or_create(
                name=f"{each_city[0]}",
                zipcode=f"{each_city[1]}",
            )
            
    def _add_categories(self):
        """
        Adding categories to the corresponding table in DB.
        """
        
        category_list = ["Entretient et révision matériel", "Chantier"]
        for category in tqdm(category_list):
            obj, created = Category.objects.get_or_create(
                title = f"{category}"
            )