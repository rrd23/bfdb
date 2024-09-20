# Используем официальный Python-образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения
COPY . .

# Открываем порт для Telegram-бота
EXPOSE 8080

# Запуск Telegram-бота
CMD ["python", "bot.py"]
