from flask import Flask
# Mengimpor modul-modul Blueprint yang sudah kita buat
from routes.dashboard_bp import dashboard_bp
from routes.asset_bp import asset_bp
from routes.user_bp import user_bp

# Inisialisasi Terminal Utama (Aplikasi Flask)
app = Flask(__name__)

# Mendaftarkan (Register) Blueprint ke Terminal Utama
# url_prefix opsional digunakan untuk mengelompokkan awalan URL
app.register_blueprint(dashboard_bp) 
app.register_blueprint(asset_bp, url_prefix='/api')  # Contoh: Rute aset akan menjadi /api/assets
app.register_blueprint(user_bp, url_prefix='/api')   # Contoh: Rute user akan menjadi /api/users

# Baris di bawah ini umumnya digunakan jika menjalankan Flask di server lokal
# Namun Vercel akan secara otomatis mengenali objek 'app' untuk deployment
if __name__ == '__main__':
    app.run(debug=True)
