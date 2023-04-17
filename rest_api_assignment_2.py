from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        "name" : "Viola",
        "age" : "28",
        "id" : 1
    },
    {
         "name" : "Tsumugi",
        "age" : "26",
        "id" : 2
    }
]

@app.route("/history")
def history() :
    return "Welcome To 1849 !!!"

@app.route("/read-data")
def read_data() :
    return jsonify(
    {
    "data" : tasks
    }
    )

@app.route("/write-data", methods=["POST"])
def new_data():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)
    
    task = {
        "name" :  request.json["name"],
        "age" : request.json["age"],
        "id": tasks[-1]["id"] + 1,    
    }

    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })


if(__name__ == "__main__") :
    app.run(debug=True)
