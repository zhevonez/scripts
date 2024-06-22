from pydub import AudioSegment
import os

def change_bitrate(file_name, target_bitrate):
    try:
        # провер очка файлов
        if not os.path.isfile(file_name):
            print(f"файл {file_name} не найден.")
            return

        # загруз очка
        audio = AudioSegment.from_file(file_name)

        # новый путь # можно поменять конвертед на чтото другое
        file_root, file_ext = os.path.splitext(file_name)
        output_path = f"{file_root}_converted{file_ext}"

        audio.export(output_path, format='mp3', bitrate=f'{target_bitrate}k')
        print(f"файл сохранен как {output_path} с битрейтом {target_bitrate} kbps.")

    except Exception as e:
        print(f"произошла ошибка: {e}")

file_name = input("введите название файла (с расширением): ")
target_bitrate = input("введите желаемый битрейт (kbps): ")
change_bitrate(file_name, target_bitrate)


# made by zhevonez