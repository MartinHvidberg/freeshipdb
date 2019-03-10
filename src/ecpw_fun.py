
import ecpw
ecs = ecpw.Store()

db_ip, db_name, db_pw = ecs.gets('PostgreSQL_mh', ['ip', 'name', 'password'])

print("Entry: {}, use credentials: {} / {}".format(db_ip, db_name, db_pw))