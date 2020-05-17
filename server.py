import csv
from flask import Flask,render_template,url_for,request,redirect
from icon_filter import image_filter
app = Flask(__name__)

#image_filter('C:\\Users\\asifi\\PycharmProjects\\WebDevelopment\\venv\\static\\assets\\images\\aaa.jpg','C:\\Users\\asifi\\PycharmProjects\\WebDevelopment\\venv\\static\\assets\\images\\asif.jpg')

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('C:\\Users\\asifi\\PycharmProjects\\WebDevelopment\\venv\\database.txt',"a") as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        print(name,email,subject,message)
        database.write(f'name:{name}\nemail:{email}\nsubject: {subject}\nmessage: {message}\n\n')
        database.close()

def spreadsheet(data):
    with open('C:\\Users\\asifi\\PycharmProjects\\WebDevelopment\\venv\\database.csv',"a",newline='') as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database,delimiter=',',lineterminator='\r\n',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])
        database.close()

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            spreadsheet(data)
            return redirect('/thankyou.html')
        except:
            return 'Your Response has failed. Try again!'
    else:
        return 'something went wrong.Try again!'
