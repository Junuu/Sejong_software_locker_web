from flask import Flask, render_template ,request, redirect, session
import hashlib
import pymysql
import bcrypt

app = Flask(__name__)

app.secret_key = "sejonglockerkey"


@app.route("/")
def home():
    db = pymysql.connect(host='localhost', port=3306, user= 'root', passwd='your_password', db='your_dbname')
    cursor = db.cursor()
    sql_A = "SELECT * FROM locker_info WHERE section='A' ORDER BY `row` ,`column`;"
    sql_B = "SELECT * FROM locker_info WHERE section='B' ORDER BY `row` ,`column`;"
    sql_C = "SELECT * FROM locker_info WHERE section='C' ORDER BY `row` ,`column`;"
    sql_D = "SELECT * FROM locker_info WHERE section='D' ORDER BY `row` ,`column`;"
    sql_E= "SELECT * FROM locker_info WHERE section='E' ORDER BY `row` ,`column`;"
    rows_count = cursor.execute(sql_A)    
    get_A_data = cursor.fetchall()
    cursor.execute(sql_B)    
    get_B_data = cursor.fetchall()
    cursor.execute(sql_C)    
    get_C_data = cursor.fetchall()
    cursor.execute(sql_D)    
    get_D_data = cursor.fetchall()
    cursor.execute(sql_E)    
    get_E_data = cursor.fetchall()
    db.close()
    if rows_count > 0:        
        A_table_info = '''A(10*6칸)<table class="tg table3">'''
        count = 1
        for i in range(1,7):
            A_table_info += "<tr>"
            for j in range(1,11):
                A_table_info += '''<td class="'''                
                if get_A_data[(i-1)*10 + (j-1)][3] == "usable":                    
                    A_table_info += '''tg-0lax">''' + str(count)
                elif get_A_data[(i-1)*10 + (j-1)][3] =="disable":
                    A_table_info += '''tg-3ts9">''' + str(count)
                else:
                    A_table_info += '''tg-z0iz">'''+ str(count)
                    #A_table_info += '''tg-z0iz"></td>'''
                count += 1
                A_table_info += '''</td>'''
                
            A_table_info += "</tr>"
        A_table_info += "</table><br><br><br>"

        B_table_info = '''B(10*6칸)<table class="tg table3">'''
        count = 1
        for i in range(1,7):
            B_table_info += "<tr>"
            for j in range(1,11):
                B_table_info += '''<td class="'''
                if get_B_data[(i-1)*10 + (j-1)][3] == "usable":                    
                    B_table_info += '''tg-0lax">''' + str(count)
                elif get_B_data[(i-1)*10 + (j-1)][3] =="disable":
                    B_table_info += '''tg-3ts9">''' + str(count)
                else:
                    B_table_info += '''tg-z0iz">'''+ str(count)                    
                count += 1
                B_table_info += '''</td>'''
            B_table_info += "</tr>"
        B_table_info += "</table><br><br><br>"

        C_table_info = '''C(6*6칸)<table class="tg table3">'''
        count = 1
        for i in range(1,7):
            C_table_info += "<tr>"
            for j in range(1,7):
                C_table_info += '''<td class="'''
                if get_C_data[(i-1)*6 + (j-1)][3] == "usable":                    
                    C_table_info += '''tg-0lax">''' + str(count)
                elif get_C_data[(i-1)*6 + (j-1)][3] =="disable":
                    C_table_info += '''tg-3ts9">''' + str(count)
                else:
                    C_table_info += '''tg-z0iz">'''+ str(count)                    
                count += 1
                C_table_info += '''</td>'''
            C_table_info += "</tr>"
        C_table_info += "</table><br><br><br>"

        D_table_info = '''D(6*6칸)<table class="tg table3">'''
        count = 1
        for i in range(1,7):
            D_table_info += "<tr>"
            for j in range(1,7):
                D_table_info += '''<td class="'''
                if get_D_data[(i-1)*6 + (j-1)][3] == "usable":                    
                    D_table_info += '''tg-0lax">''' + str(count)
                elif get_D_data[(i-1)*6 + (j-1)][3] =="disable":
                    D_table_info += '''tg-3ts9">''' + str(count)
                else:
                    D_table_info += '''tg-z0iz">'''+ str(count)                    
                count += 1
                D_table_info += '''</td>'''
            D_table_info += "</tr>"
        D_table_info += "</table><br><br><br>"

        E_table_info = '''E(6*6칸)<table class="tg table3">'''
        count = 1
        for i in range(1,7):
            E_table_info += "<tr>"
            for j in range(1,7):
                E_table_info += '''<td class="'''
                if get_E_data[(i-1)*6 + (j-1)][3] == "usable":                    
                    E_table_info += '''tg-0lax">''' + str(count)
                elif get_E_data[(i-1)*6 + (j-1)][3] =="disable":
                    E_table_info += '''tg-3ts9">''' + str(count)
                else:
                    E_table_info += '''tg-z0iz">'''+ str(count)                    
                count += 1
                E_table_info += '''</td>'''
            E_table_info += "</tr>"
        E_table_info += "</table><br><br><br>"

        table_info = A_table_info + B_table_info + C_table_info + D_table_info + E_table_info
    else:
        print("nothing")
    
    userid = session.get('userid', None)
    locker_in_used = session.get('locker_in_used',None)
    locker_section = session.get('locker_section',None)    
    locker_num = session.get('locker_num',None)
    print(locker_num)
    locker_num_for_user = 0
    if locker_num != None:
        temp = locker_num.split(',')
        A = int(temp[0][1:-1])
        B = int(temp[1][1:-1])
        print(locker_section)
        print(type(locker_section))
        if locker_section == "A" or locker_section == "B":
            print(locker_section)
            locker_num_for_user=(A-1)*10 + B
        else:            
            locker_num_for_user=(A-1)*6 + B
    print(locker_num_for_user)
    return render_template("index.html",result_mesagge='',userid=userid,locker_in_used=locker_in_used,locker_section=locker_section,locker_num=locker_num,table_info = table_info,locker_num_for_user=locker_num_for_user)

