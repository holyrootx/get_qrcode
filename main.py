from flask import Flask,request,url_for,redirect,render_template
# route(/) slash 부터 시작 
# rediret(url_for('fildname'))
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('driverform'))

def checkform(form_data):
    """작성 유효성 검사
    1) 공백인지 체크 (값이 모두 입력되었는지 체크)
    return True or False
    """
    driver_name = form_data.get('driver_name')
    phone_number = form_data.get('phone_number')
    car_number = form_data.get('car_number')

    if driver_name and phone_number and car_number:
        return True
    else:
        return False



@app.route('/driverform',methods = ["Post","GET"])
def driverform():
    if request.method == "POST":
        # request form 객체는 immutableMultiDict 
        # dictname[key] = value
        for data in request.form.values():
            print(data)
        if checkform(request.form):
            #데이터 잘 입력 했으면 세션이나 쿠키 처리하고 끝 페이지로 리다이렉션 
            # 세션 쿠키 처리 로직
            return render_template('driverBye.html') # 잘가요 페이지 
        else:
            return redirect(url_for('driverform')) # 입력 이상하게 했으니까 다시 입력 ㄱㄱ
    else:
        return render_template('driverform.html') # get 방식이면 URL에 입력한거니까 폼 켜주기

    

@app.route('/driverBye')
def driverBye():
    return render_template('driverBye.html')

@app.route('/driverformAction')
def driverformAction():
    pass

app.run(debug=True,port=5001)

"""
1) driverform page로 들어온다 
2) 작성한다 post

"""