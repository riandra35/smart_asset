from flask import Blueprint, render_template, request, jsonify
from db_config import supabase

# Inisialisasi Blueprint untuk modul pengguna
user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def list_users():
    try:
        # Menjalankan DML SELECT untuk mengambil data pengguna[cite: 2]
        response = supabase.table('users').select('*').order('id').execute()
        users_data = response.data
    except Exception as e:
        users_data = []
        print(f"Error: {e}")
    return render_template('users/list.html', users=users_data)

@user_bp.route('/api/users/add', methods=['POST'])
def add_user():
    data = request.json
    try:
        # Menjalankan DML INSERT untuk data pengguna baru[cite: 2]
        supabase.table('users').insert({
            "nama_lengkap": data.get('nama_lengkap'),
            "email": data.get('email'),
            "role": data.get('role', 'Staff')
        }).execute()
        return jsonify({"status": "success", "message": "Pengguna berhasil ditambahkan!"})
    except Exception as e:
        # Menangani error, termasuk pelanggaran constraint unique pada email
        return jsonify({"status": "error", "message": str(e)}), 500

@user_bp.route('/api/users/edit/<int:id>', methods=['POST'])
def edit_user(id):
    data = request.json
    try:
        # Menjalankan DML UPDATE untuk merubah data pengguna[cite: 2]
        supabase.table('users').update({
            "nama_lengkap": data.get('nama_lengkap'),
            "email": data.get('email'),
            "role": data.get('role')
        }).eq('id', id).execute()
        return jsonify({"status": "success", "message": "Data pengguna diperbarui!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@user_bp.route('/api/users/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        # Menjalankan DML DELETE untuk menghapus data pengguna[cite: 2]
        supabase.table('users').delete().eq('id', id).execute()
        return jsonify({"status": "success", "message": "Pengguna berhasil dihapus!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
