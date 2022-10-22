import requests


class YaUploader:
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'

    def __init__(self, my_token: str):
        self.token = my_token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self, yadisk_path):
        resp = requests.put(f'{self.URL}?path={yadisk_path}', headers=self.get_headers())
        print(resp)
        return resp

    def delete_folder(self, yadisk_path):
        resp = requests.delete(f'{self.URL}?path={yadisk_path}', headers=self.get_headers())
        print(resp)
        return resp

if __name__ == '__main__':
    path_to_file_yd = 'Укажите путь для создания папки на Яндекс.диске'
    token = 'Укажите токен'
    uploader = YaUploader(token)
    uploader.create_folder(path_to_file_yd)
    uploader.delete_folder(path_to_file_yd)
