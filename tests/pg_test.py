import psycopg2
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

bu hatayı koplayaıp bana atsana 
# Bağlantı bilgileri
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')  

try:
    # Bağlantıyı kur
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=db_user,
        password=db_password,
        sslmode='require',
    )
    
    # Bağlantı başarılıysa
    print("✅ Veritabanına bağlantı başarılı!")

    # Basit bir sorgu (örneğin versiyon bilgisi)
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print("PostgreSQL Versiyonu:", version)

except Exception as e:
    print("❌ Bağlantı hatası:", e)

finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("🔌 Bağlantı kapatıldı.")
