from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()


def create_and_upload_file(file_name = 'test.txt', file_content = 'Hey Dude!'):
    try:
        drive = GoogleDrive(gauth)

        my_file = drive.CreateFile({'title': f'{file_name}'})
        my_file.SetContentString(file_content)
        my_file.Upload()

        return f'File {file_name} was uploaded!Have a good day!'
    except Exception as _ex:
        return 'Got some trouble, check your code please!'


create_and_upload_file()