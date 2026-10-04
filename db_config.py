import os
from supabase import create_client, Client

# Mengambil kredensial dengan aman dari Environment Variables
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# Memastikan kredensial tersedia sebelum aplikasi berjalan
if not url or not key:
    raise ValueError("SUPABASE_URL dan SUPABASE_KEY belum dikonfigurasi di Environment Variables!")

# Menginisialisasi klien Supabase
supabase: Client = create_client(url, key)
