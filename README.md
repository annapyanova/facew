<h1><i>Требования и инструкция для запуска проекта.</i></h1>


### Для запуска обязательно наличие дистрибутива Ubuntu (wsl2).
---
Инструкция для запуска:
1) Произведите клонирование данного репозитория на локальный компьтер (`git clone https://github.com/annapyanova/facew.git`).
2) Откройте терминал **wsl2** и перейдите в дирректорию **facew**.
  
      ![image](https://user-images.githubusercontent.com/90253693/169549078-1f5e1a8e-0c8d-48a7-bdc9-a51ef7905052.jpg)

3) Выполните команду `sudo docker-compose build` для сборки проекта.
4) После завершения сборки выполните `sudo docker-compose up` для поднятия докер-контейнеров.
5) Для просмотра результата используйте браузер ***Mozila Firefox***.
6) Откройте его и перейдите по адресу [localhost:5000](http://localhost:5000/).
7) Через несколько секунд на веб-странице начнётся транслирование видео.
     
     ![image](https://user-images.githubusercontent.com/90253693/169554977-64720270-91ad-4fb0-b09e-d868002e7537.jpg)

8) Для запуска тестов выполните команду `python3 -m pytest` **(не останавливая докер-контейнеры)**, после чего будет получено сообщение об успешном прохождении 5 тестов.

   ![image](https://user-images.githubusercontent.com/90253693/169556039-c2d1096f-35e1-461f-af7f-e08204086f7c.png)
 
