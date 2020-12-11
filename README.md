# Django_app_SQL_filters

Проект размещен на сервер (Yandex Cloud) и доступен по публичному адресу: http://130.193.56.29/
*В файле nginx.conf описаны настройки nginx для сервера.

ТЗ:
 1. Весь проект Django состоит из одного приложения.
 2. Необходимо описать модель автомобиля (Car) с полями:
      - производитель (BMW, Audi, Tesla и т.д.) (CharField)
      - модель авто (S, TT, X6 и т.д.) (CharField)
      - год выпуска (IntegerField)
      - коробка передач (SmallIntegerField with choices "механика", "автомат", "робот")
      - цвет
 3. Необходимо создать главную страницу со списком автомобилей.
 4. На главной странице создать форму «фильтрации» (поиска) автомобилей.
 5. GET-запросом отправлять данные о фильтрах.
 6. Во view собирать запрос с помощью Q-объектов и отображать авто на главной с учётом фильтров.


Функционал:
1. Отоброжение инфомации об автомобилях из БД.
2. Возможность фильтрации отоброжаемых карточек с автомобилями при помощи формы поиска.

![Screen](/screenshots/screen_1.png)


Разворачиваем проект локально:

1. Скачайте репозиторий
2. Создайт виртуальное окружение:
          
        python -m venv env
       
3. Активируйте виртуальное окружение: 

        source env/bin/activate
        
4. Чтобы установить все требуемые библиотеки python в новом окружении выполните команду: 

        pip install -r requirements.txt
   
   Если у вас macOS до выполнения команды pip install -r requirements.txt выполните команду:       
   
           env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2==2.8.4      
   
   Для предотвращения появления ошибки (error: command 'gcc' failed with exit status 1.) при установке зависимостей.

5. Для работы проекта заполните переменную SECRET_KEY в файле settings.py,создав файл переменных окружения (.env) с ее значением.

6. Раскомментируйте насройки бд (DATABASE) в файле homework/settings.py и закомментируйте настройки бд для сервера.

7. Чтбы запустить сервер введите команду: 

       python manage.py runserver

8. Для входа в администравтивную панель проекта создайте суперпользователя при помощи команды: 

       python manage.py createsuperuser
