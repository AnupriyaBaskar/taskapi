from flask import Flask,jsonify,request

app = Flask(__name__)


#datas
details = [
    {"id":1,"name":"Anu","age":20},
    {"id":2,"name":"Aishu","age":25},
    {"id":3,"name":"Lakshmi","age":30},
    {"id":4,"name":"Vino","age":20},
    {"id":5,"name":"Vishalam","age":20},
    {"id":6,"name":"Dhatch","age":26},
    {"id":7,"name":"Ashmitha","age":20},
    {"id":8,"name":"Keerthana","age":19},
    {"id":9,"name":"priya","age":22}
]

# Reading Method getting 

@app.route("/details",methods = ['GET'])

def getdetails():
    return details

# Getting data

@app.route("/details/<int:id>",methods = ['GET'])

def acceptdata(id):
    for data in details:
        if data['id'] == id:
            return data
        else:
            return{'error':"No data found"}

# Create data
@app.route("/details",methods = ['POST'])

def create_data():
    new_data = {'id':len(details) + 1,'name':request.json['name'],'age':request.json['age']}
    details.append(new_data)
    return new_data


# Delete data
@app.route("/details/delete/<int:id>",methods = ['GET'])

def deletedata(id):
    for data in details:
        if data['id'] == id:
            details.remove(data)
        else:
            return{'error':"No data found"}

#Run the flask App

if __name__ == '__main__':
    app.run(debug=True)    