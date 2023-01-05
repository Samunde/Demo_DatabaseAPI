import mysql.connector as mariadb

class ConnectionDAO:
    con=None
    cur=None
    @classmethod
    def connect(cls):
        cls.con=mariadb.connect(user="root",
                                    password="samundeeswari",
                                    database="test_sam_db"
                                    )
        cls.cur=cls.con.cursor()
    @classmethod
    def close(cls):
        if not cls.con:
            cls.con.close()
class Queries:
    
    create_user_t="create table user\
                    (Email varchar(100),\
                      Name varchar(50),\
                        Password varchar(30))"
    insert_user="insert into user(Email,Name,Password) \
                values('ywbaek@perscholas.org','young','letsgomates'),\
                        ('mcordon@perscholas.org','marcial','perscholas'),\
                            ('mhaseep@perscholas.org','haseep','platform')"
class userDAO(ConnectionDAO):
    def generate_user_table(self):
        userDAO.connect()
        userDAO.cur.execute(Queries.create_user_t)

        userDAO.cur.execute(Queries.insert_user)
        userDAO.con.commit()
        
        userDAO.con.close()
def main():
    u=userDAO()
    u.generate_user_table()
main()