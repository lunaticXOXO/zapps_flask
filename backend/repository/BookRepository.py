

def QueryShowBook():
  query = "SELECT * FROM book_stock"
  return query


def QueryAddBooks():
  query = "INSERT INTO book_stock(isbn,bookname,author,penerbit,category,quantity,price)VALUES(%s,%s,%s,%s,%s,%s,%s)" 
  return query


def QueryUpdateBooks():
  query = "UPDATE book_stock SET isbn = %s, bookname = %s, author = %s, penerbit = %s, category = %s, quantity = %s, price = %s WHERE isbn = %s"
  return query

def QueryDeleteBooks(isbn):
  query = "DELETE FROM book_stock WHERE isbn = '"+isbn+"'"
  return query


def QueryGetQuantityBooks(isbn):
  query = "SELECT quantity FROM book_stock WHERE isbn = '"+isbn+"'"
  return query


def QueryUpdateQuantityBooks(quantity,isbn):
  query = "UPDATE book_stock SET quantity = '"+quantity+"' WHERE isbn = '"+isbn+"'"
  return query


def QueryGetPriceBooks(isbn):
  query = "SELECT price FROM book_stock WHERE isbn = '"+isbn+"'"
  return query