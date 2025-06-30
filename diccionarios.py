diccionario_vacio = {};

persona = {"nombre":"Ana", 
    "apellido": "Perez",
    "ciudad": "Santiago",
    "edad": 28,
    "hobbies": ["leer", "viajar"]
};

print(persona);

# imprimir un dato especifico del diccionario
print(persona["nombre"]);
print(persona["apellido"]);
print(persona["ciudad"]);
print(persona["edad"]);
print(persona["hobbies"]);

print(persona.get("profesion"));

# Añadir elementos al diccionario:
persona["profesion"] = "Ingeniera en Informática";

print(persona);

# Modificar un valor del diccionario
persona["edad"] = 56;
print(persona);

# Eliminar un dato del diccionario
# del()
del persona["ciudad"];
print(persona);

# pop()
dato_eliminado = persona.pop("profesion");

print(f"El dato eliminado del diccionario es {dato_eliminado}");
print(persona);
