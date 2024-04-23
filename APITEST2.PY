from flask import Flask, jsonify, request

app = Flask(__name__)

students = []

@app.route('/')
def background():
    return "Selamat Datang Di Percobaan API "

@app.route('/students', methods=['GET', 'POST'])
def handle_students():
    if request.method == 'GET':
        return jsonify({"data": students}), 200
    
    if request.method == 'POST':
        data = request.get_json()
        students.append(data)
        return jsonify({"message": "Student added", "data": data}), 201

@app.route('/students/<string:npm>', methods=['PUT', 'DELETE'])
def update_or_delete_student(npm):
    global students
    
    if request.method == 'PUT':
        data = request.get_json()
        for student in students:
            if student["NPM"] == npm:
                student.update(data)
                return jsonify({"message": "Murid Telah Di Update", "data": student}), 200
        return jsonify({"message": "Murid Tidak Ditemukan"}), 404
    
    if request.method == 'DELETE':
        initial_length = len(students)
        students = [student for student in students if student["NPM"] != npm]
        
        if len(students) < initial_length:
            return jsonify({"message": "Murid Dihapus"}), 200
        else:
            return jsonify({"message": "Murid Tidak Ditemukan"}), 404

if __name__ == '__main__':
    app.run(debug=True)
