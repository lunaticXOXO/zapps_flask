import database.database as database
from flask import Flask,request,session,make_response,jsonify
import repository.ReturnBookRepository as return_repo
import repository.BorrowBookRepository as borrow_repo
import repository.BookRepository as book_repo
import repository.ViolationRepository as violation_repo
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY','your_secret_key')


def GetQuantityBookStock(nisn_book):
      conn = database.connector()
      cursor = conn.cursor()
      query_qtyBook = book_repo.QueryGetQuantityBooks(nisn_book)
      cursor.execute(query_qtyBook)
      datas = cursor.fetchone()
      quantity_books = datas[0]

      return quantity_books


def GetQuantityBookBorrow(borrow):
    conn = database.connector()
    cursor = conn.cursor()
    query_qtyBorrow = borrow_repo.QueryShowQuantityBorrow(borrow)
    cursor.execute(query_qtyBorrow)

    datas2 = cursor.fetchone()
    quantity_borrow = datas2[0]
    return quantity_borrow


def GetDeadlineBooks(borrow):
    conn = database.connector()
    cursor = conn.cursor()
    query = borrow_repo.QueryGetDeadline(borrow)
    cursor.execute(query)

    data = cursor.fetchone()
    dateline = data[0]
    return dateline

def CreateReturn():
    conn = database.connector()
    cursor = conn.cursor()
    try:
        if session['loggedin'] == True and (session['usertype'] == 1 or session['usertype'] == 2):
            query = return_repo.QueryCreateReturnBook()
            data = request.json

            idreturn = data["idreturn"]
            nama_pengembali = data["nama_pengembali"]
            tanggal_kembali = datetime.now()
            tanggal = tanggal_kembali.date()
            isReturn = 1
            quantity_return = data["quantity"]
            nisn_book = data["book_stock"]
            userid = data["users"]
            borrow = data["borrow"]

            values = (idreturn,nama_pengembali,
                    str(tanggal),isReturn,
                    quantity_return,nisn_book,
                    userid,borrow)
            
            cursor.execute(query,values)
            quantity_books = GetQuantityBookStock(nisn_book)
            qty_bookstock = quantity_books + quantity_return
           
            query_updateQty = book_repo.QueryUpdateQuantityBooks(str(qty_bookstock),nisn_book)
            cursor.execute(query_updateQty)
            quantity_borrow = GetQuantityBookBorrow(borrow)
            
            qty_borrowNow = 0
            query_updatePinjam = borrow_repo.QueryUpdateStatusPeminjaman(borrow)
            qty_borrowNow = quantity_borrow - quantity_return
            if qty_borrowNow <= 0:
                values_update = (qty_borrowNow,0)
            else:
                values_update = (qty_borrowNow,1)

            cursor.execute(query_updatePinjam,values_update)

            dateline = GetDeadlineBooks(borrow)
            range_date = (tanggal - dateline).days

            if tanggal < dateline:
               cek = False
            else:
                query_violation = violation_repo.QueryCreateViolation()
                biaya = range_date * os.getenv('DENDA_HARI')
                values_violation = (nama_pengembali,biaya,2,nisn_book,userid)
                cursor.execute(query_violation,values_violation)
                cek = True

            conn.commit()
            if cek == False:
                output = {"status" : "success", "denda" : "False"}
            else:
                output = {"status" : "success", "denda" : "True"}
        else:
            output = {"status" : "unauthorized"}

    except Exception as e:
        print("error",str(e))
        output = {"status" : "failed"}

    return output


def ShowBookIsReturn():
    conn = database.connector()
    cursor = conn.cursor()

    try:
        if session['loggedin'] == True and (session['usertype'] == 1 or session['usertype'] == 2):
            query = return_repo.QueryShowBookIsReturn()
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