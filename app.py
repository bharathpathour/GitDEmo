from flask import Flask, request, jsonify

app = Flask(__name__)

user_list = [
    {
        "id" : 0,
        "name" : "Bharath",
        "email" : "b@gmail.com",
        "password" : "Pass"
    },
    {
        "id" : 1,
        "name" : "sharath",
        "email" : "s@gmail.com",
        "password" : "Pass1"
    }
]

@app.route('/user', methods = ['GET', 'POST'])
def user():
    if request.method == 'GET':
        if len(user_list)>0:
            return jsonify(user_list)
        else:
            'Nothing found', 404

    if request.method == 'POST':
        new_user = request.form['name']
        new_email = request.form['email']
        new_password = request.form['password']
        iD = user_list[-1]['id']+1

        new_users = {
            'id': iD,
            'name': new_user,
            'email': new_email,
            'password': new_password
        }
        user_list.append(new_users)
        return jsonify(user_list), 201

@app.route('/user/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def single_user(id):
    if request.method == 'GET':
        for user in user_list:
            if user['id'] == id:
                return jsonify(user)
            pass
        if request.method == 'PUT':
            for user in user_list:
                if user['id'] == id:
                    user['name'] = request.form['name']
                    user['email'] = request.form['email']
                    user['password'] = request.form['password']
                    updated_user = {
                        'id': id,
                        'name': user['name'],
                        'email': user['email'],
                        'password': user['password']
                    }
                    return jsonify(updated_user)
        if request.method == 'DELETE':
            for index, user in enumerate(user_list):
                if user['id'] == id:
                    user_list.pop(index)
                    return jsonify(user_list)

if __name__ == '__main__':
    
    app.run(debug=True)

