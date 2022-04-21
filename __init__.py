from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

db = SQLAlchemy()
migrate = Migrate()

# # 사람 -> 이름, 나이, 주소

def create_app() :

    app = Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    
    from . import models
    from .views import test_view
    app.register_blueprint(test_view.bp)
    
    # /는 서버 주소를 의미 -> 127.0.0.1:5000/
    @app.route('/')
    def test_view() :
        return '123123'

    return app

#    def __init__(self, name, age, address) :
#        self.name = name
#        self.age = age
#        self.address = address
        
# p1 = Person(name="john", age=20, address="NewYork")        
# p2 = Person("chris", 30, "Miami")

# print(p1.address)
# print(p1.name)
# print(p2.address)
        
# # 회원 -> 로그인아이디, 비밀번호, 닉네임

# # 게시물 -> 제목, 내용, 작성자, 작성일, 조회수


# 댓글 -> 


