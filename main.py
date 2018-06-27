import sqlite3

class db:
    def __init__(self):
        self.conn = sqlite3.connect('man.db',check_same_thread=False)  # person.db
        self.cursor = self.conn.cursor()

    def write_unicode(self,text, charset='windows-1251'):
        return text.encode(charset)

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

    def get_list(self):
        results = []
        self.cursor.execute("select * from person")
        for row in self.cursor.fetchall():
            #result.append({'name':self.write_unicode(row[0]),'surname':self.write_unicode(row[1])})
          results.append({'name': row[0], 'surname': row[1]})
        return results

    def new_base(self):
        self.cursor.execute("""CREATE TABLE  person (
            name text,
            surname text
        )""")
    def close(self):
            self.conn.close()


if __name__ == "__main__":
    database = db()
    #database.new_base()
    #database.commit('Anton','jopa')
    #database.get_date('name','Anton')
    print(database.get_list())
    database.close()


