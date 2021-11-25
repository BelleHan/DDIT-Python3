from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__, static_url_path="", static_folder="static")
app.config['SECRET_KEY'] = '1234'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

def myreceive(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('to_server')
def to_server(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('to_client', json, callback=myreceive)

if __name__ == '__main__':
    socketio.run(app, host = "0.0.0.0",port=9999)