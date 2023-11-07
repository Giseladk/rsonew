import streamlit as st 
from streamlit_option_menu import option_menu
from PIL import Image


st.set_page_config(page_title="ONEW MEDICAL CENTER", layout="wide")

# Header
st.title("ONEW MEDICAL CENTER")

# sidebar
with st.sidebar:
    selected=option_menu(
        menu_title="Main Menu",
        options=["Home","Formulir Pendaftaran Pasien","UGD","Rawat Inap","Rawat Jalan"],
        icons=["house","chat-text-fill","tree","book","house"],
        )

if selected == "Home":
    col1, col2, col3 = st.columns(3)
    with col1:
        header = st.image("rs1.jpeg", caption="jalan Mlatiharjo 1 no.431A, Mlatibaru, Semarang Timur, Kota Semarang, Jawa Tengah", use_column_width=True,)
    with col2:
        st.info(":phone: 08136578")
        st.info(":mailbox: rsonew12@gmail.com")
    with col3:
        st.info("Call Center/Saran")
        contact_form = """
        <form action="https://formsubmit.co/mgiselladk@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here"></textarea> 
            <button type="submit">Send</button>
        </form> 
        """
        st.markdown(contact_form, unsafe_allow_html=True)
    
    st.title(f"Selamat Datang di Onew Medical Center")
    st.subheader("Berdedikasi atas sumpah profesi untuk membangun negeri")
    st.write("Onew Medical Center merupakan salah satu pusat kesehatan terbesar yang ada di Indonesia. Onew Medical Center merupakan satu-satunya pusat kesehatan terbesar di Jawa Tengah yang berlokasi di Semarang. Pusat kesehatan ini berdiri sejak tahun 1980 dengan inovasi serta perkembangan yang selalu mengikuti zaman.")
    

if selected == "Formulir Pendaftaran Pasien":
    col1, col2, = st.columns(2)
    with col1:
        header = st.image("rsonew1.jpg", width="1200", use_column_width=True)

    st.subheader(f"Pendaftaran Pasien Baru")
    st.markdown('''

        ''')
    my_form = st.form(key = "form1")
    name = my_form.text_input(label = "Nama Pasien")
    number = my_form.slider("umur", min_value=10, max_value = 100 )
    name = my_form.text_input(label = "Jenis Kelamin")
    name = my_form.text_input(label = "Agama")
    name = my_form.text_input(label = "Alamat")
    name = my_form.text_input(label = "Telepon")
    name = my_form.text_input(label = "Pekerjaan")
    name = my_form.text_area(label = "Keterangan")
    button = my_form.form_submit_button(label = "Submit")

   
if selected == "UGD":
    st.title(f"Selamat Datang di Menu {selected}")
    st.subheader(f"Unit Gawat Darurat (UGD) Onew Medical Center")
    st.markdown('''

        ''')

    image= Image.open('ugd1.jpeg')
    st.image(image, width=500, caption='Pusat Onew Medical Center')
    st.markdown('''


        ''')

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.info('''
        **Unit Gawat Darurat (UGD) merupakan salah satu unit dalam rumah sakit yang menyediakan penanganan awal pasien, 
        sesuai dengan tingkat kegawatannya. Seorang petugas screening akan memilah pasien ke dalam kelompok triase. 
        Adapun kelompok triase tersebut terdiri dari; triase merah, triase kuning, triase hijau, dan triase hitam.**
        ''')

    with col2:
        image = Image.open('ugd2.jpeg')
        st.image(image, width=300, caption='UGD Onew Medical Center')

    st.markdown('''


        ''')

    col1, col2 = st.columns(2, gap="small")
    with col1:
        image = Image.open('ugd3.jpeg')
        st.image(image, width=250, caption='Bangsal UGD Onew Medical Center')

    with col2:
        st.info('''
            **Dalam penerapannya, Onew Medical Center memiliki Unit Gawat Darurat yang paling besar di wilayah Jawa Tengah.
            Sebagai pusat kesehatan, Onew Medical Center berupaya mengembangkan Unit Gawat Darurat (UGD) yang dapat menampung 
            pasien serta memberikan pasien pelayanan secepat dan sebaik mungkin sesuai dengan standar SOP.** 
            ''')
    st.markdown('''

    
        ''')

    st.info('''
        **Unit Gawat Darurat dalam Onew Medical Center, tak hanya melayani pasien umum saja, melainkan pasien rujukan, pasien BPJS, dan pasien 
        pindahan. Selain dengan fasilitasnya yang sangat memadai, unit ini juga dikenal akan tenaga medis yang cekatan dalam menagani pasien. 
        Sesuai dengan motto kami, bahwa kami 'Berdedikasi atas sumpah profesi, untuk membangun negeri.**
        ''')

