from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Параметры подключения к БД (из переменных окружения или по умолчанию)
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'appdb')
DB_USER = os.getenv('DB_USER', 'appuser')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'SecurePass123!')

@app.route('/')
def hello():
    return "Hello, DevOps Journey! 🚀"

@app.route('/db-check')
def db_check():
    try:
        # Подключение к PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.close()
        return "✅ Connection to PostgreSQL successful!"
    except Exception as e:
        return f"❌ Database connection failed: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
