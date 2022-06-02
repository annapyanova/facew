<h1><i>Требования и инструкция для запуска проекта.</i></h1>


### Для запуска обязательно наличие дистрибутива Ubuntu (wsl2), зависимостей, указанных в requirements.txt, а также скомпилированного OpenCV вместе с Gstreamer ([galaktyk.medium.com](https://galaktyk.medium.com/how-to-build-opencv-with-gstreamer-b11668fa09c)).
---
Инструкция для запуска:
1) Произведите клонирование данного репозитория на локальный компьтер (`git clone https://github.com/annapyanova/facew.git`).
2) Откройте терминал **wsl2** и перейдите в дирректорию **facew/server**.  
  
      ![image](https://user-images.githubusercontent.com/90253693/171023619-5017064d-e0f1-4997-a239-2fb822607559.png)

3) С помощью команды `python3 save_model.py` выполните конвертацию весов. Результат будет записан в папку **facew/server/checkpoints**.
4) Параллельно откройте **второй терминал wsl2**, в котором перейдите в дирректорию **facew**.
5) В нём выполните команду `sudo docker-compose build` для сборки проекта.
6) В этом же терминале выполните `sudo docker-compose up` для поднятия докер-контейнеров с postgresql, pgadmin и frontend.
7) В первом терминале запустите команду `python3 server.py` (запуск backend).
8) Для просмотра результата используйте браузер ***Mozila Firefox***.
9) Откройте его и перейдите по адресу [localhost:5000](http://localhost:5000/).
10) Через несколько секунд на веб-странице начнётся транслирование видео.
     
     ![image](https://user-images.githubusercontent.com/90253693/169554977-64720270-91ad-4fb0-b09e-d868002e7537.jpg)

11) Для запуска тестов выполните во втором терминале команду `python3 -m pytest` **(не останавливая докер-контейнеры)**, 
после чего будет получено сообщение об успешном прохождении 5 тестов.

   ![image](https://user-images.githubusercontent.com/90253693/169556039-c2d1096f-35e1-461f-af7f-e08204086f7c.png)
 
