from backend.settings import DJANGO_DB_TYPE

if DJANGO_DB_TYPE == 'mysql':
    import pymysql
    pymysql.install_as_MySQLdb()
