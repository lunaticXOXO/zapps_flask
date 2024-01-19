from flask import Flask,session
from flask_cors import CORS
from controller.BooksController import *
from controller.UsersController import *
from controller.BorrowBookController import *
from controller.ReturnBookController import *
from controller.BookViolationController import *
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY','your_secret_key')

CORS(app)

class main():
  
    #CRUD book stocks
    @app.route('/api/books',methods = ['POST'])
    def add_books():
        return InsertBookStock()

    @app.route('/api/books',methods = ['GET'])
    def show_books():
        return ShowBooks()

    @app.route('/api/update_book/<isbn>',methods = ['POST'])
    def update_books(isbn):
        return UpdateBooks(isbn)
    
    @app.route('/api/delete_book/<isbn>',methods = ['DELETE'])
    def delete_books(isbn):
        return DeleteBooks(isbn)

   
    #Borrow Books
    @app.route('/api/borrow',methods = ['POST'])
    def create_borrow():
        return CreatePeminjaman()
    
    @app.route('/api/list_borrow',methods=['GET'])
    def show_detailborrow():
        return ShowDetailPeminjaman()
    
    @app.route('/api/is_borrow',methods = ['GET'])
    def show_isborrow():
        return ShowIsPinjamBooks()
    
    @app.route('/api/is_return',methods = ['GET'])
    def show_isreturn():
        return ShowIsReturn()

    @app.route('/api/update_borrow/<idborrow>')
    def update_duedate(idborrow):
        return UpdateDueDate(idborrow)

    #Borrow Books & Return Member
    @app.route('/api/list_borrow_member',methods = ['GET'])
    def show_borrowMember():
        return ShowBorrowooksByMember()
    
    @app.route('/api/list_return_member',methods = ['GET'])
    def show_returnMember():
        return ShowReturnBooksMember()


    #Return Books
    @app.route('/api/create_return',methods = ['POST'])
    def create_return():
        return CreateReturn()

    @app.route('/api/list_returnbook',methods = ['GET'])
    def listreturn_book():
        return ShowBookIsReturn()
    
    #Violation
    @app.route('/api/create_violation',methods = ['POST'])
    def create_violation():
        return CreateViolationBook()

    #Users
    @app.route('/api/register',methods = ['POST'])
    def register_user():
        return Register()
    
    @app.route('/api/login',methods = ['POST'])
    def login_user():
        return Login()
    
    @app.route('/api/logout',methods = ['POST'])
    def logout():
        return Logout()
    
    @app.route('/api/staff_logged',methods = ['GET'])
    def detail_staff():
        return ShowUserByStaff()

    @app.route('/api/sadmin_logged',methods = ['GET'])
    def detail_sadmin():
        return ShowUserBySuperUser()

    @app.route('/api/add_detailuser',methods = ['POST'])
    def add_detailuser():
        return AddDetailInformation()

    @app.route('/api/update_detailuser',methods = ['POST'])
    def update_detailuser():
        return UpdateDetailInformation()

    if __name__ =="__main__":
        app.run(host='0.0.0.0',debug = True,port = 8181) 
        print("Connected to port 8181")