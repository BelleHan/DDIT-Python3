from flask import Flask,request,render_template 

app = Flask(__name__) 

@app.route('/dan') 
def dan(): 
    b = ["홍길동", "전우치", "이승은"]
    a = request.args.get('a', "2")
    return render_template("dan.html", a=a, b=b, int=int, enumerate=enumerate)


if __name__ == '__main__': 
    app.run(debug=True)

