from flask import Blueprint, render_template

# Menginisialisasi Blueprint untuk dashboard
dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def index():
    # Menampilkan halaman utama (sementara menggunakan base.html atau dashboard khusus nantinya)
    return render_template('base.html')
