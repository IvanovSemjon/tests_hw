import requests
token = 'OAuth y0_AgAAAAB1hKjJAADLWwAAAAECOZK6AACUqbMBw9lFMLhn3OkkYmj6E4gIQg'


class Yandex:
    # Метод для получения основных параметров
    def __init__(self, folder_name, token):
        self.token = token
        self.url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        self.headers = {'Authorization': self.token}
        self.folder = self._create_folder(folder_name)

    # Метод создания папки на Ядиске
    def _create_folder(self, folder_name):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {'path': folder_name}
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            requests.put(url, headers=self.headers, params=params)
            print(f'\nПапка {folder_name} успешно создана в корневом каталоге Яндекс диска\n')
        else:
            print(f'\nПапка {folder_name} уже существует. Файлы с одинаковыми именами не будут скопированы\n')
        # Запрос после создания папки если status_code = 200, то папка есть в корневом каталоге Яндекс диска
        response2 = requests.get(url, headers=self.headers, params=params)
        # Получение из запроса названия созданной папки, чтобы убедиться что она создана
        response3 = response2.json()['path']
        return response2, response3

# Проверка создания папки 'photo' в корневом каталоге Яндекс диска
yandex_photo = Yandex('photo', token)