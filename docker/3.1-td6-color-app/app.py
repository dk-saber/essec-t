from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Récupération de la couleur depuis la variable d'environnement APP_COLOR
    # Valeur par défaut : 'red' si APP_COLOR n'est pas définie
    app_color = os.environ.get('APP_COLOR', 'red')
    
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Environment de variables - Docker</title>
        <style>
            body {{
                background-color: {app_color};
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
            }}
            .container {{
                text-align: center;
                background-color: white;
                padding: 50px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #333;
                margin-bottom: 20px;
            }}
            .color-display {{
                font-size: 24px;
                color: {app_color};
                font-weight: bold;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1> Environment de variables Docker</h1>
            <p>Cette application utilise des variables d'environnement</p>
            <div class="color-display">
                Couleur actuelle: {app_color.upper()}
            </div>
        </div>
    </body>
    </html>
    '''
    return html

if __name__ == '__main__':
    # Exécution de l'application sur le port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
