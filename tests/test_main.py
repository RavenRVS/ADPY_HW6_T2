import pytest
import requests

from main import YaUploader

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = 'Укажите токен'


def test_create_folder():
    path_to_file_yd = 'Укажите путь для создания папки на Яндекс.диске'

    cls = YaUploader(TOKEN)
    resp = cls.create_folder(path_to_file_yd)

    assert resp.status_code == 201
    assert requests.get(f'{URL}?path={path_to_file_yd}', headers=cls.get_headers()).status_code == 200
    cls.delete_folder(path_to_file_yd)

