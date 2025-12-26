# Это объединённый файл всех методов для работы с json файлами, что я написал
# На данный момент это json_write(filename,data) - создан для записи данных в json файл
# и ещё один метод json_read(filename) - создан для чтения данных из json файла
import json

# to read data from the json file
def json_read(filename):
    try:
        with open(filename,'r',encoding='utf-8') as json_file:
            return json.load(json_file)
    except Exception as error:
        print(f"Ошибка чтения в {filename}: {error}")
        return None


# to write data into json file
def json_write(filename,data):
    try:
        with open(filename,'w',encoding='utf-8') as json_file:
            # ensure_ascii нужно для того чтоб кирилица сохранялась
            # indent значит отступы чтоб читаемо было
            json.dump(data,json_file,indent=4,ensure_ascii=False)

    except Exception as error:
        print(f"Ошибка записи в {filename}: {error}")