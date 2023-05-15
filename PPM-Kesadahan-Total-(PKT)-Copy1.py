import streamlit as st
from PIL import Image

#Memunculkan tampilan sidebar
add_selectbox = st.sidebar.selectbox("Menu :mag:",("Tentang Aplikasi","Tentang PPM Kesadahan Total","Perhitungan Nilai PPM Kesadahan Total"))

#Halaman Tentang Aplikasi 
if add_selectbox == 'Tentang Aplikasi':
    
    st.title('Penjelasan Aplikasi :computer:')
    st.image("Web Aplikasi.JPG")
    st.write('Aplikasi ini dibuat untuk mempermudah dalam melakukan perhitungan Parts Per Million Kesadahan Total (PPM Kesadahan Total) yang sering dilakukan saat melakukan suatu analisis dilaboratorium dan harus dilakukan dalam waktu yang singkat. Dengan adanya perkembangan teknologi, aplikasi perhitungan pun dapat dibuat untuk mempermudah dan meminimalisir terjadinya kesalahan dalam perhitungan PPM Kesadahan Total yang dilakukan saat proses analisis dilaboratorium. ')

#Halaman Tentang PPM Kesadahan Total
if add_selectbox == 'Tentang PPM Kesadahan Total':
    st.subheader('Penjelasan PPM Kesadahan Total')
    st.image("Rumus PPM.JPG")
    
    st.markdown("""Keterangan :\n
                 Parts Per Million Kesadahan Total (PPM Kesadahan Total) = Konsentrasi larutan yang ingin dicari dalam satuan mg/L\n
                 Molaritas titran = Konsentrasi larutan bahan baku sekunder yang digunakan\n
                 Volume titran = Volume yang didapatkan dari hasil titrasi\n
                 BM = Berat Molekul dari sampel\n
                 FP = Faktor Pengali\n
                 Volume Sampel = Volume sampel yang digunakan untuk mengetahui nilai PPM Kesadahan Total""")
                   
    st.write(' PPM merupakan singkatan dari Parts Per Million yang merupakan perbandingan antara konsentrasi zat terlarut dengan zat pelarutnya, sedangkan Kesadahan total adalah jumlah ion–ion kalsium dan magnesium dalam air yang dapat ditentukan melalui titrasi menggunakan EDTA (Etilen Diamin Tetra Asetat) sebagai titran dengan menggunakan indikator EBT, selain itu kesadahan total juga dapat dilakukan dengan proses analisis lainnya. Hasil dari analisis tersebut kemudian dilakukan perhitungan dengan mencari nilai Parts Per Million Kesadahan Total (PPM Kesadahan Total) dari sampel yang telah dianalisis dengan rumus perhitungan seperti diatas.  ')

    
#Halaman Perhitungan Nilai PPM Kesadahan Total
if add_selectbox == 'Perhitungan Nilai PPM Kesadahan Total':
    st.title('Perhitungan Nilai PPM Kesadahan Total')
    
    jumlah_digit=4
    Molaritas = st.number_input(f'Masukan Nilai Molaritas Titran (mmol/ml)', format='%.'+str(jumlah_digit)+'f')
    Volume1 = st.number_input('Masukan Nilai Volume Titran (ml)')
    Nama_BM = st.selectbox('BM (mg/mmol)', ['Pilih BM','BM CaCO3 100 mg/mmol','BM Ca 40 mg/mmol','BM MgCO3 100 mg/mmol'])
    Nilai_BM = st.selectbox('Nilai BM (mg/mmol)', ['Pilih Nilai BM',100,40,84])
    FP = st.selectbox('Nilai FP', ['Pilih Nilai FP',1,100/50,100/25,250/50,100/10])
    Volume2 = st.number_input('Masukan Nilai Volume Sampel (L)')
    Hitung = st.button('Hitung Nilai PPM Kesadahan Total')
 
    if Hitung:
        Nilai_PPM_Kesadahan_Total = (Molaritas*Volume1*Nilai_BM*FP)/Volume2
        st.success(f'Nilai PPM Kesadahan Total Adalah {Nilai_PPM_Kesadahan_Total} mg/L')
        
        