from flask import Flask,request,render_template,jsonify
from day09.dao_emp import DaoEmp

# app = Flask(__name__) 
app = Flask(__name__, static_url_path="", static_folder="static")

de = DaoEmp()

@app.route('/emp') 
def emp(): 
    emps = de.select()
    return render_template("emp.html", emps=emps)


@app.route('/insert.ajax', methods=['POST'])
def ajax_insert():
    data = request.get_json()
    cnt = de.insert(data['e_id'], data['name'], data['tel'])
    result = "ng"
    if cnt == 1 :
        result = "ok"
    return jsonify(result = result)


@app.route('/update.ajax', methods=['POST'])
def ajax_update():
    data = request.get_json()
    cnt = de.update(data['e_id'], data['name'], data['tel'])
    result = "ng"
    if cnt == 1 :
        result = "ok"
    return jsonify(result = result)


@app.route('/delete.ajax', methods=['POST'])
def ajax_delete():
    data = request.get_json()
    cnt = de.delete(data['e_id'])
    result = "ng"
    if cnt == 1 :
        result = "ok"
    return jsonify(result = result)


if __name__ == '__main__': 
    app.run(debug=True)
    
    
    
    