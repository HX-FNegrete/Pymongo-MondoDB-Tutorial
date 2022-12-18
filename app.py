from pymongo import MongoClient

MONGO_URI = "mongodb://localhost"

# Conexión con la base de datos
client = MongoClient(MONGO_URI)

# Almacena la BD
db = client["teststore"]
# Almacena la colección
collection = db["products"]

# Insertar un solo nuevo dato dentro de nuestr nueva DB
# El id de producto siempre tiene que tener _ antes de comenzar, para que lo interprete como tal
# collection.insert_one({"_id": 2, "name": "keyboard", "price": 300})

# Insertar varios datos dentro de una colección
product_one = {"name": "mouse"}
product_two = {"name": "monitor"}
# Los ingresamos como una lista dentro del parámetro
# collection.insert_many([product_one, product_two])

# Como obtener los datos de nuestra base de datos. El método find() nos devuelve
# todos los datos dentro de la colección que le pasemos.
# Podemos no pasarme ningún parámetro a find(), pero, si queremos hacer una búsqueda,
# podemos incluir un dict del estilo {"price":300}
results = collection.find({"price": 300})

for r in results:
    print(r)  # Si queremos ser más específicos, podríamos poner result["name"]

# Otra forma de buscar un solo dato (producto en este caso), y que sea un objeto distinto a una lista
result = collection.find_one({"name": "mouse"})
print(result)

# Cuantos documentos tenemos en la Base de Datos. Le tenemos que pasar un {} para indicarle que no le vamos
# a pasar datos, y que nos devuelva todos los documentos.
number_products = collection.count_documents({})
print(number_products)
