from flask import Blueprint, render_template, request, jsonify
from db_config import supabase

asset_bp = Blueprint('asset', __name__)

@asset_bp.route('/assets', methods=['GET'])
def list_assets():
    try:
        # Menjalankan DML SELECT untuk membaca seluruh data[cite: 2]
        response = supabase.table('assets').select('*').order('id').execute()
        assets_data = response.data
    except Exception as e:
        assets_data = []
        print(f"Error: {e}")
    return render_template('assets/list.html', assets=assets_data)

@asset_bp.route('/assets/add', methods=['POST'])
def add_asset():
    data = request.json
    thn_pengadaan = data.get('thn_pengadaan')
    
    try:
        # Menjalankan DML INSERT untuk data baru[cite: 2]
        supabase.table('assets').insert({
            "nama_aset": data.get('nama_aset'),
            "kategori": data.get('kategori'),
            "status": data.get('status', 'Tersedia'),
            "lokasi": data.get('lokasi'),
            "thn_pengadaan": thn_pengadaan if thn_pengadaan else None
        }).execute()
        return jsonify({"status": "success", "message": "Data berhasil ditambahkan!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@asset_bp.route('/assets/edit/<int:id>', methods=['POST'])
def edit_asset(id):
    data = request.json
    thn_pengadaan = data.get('thn_pengadaan')
    
    try:
        # Menjalankan DML UPDATE untuk merubah data[cite: 2]
        supabase.table('assets').update({
            "nama_aset": data.get('nama_aset'),
            "kategori": data.get('kategori'),
            "status": data.get('status'),
            "lokasi": data.get('lokasi'),
            "thn_pengadaan": thn_pengadaan if thn_pengadaan else None
        }).eq('id', id).execute()
        return jsonify({"status": "success", "message": "Data berhasil diperbarui!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@asset_bp.route('/assets/delete/<int:id>', methods=['DELETE'])
def delete_asset(id):
    try:
        # Menjalankan DML DELETE untuk menghapus data[cite: 2]
        supabase.table('assets').delete().eq('id', id).execute()
        return jsonify({"status": "success", "message": "Data berhasil dihapus!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
