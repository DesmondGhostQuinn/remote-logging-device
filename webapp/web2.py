from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from flask_pymongo import MongoClient
import smtplib
import yagmail


app = Flask(__name__)

#specify the mongo database being used
app.config['MONGO_DBNAME'] = 'thedb'
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/thedb"


mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('ehome.html')      

@app.route('/tnc')
def tnc():
    return render_template('termsandconditions.html')

@app.route('/why')
def why():
    return render_template('whylasermaze.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/rental')
def rental():
    return render_template('rental.html')

@app.route('/refund')
def refund():
    return render_template('refund.html')

@app.route('/member')
def member():
    return render_template('member.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/faq')
def faq():
    return render_template('efaq.html')

@app.route('/corporate')
def corporate():
    return render_template('corporate.html')

@app.route('/profile', methods=["POST", "GET"])
def profile():
	if 'tag' in session:
		p = mongo.db.gamer.find_one({'tag': session['tag']})
		return render_template('eprofile.html',username=p['name'],points=p['points'])		
	return render_template('homepage.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        t = mongo.db.gamer.find_one({'tag' : request.form['tag']})
        if t:
            session['tag'] = request.form['tag']
            session['logged_in'] = True
            return redirect(url_for('profile'))
	return 'Invalid Gamertag'
    return render_template('elogin.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        reply_to = request.form['email']
        message = request.form['message']
        message = reply_to+'--says that--'+message
        yag = yagmail.SMTP('endsemproject24@gmail.com', 'sainasimran1')	#the email id and password is specified
        yagmail.SMTP('endsemproject24@gmail.com').send('endsemprojectproject24@gmail.com', reply_to, message)
        return redirect(url_for('home'))
    return render_template('contact.html')

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST' :
        m1=mongo.db.gamer.find_one({'title': "forc"})	#document with this particular field keeps track of the count
        if m1:
            n=m1['count']
        n1=int(n)
        nx=str(n1+1)
	#count is updated
        mongo.db.gamer.update(m1,{'$set':{'count':n1+1}})	
        #collection is updated
	mongo.db.gamer.insert({'name' : request.form['name'], 'email' : request.form['email'], 'phone' : request.form['phone'], 'tag':nx, 'points': 0, 'index' : 0, 'age': request.form['age']})
 	return render_template('gametagdisp.html', id = nx)	#id of the new user is returned
    return render_template('esignup.html')


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
