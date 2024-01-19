from flask import Blueprint, render_template, request

exam = Blueprint ("exam", __name__)

@exam.route('/exam/', methods=['GET', 'POST'])
def main ():
    errors = {}

    if request.method == 'POST':
        n1 = request.form.get('n1')
        n2 = request.form.get('n2')
        n3 = request.form.get('n3')
        n4 = request.form.get('n4')

        if not n1 or not n1.isdigit():
            errors['n1'] = 'Пожалуйста, введите корректное число в поле Число 1.'

        if not n2 or not n2.isdigit():
            errors['n2'] = 'Пожалуйста, введите корректное число в поле Число 2.'

        if not n3 or not n3.isdigit():
            errors['n3'] = 'Пожалуйста, введите корректное число в поле Число 3.'

        if not n4 or not n4.isdigit():
            errors['n4'] = 'Пожалуйста, введите корректное число в поле Число 4.'

        if not errors:
            numbers = [int(n1), int(n2), int(n3), int(n4)]
            numbers.sort(reverse=False)
            result = numbers
        else:
            result = None
    else:
        result = None

    return render_template ('exam/exam.html', errors=errors, result=result)