import requests
from pprint import pprint
# from ya_disk import YandexDisk
# -----------------------------------task_2_yandex--------------------------------------
TOKEN = "AQAAAAAAGUQeAADLW859Tk4gikBEmkURmI0u8H0"
class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "OAuth {}".format(self.token)
        }
    def get_files_list(self):
        files_url = "https://cloud-api.yandex.net/v1/disk/resources/files"
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

#  получаем ссылку для загрузки нашего файла через get
    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        response_href = self._get_upload_link(disk_file_path=disk_file_path)
        url = response_href.get("href", "")
        response = requests.put(url, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    pprint(ya.upload_file_to_disk(disk_file_path='NET/test_1.txt', filename="test_1.txt"))