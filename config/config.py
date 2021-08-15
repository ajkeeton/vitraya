import sqlite3

con = sqlite3.connect('conf.db')

def make_sensor(row):
    return [{
        "id": row[0],
        "type": row[1],
        "midi_chan": int(row[2]),
    }]

def make_led(row):
    return [{
        "id": row[0],
        "min": float(row[2]),
        "max": float(row[3]),
        "init": float(row[4]),
        "vel": float(row[5])
    }]

def load_sql():
    q = """
        select s.id, s.type, s.midi_chan,
            (select l.id, l.sid, l.min, l.max, l.init from leds as l where l.sid = s.id) 
        from sensors as s
        """

    q = """select l.*, s.* from leds as l inner join sensors s on l.sid = s.id"""

    cur = con.cursor()
    rows = cur.execute(q).fetchall()

    conf = { "sensors": [], "leds": [] }
    for row in rows:
        print(row)
        conf["sensors"] += make_sensor(row)
        conf["leds"] += make_led(row)

    return conf

def new():
    cur = con.cursor()

    qs = [
        'drop table if exists sensors;',
        'drop table if exists leds;',
        ''' 
        create table sensors (
            id integer primary key,
            type string,
            midi_chan integer
        );
        ''',
        '''
        create table leds (
            id integer primary key,
            sid integer,
            min real,
            max real,
            init real,
            vel real,
            foreign key(sid) references sensors(id)
        );
        '''
    ]
    for q in qs:
        cur.execute(q)

    con.commit()

def mock():
    cur = con.cursor()

    qs = [
        '''insert into sensors (id, type, midi_chan) 
            values 
              (0, "infrared", 0),
              (1, "infrared", 1),
              (2, "infrared", 2),
              (3, "infrared", 3)

        ''',
        '''insert into leds (sid, min, max, init, vel) 
            values 
              (0, 0, 127, 50, 10),
              (1, 50, 100, 50, 20),
              (2, 90, 127, 120, 10),
              (3, 0, 127, 100, 10)
        ''',
    ]
    for q in qs:
        cur.execute(q)
    
    con.commit()
