from flask import Flask
from markupsafe import escape
from flask import request
from flask import render_template
#from flask import escape


app=Flask(__name__)

#flask_static routing
"""
Tipe tipe variabel
string
int
float
path
uuid"""

@app.route('/')
def index():
    mylist=['apel','mangga','jeruk']
    dict={'nama':'hakim','alamat':'bandung','usia':20}
    return render_template('index.html', nama='Hakim', condition='How are you today?', list=mylist,
                          dic=dict)

@app.route('/about')
def about():
    return '<h1>About Us</h1>'

@app.route('/contact')
def contact():
    return '<h1>Contact Us</h1>'

#Flask dynamic routing
@app.route('/profile',defaults={'route':"home",'username':str})
@app.route('/profile/<string:username>',defaults={'route':"profile"})
def profile_name(username,route):
    if route == "home":
        return '<h1>Profile Home</h1>'
    elif route == "profile":
        return '<h1>Hello %s</h1>' % username


'''@app.route('/profile',defaults={'_route':"home",'nilai':0})
@app.route('/profile/<int:nilai>',defaults={'_route':"profile"})
def profile_name(nilai,_route):
    if _route == "home":
        return '<h1>ProfileHome</h1>'
    elif _route == "profile":
        nilai = nilai+100
        return'<h1>Hello %s</h1>' % nilai
'''


#HTML ESCAPE
'''
HTML ESCAPE berarti menghapus spesial karakter dalam HTML
contoh : < > &
Char diatas mempunyai fungsi yang sangat berarti di html
Tujuan dari html escape unutk MENCEGAH WEBSITE DARI KODE JAHAT
seseorang yang ingin men-inject kode dalam website.
LET'S GET IT...........
'''
@app.route("/htmlescape/<code>")
def htmlescape(code):
    return escape(code)

#UNIQUE URLs/Redirection Behavior
'''
DUA ROUTE DIBAWAH PERBEDAANNYA HANYALAH PENGGUNAAN SLASH
DI AKHIR ROUTING
@app.route('/projects/')
def projects():
    return : 'The project page'

@app.route('/projects/')
def projects():
    return : 'The project page'

@app.route('/about')
def about():
    return : 'The about page'    
'''
@app.route('/routetanpaslash')
def routetanpaslash():
    return '<h1>Route tanpa slash</h1>'

@app.route('/routedenganslash/')
def routedenganslash():
    return '<h1>Route dengan slash</h1>'
#sebenernya kegunaannya hanya untuk prevention 404

#URL Building
'''
untuk membuat url ke func tertentu, kita dapat menggunakan
fungsi url_for(). func ini berfungsi untuk menerima nama fungsi
sebagai argumen pertama dan sejumlah argumen kata kunci.
Contoh penerapan:

@app.route('/login')
def login():
    return 'login'

'''
#URL Building untuk static file
'''
Static file berguna untuk menyimpan file-file pendukung seperti gambar,
css, ataupun javasript.

url_for('static', filename='style.css')
'''

#HTTP Request/method
'''
dalam flask terdapat method POST and GET.
Jika menggunakan GET, maka method HEAD auto berfungsi.

contoh
from flask import request

@app.route('login', methods=['GET','POST'])
def login():
    if request.method == 'POST' :
        return do_the_login()
    else:
        return show_the_login_form()

HTTP Request :
ambil value dari form : request.form['name']
ambil parameter dari url req : request.args.get('parameter')
mengambil file url dari req : request.files['the_file']
mengambil jenis method : reuest.method
mengambil path request : request.path
'''

#Berikut adalah metode GET

@app.route('/cobarequest', methods=['GET','POST'])
def cobarequest():
    if request.method == 'GET':
        return request.args.get('nama', '') + request.args.get('alamat', '')
    elif request .method == 'POST':
        return request.form['nama']

#code dibawah versi GPT, output yang dihasilkan lebih rapi
    '''
    if request.method == 'GET':
        # Cek keberadaan parameter 'nama' dan 'alamat'
        nama = request.args.get('nama', '')  # Nilai default adalah string kosong jika tidak ada
        alamat = request.args.get('alamat', '')  # Nilai default adalah string kosong jika tidak ada
        return f'{nama} {alamat}'
    elif request.method == 'POST':
        return '<h1>Coba POST</h1>
'''

#Render HTML



app.run(debug=True)


