from  flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.dojo import Dojo
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #ninja models create
    @classmethod
    def ninja_save(cls, data):
        query = """
        INSERT INTO ninjas 
        (first_name, last_name, age, dojo_id)
        VALUES (%(first_name)s,%(last_name)s, %(age)s, %(dojo_id)s)
        ;
        """
        return connectToMySQL('dojo_ninja').query_db(query, data)

    #ninja models read
    @classmethod
    def get_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojo_ninja').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas