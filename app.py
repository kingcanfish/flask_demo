# charset=utf8
from flask import Flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:123456@localhost/test?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


db = SQLAlchemy(app)
CORS(app)


class StudentModel(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_card = db.Column(db.String(16), nullable=False, unique=True)
    name = db.Column(db.String(16), nullable=False)
    clazz = db.Column(db.String(16))
    description = db.Column(db.String(256))

    def to_dic(self):
        return {
            "id": self.id,
            "id_card": self.id_card,
            "name": self.name,
            "clazz": self.clazz,
            "description": self.description
        }


db.create_all()


def dict_has_null(data):
    for key in data.keys():
        if not data[key]:
            return True
        return False


@app.route('/students/<int:id_>', methods=["GET"])
def get_student(id_):
    # student = StudentModel.query.filter_by(id=id).first()
    student = StudentModel.query.get(id_)
    if not student:
        return jsonify({
            "status": 0,
            "message": "没有该学生",
            "data": ""
        })
    data = student.to_dic()
    return jsonify({
        "status": 1,
        "message": "获取成功",
        "data": data
    })


@app.route('/students', methods=["GET"])
def get_all():
    students = StudentModel.query.all()

    data = [student.to_dic() for student in students]
    return jsonify({
        "status": 0,
        "message": "获取成功",
        "data": data
    })


@app.route('/students/append', methods=["POST"])
def append_student():
    # name = request.json.get("name")
    # clazz = request.json.get("clazz")
    # description = request.json.get("description")
    # id_card = request.json.get("id_card")

    data = {
        "name": request.json.get("name"),
        "clazz": request.json.get("clazz"),
        "description": request.json.get("description"),
        "id_card": request.json.get("id_card")
    }
    if dict_has_null(data):
        return jsonify({
            "status": 0,
            "message": "参数有空值",
            "data": ""
        })
    student = StudentModel(**data)
    db.session.add(student)
    db.session.commit()
    return jsonify({
        "status": 1,
        "message": "操作成功",
        "data": ""
    })


@app.route('/student', methods=["DELETE"])
def delete_student():
    id_ = request.args.get("id")
    student = StudentModel.query.get(id_)
    if not student:
        return jsonify({
            "status": 1,
            "message": "操作成功",
            "data": ""
        })
    db.session.delete(student)
    db.session.commit()
    return jsonify({
        "status": 1,
        "message": "操作成功",
        "data": ""
    })


@app.route('/students/modify', methods=["PUT"])
def modify_student():
    id_ = request.args.get("id")
    # data = {
    #     "name": request.json.get("name"),
    #     "clazz": request.json.get("clazz"),
    #     "description": request.json.get("description"),
    #     "id_card": request.json.get("id_card")
    # }

    description = request.json.get("description")
    student = StudentModel.query.get(id_)
    if not student:
        return jsonify({
            "status": 0,
            "message": "没有该学生",
            "data": ""
        })

    student.description = description

    db.session.commit()
    return jsonify({
        "status": 1,
        "message": "操作成功",
        "data": ""
    })


if __name__ == '__main__':
    app.run()
