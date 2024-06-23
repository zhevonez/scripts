from telegraph import Telegraph
from telegraph.exceptions import RetryAfterError
import time
import sys

# запрос данных
title = input("Введите заголовок: ")
text = input("Введите текст: ")
time = input("Введите время (в секундах): ")
shortname = input("Введите ваше имя: ")

# проверка
try:
    time = float(time)
except ValueError:
    print("Время должно быть числом.")
    sys.exit()

# создание учетки
tg = Telegraph()
tg.create_account(short_name=shortname)

while True:
    try:
        otvet = tg.create_page(
            f'{title}',
            html_content=f'{text}'
        )
        print(otvet['url'])
        
        # задержка
        time.sleep(time)
    
    except RetryAfterError as e:
        # флуд контроль после превышения
        retry_after = e.retry_after
        print(f"Флуд контроль задел нас. Пытка продолжится через {retry_after} секунд...")
        time.sleep(retry_after)
    except Exception as e:
        # если ошибка
        print(f"Ошибка: {e}")
        sys.exit()

# // made by zhevonez // 
