import os
import xml.etree.ElementTree as ET

# Obtener la ruta completa del archivo XML
script_dir = os.path.dirname(__file__)  # Objeto de la clase os.PathLike que representa el directorio del script
xml_file = os.path.join(script_dir, "schema.xml")  # Método join() de la clase os.PathLike, que devuelve una ruta completa

# Leer el contenido del archivo XML
with open(xml_file, "r") as file:
    xml_data = file.read()  # Método read() de la clase TextIOWrapper que devuelve el contenido del archivo como una cadena de texto
    print("Contenido del archivo XML:")
    print(xml_data)
    print("\n")

# Parse XML
root = ET.fromstring(xml_data)  # Método fromstring() de la clase ElementTree, que devuelve el elemento raíz del árbol XML

# Procesar el esquema
# Iterar sobre los elementos 'element' del esquema XML
for element in root.findall('.//{http://www.w3.org/2001/XMLSchema}element'):  
    name = element.get('name')  # Método get() de la clase Element, que devuelve el valor del atributo 'name'
    type_ = element.get('type')  # Método get() de la clase Element, que devuelve el valor del atributo 'type'
    print(f"Elemento: {name}, Tipo: {type_}")

# Iterar sobre los elementos 'complexType' del esquema XML
for complex_type in root.findall('.//{http://www.w3.org/2001/XMLSchema}complexType'):  
    name = complex_type.get('name')  # Método get() de la clase Element, que devuelve el valor del atributo 'name'
    print(f"Tipo Complejo: {name}")
    # Iterar sobre los elementos 'element' dentro de 'complexType'
    for child in complex_type.findall('.//{http://www.w3.org/2001/XMLSchema}element'):
        child_name = child.get('name')  # Método get() de la clase Element, que devuelve el valor del atributo 'name'
        child_type = child.get('type')  # Método get() de la clase Element, que devuelve el valor del atributo 'type'
        print(f"    Elemento: {child_name}, Tipo: {child_type}")

    # Iterar sobre los elementos 'sequence' dentro de 'complexType'
    for sequence in complex_type.findall('.//{http://www.w3.org/2001/XMLSchema}sequence'):  
        # Iterar sobre los elementos 'element' dentro de 'sequence'
        for child in sequence.findall('.//{http://www.w3.org/2001/XMLSchema}element'):  
            child_name = child.get('name')  # Método get() de la clase Element, que devuelve el valor del atributo 'name'
            child_type = child.find('{http://www.w3.org/2001/XMLSchema}complexType/{http://www.w3.org/2001/XMLSchema}sequence')  # Método find() de la clase Element, que busca elementos secundarios que coincidan con la ruta dada
            # Verificar si child_type no es None
            if child_type is not None:
                # Iterar sobre los elementos secundarios dentro de child_type
                for inner_child in child_type.findall('.//{http://www.w3.org/2001/XMLSchema}element'):
                    inner_child_name = inner_child.get('name')  # Método get() de la clase Element, que devuelve el valor del atributo 'name'
                    inner_child_type = inner_child.get('type')  # Método get() de la clase Element, que devuelve el valor del atributo 'type'
                    print(f"    Elemento: {child_name}/{inner_child_name}, Tipo: {inner_child_type}")