from flask_app.config.mysqlconnection import connectToMySQL
from  flask_app.models.ninja import Ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    #dojo model create
    @classmethod
    def dojo_save( cls , data ):
        query = """
        INSERT INTO dojos 
        (name) 
        VALUES (%(name)s);
        """
        result = connectToMySQL('dojo_ninja').query_db(query, data) 
        return result

    #dojo model read
    @classmethod
    def get_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_ninja').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_a_dojo_with_ninjas(cls, data):
        query = """
        SELECT * FROM dojos
        LEFT JOIN ninjas
        ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s
        ;"""
        all_results = connectToMySQL('dojo_ninja').query_db(query, data)
        print("****************", all_results)
        the_dojos_ninjas = cls(all_results[0])
        for info in all_results:
            new_ninja ={
                "id" : info["ninjas.id"],
                "first_name" : info["first_name"],
                "last_name" : info["last_name"],
                "age" : info["age"],
                "created_at" : ["ninjas.created_at"],
                "updated_at" : ["ninjas.updated_at"]
            }
            the_dojos_ninjas.ninjas.append(Ninja(new_ninja))
        return the_dojos_ninjas
   
    #dojo model update
    #dojo model delete