_mongo_server = "0.0.0.0"
_mongo_port = "27017"
_mongo_user = "user"
_mongo_pwd = "password"
_mongo_authentication_database = "database"

mongo_connection_string = "mongodb://{0}:{1}@{2}:{3}/{4}".format(_mongo_user, _mongo_pwd, _mongo_server, _mongo_port, _mongo_authentication_database)
mongo_database_name = "database"