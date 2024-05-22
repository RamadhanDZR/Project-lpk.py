import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# 1. as sidebar menu
with st.sidebar:
    selected_option = option_menu("Menu Utama", options=["Beranda","Tentang Kami","Kalkulator"], icons=["house-door","person-vcard", "calculator"])

with st.sidebar.container():
    
    import json
    import requests   
    from streamlit_lottie import st_lottie

    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    lottie_hello = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_XvtPY8hkC5.json")
    st_lottie(lottie_hello, key = "hello")

if selected_option == "Beranda":
    st.header(':red[Pengertian Unsur]')

    st.write('Unsur adalah zat murni yang sudah tidak bisa dibagi lagi menjadi zat lain yang lebih sederhana dengan reaksi kimia biasa. Di dalam unsur terdapat terdapat atom-atom bermuatan, seperti proton, neutron, dan elektron. Setiap jenis unsur memiliki sifat khas yang berbeda-beda, berkaitan dengan kereaktifan, titik didih, titik lelehnya, energi ionisasi, hingga jari-jarinya. Memangnya, berapa jumlah unsur yang dikenal? Sejauh ini, terdapat 118 unsur yang sudah ditemukan. Dari total jumlah tersebut, 94 diantaranya unsur yang terbentuk secara alami dan sisanya unsur buatan.')
    import pandas as pd

    # Data unsur-unsur
    elements_data = [
        {"Symbol": "H", "Name": "Hydrogen", "Atomic Number": 1, "Atomic Weight": 1.008, "Group": 1, "Period": 1},
        {"Symbol": "He", "Name": "Helium", "Atomic Number": 2, "Atomic Weight": 4.0026, "Group": 18, "Period": 1},
        {"Symbol": "Li", "Name": "Lithium", "Atomic Number": 3, "Atomic Weight": 6.94, "Group": 1, "Period": 2},
        {"Symbol": "Be", "Name": "Beryllium", "Atomic Number": 4, "Atomic Weight": 9.0122, "Group": 2, "Period": 2},
        {"Symbol": "B", "Name": "Boron", "Atomic Number": 5, "Atomic Weight": 10.81, "Group": 13, "Period": 2},
        {"Symbol": "C", "Name": "Carbon", "Atomic Number": 6, "Atomic Weight": 12.011, "Group": 14, "Period": 2},
        {"Symbol": "N", "Name": "Nitrogen", "Atomic Number": 7, "Atomic Weight": 14.007, "Group": 15, "Period": 2},
        {"Symbol": "O", "Name": "Oxygen", "Atomic Number": 8, "Atomic Weight": 15.999, "Group": 16, "Period": 2},
        {"Symbol": "F", "Name": "Fluorine", "Atomic Number": 9, "Atomic Weight": 18.998, "Group": 17, "Period": 2},
        {"Symbol": "Ne", "Name": "Neon", "Atomic Number": 10, "Atomic Weight": 20.180, "Group": 18, "Period": 2},
        {"Symbol": "Na", "Name": "Sodium", "Atomic Number": 11, "Atomic Weight": 22.990, "Group": 1, "Period": 3},
        {"Symbol": "Mg", "Name": "Magnesium", "Atomic Number": 12, "Atomic Weight": 24.305, "Group": 2, "Period": 3},
        {"Symbol": "Al", "Name": "Aluminium", "Atomic Number": 13, "Atomic Weight": 26.982, "Group": 13, "Period": 3},
        {"Symbol": "Si", "Name": "Silicon", "Atomic Number": 14, "Atomic Weight": 28.085, "Group": 14, "Period": 3},
        {"Symbol": "P", "Name": "Phosphorus", "Atomic Number": 15, "Atomic Weight": 30.974, "Group": 15, "Period": 3},
        {"Symbol": "S", "Name": "Sulfur", "Atomic Number": 16, "Atomic Weight": 32.06, "Group": 16, "Period": 3},
        {"Symbol": "Cl", "Name": "Chlorine", "Atomic Number": 17, "Atomic Weight": 35.45, "Group": 17, "Period": 3},
        {"Symbol": "Ar", "Name": "Argon", "Atomic Number": 18, "Atomic Weight": 39.948, "Group": 18, "Period": 3},
        {"Symbol": "K", "Name": "Potassium", "Atomic Number": 19, "Atomic Weight": 39.098, "Group": 1, "Period": 4},
        {"Symbol": "Ca", "Name": "Calcium", "Atomic Number": 20, "Atomic Weight": 40.078, "Group": 2, "Period": 4},
        {"Symbol": "Sc", "Name": "Scandium", "Atomic Number": 21, "Atomic Weight": 44.956, "Group": 3, "Period": 4},
        {"Symbol": "Ti", "Name": "Titanium", "Atomic Number": 22, "Atomic Weight": 47.867, "Group": 4, "Period": 4},
        {"Symbol": "V", "Name": "Vanadium", "Atomic Number": 23, "Atomic Weight": 50.942, "Group": 5, "Period": 4},
        {"Symbol": "Cr", "Name": "Chromium", "Atomic Number": 24, "Atomic Weight": 51.996, "Group": 6, "Period": 4},
        {"Symbol": "Mn", "Name": "Manganese", "Atomic Number": 25, "Atomic Weight": 54.938, "Group": 7, "Period": 4},
        {"Symbol": "Fe", "Name": "Iron", "Atomic Number": 26, "Atomic Weight": 55.845, "Group": 8, "Period": 4},
        {"Symbol": "Co", "Name": "Cobalt", "Atomic Number": 27, "Atomic Weight": 58.933, "Group": 9, "Period": 4},
        {"Symbol": "Ni", "Name": "Nickel", "Atomic Number": 28, "Atomic Weight": 58.693, "Group": 10, "Period": 4},
        {"Symbol": "Cu", "Name": "Copper", "Atomic Number": 29, "Atomic Weight": 63.546, "Group": 11, "Period": 4},
        {"Symbol": "Zn", "Name": "Zinc", "Atomic Number": 30, "Atomic Weight": 65.38, "Group": 12, "Period": 4},
        {"Symbol": "Ga", "Name": "Gallium", "Atomic Number": 31, "Atomic Weight": 69.723, "Group": 13, "Period": 4},
        {"Symbol": "Ge", "Name": "Germanium", "Atomic Number": 32, "Atomic Weight": 72.63, "Group": 14, "Period": 4},
        {"Symbol": "As", "Name": "Arsenic", "Atomic Number": 33, "Atomic Weight": 74.922, "Group": 15, "Period": 4},
        {"Symbol": "Se", "Name": "Selenium", "Atomic Number": 34, "Atomic Weight": 78.971, "Group": 16, "Period": 4},
        {"Symbol": "Br", "Name": "Bromine", "Atomic Number": 35, "Atomic Weight": 79.904, "Group": 17, "Period": 4},
        {"Symbol": "Kr", "Name": "Krypton", "Atomic Number": 36, "Atomic Weight": 83.798, "Group": 18, "Period": 4},
        {"Symbol": "Rb", "Name": "Rubidium", "Atomic Number": 37, "Atomic Weight": 85.468, "Group": 1, "Period": 5},
        {"Symbol": "Sr", "Name": "Strontium", "Atomic Number": 38, "Atomic Weight": 87.62, "Group": 2, "Period": 5},
        {"Symbol": "Y", "Name": "Yttrium", "Atomic Number": 39, "Atomic Weight": 88.906, "Group": 3, "Period": 5},
        {"Symbol": "Zr", "Name": "Zirconium", "Atomic Number": 40, "Atomic Weight": 91.224, "Group": 4, "Period": 5},
        {"Symbol": "Nb", "Name": "Niobium", "Atomic Number": 41, "Atomic Weight": 92.906, "Group": 5, "Period": 5},
        {"Symbol": "Mo", "Name": "Molybdenum", "Atomic Number": 42, "Atomic Weight": 95.95, "Group": 6, "Period": 5},
        {"Symbol": "Tc", "Name": "Technetium", "Atomic Number": 43, "Atomic Weight": 98, "Group": 7, "Period": 5},
        {"Symbol": "Ru", "Name": "Ruthenium", "Atomic Number": 44, "Atomic Weight": 101.07, "Group": 8, "Period": 5},
        {"Symbol": "Rh", "Name": "Rhodium", "Atomic Number": 45, "Atomic Weight": 102.91, "Group": 9, "Period": 5},
        {"Symbol": "Pd", "Name": "Palladium", "Atomic Number": 46, "Atomic Weight": 106.42, "Group": 10, "Period": 5},
        {"Symbol": "Ag", "Name": "Silver", "Atomic Number": 47, "Atomic Weight": 107.87, "Group": 11, "Period": 5},
        {"Symbol": "Cd", "Name": "Cadmium", "Atomic Number": 48, "Atomic Weight": 112.41, "Group": 12, "Period": 5},
        {"Symbol": "In", "Name": "Indium", "Atomic Number": 49, "Atomic Weight": 114.82, "Group": 13, "Period": 5},
        {"Symbol": "Sn", "Name": "Tin", "Atomic Number": 50, "Atomic Weight": 118.71, "Group": 14, "Period": 5},
        {"Symbol": "Sb", "Name": "Antimony", "Atomic Number": 51, "Atomic Weight": 121.76, "Group": 15, "Period": 5},
        {"Symbol": "Te", "Name": "Tellurium", "Atomic Number": 52, "Atomic Weight": 127.6, "Group": 16, "Period": 5},
        {"Symbol": "I", "Name": "Iodine", "Atomic Number": 53, "Atomic Weight": 126.9, "Group": 17, "Period": 5},
        {"Symbol": "Xe", "Name": "Xenon", "Atomic Number": 54, "Atomic Weight": 131.29, "Group": 18, "Period": 5},
        {"Symbol": "Cs", "Name": "Cesium", "Atomic Number": 55, "Atomic Weight": 132.91, "Group": 1, "Period": 6},
        {"Symbol": "Ba", "Name": "Barium", "Atomic Number": 56, "Atomic Weight": 137.33, "Group": 2, "Period": 6},
        {"Symbol": "La", "Name": "Lanthanum", "Atomic Number": 57, "Atomic Weight": 138.91, "Group": 3, "Period": 6},
        {"Symbol": "Ce", "Name": "Cerium", "Atomic Number": 58, "Atomic Weight": 140.12, "Group": 3, "Period": 6},
        {"Symbol": "Pr", "Name": "Praseodymium", "Atomic Number": 59, "Atomic Weight": 140.91, "Group": 3, "Period": 6},
        {"Symbol": "Nd", "Name": "Neodymium", "Atomic Number": 60, "Atomic Weight": 144.24, "Group": 3, "Period": 6},
        {"Symbol": "Pm", "Name": "Promethium", "Atomic Number": 61, "Atomic Weight": 145, "Group": 3, "Period": 6},
        {"Symbol": "Sm", "Name": "Samarium", "Atomic Number": 62, "Atomic Weight": 150.36, "Group": 3, "Period": 6},
        {"Symbol": "Eu", "Name": "Europium", "Atomic Number": 63, "Atomic Weight": 151.96, "Group": 3, "Period": 6},
        {"Symbol": "Gd", "Name": "Gadolinium", "Atomic Number": 64, "Atomic Weight": 157.25, "Group": 3, "Period": 6},
        {"Symbol": "Tb", "Name": "Terbium", "Atomic Number": 65, "Atomic Weight": 158.93, "Group": 3, "Period": 6},
        {"Symbol": "Dy", "Name": "Dysprosium", "Atomic Number": 66, "Atomic Weight": 162.5, "Group": 3, "Period": 6},
        {"Symbol": "Ho", "Name": "Holmium", "Atomic Number": 67, "Atomic Weight": 164.93, "Group": 3, "Period": 6},
        {"Symbol": "Er", "Name": "Erbium", "Atomic Number": 68, "Atomic Weight": 167.26, "Group": 3, "Period": 6},
        {"Symbol": "Tm", "Name": "Thulium", "Atomic Number": 69, "Atomic Weight": 168.93, "Group": 3, "Period": 6},
        {"Symbol": "Yb", "Name": "Ytterbium", "Atomic Number": 70, "Atomic Weight": 173.05, "Group": 3, "Period": 6},
        {"Symbol": "Lu", "Name": "Lutetium", "Atomic Number": 71, "Atomic Weight": 174.97, "Group": 3, "Period": 6},
        {"Symbol": "Hf", "Name": "Hafnium", "Atomic Number": 72, "Atomic Weight": 178.49, "Group": 4, "Period": 6},
        {"Symbol": "Ta", "Name": "Tantalum", "Atomic Number": 73, "Atomic Weight": 180.95, "Group": 5, "Period": 6},
        {"Symbol": "W", "Name": "Tungsten", "Atomic Number": 74, "Atomic Weight": 183.84, "Group": 6, "Period": 6},
        {"Symbol": "Re", "Name": "Rhenium", "Atomic Number": 75, "Atomic Weight": 186.21, "Group": 7, "Period": 6},
        {"Symbol": "Os", "Name": "Osmium", "Atomic Number": 76, "Atomic Weight": 190.23, "Group": 8, "Period": 6},
        {"Symbol": "Ir", "Name": "Iridium", "Atomic Number": 77, "Atomic Weight": 192.22, "Group": 9, "Period": 6},
        {"Symbol": "Pt", "Name": "Platinum", "Atomic Number": 78, "Atomic Weight": 195.08, "Group": 10, "Period": 6},
        {"Symbol": "Au", "Name": "Gold", "Atomic Number": 79, "Atomic Weight": 196.97, "Group": 11, "Period": 6},
        {"Symbol": "Hg", "Name": "Mercury", "Atomic Number": 80, "Atomic Weight": 200.59, "Group": 12, "Period": 6},
        {"Symbol": "Tl", "Name": "Thallium", "Atomic Number": 81, "Atomic Weight": 204.38, "Group": 13, "Period": 6},
        {"Symbol": "Pb", "Name": "Lead", "Atomic Number": 82, "Atomic Weight": 207.2, "Group": 14, "Period": 6},
        {"Symbol": "Bi", "Name": "Bismuth", "Atomic Number": 83, "Atomic Weight": 208.98, "Group": 15, "Period": 6},
        {"Symbol": "Po", "Name": "Polonium", "Atomic Number": 84, "Atomic Weight": 209, "Group": 16, "Period": 6},
        {"Symbol": "At", "Name": "Astatine", "Atomic Number": 85, "Atomic Weight": 210, "Group": 17, "Period": 6},
        {"Symbol": "Rn", "Name": "Radon", "Atomic Number": 86, "Atomic Weight": 222, "Group": 18, "Period": 6},
        {"Symbol": "Fr", "Name": "Francium", "Atomic Number": 87, "Atomic Weight": 223, "Group": 1, "Period": 7},
        {"Symbol": "Ra", "Name": "Radium", "Atomic Number": 88, "Atomic Weight": 226, "Group": 2, "Period": 7},
        {"Symbol": "Ac", "Name": "Actinium", "Atomic Number": 89, "Atomic Weight": 227, "Group": 3, "Period": 7},
        {"Symbol": "Th", "Name": "Thorium", "Atomic Number": 90, "Atomic Weight": 232.04, "Group": 3, "Period": 7},
        {"Symbol": "Pa", "Name": "Protactinium", "Atomic Number": 91, "Atomic Weight": 231.04, "Group": 3, "Period": 7},
        {"Symbol": "U", "Name": "Uranium", "Atomic Number": 92, "Atomic Weight": 238.03, "Group": 3, "Period": 7},
        {"Symbol": "Np", "Name": "Neptunium", "Atomic Number": 93, "Atomic Weight": 237, "Group": 3, "Period": 7},
        {"Symbol": "Pu", "Name": "Plutonium", "Atomic Number": 94, "Atomic Weight": 244, "Group": 3, "Period": 7},
        {"Symbol": "Am", "Name": "Americium", "Atomic Number": 95, "Atomic Weight": 243, "Group": 3, "Period": 7},
        {"Symbol": "Cm", "Name": "Curium", "Atomic Number": 96, "Atomic Weight": 247, "Group": 3, "Period": 7},
        {"Symbol": "Bk", "Name": "Berkelium", "Atomic Number": 97, "Atomic Weight": 247, "Group": 3, "Period": 7},
        {"Symbol": "Cf", "Name": "Californium", "Atomic Number": 98, "Atomic Weight": 251, "Group": 3, "Period": 7},
        {"Symbol": "Es", "Name": "Einsteinium", "Atomic Number": 99, "Atomic Weight": 252, "Group": 3, "Period": 7},
        {"Symbol": "Fm", "Name": "Fermium", "Atomic Number": 100, "Atomic Weight": 257, "Group": 3, "Period": 7},
        {"Symbol": "Md", "Name": "Mendelevium", "Atomic Number": 101, "Atomic Weight": 258, "Group": 3, "Period": 7},
        {"Symbol": "No", "Name": "Nobelium", "Atomic Number": 102, "Atomic Weight": 259, "Group": 3, "Period": 7},
        {"Symbol": "Lr", "Name": "Lawrencium", "Atomic Number": 103, "Atomic Weight": 266, "Group": 3, "Period": 7},
        {"Symbol": "Rf", "Name": "Rutherfordium", "Atomic Number": 104, "Atomic Weight": 267, "Group": 4, "Period": 7},
        {"Symbol": "Db", "Name": "Dubnium", "Atomic Number": 105, "Atomic Weight": 268, "Group": 5, "Period": 7},
        {"Symbol": "Sg", "Name": "Seaborgium", "Atomic Number": 106, "Atomic Weight": 269, "Group": 6, "Period": 7},
        {"Symbol": "Bh", "Name": "Bohrium", "Atomic Number": 107, "Atomic Weight": 270, "Group": 7, "Period": 7},
        {"Symbol": "Hs", "Name": "Hassium", "Atomic Number": 108, "Atomic Weight": 269, "Group": 8, "Period": 7},
        {"Symbol": "Mt", "Name": "Meitnerium", "Atomic Number": 109, "Atomic Weight": 278, "Group": 9, "Period": 7},
        {"Symbol": "Ds", "Name": "Darmstadtium", "Atomic Number": 110, "Atomic Weight": 281, "Group": 10, "Period": 7},
        {"Symbol": "Rg", "Name": "Roentgenium", "Atomic Number": 111, "Atomic Weight": 282, "Group": 11, "Period": 7},
        {"Symbol": "Cn", "Name": "Copernicium", "Atomic Number": 112, "Atomic Weight": 285, "Group": 12, "Period": 7},
        {"Symbol": "Nh", "Name": "Nihonium", "Atomic Number": 113, "Atomic Weight": 286, "Group": 13, "Period": 7},
        {"Symbol": "Fl", "Name": "Flerovium", "Atomic Number": 114, "Atomic Weight": 289, "Group": 14, "Period": 7},
        {"Symbol": "Mc", "Name": "Moscovium", "Atomic Number": 115, "Atomic Weight": 290, "Group": 15, "Period": 7},
        {"Symbol": "Lv", "Name": "Livermorium", "Atomic Number": 116, "Atomic Weight": 293, "Group": 16, "Period": 7},
        {"Symbol": "Ts", "Name": "Tennessine", "Atomic Number": 117, "Atomic Weight": 294, "Group": 17, "Period": 7},
        {"Symbol": "Og", "Name": "Oganesson", "Atomic Number": 118, "Atomic Weight": 294, "Group": 18, "Period": 7}
    ]

    # Buat DataFrame menggunakan pandas
    df = pd.DataFrame(elements_data)

    # Tampilkan tabel periodik menggunakan Streamlit
    st.header(':red[Tabel Periodik Unsur]')
    st.write(df)
        
    #Pengertian Lambang Unsur
    st.header(':red[Lambang Unsur]')
    st.write('Jika kamu perhatikan tabel di atas, setiap unsur memiliki nama yang berbeda-beda dan umumnya berupa singkatan. Lalu, apa sih dasar penamaan unsur itu?')
    st.write('Sebenarnya, dasar penamaan unsur sudah dimulai berabad-abad silam. Namun, dasar yang digunakan menjadi tidak relevan seiring dengan penemuan unsur-unsur baru. Barulah pada tahun 1813, seorang ahli kimia asal Swedia, Jons Jacob Berzelius, mulai merumuskan penamaan unsur. Menurut Berzelius, penamaan unsur harus mengacu pada beberapa aturan berikut.')
    st.write('''
        1. Nama unsur harus ditulis dalam bahasa Latin. Contoh bahasa Latin perak adalah argentum dan emas adalah aurum.
        2. Pelambangan diambil dari nama depan unsurnya dan harus ditulis dengan huruf kapital. Contoh carbon ditulis C, oksigen ditulis O, fosfor ditulis F, dan sebagainya.
        3. Jika ada unsur yang berawalan huruf sama, maka lambangnya ditulis dua huruf. Huruf pertama ditulis kapital dan huruf kedua ditulis dengan huruf kecil. Misal argentum ditulis sebagai Ag dan aurum ditulis sebagai Au atau carbon ditulis C dan calcium ditulis Ca.
             ''')
        

