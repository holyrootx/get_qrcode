from flask import Flask,request,url_for,redirect,render_template,session
# route(/) slash 부터 시작 
# rediret(url_for('fildname'))
app = Flask(__name__)
app.secret_key = 'your_secret_key' # user borwser 에 저장함
@app.route('/')
def index():
    """session.get('count')
    처음에 index page로 오면 
    driverform.html로 redirection된다.
    그러나 driverform -> driverCheck -> driverCheckAction.html 을 거쳐가면서 session['count']의 value를 counting한다.
    그래서 한번 방문한 사람을 거르려고 이러한 코드를 추가했다.
    방문을 했다면 session['count']의 값이 counting 됬다는 전제로말이다.
    """
    try:
        if session.get('count'): # 방문한 적이 있으면
            return render_template('visited.html',driver_name=session.get('driver_name')) # 이미 방문했다고 다른 페이지 보여줌
    except KeyError: # session[count]의 값이 없는 경우 === 방문을 한번도 하지않은 경우
        session['count'] = 0 # 
    return redirect(url_for('driverform')) # Driverform url로 이동

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

    session['driver_name'] = driver_name
    session['phone_number'] = phone_number
    session['car_number'] = car_number

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
        if checkform(request.form): # input 3개 다 입력했나 체크
            return get_form_data(request.form) # 잘가요 랜더링한 페이지 리턴 driverCheck 문서 랜더링 
        else:
            return redirect(url_for('driverform')) # 입력 이상하게 했으니까 다시 입력 ㄱㄱ
    else:
        if session.get('count'):
            return render_template('visited.html',driver_name=session.get('driver_name'))
        return render_template('driverform.html') # get 방식이면 URL에 입력한거니까 폼 켜주기

    

@app.route('/driverCheck',methods = ["POST","GET"])
def driverCheck():
    """
    다시 수정하기 버튼과 저장하기 버튼 
    이렇게 버튼이 2개 있는데 
    driverCheckAction으로 POST방식으로 보낸다.
    """
    return render_template('driverCheck.html')

@app.route('/driverCheckAction',methods = ["POST"])
def driverCheckAction():
    btn_value = request.values.get("btn_value")
    if btn_value == "yes":
        """작성을 완료하면 세션의 count를 1로 만들고 lastpage로 리턴 """
        session['count'] = 1
        return render_template('lastpage.html',driver_name = session.get('driver_name'),phone_number=session.get('phone_number'),car_number=session.get('car_number'))
    else:
        """수정해야 하면 다시 driverform으로 보낸다."""
        return redirect(url_for('driverform'))
    
# @app.route('/lastpage')
# def lastpage():
#     return render_template('lastpage.html')    

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