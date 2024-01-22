import database.database as database
from flask import Flask,request,session,make_response,jsonify
import repository.BorrowBookRepository as borrow_repo
import repository.BookRepository as book_repo
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY','your_secret_key')


def CreatePeminjaman():
    conn = database.connector()
    cursor = conn.cursor()
   
    try:
        query = borrow_repo.QueryCreatePeminjaman()
        data = request.json
        idborrow = data["idborrow"]
        nama_peminjam = data["nama_peminjam"]
        tanggal_pinjam = datetime.now()

        tanggal = tanggal_pinjam.date()
        print("tanggal pinjam : ", tanggal)

        deadline_pinjam = data["deadline_pinjam"]
        quantity_pinjam = data["quantity"]
        quantity_pinjam = int(quantity_pinjam)
        isBorrow = 1
        nisn_book = data["book_stock"]
        userid = data["users"]

        values = (idborrow,
                nama_peminjam,
                str(tanggal),
                deadline_pinjam,
                quantity_pinjam,
                str(isBorrow),
                nisn_book,
                userid)
        
        cursor.execute(query,values)
        query_getqty = book_repo.QueryGetQuantityBooks(nisn_book)
        
        cursor.execute(query_getqty)
        selected = cursor.fetchone()
        quantity_books = selected[0]
           
        quantity_now = quantity_books - quantity_pinjam
        quantity_now = str(quantity_now)

        query_updateqty = book_repo.QueryUpdateQuantityBooks(quantity_now,nisn_book)
        cursor.execute(query_updateqty)

        conn.commit()
        cursor.close()
        conn.close()
        hasil = {"status" : "success"}
        
    except Exception as e:
        hasil = {"status" : "failed"}
        print("error",str(e))

    return hasil


def ShowDetailPeminjamanUsers(idborrow):
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = borrow_repo.QueryShowDetailPeminjamanUsers(idborrow)
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

def ShowDetailPeminjamanReturn(idborrow):
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = borrow_repo.QueryShowDetailPeminjamanReturn(idborrow)
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


def ShowPeminjamanById(idborrow):
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = borrow_repo.QueryShowPeminjamanById(idborrow)
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


def ShowIsPinjamBooks():
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = borrow_repo.QueryShowBukuIsPinjam()
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


def ShowIsReturn():
    conn = database.connector()
    cursor = conn.cursor()

    try:
       
        query = borrow_repo.QueryShowBukuReturn()
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


def UpdateDueDate(idborrow):
    conn = database.connector()
    cursor = conn.cursor()

    try:
        if session['loggedin'] == True and (session['usertype'] == 1 or session['usertype'] == 2):
            data = request.json
            deadline_pinjam = data["deadline_pinjam"]

            query = borrow_repo.QueryUpdateDuedate(deadline_pinjam,idborrow)
            cursor.execute(query)
            conn.commit()

            output = {"status" : "success"}
    except Exception as e:
        print("error",str(e))
        output = {"status" : "success"}

    return output





def ShowBorrowooksByMember(userid):
    conn = database.connector()
    cursor = conn.cursor()

    try:
            query = borrow_repo.QueryShowBorrowBookMember(userid)
          
            values = (userid)
            cursor.execute(query,values)
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


def ShowReturnBooksMember(userid):
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = borrow_repo.QueryShowReturnBookMember(userid)
        values = (userid)
        cursor.execute(query,values)
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


