import pandas as pd
import requests
import json
from tqdm.auto import tqdm
from time import sleep


class HashInscriptionChecker:
    
    def __init__(self, hash_path):
        self.df = pd.read_csv(hash_path)
        return
    
    
    def get_inscription_id(self, df):
        """
        From hash Dataframe, find onchain inscriptions IDs using 
        OrdinalsBot APIs. If frontrun, take first inscription
        """
    
        def fetch_inscription_info(hash_value, max_retries=5, backoff_factor=1.0):
            url = f'https://api2.ordinalsbot.com/search?hash={hash_value}'
            retries = 0
            while retries < max_retries:
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        data = response.json()
                        # Sort the results by 'createdat' in ascending order
                        sorted_results = sorted(data['results'], key=lambda k: k['createdat'])
                        num_inscriptions = len(sorted_results)
                        # Extract the first inscription id after sorting if available
                        inscription_id = sorted_results[0].get('inscriptionid', None) if num_inscriptions > 0 else None
                        return inscription_id, num_inscriptions
                    else:
                        print(f"Failed to fetch data for hash {hash_value}, status code {response.status_code}")
                        retries += 1
                        sleep(backoff_factor * (2 ** retries))  # Exponential backoff
                except requests.RequestException as e:
                    print(f"Request failed: {e}, retrying ({retries+1}/{max_retries})...")
                    retries += 1
                    sleep(backoff_factor * (2 ** retries))  # Exponential backoff
            return None, 0
        
        df['inscription_id'] = None
        df['num_inscriptions'] = 0 
        
        # Update the dataframe with progress bar
        for index in tqdm(df.index, desc="Fetching inscription info"):
            hash_value = df.at[index, 'hash']
            inscription_id, num_inscriptions = fetch_inscription_info(hash_value)
            df.at[index, 'inscription_id'] = inscription_id
            df.at[index, 'num_inscriptions'] = num_inscriptions
            
        return df
    
    
    def create_inscription_json(self, filename, asset_name):
        inscription_list = []

        for i in self.df.to_dict(orient='records'):
            image_id = i['image_id']
            name = f'{asset_name} #{image_id}'

            x = {
                'id': i['inscription_id'],
                'meta': {
                    'name': name
                }
            }
            inscription_list.append(x)

        with open(filename, 'w') as file:
            json.dump(inscription_list, file, indent=4, sort_keys=True)
        
    
    def run(self, filename, asset_name="Test"):
        self.df = self.get_inscription_id(self.df)
        self.create_inscription_json(filename, asset_name)
        return f"Inscription json saved at {filename}!"