@app.route("/login.html",methods=['GET'])
def login_page():
    
    return render_template("login.html",result_message='')

@app.route('/logout',methods=['GET'])
def logout():
    session.pop('userid',None)
    session.pop('locker_in_use',None)
    session.pop('locker_section',None)
    session.pop('locker_num',None)    
    return redirect('/')

@app.route("/signup.html",methods=['GET'])
def signup_page():            
    return render_template("signup.html",result_message='')

@app.route("/login",methods=['POST'])
def login():
    db = pymysql.connect(host='localhost', port=3306, user= 'root', passwd='your_password', db='your_dbname')
    cursor = db.cursor()
    if request.method =='POST':
        login_info = request.form
        username = login_info['id']
        password = login_info['password']
        print(username,password)

        sql1 = "SELECT * FROM user_info WHERE School_id=%s"
        rows_count = cursor.execute(sql1,username)        
        
        if rows_count > 0:
            user_info = cursor.fetchone()
            db.close()
            is_pw_correct = bcrypt.checkpw(password.encode('UTF-8') , user_info[1].encode('UTF-8'))
            if is_pw_correct:                
                session['userid'] = user_info[0]
                session['locker_in_used'] = user_info[2]
                session['locker_section'] = user_info[3]
                session['locker_num'] = user_info[4]
                return redirect('/')
            else:
                
                return render_template("login.html",result_message="<script>alert('비밀번호가 틀렸습니다.')</script>")

        else:
            return render_template("login.html",result_message="<script>alert('존재하지 않는 아이디 입니다.')</script>")
        
        
    return render_template("login.html",result_mesagge="")



