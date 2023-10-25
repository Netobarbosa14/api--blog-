from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# Criar um API Flask
app = Flask(__name__)


# Criar uma instância de SQLAlchemy
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Y48mY&AJ3%gw42b@db.tkabwimroyfvzxyyeobm.supabase.co:5432/postgres'
db = SQLAlchemy(app)

# Definir a estrutura da tabela Autor
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem', backref='autor')

# Definir a estrutura da tabela Postagem
class Postagem(db.Model): 
    __tablename__ = 'postagem'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

# Executar o comando para criar o banco de dados
def inicializar_banco():
    with app.app_context():
        db.drop_all()
        db.create_all()
        # Criar usuários administradores
        admin1 = Autor(nome='netobarbosa', email='netobarbosa@gmail.com', senha='12345678', admin=True)
        db.session.add(admin1)
        db.session.commit()


if __name__ == '__main__':
    inicializar_banco()




