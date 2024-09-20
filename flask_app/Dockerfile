FROM python:3.11-slim

# Устанавливаем необходимые системные зависимости для сборки psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения
COPY . .

# Открываем порт для Telegram-бота
EXPOSE 8080

# Запуск Telegram-бота
CMD ["python", "app.py"]
