import xml.etree.ElementTree as ET

# Clase base para todos los elementos XML
class XMLElement:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def display(self, indent=0):
        attrs = ", ".join(f"{k}: {v}" for k, v in self.attributes.items())
        print(' ' * indent + f"Element: {self.name}, Attributes: {{{attrs}}}")

# Clase para elementos simples
class SimpleElement(XMLElement):
    def __init__(self, name, attributes):
        super().__init__(name, attributes)

# Clase para elementos complejos que contienen otros elementos
class ComplexElement(XMLElement):
    def __init__(self, name, attributes):
        super().__init__(name, attributes)
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    # Polimorfismo: Sobrescritura del método display para incluir los hijos
    def display(self, indent=0):
        super().display(indent)
        for child in self.children:
            child.display(indent + 2)

# Función para parsear el XML y construir el árbol de elementos
def parse_element(element):
    attributes = element.attrib
    if list(element):
        complex_element = ComplexElement(element.tag.split('}')[-1], attributes)
        for child in element:
            complex_element.add_child(parse_element(child))
        return complex_element
    else:
        return SimpleElement(element.tag.split('}')[-1], attributes)

# Función principal para leer y procesar el archivo XML
def process_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    root_element = parse_element(root)
    root_element.display()

# Ejecución del programa
if __name__ == "__main__":
    process_xml("schema.xml")