if selected_option == "Tentang Kami":
    st.title(':red[Mengenal Dekat Dengan Kami?]')
    st.subheader("Hello, to all user :wave:")
    st.write('''
        Web ini merupakan sebuah project yang dibuat oleh beberapa mahasiswa yang sedang semangatnya menuntut ilmu 😄 hehehe 
            ''')
    st.write('''
        Dalam kimia, penetapan massa unsur dalam suatu senyawa adalah langkah krusial untuk memahami sifat fisik dan kimia dari molekul tersebut.Perhitungan manual massa unsur bisa rumit dan memakan waktu, memperlambat proses sintesis senyawa kimia.Dalam beberapa tahun terakhir, Bidang Teknologi Modern telah menunjukkan kemajuan pesat dan dapat diterapkan dalam berbagai bidang, termasuk kimia.
            ''')
    st.write('''
         Aplikasi yang dikembangkan bertujuan memberikan akses yang lebih mudah dan praktis bagi pengguna untuk menentukan massa unsur dalam suatu senyawa kimia. Aplikasi ini hadir sebagai solusi untuk memudahkan pengguna dalam memahami konsep-konsep dasar kimia dan melakukan perhitungan secara cepat dan akurat.
             ''')
    st.write("jika memiliki kendala, bisa hubungi email beriku: ramadhi535@gmail.com")
    st.write("---")
    st.image("TEAM.png")
    st.write("---")
    
