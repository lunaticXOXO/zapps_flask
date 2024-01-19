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


def CreateViolationBook():
    conn = database.connector()
    cursor = conn.cursor()
    try:
        if session['loggedin'] == True and (session['usertype'] == 1 or session['usertype'] == 2):
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

