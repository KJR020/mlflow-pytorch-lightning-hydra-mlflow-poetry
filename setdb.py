import mlflow
import sqlite3
import os

DB_PATH = "db/mlruns.db"
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)  # 親ディレクトリなければ作成
conn = sqlite3.connect(DB_PATH)  # バックエンド用DBを作成
