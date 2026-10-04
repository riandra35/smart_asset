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

@asset_bp.route('/assets/add', methods=['GET', 'POST'])
def add_asset():
    if request.method == 'POST':
        nama_aset = request.form.get('nama_aset')
        kategori = request.form.get('kategori')
        status = request.form.get('status', 'Tersedia')
        lokasi = request.form.get('lokasi')

        try:
            # Eksekusi DML INSERT ke Supabase
            supabase.table('assets').insert({
                "nama_aset": nama_aset,
                "kategori": kategori,
                "status": status,
                "lokasi": lokasi
            }).execute()
            return redirect(url_for('asset.list_assets'))
        except Exception as e:
            # Menampilkan detail error asli dari Supabase/Flask ke layar browser
            return f"<h1>Gagal menyimpan data!</h1><p>Pesan Error: {str(e)}</p>", 500

    return render_template('assets/form.html')
