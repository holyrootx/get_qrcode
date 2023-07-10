from flask import Flask,request,url_for,redirect,render_template,session
# route(/) slash 부터 시작 
# rediret(url_for('fildname'))
app = Flask(__name__)
app.secret_key = 'your_secret_key'
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
def get_form_data(form_data):
    """ data 가져와서 랜더링한 html 파일 리턴"""
    driver_name = form_data.get('driver_name')
    phone_number = form_data.get('phone_number')
    car_number = form_data.get('car_number')
    return render_template('driverCheck.html',driver_name=driver_name,phone_number=phone_number,car_number=car_number)
# def combined_info():
#     driver_name = session.get('driver_name')
#     phone_num = session.get('phone_num')
#     car_number = session.get('car_number')

#     combined = f"Driver Name: {driver_name}, Phone Number: {phone_num}, Car Number: {car_number}"
#     return combined

@app.route('/driverform',methods = ["Post","GET"])
def driverform():
    if request.method == "POST":
        # request form 객체는 immutableMultiDict 
        # dictname[key] = value        
        if checkform(request.form):

            # 데이터 잘 입력 했으면 세션이나 쿠키 처리하고 끝 페이지로 리다이렉션 
            # 세션 쿠키 처리 로직
            # return combined_info()

            return get_form_data(request.form) # 잘가요 랜더링한 페이지 리턴
        else:
            return redirect(url_for('driverform')) # 입력 이상하게 했으니까 다시 입력 ㄱㄱ
    else:
        return render_template('driverform.html') # get 방식이면 URL에 입력한거니까 폼 켜주기

    

@app.route('/driverCheck',methods = ["POST","GET"])
def driverCheck():
    return render_template('driverCheck.html')

@app.route('/driverCheckAction',methods = ["POST"])
def driverCheckAction():
    btn_value = request.values.get("btn_value")
    if btn_value == "yes":
        return "yespage"
    else:
        return redirect(url_for('driverform'))
    
@app.route('/lastpage')
def lastpage():
    return render_template('lastpage.html')    

@app.route('/driverformAction')
def driverformAction():
    pass

app.run(debug=True,port=5001)

"""
1) driverform page로 들어온다 
2) 작성한다 post 
3) 유효성 검사
4) redirection -> driverCheck 
5) 스스로 오타 체크 유도 -> POST 전송
6) 다시 작성 -> 다시 POST
7) 검사
8) redirection
9) ㄹㅇ bye 페이지로 redirection 세션 3일 유지 

버튼 css 추가해야함


"""