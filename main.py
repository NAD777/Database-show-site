import sqlite3


class db:
    def __init__(self):
        self.conn = sqlite3.connect('person.db', check_same_thread=True)  # person.db
        self.cursor = self.conn.cursor()

    def write_unicode(self, text, charset='windows-1251'):
        return text.encode(charset)

    def commit(self, name, surname, patronymic, gender, inspection):
        self.cursor.execute("INSERT INTO person VALUES (:name,:surname,:patronymic,:gender,:inspection)",
                            {'name': name, 'surname': surname, 'patronymic': patronymic, 'gender': gender,
                             'inspection': inspection})
        self.conn.commit()

    def get_date(self, colomn, person, fetch='all'):
        self.cursor.execute(
            "SELECT * FROM person WHERE " + colomn + '=' + "'" + person + "'")  # c.execute("SELECT * FROM  person WHERE id = 'Ilya'")
        if (fetch == 'all'):
            return self.cursor.fetchall()
        elif (fetch == 'one'):
            return self.cursor.fetchone()
        elif (fetch == 'many'):
            return self.cursor.fetchmany()
        else:
            print('Nothing happend')
        # self.conn.commit()

    # def get_list(self, search=''):
    #     results = []
    #     if not search:
    #         self.cursor.execute("select * from person")
    #         for row in self.cursor.fetchall():
    #             # result.append({'name':self.write_unicode(row[0]),'surname':self.write_unicode(row[1])})
    #             results.append(
    #                 {'name': row[0], 'surname': row[1], 'patronymic': row[2], 'gender': row[3], 'inspection': row[4]})
    #         sp = ['name', 'surname', 'patronymic', 'gender', 'inspection']
    #         for i in sp:
    #             for row in self.get_date(i, search):
    #                 results.append({'name': row[0], 'surname': row[1], 'patronymic': row[2], 'gender': row[3],
    #                                 'inspection': row[4]})
    #     results.reverse()
    #     return results
    def get_list(self,search=''):
        results = []
        if not search:
            self.cursor.execute("select * from person")
            for row in self.cursor.fetchall():
                #result.append({'name':self.write_unicode(row[0]),'surname':self.write_unicode(row[1])})
                results.append({'name': row[0], 'surname': row[1], 'patronymic': row[2], 'gender': row[3], 'inspection': row[4]})
        elif search:
            sp=['name','surname','patronymic','gender','inspection']
            for i in sp:
                for row in self.get_date(i,search):
                    results.append({'name': row[0], 'surname': row[1], 'patronymic': row[2], 'gender': row[3],'inspection': row[4]})
        results.reverse()
        return results
    def new_base(self):
        self.cursor.execute("""CREATE TABLE  person (
            name text,
            surname text,
            patronymic text,
            gender text,
            inspection text
        )""")

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    database = db()
    database.new_base()
    # database.commit('Anton','jopa')
    # database.get_date('name','Anton')
    # print(database.get_list())
    database.close()
