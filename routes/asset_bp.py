from flask import Blueprint, render_template, request, redirect, url_for
from db_config import supabase  # Mengambil koneksi Supabase dari file Step 2

# Menginisialisasi Blueprint untuk fitur aset
asset_bp = Blueprint('asset', __name__)

# Rute DML SELECT: Mengambil dan menampilkan semua daftar aset
@asset_bp.route('/assets', methods=['GET'])
def list_assets():
    try:
        # Eksekusi DML SELECT via supabase client[cite: 1]
        response = supabase.table('assets').select('*').execute()
        assets_data = response.data
    except Exception as e:
        assets_data = []
        print(f"Error fetching data: {e}")
        
    # Mengirim data aset ke template HTML
    return render_template('assets/list.html', assets=assets_data)

# Rute DML INSERT: Menangani form penambahan aset baru[cite: 1]
@asset_bp.route('/assets/add', methods=['GET', 'POST'])
def add_asset():
    if request.method == 'POST':
        # Mengambil input dari formulir HTML
        nama_aset = request.form.get('nama_aset')
        kategori = request.form.get('kategori')
        status = request.form.get('status', 'Tersedia')
        lokasi = request.form.get('lokasi')

        # Eksekusi DML INSERT via supabase client[cite: 1]
        supabase.table('assets').insert({
            "nama_aset": nama_aset,
            "kategori": kategori,
            "status": status,
            "lokasi": lokasi
        }).execute()

        # Setelah berhasil ditambah, arahkan kembali ke halaman daftar aset
        return redirect(url_for('asset.list_assets'))

    # Jika request GET, tampilkan form input kosong
    return render_template('assets/form.html')
