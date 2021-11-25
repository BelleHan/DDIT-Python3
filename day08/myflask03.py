from flask import Flask,request,render_template 

app = Flask(__name__) 

@app.route('/vo') 
def vo(): 
    vos = [
            {"e_id":1, "name":"홍길동", "tel":"01022223333"},
            {"e_id":1, "name":"전우치", "tel":"01022224444"}
         ]
    
    return render_template("vos.html", vos=vos, enumerate=enumerate)


if __name__ == '__main__': 
    app.run(debug=True)

