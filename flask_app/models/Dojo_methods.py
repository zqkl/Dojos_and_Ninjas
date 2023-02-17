from flask_app.config.mysqlconnection import connectToMySQL
db = 'dojosandninjasdb'


class Dojos:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def show_all_dojos(cls):
        query="""
                SELECT * FROM dojos;
            """
        results = connectToMySQL(db).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos


    @classmethod
    def add_new_dojo(cls,data):
        query="""
                INSERT INTO dojos(name, created_at, updated_at )
                VALUES (%(name)s, NOW(), NOW());
        """
        return connectToMySQL(db).query_db(query,data)






