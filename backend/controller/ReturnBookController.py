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
        query = return_repo.QueryCreateReturnBook()
        data = request.json

        idreturn = data["idreturn"]
        nama_pengembali = data["nama_pengembali"]
        tanggal_kembali = datetime.now()
        tanggal = tanggal_kembali.date()
        isReturn = 1
        quantity_return = data["quantity"]
        quantity_return = int(quantity_return)
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

        output = None
        if tanggal < dateline:
            cek = False
        else:
            query_violation = violation_repo.QueryCreateViolation()
            biaya = range_date * os.getenv('DENDA_HARI')
            values_violation = (nama_pengembali,biaya,2,nisn_book,userid,idreturn)
            cursor.execute(query_violation,values_violation)
            cek = True
            print("test")
        conn.commit()
        
        if cek == False:
            output = {"status" : "success", "denda" : "False"}
        else:
            output = {"status" : "success", "denda" : "True"}
        
    except Exception as e:
        print("error",str(e))
        output = {"status" : "failed"}

    return output


def CreateReturnByPeminjam(idborrow):
    conn = database.connector()
    cursor = conn.cursor()
    try:
        query = borrow_repo.QueryShowPeminjamanById(idborrow)
        cursor.execute(query)

        data = request.json
        idreturn = data["idreturn"]
        quantity_return = data["quantity"]
        quantity_return = int(quantity_return)

        records = cursor.fetchall()
        for index in records:
            idborrow = index[0]
            nama_peminjam = index[1]
            isbn = index[6]
            userid = index[7]

        tanggal_kembali = datetime.now()
        tanggal = tanggal_kembali.date()
        isReturn = 1

        query_insert = return_repo.QueryCreateReturnBook()
        values = (idreturn,nama_peminjam,
                    str(tanggal),isReturn,
                    quantity_return,isbn,
                    userid,idborrow)
       
        cursor.execute(query_insert,values)
        quantity_books = GetQuantityBookStock(isbn)
        qty_bookstock = quantity_books + quantity_return
           
        query_updateQty = book_repo.QueryUpdateQuantityBooks(str(qty_bookstock),isbn)
        cursor.execute(query_updateQty)
        quantity_borrow = GetQuantityBookBorrow(idborrow)
            
        qty_borrowNow = 0
        query_updatePinjam = borrow_repo.QueryUpdateStatusPeminjaman(idborrow)

        qty_borrowNow = quantity_borrow - quantity_return
        dateline = GetDeadlineBooks(idborrow)
        range_date = (tanggal - dateline).days

        output = None
        #Jika tepat waktu
        if tanggal <= dateline:
            if qty_borrowNow <= 0:
                values_update = (qty_borrowNow,0,0)
            else:
                values_update = (qty_borrowNow,1,0)
            cursor.execute(query_updatePinjam,values_update)
            cek = False

        #Jika telat
        else:
            if qty_borrowNow <= 0:
                values_update = (qty_borrowNow,0,2)
            else:
                values_update = (qty_borrowNow,1,2)
            cursor.execute(query_updatePinjam,values_update)

            query_violation = violation_repo.QueryCreateViolation()
            denda_hari = os.getenv('DENDA_HARI')
            denda_hari = int(denda_hari)
            biaya = range_date * denda_hari

            print("denda hari :",denda_hari)
            print("biaya : ",biaya)
            print("range_date : ",range_date)

            values_violation = (nama_peminjam,biaya,quantity_return,2,idborrow)
            cursor.execute(query_violation,values_violation)

            cek = True
            print("test")
        conn.commit()
        
        if cek == False:
            output = {"status" : "success", "denda" : "False"}
        else:
            output = {"status" : "success", "denda" : "True"}
        
    except Exception as e:
        print("error",str(e))
        output = {"status" : "failed"}

    return output
       


def ShowBookIsReturn():
    conn = database.connector()
    cursor = conn.cursor()

    try:
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




def ShowDetailReturnBooks(idreturn):
    conn = database.connector()
    cursor = conn.cursor()
    
    try:
        query = return_repo.QueryDetailReturnByID(idreturn)
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