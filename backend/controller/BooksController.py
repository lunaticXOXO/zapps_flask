from flask import Flask,request,make_response,jsonify,session
import database.database as database
import repository.BookRepository as books_repo
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY','your_secret_key')

def InsertBookStock():
    conn = database.connector()
    cursor = conn.cursor()
    query = books_repo.QueryAddBooks()
    try:
       
        data = request.json

        isbn = data["isbn"]
        bookname = data["bookname"]
        author = data["author"]
        penerbit = data["penerbit"]
        category = data["category"]
        quantity = data["quantity"]
        price = data["price"]

        values = (isbn,bookname,
                    author,penerbit,
                    category,quantity,
                    price)
            
        cursor.execute(query, values)
        conn.commit()
      
        cursor.close()
        conn.close()

        output = {"status" : "success"}
    except Exception as e:
        print("error",str(e))
        output = {"status" : "failed"}

    return output


def UpdateBooks(isbn):
    conn = database.connector()
    cursor = conn.cursor()
    query = books_repo.QueryUpdateBooks()
    try:
        data = request.json

        isbn = data["isbn"]
        bookname = data["bookname"]
        author = data["author"]
        penerbit = data["penerbit"]
        category = data["category"]
        quantity = data["quantity"]
        price = data["price"]

        values = (isbn,bookname,
                    author,penerbit,
                    category,quantity,
                    price,isbn)
            
        cursor.execute(query,values)
        conn.commit()
       
        cursor.close()
        conn.close()
        output = {"status" : "success"}

    except Exception as e:
        output = {"status" : "failed"}
        print("error",str(e))
    
    return output

def ShowBooks():
    conn = database.connector()
    cursor = conn.cursor()

    try:
    
        query = books_repo.QueryShowBook()
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
    
   


def DeleteBooks(isbn):
    conn = database.connector()
    cursor = conn.cursor()
   
    try:
        query = books_repo.QueryDeleteBooks(isbn)
        cursor.execute(query)
        conn.commit()
        output = {"status" : "success"}

    except Exception as e:
        output = {"status" : "failed"}
        print("error",str(e))
    
    cursor.close()
    conn.close()

    return output


def DetailBooks(isbn):
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = books_repo.QueryDetailBooks(isbn)
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
    

def DetailBooksComplete(isbn):
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = books_repo.QueryDetailBooks2(isbn)
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

def DetailBooksReturn(isbn):
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = books_repo.QueryDetailBooksReturn(isbn)
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

def BoosByISBN(isbn):
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = books_repo.QueryGetBooksById(isbn)
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



def GetPriceBooks(isbn):
    conn = database.connector()
    cursor = conn.cursor()

    try:
        query = books_repo.QueryGetPriceBooks(isbn)
        cursor.execute(query)
        data = cursor.fetchone()

        price = data[0]

    except Exception as e:
        print("error",str(e))
        
    return price