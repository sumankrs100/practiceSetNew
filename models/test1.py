"""
Test class 1
"""


class Test1:
    def __init__(self, db, first_name=None, last_name=None, dob=None, sex=None):
        self.db = db
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.sex = sex
        self.create_record()

    def __repr__(self):
        return "<Person(name='{} {}', dob={}, sex={})>" \
            .format(self.first_name, self.last_name, self.dob, self.sex)

    def create_record(self):

        rec_dict = {"first_name": self.first_name,
                    "last_name": self.last_name,
                    "dob": self.dob,
                    "sex": self.sex}
        if None not in rec_dict.values():
            self.db.insert("test_table1", rec_dict)
            self.db.update("test_table1", self.last_name)

    def select_rec(self):
        result = self.db.select("test_table1")
        return result


