from ya_api import Yandex


token = 'OAuth y0_AgAAAAB1hKjJAADLWwAAAAECOZK6AACUqbMBw9lFMLhn3OkkYmj6E4gIQg'
# Название создаваемой папки
folder_name = 'photo'

# Тест метода _create_folder для проверки создания и наличия папки
# в корневом каталоге Яндекс диска
def test_folder_creation():
    # Запускаем _create_folder
    res = (Yandex(folder_name, token)._create_folder(folder_name))
    # Проверяем, что status_code == 200, -> папка есть в Яндекс диске
    assert res[0].status_code == 200
    # Проверяем, что папка Vk_photo есть в Яндекс диске
    assert res[1] == 'disk:/photo'
    # Проверяем наличие ошибок
    assert 'error' not in res

# Вызов функции test_folder_creation()
test_folder_creation()