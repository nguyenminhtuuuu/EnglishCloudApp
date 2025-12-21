import cloudinary
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)  # định vị vị trí của project hiện tại
app.secret_key = 'S@mpleSecretKey123!@#' # Bạn có thể đặt chuỗi tùy ý

# --- CẤU HÌNH DATABASE CHO AWS RDS ---
# Định dạng: mysql+pymysql://user:password@endpoint/db_name
DB_USER = os.environ.get("DB_USER", "cloud")
DB_PASS = os.environ.get("DB_PASS", "Abc123456")
DB_HOST = os.environ.get("DB_HOST", "edb.c35vmpiylecj.us-east-1.rds.amazonaws.com") # Đây sẽ là Endpoint của RDS
DB_NAME = os.environ.get("DB_NAME", "edb")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8

db = SQLAlchemy(app)

# Cấu hình Cloudinary (Nên đưa API Key vào biến môi trường để bảo mật)
cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_NAME", "deeqcwnpm"),
    api_key=os.environ.get("CLOUDINARY_API_KEY", "642514279843968"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET", "iOM3oFrZpEwBIrnkHdaPfmT8njY")
)

login = LoginManager(app)

