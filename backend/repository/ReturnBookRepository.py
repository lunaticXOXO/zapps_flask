
def QueryCreateReturnBook():
    query = "INSERT INTO book_return(idreturn,nama_pengembali,tanggal_kembali,isReturn,quantity,nisn_book,userid,borrow)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    return query


def QueryShowBookIsReturn():
    query = """SELECT book_return.idreturn,book_return.nama_pengembali, 
		 book_return.tanggal_kembali,
		 book_return.quantity,book_stock.bookname
FROM book_return 
JOIN book_stock ON book_stock.isbn = book_return.nisn_book
JOIN users ON users.id = book_return.userid
WHERE book_return.isReturn = 1"""
    return query