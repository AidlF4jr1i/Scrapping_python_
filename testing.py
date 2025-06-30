import requests

# URL target tetap sama, namun parameter akan dikirim via POST
url = 'https://id.indeed.com/jobs'

# Kita gunakan 'data' bukan 'params'. Ini adalah payload untuk POST.
# Tambahkan juga parameter yang ditemukan dari inspect element.
payload = {
    'q': 'Python',
    'l': 'Palembang',
    'radius': '25',
    'from': 'searchOnDesktopSerp'
}

# Header Anda sudah bagus, kita gunakan kembali
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

session = requests.Session()

try:
    # Langkah pertama (mengunjungi halaman utama) tetap sama, menggunakan GET
    print("Mengunjungi halaman utama untuk mengambil cookies...")
    session.get('https://id.indeed.com/', headers=headers)
    print("Berhasil mengunjungi halaman utama.")

    # Langkah kedua: Lakukan pencarian menggunakan metode POST
    print("Melakukan pencarian pekerjaan dengan metode POST...")
    # Perhatikan perubahan dari .get ke .post dan dari params= ke data=
    res = session.post(url, data=payload, headers=headers)

    print(f"Status Code Akhir: {res.status_code}")

    if res.status_code == 200:
        print("🎉 Berhasil! Halaman hasil pencarian berhasil diakses.")
        # Anda bisa menyimpan hasilnya ke file HTML untuk dilihat
        with open('indeed_results.html', 'w', encoding='utf-8') as f:
            f.write(res.text)
        print("Hasil telah disimpan ke 'indeed_results.html'")
    else:
        print(f"Gagal. Server memberikan status {res.status_code}.")
        print("Ini mungkin berarti ada perlindungan lain seperti CAPTCHA.")

except requests.exceptions.RequestException as e:
    print(f"Terjadi error koneksi: {e}")