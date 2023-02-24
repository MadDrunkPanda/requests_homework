import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path, filename_list ):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        resp = requests.get(upload_url, headers=headers, params=params)
        x = resp.json()
        url = x.get('href')
        for file in filename_list:
             response = requests.put(url, data = open(file, 'rb'))






if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = " "
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


