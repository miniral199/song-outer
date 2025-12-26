from files.json_io import json_write

def import_song_json(filename_from,filename_to):
    try:
        song=""" """
        with open(filename_from,'r',encoding='utf-8') as file:
            song=file.read()

        song_arr=song.strip().split('\n')
        filename=filename_to
        json_write(filename,song_arr)
    except Exception as e:
        print(f'Возникла ошибка:{e}')
        return False
    print('Импортирование песни завершено успешно!')
    return True
