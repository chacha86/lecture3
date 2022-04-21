from flask import Blueprint, render_template
from pybo import db
from pybo.models import Person, Car

# 경로 -> 상대경로 -> 자기자신 기준.
#      -> 절대경로 -> 루트(최상위) 기준
# 라우팅 해주는 객체
bp = Blueprint('test', __name__, url_prefix="")

# /는 서버 주소를 의미 -> 127.0.0.1:5000/hello
@bp.route('/hello')
def hello() :
    return "hello"

@bp.route('/bye')
def bye() :
    return "bye"

@bp.route('/introduce')
def introduce() :
    return "my name is cha"

@bp.route('/print_person/<int:no>')
def print_person(no) :
    
    #p1 = db.session.query(Person).first()
    # 여러개인가 한개인가
    # p1 = db.session.query(Person).filter(Person.no == 3).all()
    p2 = db.session.query(Person).filter(Person.no == no).first()
    
    return "{}살 {}사는 {}입니다.".format(p2.age, p2.address, p2.name)
    # return ""

@bp.route('/print_car/<int:no>')
def print_car(no) :
    c1 = db.session.query(Car).filter(Car.no == no).first()

    return "{} {}만원짜리 {}".format(c1.color, c1.price, c1.model)


@bp.route('/gugu')
def gugu() :
    return render_template('gugu.html')

@bp.route('/discount/<int:age>')
def discount(age) :
    
    return render_template('discount.html', age=age)

@bp.route('test')
def test() :
    c1 = db.session.query(Car).filter(Car.model == "아반떼").first()
    car_list = db.session.query(Car).all()
    
    return render_template('test.html', car_list=car_list)


@bp.route('/print_car_list')
def print_car_list() :

    c1 = db.session.query(Car).filter(Car.model == "아반떼").first()
        
    return """ 
        <table>
            <tr class="red">
                <td>Model</td>
                <td>Price</td>
                <td>Color</td>
            </tr>
            <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
            <tr>
                <td>싼타페</td>
                <td>3000</td>
                <td>파란색</td>
            </tr>
            <tr>
                <td>모닝</td>
                <td>1000</td>
                <td>하얀색</td>
            </tr>
        </table>
    """.format(c1.model, c1.price, c1.color)