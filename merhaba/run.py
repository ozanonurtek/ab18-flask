from flask import Flask
from random import randint
app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    return "Merhaba Flask"

@app.route('/about')
def about():
    return "<h1>Selam</h1>"

@app.route('/rastgele')
def my_rand():
    number_one = randint(0,400)
    number_two = randint(0,200)
    my_string = "<h2>" + str(number_one + number_two) + "</h2>"
    return my_string

@app.route('/profile/<profile_name>')
def show_user(profile_name):
    my_new_profile_name = profile_name * 3
    return my_new_profile_name

@app.route('/users/<int:user_id>')
def show_user_name_with(user_id):
    return search_user(user_id)


def search_user(user_id):
    dict = {1: "Ozan", 2: "Furkan"}
    if user_id in dict:
        return users[user_id]
    else:
        return "Sen kimsin."

if __name__ == '__main__':
    app.run(debug=True)
