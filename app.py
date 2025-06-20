from flask import Flask, render_template

app = Flask(__name__)

job_list = [{'id':1, 'title':'Data Analyst', 'location':'Bengaluru', 'salary':'10,00,000'},
             {'id':2, 'title':'Data Scientist', 'location':'Delhi', 'salary':'15,00,000'}]

@app.route('/')
def hello_world():
    return render_template('home.html', company_name='Jovian', jobs= job_list)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
