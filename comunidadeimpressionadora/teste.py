from comunidadeimpressionadora import database
from comunidadeimpressionadora import app
from comunidadeimpressionadora.models import Usuario


# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario1 = Usuario(username='Rafinha',email='rafinha123@gmail.com' ,senha='123456')
#     usuario2= Usuario(username='camila',email='camila123@gmail.com' ,senha='567890')
#     database.session.add(usuario1)
#     database.session.add(usuario2)
#     database.session.commit()

# with app.app_context():
#     #usuario_teste = Usuario.query.filter_by(id=2).first()
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     primeiro_usuario = Usuario.query.first()
#     print(primeiro_usuario.username)

# with app.app_context():
#     primeiropost = Post(id_usuario=1, titulo= 'jaja o curso termina em',corpo='mais 3 meses e estarrei formado')
#     database.session.add(primeiropost)
#     database.session.commit()

# with app.app_context():
#     database.drop_all()
#     database.create_all()

# with app.app_context():
#     database.create_all()

# with app.app_context():
#     segundo_usuario = Usuario.query.filter_by(username='novorafa').first()
#     print(segundo_usuario.senha)

# query da uma lista com o filter_by entao colocamos o first() para pegar o 1 valor