if selected_option == "Kalkulator":
        st.header(':red[Kalkulator Penentu Massa Unsur Dalam Suatu Senyawa]')
    # Fungsi untuk menghitung rasio massa atom relatif dengan massa molekul relatif
        def hitung_ratio(atom, senyawa, data1, data2):
            # Data massa atom relatif unsur
            massa_atom = {
                'H': 1.008,
                'He': 4.0026,
                'Li': 6.94,
                'Be': 9.0122,
                'B': 10.81,
                'C': 12.011,
                'N': 14.007,
                'O': 15.999,
                'F': 18.998,
                'Ne': 20.180,
                'Na': 22.990,
                'Mg': 24.305,
                'Al': 26.982,
                'Si': 28.085,
                'P': 30.974,
                'S': 32.06,
                'Cl': 35.45,
                'Ar': 39.948,
                'K': 39.098,
                'Ca': 40.078,
                'Sc': 44.956,
                'Ti': 47.867,
                'V': 50.942,
                'Cr': 51.996,
                'Mn': 54.938,
                'Fe': 55.845,
                'Co': 58.933,
                'Ni': 58.693,
                'Cu': 63.546,
                'Zn': 65.38,
                'Ga': 69.723,
                'Ge': 72.63,
                'As': 74.922,
                'Se': 78.971,
                'Br': 79.904,
                'Kr': 83.798,
                'Rb': 85.468,
                'Sr': 87.62,
                'Y': 88.906,
                'Zr': 91.224,
                'Nb': 92.906,
                'Mo': 95.95,
                'Tc': 98,
                'Ru': 101.07,
                'Rh': 102.91,
                'Pd': 106.42,
                'Ag': 107.87,
                'Cd': 112.41,
                'In': 114.82,
                'Sn': 118.71,
                'Sb': 121.76,
                'Te': 127.6,
                'I': 126.9,
                'Xe': 131.29,
                'Cs': 132.91,
                'Ba': 137.33,
                'La': 138.91,
                'Ce': 140.12,
                'Pr': 140.91,
                'Nd': 144.24,
                'Pm': 145,
                'Sm': 150.36,
                'Eu': 151.96,
                'Gd': 157.25,
                'Tb': 158.93,
                'Dy': 162.5,
                'Ho': 164.93,
                'Er': 167.26,
                'Tm': 168.93,
                'Yb': 173.05,
                'Lu': 174.97,
                'Hf': 178.49,
                'Ta': 180.95,
                'W': 183.84,
                'Re': 186.21,
                'Os': 190.23,
                'Ir': 192.22,
                'Pt': 195.08,
                'Au': 196.97,
                'Hg': 200.59,
                'Tl': 204.38,
                'Pb': 207.2,
                'Bi': 208.98,
                'Po': 209,
                'At': 210,
                'Rn': 222,
                'Fr': 223,
                'Ra': 226,
                'Ac': 227,
                'Th': 232.04,
                'Pa': 231.04,
                'U': 238.03,
                'Np': 237,
                'Pu': 244,
                'Am': 243,
                'Cm': 247,
                'Bk': 247,
                'Cf': 251,
                'Es': 252,
                'Fm': 257,
                'Md': 258,
                'No': 259,
                'Lr': 266,
                'Rf': 267,
                'Db': 268,
                'Sg': 269,
                'Bh': 270,
                'Hs': 269,
                'Mt': 278,
                'Ds': 281,
                'Rg': 282,
                'Cn': 285,
                'Nh': 286,
                'Fl': 289,
                'Mc': 289,
                'Lv': 293,
                'Ts': 294,
                'Og': 294,
            }
            
            # Hitung jumlah massa atom dalam senyawa
            total_massa_atom = 0
            for elemen, jumlah in senyawa.items():
                if elemen in massa_atom:
                    total_massa_atom += massa_atom[elemen] * jumlah
            
            # Hitung rasio massa atom dengan massa molekul relatif
            if atom in massa_atom and total_massa_atom != 0:
                rasio = massa_atom[atom] / total_massa_atom
                # Menghitung hasil dikalikan dengan data yang dimasukkan pengguna
                hasil = rasio * data1 * data2
                return hasil
            else:
                return "Error: Unsur atau senyawa tidak valid"

        # Tampilan menggunakan Streamlit
        def main():
            
            # Input unsur dan senyawa
            atom = st.text_input("Masukkan simbol atom (H, C, O, dll.):")
            senyawa = st.text_input("Masukkan rumus senyawa (Contoh: H2O):")
            
            # Input nilai data 1 dan data 2
            data1 = st.number_input("Masukkan nilai massa senyawa:")
            data2 = st.number_input('Masukkan jumlah atom unsur yang dicari:',value=0, placeholder="Ketikkan angka di sini...")
            
            if st.button('Hitung'):
                # Parsing rumus senyawa menjadi dictionary
                senyawa_dict = {}
                elemen = ''
                for char in senyawa:
                    if char.isalpha():
                        if elemen:
                            if elemen in senyawa_dict:
                                senyawa_dict[elemen] += 1
                            else:
                                senyawa_dict[elemen] = 1
                        elemen = char
                    else:
                        if elemen:
                            if elemen in senyawa_dict:
                                senyawa_dict[elemen] += int(char)
                            else:
                                senyawa_dict[elemen] = int(char)
                if elemen:
                    if elemen in senyawa_dict:
                        senyawa_dict[elemen] += 1
                    else:
                        senyawa_dict[elemen] = 1
                
                # Hitung rasio
                hasil = hitung_ratio(atom, senyawa_dict, data1, data2)
                st.write("Massa unsur",atom,"dalam",senyawa,"adalah",hasil)

        if __name__ == "__main__":
            main()