if selected == "Rawat Inap":
    st.title(f"Selamat Datang di Menu {selected}")
    st.subheader(f"Unit Rawat Inap Onew Medical Center")
    st.info('''
        **Unit Rawat Inap (URI) atau Instalasi Rawat Inap (IRNA) merupakan salah satu bagian pelayanan klinis yang melayani pasien karena 
        keadaannya harus dirawat selama 1 hari atau lebih. Rawat inap sendiri merupakan pelayanan terhadap pasien yang masuk ke rumah sakit 
        dengan menggunakan tempat tidur untuk keperluan observasi, diagnosis, terapi, rehabilitasi medik dan penunjang medik lainnya**
        ''')
    st.markdown('''


        ''')
    st.info('''
        Unit rawat inap (URI) pada Onew Medical Center terletak di lantai 1, lantai 2, dan lantai 3. Pada unit ini, Onew Medical Center membagi
        menjadi tiga kelas, yaitu kelas pertama yang terletak di lantai 3, kelas kedua yang terletak di lantai dua, dan kelas ketiga yang terletak 
        di lantai 3. Dalam masing-masing kelas, terdapat beberapa ruangan dengan masing-masing nama. Kelas pertama dengan lima ruangan, yaitu 
        ''')
    st.subheader("Fasilitas Ruang Rawat Inap")
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        image = Image.open('rawatinap1.jpeg')
        st.image(image, width=250, caption='Bangsal Rawat inap Onew Medical Center')
    with col2:
        image = Image.open('rawatinap2.jpeg')
        st.image(image, width=250, caption='Bangsal Rawat inap Onew Medical Center')
    with col3:
        image = Image.open('rawatinap3.jpeg')
        st.image(image, width=250, caption='Bangsal Rawat inap Onew Medical Center')


    
        
if selected == "Rawat Jalan":
    st.title(f"Selamat Datang di Menu {selected}")
    st.subheader(f"Unit Rawat Jalan Onew Medical Center")
    st.write(f"Unit Rawat Jalan (URJ) merupakan unit yang melayani tindakan observasi, diagnosis, pengobatan, dan fisioterapi. Unit Rawat Jalan (URJ) adalah pelayanan kesehatan yang dilakukan tanpa pasien menginap. Pelayanan ini termasuk salah satu indikator penting yang sangat diperhatikan.")
    
    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        image = Image.open('rawatjalan1.jpeg')
        st.image(image, width=250, caption='Pelayanan pasien rawat jalan Onew Medical Center')
    with col2:
        image = Image.open('rawatjalan2.jpeg')
        st.image(image, width=250, caption='Pelayanan pasien rawat jalan Onew Medical Center')
    with col3:
        image = Image.open('rawatjalan3.jpeg')
        st.image(image, width=250, caption='Pelayanan pasien rawat jalan Onew Medical Center')

    st.info("Fasilitas Onew Medical Center Lainnya")
    
    st.image("lain1.jpeg", width="1200", caption="Resepsionis Onew Medical Center", use_column_width=True)
    st.image("lain2.jpeg", width="1200", caption="Ruang ICU Onew Medical Center", use_column_width=True)
    st.image("lain3.jpeg", width="1200", caption= "Ruang Konsultasi Onew Medical Center",use_column_width=True)





