


def QueryCreateViolation():
    query = "INSERT INTO book_violation(nama,biaya_denda,violation_type,nisn_book,userid)VALUES(%s,%s,%s,%s,%s)"
    return query