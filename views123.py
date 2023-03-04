from flask import Flask,render_template,redirect,request
import pymysql as py
app=Flask(__name__)
@app.route('/')
def display():
    try:
        db=py.Connect(host='localhost',user='root',password='',database='todo')
        cur=db.cursor()
        sqq='select * from Republic_Day_Project'
        cur.execute(sqq)
        data=cur.fetchall()
    except Exception as e:
        print('Error:',e)    
    return render_template('text.html',data=data)

@app.route('/store',methods=['POST'])
def store():
    t=request.form['Name']
    det=request.form['Contact_Number']
    ml=request.form['Email_Adress']
    ad=request.form['Adress']
    info=request.form['Blood_Group']
    dataa=request.form['Message']

    try:
        db=py.Connect(host='localhost',user='root',password='',database='todo')
        cur=db.cursor()
        qu='insert into Republic_Day_Project(Name,Contact_Number,Email_Adress,Adress,Blood_Group,Message) values("{}","{}","{}","{}","{}","{}")'.format(t,det,ml,ad,info,dataa)
        cur.execute(qu)
        db.commit()
    except Exception as e:
        print('FAILED to INSERT',e)
    return redirect('/')
    
app.run(debug=True)
