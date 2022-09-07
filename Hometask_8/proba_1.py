import requests
from ppriint import pprint
pprint("Ura")


Class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        params = {'path': "https://disk.yandex.ru/client/disk/%D0%94%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B"}
        # """Метод загружает файлы по списку file_list на яндекс диск"""
        response = request.put("")
/v1/disk/resources

r = requests.put('https://httpbin.org / put', data ={'key':'value'})
if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = D:\Documents\Информация об отделе\2022\Бассейн
    token = AQAAAAAAGUQeAADLW859Tk4gikBEmkURmI0u8H0
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)












