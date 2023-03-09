db = {
    'user'     : 'root',
    'password' : '',
    'host'     : '',
    'port'     : ,
    'database' : ''
}
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
test_config={
    'DB_URL' : f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
}
JWT_SECRET_KEY='MY_SECRET'

