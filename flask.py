from flask import Flask, redirect, url_for, jsonify, make_response





app = Flask(__name__)

@app.route('/admin')
@app.route('/',methods=['GET'])
def hello_admin():
   result = {'a': 'b'}
   return make_response(jsonify(result),201)

@app.route('/guest/<guest>')
def hello_guest(guest):
   return jsonify({'msg':'Hello %s as Guest' % guest},status_code = 201)



@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug = True)