@app.route("/register",methods=['POST'])
def register():
    try:
        if request.method == 'POST':
            db = pymysql.connect(host='localhost', port=3306, user= 'root', passwd='your_password', db='your_dbname')
            cursor = db.cursor()
            register_info = request.form
                    
            username = register_info['id']                        
            check_pass1 = register_info['password']            
            check_pass2 = register_info['password1']
            if username == "":
                return render_template('signup.html',result_message="<script>alert('아이디를 입력해주세요.')</script>")

            if check_pass1 == "":
                return render_template('signup.html',result_message="<script>alert('비밀번호를 입력해주세요.')</script>")
            if check_pass1 != check_pass2:
                return render_template('signup.html',result_message="<script>alert('동일한 비밀번호를 입력해 주세요.')</script>")
            else:
                hashed_password = bcrypt.hashpw(register_info['password'].encode('utf-8'),bcrypt.gensalt())
                print(username,hashed_password)
                sql = "INSERT INTO user_info(School_ID, Password) VALUES (%s,%s);"            

                cursor.execute(sql,(username, hashed_password))
                db.commit()
                db.close()
    except:
        return render_template('signup.html',result_message="<script>alert('현재 존재하는 아이디입니다. 다른 아이디로 회원가입 해주세요.')</script>")
    return render_template('login.html',result_message="<script>alert('회원가입이 완료되었습니다.')</script>")

@app.route('/apply_locker', methods=['POST'])
def apply_locker():    
    if request.method == 'POST':
        db = pymysql.connect(host='localhost', port=3306, user= 'root', passwd='your_password', db='your_dbname')
        cursor = db.cursor()
        data = request.get_data()
        data = data.decode('utf-8')        
        id, tdindex, trindex = data.split(" ")
        section = ''
        # 사물함 구역 얻기
        if int(tdindex) <= 17:
            section = 'A'
        elif int(tdindex) <=23:
            section = 'B'
        elif int(tdindex) <=29:
            section ='C' 
        elif int(tdindex) <=35:
            section = 'D'
        else:
            section = 'E'
        
        tdindex = str((int(tdindex) % 6) + 1)
        
        print(id,section,tdindex,trindex)        
        
        sql = ''' UPDATE user_info SET locker_in_use = 1, locker_section = %s, locker_num = "%s,%s" Where School_ID = %s'''
        cursor.execute(sql,(section,tdindex,trindex,id))        
        sql = '''UPDATE locker_info SET locker_statement = "using" where `row`=%s AND `column`=%s AND section=%s; '''        
        cursor.execute(sql,(tdindex,trindex,section))
        sql1 = "SELECT * FROM user_info WHERE School_id=%s"        
        cursor.execute(sql1,session.get('userid', None))
        user_info = cursor.fetchone()
        session['locker_in_used'] = user_info[2]
        session['locker_section'] = user_info[3]
        session['locker_num'] = user_info[4]
        db.commit()
        db.close()        
        
        
              
        #alert("Row: "+(trindex % 6 +1)+" Column: "+tdindex);
    return redirect("/")

@app.route('/return_locker', methods=['POST'])
def return_locker():    
    if request.method == 'POST':
        db = pymysql.connect(host='localhost', port=3306, user= 'root', passwd='your_password', db='your_dbname')
        cursor = db.cursor()
        data = request.get_data()
        data = data.decode('utf-8')        
        id, tdindex, trindex = data.split(" ")
        section = ''
        # 사물함 구역 얻기
        if int(tdindex) <= 17:
            section = 'A'
        elif int(tdindex) <=23:
            section = 'B'
        elif int(tdindex) <=29:
            section ='C'
        elif int(tdindex) <=35:
            section = 'D'
        else:
            section = 'E'
        
        tdindex = str((int(tdindex) % 6) + 1)
        
        print(id,section,tdindex,trindex)

        sql = ''' UPDATE user_info SET locker_in_use = 0, locker_section = NULL, locker_num = NULL Where School_ID = %s'''
        cursor.execute(sql,id)
        sql = '''UPDATE locker_info SET locker_statement = "usable" where `row`=%s AND `column`=%s AND section=%s; '''        
        cursor.execute(sql,(tdindex,trindex,section))
        sql1 = "SELECT * FROM user_info WHERE School_id=%s"        
        cursor.execute(sql1,session.get('userid', None))
        user_info = cursor.fetchone()
        session['locker_in_used'] = user_info[2]
        session['locker_section'] = user_info[3]
        session['locker_num'] = user_info[4]
        db.commit()
        db.close()
        
    return redirect('/');    


if __name__ == '__main__':
    app.run(debug=True)
