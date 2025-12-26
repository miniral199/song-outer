import time
from files.import_song_json import import_song_json
from files.json_io import json_read

def print_song(filename_from=None,filename_to=None):
    config = json_read("files/config.json")
    if config is None:
        print("Ошибка загрузки конфига, использую данные по умолчанию!")
        config={
            "speed": {
                "start": 0.25,
                "min": 0.8,
                "decrement": 0.3
            },
            "filenames": {
                "filename_from": "text_song.txt",
                "filename_to": "text_song.json"
            }
        }
    start_speed=config['speed']['start']
    min_speed=config['speed']['min']
    decrement_speed=config['speed']['decrement']

    speed=start_speed

    if filename_from is None:
        filename_from=config['filenames']['filename_from']

    if filename_to is None:
        filename_to=config['filenames']['filename_to']


    import_status = import_song_json(filename_from, filename_to)
    if not import_status:
        print('Произошла проблема при импорте текста песни')
        exit()
    text_song = json_read(filename_to)
    if text_song is None:
        print("Не удалось загрузить песню")
        exit()
    for sentence in text_song:

        # сделал так чтоб скорость не была меньше нуля и было не слишком быстро
        speed=max(min_speed, speed-decrement_speed)
        for letter in sentence:
            print(letter, end="")
            time.sleep(speed)

        print()


if __name__=='__main__':
    print_song()