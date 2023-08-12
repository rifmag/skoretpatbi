import streamlit as st
from streamlit_option_menu import option_menu

# navigasi sidebar
with st.sidebar :
    selected = option_menu ('Hitung Nilai Hasil CAT',
    ['Hitung Nilai TPA',
     'Hitung Nilai TBI'],                     
    default_index=0)

# halaman hitung nilai TPA
if (selected == 'Hitung Nilai TPA') :
    st.title ('Hitung Nilai TPA')

# Masukkan nilai-nilai verbal, numerikal, dan figural
    nilai_verbal = st.number_input ("Masukkan Nilai Verbal", 0)
    nilai_numerikal = st.number_input ("Masukkan Nilai Numerikal", 0)
    nilai_figural = st.number_input ("Masukkan Nilai Figural", 0)

    Hitung = st.button('Hitung Nilai TPA')

    if Hitung :
        rata_rata = (nilai_verbal + nilai_numerikal + nilai_figural) / 3
        nilai_tpa = ((rata_rata / 100)*600)+200

    
        st.markdown(f'<p style="font-size: 24px;">Nilai TPA Anda Adalah= {round(nilai_tpa, 2)}</p>', unsafe_allow_html=True)

if (selected == "Hitung Nilai TBI") :
    st.title('Hitung Nilai TBI')

    # Nilai asli dan nilai konversi untuk Listening
    nilai_listening = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
    konversi_listening = [24, 25, 26, 27, 28, 29, 30, 31, 32, 32, 33, 35, 37, 38, 39, 41, 41, 42, 43, 44, 45, 45, 46, 47, 47, 48, 48, 49, 49, 50, 51, 51, 52, 52, 53, 54, 54, 55, 56, 57, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67, 68]

    # Nilai asli dan nilai konversi untuk Structure
    nilai_structure = [0, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 22.5, 25, 27.5, 30, 32.5, 35, 37.5, 40, 42.5, 45, 47.5, 50, 52.5, 55, 57.5, 60, 62.5, 65, 67.5, 70, 72.5, 75, 77.5, 80, 82.5, 85, 87.5, 90, 92.5, 95, 97.5, 100]
    konversi_structure = [20, 20, 21, 22, 23, 25, 26, 27, 29, 31, 33, 35, 36, 37, 38, 40, 40, 41, 43, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 63, 65, 67, 68]

    # Nilai asli dan nilai konversi untuk Reading
    nilai_reading = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
    konversi_reading = [21, 22, 23, 23, 24, 25, 26, 27, 28, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 43, 44, 45, 46, 46, 47, 48, 48, 49, 50, 51, 52, 52, 53, 54, 54, 55, 56, 57, 58, 59, 60, 61, 63, 65, 66, 67]

    # Buat dictionary konversi untuk setiap variabel
    konversi_dict = {
    'Listening': dict(zip(nilai_listening, konversi_listening)),
    'Structure': dict(zip(nilai_structure, konversi_structure)),
    'Reading': dict(zip(nilai_reading, konversi_reading))
    }

    # Fungsi untuk mengkonversi nilai asli ke nilai konversi
    def konversi_nilai(variabel, nilai_asli):
        return konversi_dict[variabel][nilai_asli]


    # Fungsi konversi_nilai dan konversi_dict seperti yang telah diberikan sebelumnya

    # Input nilai dari pengguna
    nilai_input = float(st.text_input ("Masukkan Nilai Listening", 0))
    nilai_asli = nilai_input
    nilai_konversi_listening = konversi_nilai('Listening', nilai_asli)

    nilai_input1 = float(st.text_input ("Masukkan Nilai Structure", 0))
    nilai_asli = nilai_input1
    nilai_konversi_structure = konversi_nilai('Structure', nilai_asli)

    nilai_input2 = float(st.text_input ("Masukkan Nilai Reading", 0))
    nilai_asli = nilai_input2
    nilai_konversi_reading = konversi_nilai('Reading', nilai_asli)

    # Menghitung nilai akhir
    Hitung = st.button('Hitung Nilai TBI')

    if Hitung :
        nilai_akhir = (nilai_konversi_listening  + nilai_konversi_structure  + nilai_konversi_reading )/3 * 10
        st.markdown(f'<p style="font-size: 24px;">Nilai TBI Anda Adalah= {round(nilai_akhir, 2)}</p>', unsafe_allow_html=True)

    
