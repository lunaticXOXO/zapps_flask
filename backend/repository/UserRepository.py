
def QueryRegisterUser():
    query = "INSERT INTO users(username,password,usertype)VALUES(%s,%s,%s)"
    return query

def QuerySelectUser(username,password):
    query = "SELECT * FROM users WHERE username = '"+username+"' AND password = '"+password+"'"
    return query


def QueryAddDetailUsers():
    query = "INSERT INTO detail_users(fullname,adress,city,telephone,usersid)VALUES(%s,%s,%s,%s,%s)"
    return query


def QueryUpdateDetailUsers():
    query = "UPDATE detail_users SET fullname = %s, adress = %s, city = %s, telephone = %s WHERE usersid = %s"
    return query

def QueryShowDetailSAdmin():
    query = """SELECT users.username,
		 detail_users.fullname,
		 detail_users.adress,
		 detail_users.city,
		 detail_users.telephone
FROM users 
JOIN detail_users ON detail_users.usersid = users.id
WHERE users.usertype = 1 OR users.usertype = 2"""
    
    return query

def QueryShowDetailStaff(userid):
    query = "SELECT users.username,detail_users.fullname,detail_users.adress,detail_users.city,detail_users.telephone FROM users JOIN detail_users ON detail_users.usersid = users.id WHERE users.id = '"+userid+"' AND users.usertype = 2"

    return query