
def QueryCreatePeminjaman():
    query = "INSERT INTO book_borrow(idborrow,nama_peminjam,tanggal_pinjam,deadline_pinjam,quantity,isBorrow,nisn_book,userid)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    return query


def QueryUpdateDuedate(deadline_pinjam,idborrow):
    query = "UPDATE book_borrow SET deadline_pinjam = '"+deadline_pinjam+"' WHERE idborrow = '"+idborrow+"'"
    return query


def QueryShowBukuIsPinjam():
    query = """SELECT book_borrow.idborrow,book_borrow.nama_peminjam, 
            book_borrow.tanggal_pinjam, book_borrow.deadline_pinjam,
            book_borrow.quantity,book_stock.bookname
            FROM book_borrow 
            JOIN book_stock ON book_stock.isbn = book_borrow.nisn_book
            JOIN users ON users.id = book_borrow.userid
            WHERE book_borrow.isBorrow = 1"""
    return query


def QueryShowBukuReturn():
    query = """SELECT book_borrow.idborrow,book_borrow.nama_peminjam, 
        book_borrow.tanggal_pinjam, book_borrow.deadline_pinjam,
        book_borrow.quantity,book_stock.bookname
        FROM book_borrow 
        JOIN book_stock ON book_stock.isbn = book_borrow.nisn_book
        JOIN users ON users.id = book_borrow.userid
        WHERE book_borrow.isBorrow = 0"""
    return query


def QueryShowDetailPeminjamanUsers(idborrow):
    query = "SELECT * FROM book_borrow JOIN users ON users.id = book_borrow.userid JOIN book_stock ON book_stock.isbn = book_borrow.nisn_book WHERE book_borrow.idborrow = '"+idborrow+"'"
    return query


def QueryShowDetailPeminjamanReturn(idborrow):
    query = "SELECT * FROM book_borrow JOIN book_return ON book_return.borrow = book_borrow.idborrow WHERE book_borrow.idborrow = '"+idborrow+"'"
    return query

def QueryShowPeminjamanById(idborrow):
    query = "SELECT * FROM book_borrow WHERE idborrow = '"+idborrow+"'"
    return query




def QueryGetDeadline(idborrow):
    query = "SELECT deadline_pinjam FROM book_borrow WHERE idborrow = '"+idborrow+"'"
    return query


def QueryShowBorrowBookMember(userid):
    query = "SELECT book_borrow.idborrow,book_borrow.nama_peminjam,book_borrow.tanggal_pinjam,book_borrow.deadline_pinjam,book_borrow.quantity,book_stock.isbn,book_stock.bookname,book_borrow.userid FROM book_borrow JOIN book_stock ON book_stock.isbn = book_borrow.nisn_book WHERE book_borrow.userid = '"+userid+"' AND book_borrow.isBorrow = 1"
    return query


def QueryShowReturnBookMember(userid):
    query = "SELECT book_borrow.idborrow,book_borrow.nama_peminjam,book_borrow.tanggal_pinjam,book_borrow.deadline_pinjam,book_borrow.quantity,book_stock.isbn,book_stock.bookname FROM book_borrow JOIN book_stock ON book_stock.isbn = book_borrow.nisn_book WHERE book_borrow.userid = '"+userid+"' AND book_borrow.isBorrow = 0"
    return query


def QueryShowQuantityBorrow(idborrow):
    query = "SELECT quantity FROM book_borrow WHERE idborrow = '"+idborrow+"'"
    return query


def QueryUpdateStatusPeminjaman(idborrow):
    query = "UPDATE book_borrow SET quantity = %s, isBorrow = %s WHERE idborrow = '"+idborrow+"'"
    return query


def QueryGetDateline(idborrow):
    query = "SELECT deadline_pinjam FROM book_borrow WHERE idborrow = '"+idborrow+"'"
    return query