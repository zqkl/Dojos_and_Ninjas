from flask_app.config.mysqlconnection import connectToMySQL
db ='dojosandninjasdb'

class Ninjas:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']


    @classmethod
    def show_all_ninjas(cls,id):
        query="""
            SELECT ninjas.first_name,ninjas.last_name,ninjas.age,dojos.name
            FROM dojos JOIN ninjas ON ninjas.dojo_id = dojos.id
            WHERE dojos.id=%(id)s;
            """
        results = connectToMySQL(db).query_db(query,id)
        return results

    @classmethod
    def create_ninja(cls,id):
        query="""
                INSERT INTO ninjas(first_name,last_name,age,dojo_id)
                VALUES(%(first_name)s,%(last_name)s,%(age)s,%(dojo)s)
        """
        return connectToMySQL(db).query_db(query,id)
        