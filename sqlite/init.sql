DROP TABLE IF EXISTS CLUB_DATA;
DROP TABLE IF EXISTS INPUT_DATA;
DROP TABLE IF EXISTS ROOM_LOG;
DROP TABLE IF EXISTS AUTH;

CREATE TABLE CLUB_DATA (
    club_name TEXT,
    club_president TEXT,
    club_email TEXT,
    club_size INTEGER,
    club_advisor TEXT,
    club_advisor_email TEXT,
    PRIMARY KEY (club_name)
);

CREATE TABLE INPUT_DATA (
    building TEXT,
    room_num INTEGER,
    times_accessed INTEGER,
    access_succeed INTEGER,
    access_fail INTEGER,
    date_entered TEXT,
    PRIMARY KEY (room_num, building)
);

CREATE TABLE ROOM_LOG (
    building TEXT,
    room_num INTEGER,
    assigned_club TEXT,
    PRIMARY KEY (assigned_club),
    FOREIGN KEY (assigned_club) REFERENCES CLUB_DATA (club_name)
);

CREATE TABLE AUTH (
    username TEXT,
    password_ TEXT,
    PRIMARY KEY (username)
)
