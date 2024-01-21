


def QueryCreateViolation():
    query = "INSERT INTO book_violation(nama,biaya_denda,quantity_denda,violationtypes,borrowid)VALUES(%s,%s,%s,%s,%s)"
    return query


def QueryShowViolationType():
    query = "SELECT * FROM violation_type"
    return query


def QueryDamagedType():
    query = "SELECT * FROM damage_level"
    return query


def QueryDamagedTypeById(id):
    query = "SELECT * FROM damage_level WHERE id = '"+id+"'"
    return query


def QueryShowDamagedType():
    query = "SELECT * FROM damage_level"
    return query


def QueryShowPelanggaranByPeminjam(idborrow):
    query = "SELECT * FROM book_violation JOIN violation_type ON violation_type.id = book_violation.violationtypes WHERE borrowid = '"+idborrow+"'"
    return query