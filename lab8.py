from flask import Blueprint, request, render_template, redirect, url_for, abort, jsonify

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/index.html')

courses = [
    {"name": "C++", "videos": 3, "price": 3000, "date_": "2023-12-11"},
    {"name": "basic", "videos": 30, "price": 0, "date_": "2023-12-19"},
    {"name": "C#", "videos": 8, "date_": "2023-12-20"}
]

@lab8.route('/lab8/api/courses/', methods=['GET'])
def get_courses():
    return courses

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_course(course_num):
    if course_num < 0 or course_num >= len(courses):
        return "Error 404: Курс не найден", 404
    return courses[course_num]