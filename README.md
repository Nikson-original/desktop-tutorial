<h1>1. Название проекта</h1>
Animal-Scanner
<h1>2. Описание (README.md)</h1>
<p>Программа для опознания животного по фото</p>
<p>Березовский Богдан, Кирилл Фёдоров</p>
<p>Основные функции:</p>
<p>Генерация названия животного и информации о нём</p>
<h1>3. Структура проекта</h1>
<p>app.py: Главный файл для запуска.</p>
<p>index.html и index.css (для веб-приложений): Статические файлы и шаблоны.</p>
<p>uploads: для хранения фото, и загрузки их оттуда</p>
<h1>4. Инструкции по запуску</h1>
<p>pip install tensorflow opencv-python matplotlib flask numpy werkzeug установить в cmd</p>
<p>Запустить Visual Studio Code, открыть папку проекта, выбрать файл app.py, запустить код (Ctrl+alt+N), перейти по указаному id в коммандной строке, а точнее http://127.0.0.1:5000</p>
<h1>5. Примеры использования</h1>
<p>Заходите на сайт, нажимаете choose file, выбираете, выгружается процентное соотношение породы, или животного, на кого похоже, выводится 5 результатов.</p>
<h1>6. Технические требования</h1>
<p>Зависит от версии Python</p>
<h1>7. Лицензия</h1>
---
<h1>8. Контакты</h1>
bohdan.berezovskyi@ivkhk.ee
kirill.fjodorov@ivkhk.ee
<h1>Объяснение кода:</h1>
<p>from flask import Flask, request, render_template, jsonify, send_from_directory: Импортируются необходимые модули из фреймворка Flask для создания веб-приложения:
</p>
<p>Flask: Создает объект приложения Flask.</p>
<p>request: Используется для получения информации из HTTP запросов.</p>
<p>render_template: Для рендеринга HTML шаблонов.</p>
<p>jsonify: Для преобразования Python объектов в формат JSON для отправки ответов клиенту.</p>
<p>send_from_directory: Для отправки файлов из указанной директории.</p>
<p>import os: Модуль для взаимодействия с операционной системой (создание директорий и т.д.).</p>
<p>import numpy as np: NumPy используется для работы с массивами данных.</p>
<p>import cv2: OpenCV - библиотека компьютерного зрения для обработки изображений.</p>
<p>from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions: Импортируются модель MobileNetV2, функции для предобработки изображений и декодирования предсказаний из TensorFlow.</p>
<p>from werkzeug.utils import secure_filename: Функция для безопасного создания имен файлов.</p>
<h2>Инициализация приложения и модели:</h2>
<p>app = Flask(__name__): Создается объект Flask приложения.</p>
<p>model = MobileNetV2(weights='imagenet'): Загружается предобученная модель MobileNetV2, которая обучена на большом наборе данных изображений ImageNet.</p>
<p>UPLOAD_FOLDER = 'uploads': Определяется папка для сохранения загруженных изображений.</p>
<p>if not os.path.exists(UPLOAD_FOLDER): os.makedirs(UPLOAD_FOLDER): Создается папка для загрузок, если она еще не существует.</p>
<h2>Функция для предсказания породы животного:</h2>
<p>def predict_animal(image_path):: Эта функция принимает путь к изображению и возвращает список предсказанных пород с вероятностями.
Загрузка и предобработка изображения: Изображение считывается, преобразуется в формат, подходящий для модели, и изменяется размер.
Предсказание: Модель делает предсказание на основе предобработанного изображения.
Декодирование предсказаний: Результаты предсказания преобразуются в понятный формат (порода, вероятность).</p>
<h2>Маршруты приложения:</h2>
<p>/uploads/<filename>: Этот маршрут используется для отдачи загруженных изображений клиенту.</p>
<p>/: Корневой маршрут, который отображает главную страницу (вероятно, HTML шаблон).</p>
<p>/predict (POST запрос): Этот маршрут обрабатывает загрузку изображений пользователем.
Проверяется, что пользователь загрузил файл.
Загруженный файл сохраняется в указанную папку.
Вызывается функция predict_animal для получения предсказаний.
Формируется JSON ответ с результатами предсказаний и ссылкой на загруженное изображение.</p>
<p>if __name__ == '__main__':: Проверяется, выполняется ли скрипт напрямую или импортируется как модуль.</p>
<p>app.run(debug=True): Запускается сервер Flask в режиме отладки.</p>
