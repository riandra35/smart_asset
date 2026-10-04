from flask import Blueprint, render_template, request, redirect, url_for
from db_config import supabase  # Mengimpor modul koneksi Supabase

# Menginisialisasi Blueprint untuk fitur pengelolaan user (pegawai)
user_bp = Blueprint('user', __name__)

# Rute DML SELECT: Mengambil dan menampilkan semua data pengguna
@user_bp.route('/users', methods=['GET'])
def list_users():
    try:
        # Menarik data dari tabel 'users' di Supabase
        response = supabase.table('users').select('*').execute()
        users_data = response.data
    except Exception as e:
        users_data = []
        print(f"Error fetching user data: {e}")
        
    # Mengirim data pengguna ke template HTML (yang nantinya akan Anda buat)
    return render_template('users/list.html', users=users_data)

# Rute DML INSERT: Menangani form penambahan pengguna baru
@user_bp.route('/users/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Mengambil input dari formulir HTML pengguna
        nama_lengkap = request.form.get('nama_lengkap')
        email = request.form.get('email')
        role = request.form.get('role', 'Staff')  # Default 'Staff' jika kosong

        # Eksekusi DML INSERT ke Supabase
        try:
            supabase.table('users').insert({
                "nama_lengkap": nama_lengkap,
                "email": email,
                "role": role
            }).execute()
        except Exception as e:
            print(f"Error inserting user: {e}")
            # Anda bisa menambahkan logika notifikasi/flash di sini jika email sudah ada

        # Setelah berhasil, arahkan kembali ke daftar pengguna
        return redirect(url_for('user.list_users'))

    # Jika request GET, tampilkan form input kosong (template yang nantinya dibuat)
    return render_template('users/form.html')
