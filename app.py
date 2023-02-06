from flask import Flask, jsonify, render_template, request

# class PrefixMiddleware(object):
#     def __init__(self, app, prefix=''):
#         self.app = app
#         self.prefix = prefix
#     def __call__(self, environ, start_response):
#         if environ['PATH_INFO'].startswith(self.prefix):
#             environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
#             environ['SCRIPT_NAME'] = self.prefix
#             return self.app(environ, start_response)
#         else:
#             start_response('404', [('Content-Type', 'text/plain')])
#             return ["This url does not belong to the app. Check your URL address.".encode()]


app = Flask(__name__,
            static_url_path='',
            static_folder='web/source',
            template_folder='web/templates')

# app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/LunchApp')

@app.route('/')
def landing_page():
    return render_template("landing_page.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/all_gems')
def all_gems():
    return render_template("all_gems.html")

if __name__ == "__main__":
    app.run(debug=True) 