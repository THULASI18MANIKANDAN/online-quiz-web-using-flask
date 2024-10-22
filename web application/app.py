from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = {
    1: {"question": "What is Flask?", "options": ["A web framework", "A database", "A programming language", "A browser"], "answer": "A web framework"},
    2: {"question": "Which method is used to start the Flask server?", "options": ["run()", "start()", "execute()", "begin()"], "answer": "run()"},
    3: {"question": "Which template engine does Flask use by default?", "options": ["Jinja2", "Django", "Mako", "Tornado"], "answer": "Jinja2"},
    4: {"question": "Which HTTP method is used to send form data?", "options": ["POST", "GET", "PUT", "DELETE"], "answer": "POST"},
    5: {"question": "What is the default port for a Flask app?", "options": ["5000", "8000", "8080", "3000"], "answer": "5000"},
    6: {"question": "Which statement is used to import Flask?", "options": ["import Flask", "from flask import Flask", "import flask", "from Flask import flask"], "answer": "from flask import Flask"},
    7: {"question": "In which folder do you place templates in a Flask project?", "options": ["templates", "static", "views", "public"], "answer": "templates"},
    8: {"question": "Which function in Flask renders a template?", "options": ["render_template()", "render()", "show_template()", "display_template()"], "answer": "render_template()"},
    9: {"question": "How do you define a route in Flask?", "options": ["@app.route()", "@route()", "@Flask.route()", "@app.url()"], "answer": "@app.route()"},
    10: {"question": "What is the purpose of the 'request' object in Flask?", "options": ["To handle incoming data", "To handle database operations", "To serve static files", "To render templates"], "answer": "To handle incoming data"},
    11: {"question": "Which decorator is used to create API endpoints in Flask?", "options": ["@app.route()", "@api.route()", "@endpoint()", "@flask.route()"], "answer": "@app.route()"},
    12: {"question": "Which command installs Flask in Python?", "options": ["pip install Flask", "pip Flask install", "install Flask", "Flask install"], "answer": "pip install Flask"},
    13: {"question": "Which statement is correct for starting a Flask app?", "options": ["app.run(debug=True)", "app.debug()", "flask.debug()", "start.app(debug=True)"], "answer": "app.run(debug=True)"},
    14: {"question": "How can you access query parameters in Flask?", "options": ["request.args", "request.query", "request.get", "request.params"], "answer": "request.args"},
    15: {"question": "How can you serve static files in Flask?", "options": ["Use the 'static' folder", "Use the 'media' folder", "Use the 'assets' folder", "Use the 'public' folder"], "answer": "Use the 'static' folder"},
    16: {"question": "What is the purpose of 'url_for' function in Flask?", "options": ["To generate URLs", "To import files", "To serve static files", "To redirect users"], "answer": "To generate URLs"},
    17: {"question": "Which HTTP method is idempotent?", "options": ["GET", "POST", "PATCH", "PUT"], "answer": "GET"},
    18: {"question": "How do you access form data in Flask?", "options": ["request.form", "request.data", "request.input", "request.body"], "answer": "request.form"},
    19: {"question": "How do you redirect users in Flask?", "options": ["redirect()", "send()", "go()", "move()"], "answer": "redirect()"},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['POST', 'GET'])
def quiz():
    if request.method == 'POST':
        user_answers = request.form.to_dict()
        score = 0
        for q_no, answer in user_answers.items():
            if questions[int(q_no)]['answer'] == answer:
                score += 1
        return render_template('result.html', score=score, total=len(questions))
    return render_template('quiz.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
