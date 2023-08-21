import requests



class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload_folder(self, path):
        URL = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        response = requests.put(f'{URL}?path={path}', headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            return "True"


#

