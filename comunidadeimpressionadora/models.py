from comunidadeimpressionadora import database, login_menager
from datetime import datetime
from flask_login import UserMixin


@login_menager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

#database.colum() é uma colu na do nosso banco de daods e passamos os parametros dento do (str, int, float)

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não Informado')

    def contar_posts(self):
        return len(self.posts)

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)


#https://upload.wikimedia.org/wikipedia/commons/a/ac/Default_pfp.jpg