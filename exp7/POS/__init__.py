from flask import Flask, render_template, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exp.db'
db = SQLAlchemy(app)

from exp7.experiment import Training,Algorithm,Corpus

@app.route("/")
@app.route("/index")
@app.route("/introduction")
def introduction():
	return render_template('introduction.html')

@app.route("/theory")
def theory():
	return render_template('theory.html')

@app.route("/objective")
def objective():
	return render_template('objective.html')

@app.route("/procedure")
def procedure():
	return render_template('procedure.html')

@app.route("/experiment")
def experiment():
	return render_template('experiment.html')

@app.route('/form-exp1',methods=['POST'])
def form_exp1():
	val = request.form['option']
	try:
		db.create_all()
		cor1=Corpus.query.all()
		algo1=Algorithm.query.all()
		train1=Training.query.all()

		cor=[]
		algo=[]
		train=[]
		i = 0
		for x in cor1:
			cor.insert(i,x.option)
			i+=1
		i = 0
		for x in algo1:
			algo.insert(i,x.option)
			i+=1
		i = 0
		for x in train1:
			train.insert(i,x.option)
			i+=1
		

		return jsonify({'train':train,'algo':algo,'cor':cor,'message':'data fetched successfully!'})

	except:
		return jsonify({'message':'Unable to fetch data!'})

@app.route("/quizzes")
def quizzes():
	return render_template('quizzes.html')

@app.route("/readings")
def readings():
	return render_template('readings.html')
