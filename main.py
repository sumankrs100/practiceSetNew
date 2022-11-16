import json
from argparse import ArgumentParser
import datetime
from dateutil.relativedelta import relativedelta
from config.database import Database
from utils.db_helper import DBHelper
from models.test1 import Test1
from models.test2 import Test2
from models.test3 import Test3


def main():
    parser = ArgumentParser()
    parser.add_argument("-e", "--environment", required=True, choices=("prod", "dev", "test"))
    parser.add_argument("-u", "--user_args")
    args = parser.parse_args()
    env = args.environment
    u_args = args.user_args
    print("Environment: ", env)
    if env == "test" and u_args is None:
        print("unable to get user args so exiting process...")
        exit()
    if u_args:
        try:
            u_dict = json.loads(u_args)
        except Exception:
            u_dict = {}
    else:
        u_dict = {}

    db_con = Database(env, **u_dict)
    db_obj = DBHelper(db_con)
    print("end of main function.....")
    return db_obj


def create_records(db):
    # If no records need to be inserted then comment below three lines
    # Also to change the names change the values in below records
    Test1(db, "f4", "l4", '20/12/2001', 'M')
    Test2(db, "f5", "l5", '21/12/2005', 'M')
    obj_test1 = Test3(db, "f8", "l6", '22/12/1990', 'M')
    # and uncomment below 1 line
    # obj_test1 = Test3(db)
    records = obj_test1.select_rec()
    return records


def get_age_values(records):
    new_recs = []
    for i in records:
        l1 = list(i)
        dob = datetime.datetime.strptime(l1[3], "%d/%m/%Y")
        age = relativedelta(datetime.datetime.now(), dob).years
        l1.append(age)
        new_recs.append(l1)
    return new_recs


def get_rec_above_specific_age(records, age_limit):
    for i in records:
        if i[-1] > age_limit:
            print(i[1], "'s age is ", i[-1], " which greater than ", age_limit)


if __name__ == "__main__":
    db_obj1 = main()
    recs = create_records(db_obj1)
    age_recs = get_age_values(recs)
    get_rec_above_specific_age(age_recs, 18)

    print("end of execution....")
