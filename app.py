# ---------------------------------------------------------
# Materia: Automatización de Infraestructura Digital II
# Alumna: Samantha Carolina Ramírez Montiel
# Profesor: Froylan Alonso Pérez Alanís
# ---------------------------------------------------------

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home ():
    return '''
<!-- 
Materia: Automatización de Infraestructura Digital II
Alumna: Samantha Carolina Ramírez Montiel
Profesor: Froylan Alonso Pérez Alanís
-->

<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8"/>
  <title>Proyecto Final - Automatización de Infraestructura Digital II</title>
  <style>
    body { 
      font-family: Arial, sans-serif; 
      background: linear-gradient(135deg,#4b0082,#8b0000); 
      color: #fff; 
      padding: 2rem; 
      margin: 0;
    }
    .card { 
      background: rgba(255,255,255,0.07); 
      padding: 1.5rem; 
      border-radius: 12px; 
      max-width: 700px; 
      margin: auto; 
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    h1 { 
      margin-top: 0; 
      color: #fff;
      border-bottom: 1px solid rgba(255,255,255,0.2);
      padding-bottom: 0.5rem;
    }
    p {
      line-height: 1.6;
      margin: 1rem 0;
    }
    strong {
      color: #f0f0f0;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>Automatización de Infraestructura Digital II</h1>
    <p><strong>Profesor:</strong> Froylan Alonso Pérez Alanís</p>
    <p><strong>Alumna:</strong> Samantha Carolina Ramírez Montiel</p>
    <p>Aplicación demostrativa para prácticas de DevOps y DevSecOps.</p>
  </div>
</body>
</html>

    '''
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' , port=5000)  
