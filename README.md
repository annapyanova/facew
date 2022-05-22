<h1><i>Требования и инструкция для запуска проекта.</i></h1>


### Для запуска обязательно наличие дистрибутива Ubuntu (wsl2) и таких пакетов, как  python3, ffmpeg, docker, docker-compose, tensorflow, numpy, cmake, cv2, psycopg2, flask, gstreamer, pytest.
---
Инструкция для запуска:
1) Произведите клонирование данного репозитория на локальный компьтер (`git clone https://github.com/annapyanova/facew.git`).
2) Откройте терминал **wsl2** и перейдите в дирректорию **facew**.

      ![image](https://user-images.githubusercontent.com/90253693/169549078-1f5e1a8e-0c8d-48a7-bdc9-a51ef7905052.jpg)

3) С помощью команды `python3 save_model.py` выполните конвертацию весов.
Результат будет записан в папку **facew/checkpoints**.
4) Параллельно откройте **второй терминал wsl2**.
5) Перенесите видео, над которым будет производиться трекинг, в папку **facew/data/video**.
6) В первом терминале выполните команду `sudo docker-compose up` для поднятия докер-контейнера с 
базой данных и frontend.
7) Во втором терминале запустите команду `python3 server.py` (запуск backend).
8) Для просмотра результата используйте браузер **Mozila Firefox**.
9) Откройте браузер и перейдите по адресу [localhost:5000](http://localhost:5000/).
10) Через несколько секунд на веб-странице начнётся транслирование видео.

      ![image](https://user-images.githubusercontent.com/90253693/169554977-64720270-91ad-4fb0-b09e-d868002e7537.jpg)

11) Для запуска тестов выполните команду `python3 -m pytest`, после чего будет получено
сообщение об успешном прохождении 5 тестов.

   ![image](https://user-images.githubusercontent.com/90253693/169556039-c2d1096f-35e1-461f-af7f-e08204086f7c.png)
 
 
