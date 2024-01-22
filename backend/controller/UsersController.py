import database.database as database
from flask import Flask,request,session,make_response,jsonify
import repository.UserRepository as user_repo
import hashlib
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def Register():
    conn = database.connector()
    cursor = conn.cursor() 

    query = user_repo.QueryRegisterUser()
    try:
        data = request.json
        username = data["username"]
        passwords = data["password"]
        userType = data["usertype"]

        passwords = hashlib.md5(passwords.encode('utf8')).hexdigest()
        values = (username,passwords,userType)
        cursor.execute(query,values)

        conn.commit()
        hasil = {"status" : "success"}

    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "failed"}

    cursor.close()
    conn.close()
    return hasil


def Login():
    conn = database.connector()
    cursor = conn.cursor()

    try:
        data = request.json
        username = data["username"]
        passwords = data["password"]

        passwords = hashlib.md5(passwords.encode('utf8')).hexdigest()
        query = user_repo.QuerySelectUser(username,passwords)
       

        cursor.execute(query)
        user = cursor.fetchall()

        userType = 0
        for data in user:
            iduser = data[0]
            userType = int(data[4])
           

        if user:
            session['loggedin'] = True
            session['id'] = iduser
            session['username'] = username
            session['usertype'] = userType

            hasil = {"status" : "success",
                    "usertype" : userType,
                    "username" : username,
                    "id" : iduser
                    }
        query_logged = user_repo.QueryTransactionLogin()
        now = datetime.now()
        values_logged = (now,iduser)
        cursor.execute(query_logged,values_logged)
        conn.commit()

        cursor.close()
        conn.close()

    except Exception as e:
        print("error",str(e))
        hasil = {"status" : "error"}

    return hasil

def GetUsertypeLogged():
    if session['loggedin'] == True:
        usertype_logged = session["usertype"]
       
        return usertype_logged

def GetUserLogged():
    if session['loggedin'] == True:
        username_logged = session["username"]
        return username_logged



def ShowUserBySuperUser():
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = user_repo.QueryShowDetailSAdmin()
        print("query : ",query)
        cursor.execute(query)
        records = cursor.fetchall()

        row_headers = [x[0] for x in cursor.description]
        json_data = []

        for data in records:
            json_data.append(dict(zip(row_headers,data)))
            
        cursor.close()
        conn.close()
        return make_response(jsonify(json_data),200)

    except Exception as e:
        print("error",str(e))
        return {"status" : "failed"}

def ShowUserByStaff(iduser):
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = user_repo.QueryShowDetailStaff(iduser)   
        cursor.execute(query)
        records = cursor.fetchall()

        row_headers = [x[0] for x in cursor.description]
        json_data = []

        for data in records:
            json_data.append(dict(zip(row_headers,data)))
            
        cursor.close()
        conn.close()
        return make_response(jsonify(json_data),200)

    except Exception as e:
        print("error",str(e))
        return {"status" : "failed"}


def ShowBasicInfoStaff(id):
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = user_repo.QueryBasicInfoStaff(id)
        cursor.execute(query)
        records = cursor.fetchall()

        row_headers = [x[0] for x in cursor.description]
        json_data = []

        for data in records:
            json_data.append(dict(zip(row_headers,data)))
            
        cursor.close()
        conn.close()
        return make_response(jsonify(json_data),200)

    except Exception as e:
        print("error",str(e))
        return {"status" : "failed"}


def AddDetailInformation():
    conn = database.connector()
    cursor = conn.cursor()

    try:
        if session['loggedin'] == True:
            query = user_repo.QueryAddDetailUsers()

            data = request.json

            iduser = session['id']
            fullname = data["fullname"]
            adress = data["adress"]
            city = data["city"]
            telephone = data["telephone"]

            values = (fullname,adress,city,telephone,iduser)
            cursor.execute(query,values)
            conn.commit()

            cursor.close()
            conn.close()
            output = {"status" : "success"}

    except Exception as e:
        output = {"status" : "failed"}
        print("error",str(e))
    
    return output


def UpdateDetailInformation():
    conn = database.connector()
    cursor = conn.cursor()

    try:
        if session['loggedin'] == True:
           
            data = request.json

            iduser = session['id']
            fullname = data["fullname"]
            adress = data["adress"]
            city = data["city"]
            telephone = data["telephone"]
            
            query = user_repo.QueryUpdateDetailUsers()
            values = (fullname,adress,city,telephone,iduser)
            
            cursor.execute(query,values)
            conn.commit()

            cursor.close()
            conn.close()
            output = {"status" : "success"}

    except Exception as e:
        output = {"status" : "failed"}
        print("error",str(e))
    
    return output


def ShowAllMember():
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = user_repo.QueryShowMembers()
        cursor.execute(query)
        records = cursor.fetchall()

        row_headers = [x[0] for x in cursor.description]
        json_data = []

        for data in records:
            json_data.append(dict(zip(row_headers,data)))
            
        cursor.close()
        conn.close()
        return make_response(jsonify(json_data),200)

    except Exception as e:
        print("error",str(e))
        return {"status" : "failed"}

def Logout():
    
    try:

        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('username', None)

        session.clear()        
        hasil = {"status" : "success"}
    except:
        hasil = {"status" : "failed"}
    return hasil