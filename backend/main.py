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
app.secret_key = os.getenv('KEY')

CORS(app)

class main():
  
    #CRUD book stocks
    @app.route('/api/books',methods = ['POST'])
    def add_books():
        return InsertBookStock()

    @app.route('/api/getbooks',methods = ['GET'])
    def show_books():
        return ShowBooks()

    @app.route('/api/update_book/<isbn>',methods = ['POST'])
    def update_books(isbn):
        return UpdateBooks(isbn)
    
    @app.route('/api/delete_book/<isbn>',methods = ['DELETE'])
    def delete_books(isbn):
        return DeleteBooks(isbn)

    @app.route('/api/details_book/<isbn>',methods = ['GET'])
    def detail_books(isbn):
        return DetailBooks(isbn)

    @app.route('/api/details_book_return/<isbn>',methods=['GET'])
    def detail_books_return(isbn):
        return DetailBooksReturn(isbn)


    @app.route('/api/showbooks_byid/<isbn>',methods= ['GET'])
    def get_books_id(isbn):
        return BoosByISBN(isbn)
    

    #Borrow Books
    @app.route('/api/borrow',methods = ['POST'])
    def create_borrow():
        return CreatePeminjaman()
    
    @app.route('/api/list_borrow_users/<idborrow>',methods=['GET'])
    def show_detailborrow_users(idborrow):
        return ShowDetailPeminjamanUsers(idborrow)
    
    @app.route('/api/list_borrow_return/<idborrow>',methods = ['GET'])
    def show_detailborrow_return(idborrow):
        return ShowDetailPeminjamanReturn(idborrow)

    @app.route('/api/list_borrow/<idborrow>',methods = ['GET'])
    def show_borrows_byid(idborrow):
        return ShowPeminjamanById(idborrow)
    
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
    @app.route('/api/list_borrow_member/<userid>',methods = ['GET'])
    def show_borrowMember(userid):
        return ShowBorrowooksByMember(userid)
    
    @app.route('/api/list_return_member/<userid>',methods = ['GET'])
    def show_returnMember(userid):
        return ShowReturnBooksMember(userid)


    #Return Books
    @app.route('/api/create_return',methods = ['POST'])
    def create_return():
        return CreateReturn()


    @app.route('/api/create_return_peminjam/<idborrow>',methods = ['POST'])
    def create_return_peminjam(idborrow):
        return CreateReturnByPeminjam(idborrow)

    @app.route('/api/list_returnbook',methods = ['GET'])
    def listreturn_book():
        return ShowBookIsReturn()
    
    @app.route('/api/detail_returnbook/<idreturn>',methods = ['GET'])
    def detail_returnBooks(idreturn):
        return ShowDetailReturnBooks(idreturn)
    
    #Violation
    @app.route('/api/create_violation',methods = ['POST'])
    def create_violation():
        return CreateViolationBook()
    
    @app.route('/api/violation_type',methods = ['GET'])
    def show_violation_type():
        return ShowViolationType()
    
    @app.route('/api/create_violation_peminjam/<idborrow>',methods = ['POST'])
    def create_violation_peminjam(idborrow):
        return CreateViolationByPeminjam(idborrow)
    
    @app.route('/api/damage_level',methods=['GET'])
    def show_damage_type():
        return ShowDamageLevel()

    @app.route('/api/violation_peminjam/<idborrow>',methods = ['GET'])
    def show_violation_peminjam(idborrow):
        return ShowViolationByPeminjam(idborrow)

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
    
    @app.route('/api/staff_basic/<id>',methods = ['GET'])
    def basic_staff(id):
        return ShowBasicInfoStaff(id)

    @app.route('/api/staff_logged/<iduser>',methods = ['GET'])
    def detail_staff(iduser):
        return ShowUserByStaff(iduser)

    @app.route('/api/sadmin_logged',methods = ['GET'])
    def detail_sadmin():
        return ShowUserBySuperUser()

    @app.route('/api/add_detailuser',methods = ['POST'])
    def add_detailuser():
        return AddDetailInformation()

    @app.route('/api/update_detailuser',methods = ['POST'])
    def update_detailuser():
        return UpdateDetailInformation()
    
    @app.route('/api/show_members',methods = ['GET'])
    def show_members():
        return ShowAllMember()

    if __name__ =="__main__":
        app.run(host='0.0.0.0',debug = True,port = 8181) 
        print("Connected to port 8181")