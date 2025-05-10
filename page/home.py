import streamlit as st

def show_home():
    with st.container():    
        st.markdown(
            """
            <h1 style='text-align: center; color:#9F8335'>Diamond Price Prediction Application</h1>
            <p style='text-align: center; font-style: italic;'>&ldquo;Bersinar dalam Data, Tepat dalam Harga&rdquo;</p>
            """,
            unsafe_allow_html=True
        )

    col1, col2, col3 = st.columns([10, 20, 10])

    with col2:
        st.image('logo/logo_diamond.png')

    with st.container():
        tab1, tab2, tab3 = st.tabs([
            'Tentang Aplikasi', 
            'Panduan Penggunaan', 
            'Tentang Berlian'
        ])

        with tab1:
            tab1.markdown('<h1 style="color:#9F8335;">Tentang Aplikasi</h1>', unsafe_allow_html=True)
            tab1.write("""Diamond Price Prediction adalah sebuah aplikasi berbasis website yang berfungsi untuk memprediksi harga berlian berdasarkan atribut-atribut tertentu. 
                        Pengguna dapat memasukkan informasi tentang warna (color), potongan (cut), kejernihan (clarity), carat, serta dimensi (depth, table, x, y, z) dari berlian. 
                        Saat ini, aplikasi ini dapat memberikan estimasi harga berlian yang akurat berdasarkan data yang diberikan. Aplikasi ini masih dalam tahap pengembangan 
                        dan tentunya membutuhkan kritik serta saran dari pengguna untuk penyempurnaan lebih lanjut.
            """)

        with tab2:
            tab2.markdown('<h1 style="color:#9F8335;">Cara Menggunakan Aplikasi</h1>', unsafe_allow_html=True)
            tab2.markdown('<h3 style="color:#9F8335;">Langkah 1: Masukkan Informasi Berlian</h3>', unsafe_allow_html=True)
            tab2.write("1. Pilih atribut berlian yang ingin Anda prediksi harganya, seperti warna (color), potongan (cut), kejernihan (clarity), carat, dan dimensi (depth, table, x, y, z).")
            tab2.write("2. Masukkan nilai untuk setiap atribut berdasarkan berlian yang Anda miliki.")
            tab2.write("3. Pastikan semua informasi telah diisi dengan benar sebelum melanjutkan.")
            tab2.image('assets/tahapan_1.gif')

            tab2.markdown('<h3 style="color:#9F8335;">Langkah 2: Lakukan Prediksi Harga</h3>', unsafe_allow_html=True)
            tab2.write("1. Klik tombol 'Prediksi Harga' untuk memulai proses prediksi.")
            tab2.write("2. Tunggu beberapa saat hingga aplikasi selesai menghitung dan memberikan estimasi harga berlian.")
            tab2.write("3. Prediksi harga akan ditampilkan di halaman yang sama.")
            tab2.image('assets/tahapan_2.gif')

            tab2.markdown('<h3 style="color:#9F8335;">Langkah 3: Tinjau Hasil Prediksi</h3>', unsafe_allow_html=True)
            tab2.write("1. Di halaman Prediksi, Anda akan melihat estimasi harga berlian berdasarkan data yang telah dimasukkan.")
            tab2.write("2. Selain itu, pada halaman ini juga menampilkan data yang Anda masukkan sebelumnya.")
            tab2.image('assets/tahapan_3.gif')

            tab2.markdown('<h3 style="color:#9F8335;">Catatan:</h3>', unsafe_allow_html=True)
            tab2.write("- Pastikan semua informasi yang Anda masukkan akurat dan sesuai dengan berlian yang Anda miliki.")
            tab2.write("- Prediksi harga berdasarkan model mungkin tidak 100% akurat. Gunakan hasil ini sebagai referensi.")

        with tab3:
            tab3.markdown('<h1 style="color:#9F8335;">Tentang Berlian</h1>', unsafe_allow_html=True)
            tab3.write("""
                    Tidak semua berlian diciptakan sama — setiap berlian itu unik. Berlian memiliki berbagai ukuran, bentuk, 
                    warna, dan karakteristik internal. Semua berlian yang sudah dipoles memiliki nilai, tergantung pada kombinasi 
                    beberapa faktor. Salah satu faktor utamanya adalah **kelangkaan** — semakin langka suatu karakteristik, semakin 
                    tinggi nilai berliannya.
            """)

            tab3.write("""
                    Untuk menilai dan membandingkan kualitas berlian, para profesional menggunakan sistem **4C** yang dikembangkan oleh **GIA 
                    (Gemological Institute of America)** pada tahun 1950-an. Sistem ini menjadi standar internasional dalam dunia perhiasan.
            """)

            tab3.write("Empat aspek utama dalam 4C adalah:")

            tab3.write("- **Clarity (Kejernihan):** Seberapa bersih berlian dari inklusi atau cacat.")
            tab3.write("- **Color (Warna):** Semakin tidak berwarna berlian, semakin tinggi nilainya.")
            tab3.write("- **Cut (Potongan):** Kualitas potongan memengaruhi kilau dan keindahan berlian.")
            tab3.write("- **Carat Weight (Berat Karat):** Ukuran berlian berdasarkan berat.")

            tab3.write("""
                    Keempat aspek ini digunakan untuk menggambarkan kualitas dan menentukan nilai berlian. Berlian dengan kombinasi 4C yang lebih 
                    tinggi biasanya lebih langka dan lebih bernilai.
            """)

            tab3.image('assets/legend_diamond.png', use_container_width=True)

            tab3.markdown("Selengkapnya mengenai berlian [di sini](https://www.gia.edu/diamond-quality-factor)")
