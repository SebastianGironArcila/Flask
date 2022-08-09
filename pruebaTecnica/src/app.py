from flask import Flask, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'mysql://root:123456@localhost:3306/api_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app, resources={r"/cursos/*": {"origins": "http://localhost"}})

# @cross_origin
@app.route('/cursos',methods=['GET'])
def listar_cursos():
    try:
       cursos = Curso.query.all()
       print(cursos)
       return Response(json.dumps(cursos),  mimetype='application/json')
    except Exception as ex:
        print(ex)
        return jsonify({'message' : "Error", 'exito': False})

class Curso(db.Model):
    
    __tablename__ = 'curso'
    codigo = db.Column(db.String(6), primary_key=True)
    nombre = db.Column(db.String(50))
    creditos = db.Column(db.Integer) 

    @property
    def serialize(self):
        return {
            'codigo': self.codigo,
            'nombre': self.nombre,
            'creditos': self.creditos
        }


if __name__ == '__main__':
    app.run()
#matematica = Curso(codigo='887766',nombre='Matematica',creditos=2.0)

#db.session.add(matematica)
#db.session.commit()






