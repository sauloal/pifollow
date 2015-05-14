import datetime
import os

from app import *

from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME

db = SQLAlchemy(app)

class Ips(db.Model):
    __tablename__ = "ips"
    
    id          = db.Column(db.Integer   , primary_key=True)
    pi_id       = db.Column(db.String(80), unique=False)
    external_ip = db.Column(db.String(20), unique=False)
    internal_ip = db.Column(db.String(20), unique=False)
    when        = db.Column(db.DateTime)

    def __init__(self, pi_id, external_ip, internal_ip):
        self.pi_id       = pi_id
        self.external_ip = external_ip
        self.internal_ip = internal_ip
        self.when        = datetime.datetime.now()

    def as_dict(self):
        return { 'id': self.pi_id, 'external_ip': self.external_ip, 'internal_ip': self.internal_ip, 'when': self.when }
        
    def as_list(self):
        return ( self.pi_id, self.external_ip, self.internal_ip, self.when )
    
    def __repr__(self):
        return '<ID %s EXTERNAL IP %s INTERNAL IP %s WHEN %s>' % ( self.pi_id, self.external_ip, self.internal_ip, str(self.when) )

class Data(db.Model):
    __tablename__ = 'data'
    
    id          = db.Column(db.Integer    , primary_key=True)
    pi_id       = db.Column(db.String(80 ), unique=False)
    filename    = db.Column(db.String(256), unique=False)
    filesize    = db.Column(db.Integer    , unique=False)
    filepath    = db.Column(db.String(256), unique=True)
    when        = db.Column(db.DateTime)
    
    def __init__(self, pi_id, filename, filesize, filepath):
        self.pi_id    = pi_id
        self.filename = filename
        self.filesize = filesize
        self.filepath = filepath
        self.when     = datetime.datetime.now()
    
    def as_dict(self):
        return { 'id': self.pi_id, 'filename': self.filename, 'filesize': self.filesize, 'filepath': self.filepath, 'when': self.when }
        
    def as_list(self):
        return ( self.pi_id, self.filename, self.filesize, self.filepath, self.when )
    
    def __repr__(self):
        return '<PI ID %s FILENAME %s FILESIZE %d FILEPATH %s WHEN %s>' % ( self.pi_id, self.filename, self.filesize, self.filepath, str(self.when) )

if not os.path.exists(DB_NAME):
    print "creating db"
    db.create_all()
    db.session.commit()
    print "db created"
