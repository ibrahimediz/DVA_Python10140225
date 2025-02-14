from flask import Blueprint,request,jsonify
from app.models import Kitap,kitap_schema,kitapler_schema,User,user_schema,users_schema
from app import db
from datetime import datetime
from flask_jwt_extended import jwt_required,create_access_token,get_jwt_identity

main = Blueprint('main',__name__)

@main.route('/register',methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error":"Kullanıcı adı ve şifre gereklidir"}),400

    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"error":"Bu kullanıcı zaten mevcut"}),400
    
    yeni_kullanici = User(username=username)
    yeni_kullanici.set_password(password)
    db.session.add(yeni_kullanici)
    db.session.commit()
    return jsonify({"message":"Kullanıcı olusturuldu"}),201


@main.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error":"Kullanıcı adı ve şifre gereklidir"}),400
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"error":"Kullanıcı adı veya şifre hatalı"}),400
    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token":access_token})

@main.route('/protected',methods=['GET'])
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    result = user_schema.dump(user)
    return jsonify(result)

@main.route('/api/kitaplar',methods=['GET'])
def kitaplar():
    kitaplar = Kitap.query.all()
    result = kitapler_schema.dump(kitaplar)
    return jsonify(result)

@main.route('/api/kitaplar/<int:id>',methods=['GET'])
def kitap(id):
    kitap = Kitap.query.get_or_404(id)
    result = kitap_schema.dump(kitap)
    return jsonify(result)


@main.route('/api/kitaplar',methods=['POST'])
def kitap_ekle():
    try:
        data = request.get_json()
        kitap_adi = data['kitap_adi']
        yazar = data['yazar']
        isbn = data['isbn']
        yayim_tarihi = datetime.strptime(data['yayim_tarihi'], '%Y-%m-%d')
        yeni_kitap = Kitap(kitap_adi=kitap_adi,
                           yazar=yazar,
                           isbn=isbn,
                           yayim_tarihi=yayim_tarihi)
        db.session.add(yeni_kitap)
        db.session.commit()
        result = kitap_schema.dump(yeni_kitap)
        return jsonify(result),201
    except Exception as e:
        return jsonify({"error":str(e)}),400


@main.route('/api/kitaplar/<int:id>',methods=['PUT'])
def kitap_guncelle(id):
    kitap = Kitap.query.get_or_404(id)
    data = request.get_json()
    try:
        if 'kitap_adi' in data:
            kitap.kitap_adi = data['kitap_adi']
        if 'yazar' in data:
            kitap.yazar = data['yazar']
        if 'isbn' in data:
            kitap.isbn = data['isbn']
        if 'yayim_tarihi' in data:
            kitap.yayim_tarihi = datetime.strptime(data['yayim_tarihi'], '%Y-%m-%d')
        db.session.commit()
        result = kitap_schema.dump(kitap)
        return jsonify(result),200
    except Exception as e:
        return jsonify({"error":str(e)}),400


@main.route('/api/kitaplar/<int:id>',methods=['DELETE'])
def kitap_sil(id):
    kitap = Kitap.query.get_or_404(id)
    try:
        db.session.delete(kitap)
        db.session.commit()
        return jsonify({"message":"Kitap Silindi"}),200
    except Exception as e:
        return jsonify({"error":str(e)}),400
    
@main.errorhandler(404)
def not_found(error):
    return jsonify({"error":"Kitap Bulunamadi"}),404

@main.errorhandler(400)
def bad_request(error):
    return jsonify({"error":"Bad Request"}),400


