from flask import Flask,request 

app = Flask(__name__) 

@app.route('/') 
def home(): 
    return 'Hello, World!' 

@app.route('/para', methods=['POST']) 
def para(): 
    
    # a = request.args.get('a', "하하하")
    a = request.form['a']
    return 'Hello!'+a

@app.route('/dan') 
def dan(): 
    a = request.args.get('a', "2")
    html = ""
    html += "<html>"
    html += "<head>"
    html += "</head>"
    html += "<body>"
    
    html += "{}*{}={}<br>".format(a,1,int(a)*1)
    html += "{}*{}={}<br>".format(a,2,int(a)*2)
    html += "{}*{}={}<br>".format(a,3,int(a)*3)
    html += "{}*{}={}<br>".format(a,4,int(a)*4)
    html += "{}*{}={}<br>".format(a,5,int(a)*5)
    
    html += "{}*{}={}<br>".format(a,6,int(a)*6)
    html += "{}*{}={}<br>".format(a,7,int(a)*7)
    html += "{}*{}={}<br>".format(a,8,int(a)*8)
    html += "{}*{}={}<br>".format(a,9,int(a)*9)
    
    html += "</body>"
    html += "</html>"
    

    return html


if __name__ == '__main__': 
    app.run(debug=True)

