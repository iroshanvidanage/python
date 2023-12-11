import json
import sqlite3

conn = sqlite3.connect('ass-roster-db.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

file_name = input('Enter file name: ')
if len(file_name) < 1:
    file_name = 'roster_data.json'

str_data = open(file_name).read()
json_data = json.loads(str_data)

for each_entry in json_data:

    name = each_entry[0]
    title = each_entry[1]
    role = each_entry[2]

    print((name, title, role))

    cur.execute('''INSERT OR IGNORE INTO User (name)
            VALUES ( ? )''', (name,))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
            VALUES ( ? )''', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
            (user_id, course_id, role) VALUES ( ?, ? , ?)''',
                (user_id, course_id, role))

conn.commit()