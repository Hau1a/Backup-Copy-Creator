import os
import shutil
from datetime import datetime
from logging import exception


def backupDirectory(source_dir:str, backup_dir:str) -> None:
    try:
        if not os.path.exists(source_dir):
            print('Целевая директория для выполнения бэкапа не существует. Запустите программу повторно с правильным путём')
            return
        os.makedirs(backup_dir,exist_ok=True)

        current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print("Начало создания бэкап-архива")
        shutil.make_archive(current_date,'zip',source_dir)
        print("Бэкап-архив создан")
        print("Начало перемещения бэкап-архива")
        shutil.move(current_date+".zip", backup_dir)
        print("Бэкап-архив перемещён ")
        return

    except Exception as e:
        print(e)
        return




if __name__ == "__main__":

    SOURCE_DIRECTORY = 'C:/Users/Haula/Desktop/Модельки'
    BACKUP_DIRECTORY = 'C:/Users/Haula/Desktop'

    backupDirectory(SOURCE_DIRECTORY,BACKUP_DIRECTORY)



