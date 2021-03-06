#!/usr/bin/env python
# -*- coding: utf-8 -*-


def all_messages():
    """
    keep all messages in ru

    Returns:
        all messages in JSON
    """
    return \
        {
            "0": "Начался запуск Nettacker ... \n\n",
            "1": "python nettacker.py [опции]",
            "2": "Показать меню справки Nettacker",
            "3": "Пожалуйста, прочтите лицензию и соглашение https://github.com/viraintel/OWASP-Nettacker\n",
            "4": "двигатель",
            "5": "Параметры ввода двигателя",
            "6": "выберите язык {0}",
            "7": "сканировать все IP-адреса в диапазоне",
            "8": "находить и сканировать субдомены",
            "9": "номера потоков для соединений с хостом",
            "10": "номера потоков для хостов сканирования",
            "11": "сохранить все журналы в файле (results.txt, results.html, results.json)",
            "12": "цель",
            "13": "Целевые параметры ввода",
            "14": "список целей, разделенных с \",\"",
            "15": "читать цель (цели) из файла",
            "16": "Параметры метода сканирования",
            "17": "выбрать метод сканирования {0}",
            "18": "выберите исключительный метод сканирования {0}",
            "19": "список пользователей, разделенных \",\"",
            "20": "читать имя пользователя из файла",
            "21": "список паролей, разделенных с \",\"",
            "22": "читать пароль (ы) из файла",
            "23": "список портов, разделенных с \",\"",
            "24": "читать пароли (ы) из файла",
            "25": "время спать между каждым запросом",
            "26": "Невозможно указать цель (ы)",
            "27": "Невозможно указать цель (ы), неспособность открыть файл: {0}",
            "28": "лучше использовать число потоков ниже 100, кстати, мы продолжаем ...",
            "29": "установите тайм-аут на {0} секунд, он слишком велик, не так ли? кстати, мы продолжаем.",
            "30": "этот модуль сканирования [{0}] не найден!",
            "31": "этот модуль сканирования [{0}] не найден!",
            "32": "вы не можете исключить все методы сканирования",
            "33": "вы не можете исключить все методы сканирования",
            "34": "модуль {0}, который вы выбрали для исключения, не найден!",
            "35": "введите методы ввода, например: «ftp_brute_users=test,admin&ftp_brute_passwds="
                  "read_from_file:/tmp/pass.txt&ftp_brute_port=21\"",
            "36": "не может читать файл {0}",
            "37": "Невозможно указать имя пользователя (ов), неспособное открыть файл: {0}",
            "38": "",
            "39": "Не удается указать пароль (ы), не удается открыть файл: {0}",
            "40": "Файл \"{0}\" не доступен для записи!",
            "41": "выберите способ сканирования!",
            "42": "удаление временных файлов!",
            "43": "результаты сортировки!",
            "44": "сделанный!",
            "45": "начать атаковать {0}, {1} из {2}",
            "46": "этот модуль \"{0}\" недоступен",
            "47": "к сожалению, эту версию программного обеспечения можно было запустить только на linux/osx/windows.",
            "48": "Ваша версия Python не поддерживается!",
            "49": "пропустить дублируемую цель (некоторые поддомены / домены могут иметь "
                  "одинаковые IP-адреса и диапазоны)",
            "50": "неизвестный тип цели [{0}]",
            "51": "проверка диапазона {0} ...",
            "52": "проверка {0} ...",
            "53": "хозяин",
            "54": "имя пользователя",
            "55": "пароль",
            "56": "порт",
            "57": "тип",
            "58": "описание",
            "59": "уровень подробного режима (0-5) (по умолчанию 0)",
            "60": "показать версию программного обеспечения",
            "61": "Проверить обновления",
            "62": "",
            "63": "",
            "64": "Повторяет попытку, когда таймаут соединения (по умолчанию 3)",
            "65": "ftp для {0}:{1} таймаут, пропуская {2}:{3}",
            "66": "успешно зарегистрирован!",
            "67": "успешно зарегистрирован, разрешение отказано для команды списка!",
            "68": "ftp-подключение к {0}: {1} не удалось, пропустив весь шаг [процесс {2} из {3}]!"
                  " переход к следующему шагу",
            "69": "входная цель для модуля {0} должна быть DOMAIN, HTTP или SINGLE_IPv4, пропуская {1}",
            "70": "имя пользователя: {0} пароль: {1} хозяин: {2} порт: {3} найдено!",
            "71": "(без разрешения для файлов списка)",
            "72": "{0} из {1} в процессе {2} из {3} {4}:{5}",
            "73": "smtp-соединение с {0}: {1} таймаут, пропуская {2}:{3}",
            "74": "smtp-соединение с {0}: {1} не удалось, пропустив весь шаг [процесс {2} из {3}]! "
                  "переход к следующему шагу",
            "75": "входная цель для модуля {0} должна быть HTTP, пропуская {1}",
            "76": "ssh для {0}:{1} таймаут, пропуская {2}:{3}",
            "77": "ssh-соединение с {0}: {1} не удалось, пропустив весь шаг [процесс {2} из {3}]! "
                  "переход к следующему шагу",
            "78": "ssh-соединение с {0}: {1} не удалось, пропустив весь шаг [процесс {2} из {3}]!"
                  " переход к следующему шагу",
            "79": "открытый порт",
            "80": "хозяин: {0} порт: {1} найдено!",
            "81": "цель {0} представлена!",
            "82": "не удается открыть файл списка прокси: {0}",
            "83": "не удается найти файл списка прокси: {0}",
            "84": "вы используете версию OWASP Nettacker {0}{1}{2}{6} с кодовым названием {3}{4}{5}",
            "85": "эта функция пока недоступна! запустите \"git clone https://github.com/viraintel/"
                  "OWASP-Nettacker.git\" или \"pip install -U OWASP-Nettacker\" чтобы получить последнюю версию.",
            "86": "постройте график всех действий и информации, вы должны использовать "
                  "вывод html. доступные графики: {0}",
            "87": "для использования функции графика ваше имя выходного файла должно заканчиваться"
                  " символом \".html\" или \".htm\"!",
            "88": "строительный график ...",
            "89": "закончите строить график!",
            "90": "Графики тестирования проникновения",
            "91": "Этот график создан OWASP Nettacker. График содержит все действия модулей,"
                  " карту сети и конфиденциальную информацию. Пожалуйста, не сообщайте этот файл "
                  "никому, если он не является надежным",
            "92": "Отчет OwASP Nettacker",
            "93": "Сведения о программном обеспечении: версия OWASP Nettacker {0} [{1}] в {2}",
            "94": "открытых портов не найдено!",
            "95": "нет имени пользователя/пароля!",
            "96": "Загружено модулей {0} ...",
            "97": "этот модуль графа не найден: {0}",
            "98": "этот модуль графа \"{0}\" недоступен",
            "99": "ping перед сканированием хоста",
            "100": "пропускающая цель отверстия {0} и метод сканирования {1} --ping-before-scan "
                   "истинны, и он не ответил!",
            "101": "вы не используете последнюю версию OWASP Nettacker, пожалуйста, обновите ее.",
            "102": "не можете проверить наличие обновлений, проверьте подключение к Интернету.",
            "103": "Вы используете последнюю версию OWASP Nettacker ...",
            "104": "список каталогов, найденный в {0}",
            "105": "вставьте порт через ключ -g или --methods-args вместо url",
            "106": "http-соединение {0} тайм-аут!",
            "107": "",
            "108": "нет каталога или файла, найденного для {0} в порту {1}",
            "109": "не удалось открыть {0}",
            "110": "Значение dir_scan_http_method должно быть GET или HEAD, по умолчанию установлено GET.",
            "111": "перечислить все методы args",
            "112": "не может получить {0} модуль args",
            "113": "",
            "114": "",
            "115": "",
            "116": "",
            "117": ""
        }
