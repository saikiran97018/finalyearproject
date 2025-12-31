from flask import Flask, render_template
from flask_cors import CORS
from routes.certificate_routes import certificate_bp

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

CORS(app)

# API routes
app.register_blueprint(certificate_bp, url_prefix='/api/certificates')

# Frontend route
@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
