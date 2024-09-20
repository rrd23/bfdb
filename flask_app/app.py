from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Создаём приложение Flask
app = Flask(__name__)

# Настройки для подключения к базе данных PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask_user:yourpassword@db:5432/datanum'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализируем объект базы данных
db = SQLAlchemy(app)

# Модель данных UserData
class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telegram_id = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<UserData {self.telegram_id}: {self.username}, {self.score}>'

# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# Маршрут для сохранения данных через API
@app.route('/save_score', methods=['POST'])
def save_score():
    data = request.get_json()
    telegram_id = request.headers.get('X-User-Id')
    username = data.get('username')
    score = data.get('score')

    if telegram_id and username and score is not None:
        new_data = UserData(telegram_id=telegram_id, username=username, score=score)
        db.session.add(new_data)
        db.session.commit()
        return jsonify({"message": "Счёт сохранён успешно", "score": score})
    
    return jsonify({"message": "Ошибка: данные не были переданы"}), 400

# Маршрут для получения сохранённых данных через API
@app.route('/get_score', methods=['GET'])
def get_score():
    telegram_id = request.headers.get('X-User-Id')
    user_data = UserData.query.filter_by(telegram_id=telegram_id).first()
    
    if user_data:
        return jsonify({"score": user_data.score, "username": user_data.username})
    
    return jsonify({"score": "Нет сохранённых данных"})

if __name__ == "__main__":
    # Создаём таблицы, если их ещё нет
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
