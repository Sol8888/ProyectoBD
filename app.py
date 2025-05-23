from flask import Flask
from app.vistas_principales.routes import inicio_bp
from app.parroquia_principal.routes import parroquia_bp

app = Flask(__name__)
app.register_blueprint(inicio_bp)
app.register_blueprint(parroquia_bp)

if __name__ == '__main__':
    app.run(debug=True)
