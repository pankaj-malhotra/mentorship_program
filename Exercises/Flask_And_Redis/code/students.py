from flask import Flask
from flask_restful import Resource, Api, reqparse
from redis import Redis

app = Flask(__name__)
api = Api(app)
r = Redis(host='localhost', port=6379, db=0)


class Student(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    parser.add_argument('age',
        type=int,
        required=False,
        help="This field cannot be left blank!"
    )

    parser.add_argument('gender',
        type=str,
        required=False,
        help="This field cannot be left blank!"
    )

    def get(self, roll_no):
        result = self.find_by_roll_number(roll_no)

        if result:
            return {roll_no: result}
        else:
            return {'message': "Student with rollNo '{}' is not found".format(roll_no)}, 404

    @classmethod
    def find_by_roll_number(cls, roll_no):
        keys = r.hkeys(roll_no)

        result = {}

        for key in keys:
            key = key.decode("utf-8")
            val = r.hget(roll_no, key)
            val = val.decode("utf-8")
            result[key] = val

        return result

    def post(self, roll_no):
        if r.hgetall(roll_no):
            return {'message': "A student with rollNo '{}' already exists".format(roll_no)}, 400

        data = Student.parser.parse_args()
        student = {'name': data['name'],
                'age': int(data['age']),
                'gender': data['gender']}
        r.hmset(roll_no, student)
        return student, 201

    def delete(self, roll_no):
        keys = r.hkeys(roll_no)

        result = None

        for key in keys:
            key = key.decode("utf-8")
            result = r.hdel(roll_no, key)

        if result:
            return {'message': "Student with rollNo '{}' deleted successfully".format(roll_no)}, 201
        else:
            return {'message': "Student with rollNo '{}' does not exist".format(roll_no)}, 400


class StudentList(Resource):
    def get(self):
        students = []

        for rollNumber in r.scan_iter():
            student = Student.find_by_roll_number(rollNumber)
            students.append({rollNumber.decode("utf-8"): student})

        if students:
            return {'students': students}, 200
        else:
            return {'message': "No students are found"}, 404


api.add_resource(Student, '/student/<string:roll_no>')
api.add_resource(StudentList, '/students')


if __name__ == '__main__':
    app.run(port=5000)

