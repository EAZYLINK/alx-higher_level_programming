#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import sys
import MYSQLdb

if __name__ = "__main__":
    db = MYSQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) from state in c.fetchall()]#!/usr/bin/python3
    """script that lists all states from the database hbtn_0e_0_usa"""

    import sys
    import MYSQLdb

    if __name__ = "__main__":
        db = MYSQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        c = db.cursor()
        c.execute("SELECT * FROM `states`")
        [print(state) from state in c.fetchall()]
