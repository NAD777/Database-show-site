import sqlite3

class db:
    def __init__(self):
        self.conn = sqlite3.connect('man.db',check_same_thread=False)  # person.db
        self.cursor = self.conn.cursor()

    def commit(self,name,surname):
        self.cursor.execute("INSERT INTO person VALUES (:name,:surname)",
                  {'name': name, 'surname': surname})
        self.conn.commit()
    def get_date(self,colomn,person,fetch='all'):
        self.cursor.execute("SELECT * FROM person WHERE "+colomn+'='+"'"+person+"'") # c.execute("SELECT * FROM  person WHERE id = 'Ilya'")
        if(fetch == 'all'):
            print(self.cursor.fetchall())
        elif(fetch=='one'):
            print(self.cursor.fetchone())
        elif(fetch=='many'):
            print(self.cursor.fetchmany())
        else:
            print('Nothing happend')
        self.conn.commit()

    def new_base(self):
        self.cursor.execute("""CREATE TABLE  person (
            name text,
            surname text
        )""")
    def close(self):
            self.conn.close()



#name="Ilya"
#surname="Kolomin"
#Person1 = Person(name,surname)
#database = db()
#database.new_base()
#database.commit('Anton','jopa')
#database.get_date('name','Anton')
#database.close()


