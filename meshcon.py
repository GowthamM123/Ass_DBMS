from flask import Flask, render_template,request
import psycopg2

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('mesh.html')

@app.route('/submit',methods=['POST'])
def submit():
    if request.method== 'POST':
        user=request.form['name']
        address=request.form['address']
        phone=request.form['phone']
        message=request.form['message']

        #Connection

        conn=psycopg2.connect(
            host='localhost',
            database='login',
            user='postgres',
            password='GOWTHAM@123'
        )
        cur=conn.cursor()

        cur.execute('INSERT INTO form VALUES(%s,%s,%s,%s)',(user,address,phone,message))

        conn.commit()
        cur.close()
        conn.close()

        return 'Successfully submitted!!!'

if __name__ == '__main__':
    app.run(debug=True)
