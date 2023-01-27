from flask import Flask, request,  session, jsonify
# import config cors :
from flask_cors import CORS, cross_origin
from flask_mail import Mail, Message
import random

my_app = Flask(__name__)
# config cors policy :
cors = CORS(my_app)
my_app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
my_app.config['MAIL_PORT'] = 2525
my_app.config['MAIL_USERNAME'] = 'c5efccbec4bb79'
my_app.config['MAIL_PASSWORD'] = 'ca05c6373cf575'
my_app.config['MAIL_USE_TLS'] = True
my_app.config['MAIL_USE_SSL'] = False

my_app.config['CORS_HEADERS'] = 'Content-Type'

mail = Mail(my_app)

'''
create My fake user data 

'''
USERS = [
        'SalahIddine.Diouri@usmba.ac.ma',
        'Chopen8444@gmail.com',
        'Ahmed.iyouri@hotmail.com'
]
PASSWORDS = [
        '123456789',
        '246810123',
        '751322225'
]

TEMP_RESET = []



@my_app.route('/Reset', methods=['GET', 'POST'])
@cross_origin()
def reset_Handler():
    if request.method == 'POST':
        # login operation need a handler :
        data = request.form.to_dict()
        email_list = data['emailList'].split(',')
        Response = []
        for email in email_list:
            if email in USERS:
                print(f'\n Reset User : {email} ')
                custom_reste = random.sample(range(0, 50), 4)
                TEMP_RESET.append([email,custom_reste])
        for temp_item in TEMP_RESET:
            try:
                msg = Message('Hello from the other side!',
                sender='peter@mailtrap.io', recipients=[temp_item[0]])
                msg.body = f"Hey your verification code is { temp_item[1][0] }-{ temp_item[1][1] }-{ temp_item[1][2] }-{ temp_item[1][3] } "
                mail.send(msg)
                Response.append(
                    {'State': 200, 'User': temp_item, 'isPasswordReset': True}
                )
            except Exception as e:
                print("error send verification : "+str(e))
                Response.append(
                    {'State': 404, 'User': temp_item, 'isPasswordReset': False}
                )
        return jsonify({ 'ResponseData':Response})


if __name__ == '__main__':
    # run our server :
    my_app.secret_key = 'super secret key'
    my_app.config['SESSION_TYPE'] = 'filesystem'
    my_app.run(debug=True)
