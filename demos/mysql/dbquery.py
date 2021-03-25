import mysql.connector
# now wrap in try ... mysql.connector.connect(host='localhost',database='mylib',user='root',password='')



from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='mylib',
                                       user='root',
                                       password='')
        if conn.is_connected():
            print('Connected to MySQL database')

        mycursor = conn.cursor()
#insert sql statements here
        mycursor.execute("SELECT * FROM Author")

        myresult = mycursor.fetchall()

        for authors in myresult:
            print(authors)
    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()

