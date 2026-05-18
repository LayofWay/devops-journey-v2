# === БАЗОВЫЙ ОБРАЗ ===
# Используем официальный лёгкий образ Python
FROM python:3.12-slim

# === МЕТАДАННЫЕ ===
# Информация об образе (не обязательно, но полезно)
LABEL maintainer="layway@example.com"
LABEL description="Flask app for DevOps Journey v2"

# === РАБОЧАЯ ПАПКА ===
# Все следующие команды будут выполняться в этой папке внутри контейнера
WORKDIR /app

# === ЗАВИСИМОСТИ ===
# Копируем файл зависимостей ПЕРЕД кодом (для кеширования слоёв)
COPY requirements.txt .

# Устанавливаем библиотеки
# --no-cache-dir уменьшает размер образа
RUN pip install --no-cache-dir -r requirements.txt

# === КОД ПРИЛОЖЕНИЯ ===
# Копируем исходный код в контейнер
COPY app.py .

# === СЕТЬ ===
# Открываем порт 5000 для внешних подключений
EXPOSE 5000

# === ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ ===
# Значения по умолчанию (можно переопределить при запуске)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV DB_HOST=localhost
ENV DB_NAME=appdb
ENV DB_USER=appuser
ENV DB_PASSWORD=SecurePass123!

# === КОМАНДА ЗАПУСКА ===
# Что выполнить при старте контейнера
CMD ["python", "app.py"]
