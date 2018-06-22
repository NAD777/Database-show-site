import sqlite3
from person import Person
class db:
    def __init__(self):
        self.conn = sqlite3.connect('man.db')  # person.db
        self.cursor = self.conn.cursor()

    def commit(self,Person):
        self.cursor.execute("INSERT INTO person VALUES (:name,:surname)",
                  {'name': Person.name, 'surname': Person.surname})
        self.conn.commit()
    def get_date(self,colomn,person):
        self.cursor.execute("SELECT * FROM person WHERE "+colomn+'='+"'"+person+"'") # c.execute("SELECT * FROM  person WHERE id = 'Ilya'")
        print(self.cursor.fetchall())
        self.conn.commit()
    def new_base(self):
        self.cursor.execute("""CREATE TABLE  person (
            name text,
            surname text
        )""")
    def close(self):
            self.conn.close()



name="Anton"
surname="Nekhaev"
#Person1 = Person(name,surname)
database = db()
#database.new_base()
#database.commit(Person1)
database.get_date('name','Anton')
database.close()


