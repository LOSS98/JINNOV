from flask import *
from models.utils import *

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    return render_template("mail_form_student.html")

#route pour la création de devis
@app.route('/mail_devis', methods=["POST"])
def mail_devis():
    return Mail_devis_create()
    
#route pour la création d"une demande d'inscriptions
@app.route('/mail_student', methods=["POST"])
def mail_student():
    return Mail_student_create()
    
if __name__ == '__main__':
    app.run(debug=True)