import database.database as database
from flask import Flask,request,session,make_response,jsonify
import repository.BorrowBookRepository as borrow_repo
import repository.BookRepository as book_repo
import repository.ViolationRepository as violation_repo
import controller.ReturnBookController as return_controller
import controller.BooksController as book_controller
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY','your_secret_key')


def CreateViolationBook():
    conn = database.connector()
    cursor = conn.cursor()
    try:
        query = violation_repo.QueryCreateViolation()
        data = request.json
        nama = data["nama"]
        violation_type = data["violation_type"]
        nisn_book = data["bookstock"]
        userid = data["users"]
            
        price_book = book_repo.QueryGetPriceBooks(nisn_book)
        values = (nama,price_book,violation_type,nisn_book,userid)
        cursor.execute(query,values)

        conn.commit()
        output = {"status" : "success", "denda" : "False"}

    except Exception as e:
        print("error",str(e))
        output = {"status" : "failed"}
        
    return output


def CreateViolationByPeminjam(idborrow):
    conn = database.connector()
    cursor = conn.cursor()
    try:
        query_borrow = borrow_repo.QueryShowPeminjamanById(idborrow)
        cursor.execute(query_borrow)
        records = cursor.fetchall()

        data = request.json
        violation_type = data["violation_type"]
        damaged_level  = data["damaged_level"]
        print("test")
       
    
        for index in records:
            idborrow = index[0]
            nama_peminjam = index[1]
            isbn = index[6]


        totalDenda = 0
        deadline = return_controller.GetDeadlineBooks(idborrow)
        quantity_borrow = return_controller.GetQuantityBookBorrow(idborrow)
        priceBook = book_controller.GetPriceBooks(isbn)

        pengajuan_datetime = datetime.now()    
        pengajuan_date = pengajuan_datetime.date()
        range_date = (pengajuan_date - deadline).days

        

        query_damageType = violation_repo.QueryDamagedTypeById(str(damaged_level))
        cursor.execute(query_damageType)
        data = cursor.fetchone()
        idTypeBroken = data[0]
        charged = data[2]


        denda_hari = os.getenv('DENDA_HARI')
        denda_hari = int(denda_hari)
       
        if idTypeBroken == 0:
            if range_date <= 0:
                totalDenda = totalDenda + (priceBook * quantity_borrow)
            else:
                totalDenda = totalDenda + (priceBook * quantity_borrow * denda_hari) * range_date 
        else:
            discount_price = priceBook * charged
            discount_paid = priceBook - discount_price
            if range_date <= 0:
                totalDenda = totalDenda + (discount_paid * quantity_borrow)
            else:
                totalDenda = totalDenda + (discount_paid * quantity_borrow * denda_hari) * range_date 

        query_violation = violation_repo.QueryCreateViolation()
        values = (nama_peminjam,totalDenda,quantity_borrow,violation_type,idborrow)
        cursor.execute(query_violation,values)

        query_updatePinjam = borrow_repo.QueryUpdateStatusPeminjaman(idborrow)
        values_update = (0,0,violation_type)
        cursor.execute(query_updatePinjam,values_update)

        conn.commit()
        cursor.close()
        conn.close()
        output = {"status" : "success"}
    except Exception as e:
        output = {"status" : "failed"}
        print("error",str(e))

    return output

def ShowViolationType():
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = violation_repo.QueryShowViolationType()
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

def ShowDamageLevel():
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = violation_repo.QueryShowDamagedType()
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


def ShowViolationByPeminjam(idborrow):
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = violation_repo.QueryShowPelanggaranByPeminjam(idborrow)
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
