from flask import *
from mysql import connector

app = Flask(__name__)

#open connection
db = connector.connect(
    host    = 'localhost',
    user    = 'root',
    passwd  = '',
    database= 'db_sample_api_0491'
)
@app.route('/admin')
def admin():
    cursor = db.cursor()
    cursor.execute('select * from tbl_students_0491')
    result = cursor.fetchall()
    cursor.close()
    return render_template('bases.html', hasil = result)

@app.route('/')
def main():
    cursor = db.cursor()
    cursor.execute('select * from tbl_students_0491')
    result = cursor.fetchall()
    cursor.close()
    return render_template('indexes.html', hasil = result)
    
@app.route('/tambah/')
def tambah_data():
    return render_template('tambahs.html')

@app.route('/proses_tambah/', methods=['POST'])
def proses_tambah():
    nim = request.form['nim']
    nama = request.form['nama']
    jk = request.form['jk']
    jurusan = request.form['prodi']
    daerah = request.form['daerah']
    cur = db.cursor()
    cur.execute('INSERT INTO tbl_students_0491 (nim, nama, jk, jurusan, alamat) VALUES (%s, %s, %s, %s, %s)', (nim, nama, jk, jurusan, daerah))
    db.commit()
    return redirect(url_for('admin'))

@app.route('/ubah/<id>', methods=['GET'])
def ubah_data(id):
    cur = db.cursor()
    cur.execute('select * from tbl_students_0491 where id=%s', (id,))
    res = cur.fetchall()
    cur.close()
    return render_template('ubahs.html', hasil=res)

@app.route('/proses_ubah/', methods=['POST'])
def proses_ubah():
    fid = request.form['id']
    nim = request.form['nim']
    nama = request.form['nama']
    jk = request.form['jk']
    prodi = request.form['prodi']
    asal = request.form['daerah']
    cur = db.cursor()
    sql = "UPDATE tbl_students_0491 SET nim=%s, nama=%s, jk=%s, jurusan=%s, alamat=%s WHERE id=%s"
    value = (nim, nama, jk, prodi, asal, fid)
    cur.execute(sql, value)
    db.commit()
    return redirect(url_for('admin'))

@app.route('/hapus/<id>', methods=['GET'])
def hapus_data(id):
    cur = db.cursor()
    cur.execute('DELETE from tbl_students_0491 where id=%s', (id,))
    db.commit()
    return redirect(url_for('admin'))
if __name__ == '__main__':
    app.run()