_mongo_server = "127.0.0.1"
_mongo_port = "27017"
_mongo_user = "pw_user"
_mongo_pwd = "pw_user.8657"
_mongo_authentication_database = "property_wizard"

mongo_connection_string = "mongodb://{0}:{1}@{2}:{3}/{4}".format(_mongo_user, _mongo_pwd, _mongo_server, _mongo_port, _mongo_authentication_database)
mongo_database_name = "property_wizard"