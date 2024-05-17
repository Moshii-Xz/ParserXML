# XML Parser

Este proyecto es un parser de archivos XML escrito en Python que utiliza la programación orientada a objetos (POO) para estructurar y procesar el contenido del archivo. El objetivo del programa es leer y detallar la estructura del archivo XML, incluso si se modifica o se le agregan nuevas etiquetas.

## Características

- **Programación Orientada a Objetos (POO)**: El código utiliza POO para estructurar el programa de manera modular y extensible.
- **Polimorfismo**: Aplicado mediante la sobrescritura de métodos en clases derivadas.
- **Parseo Recursivo**: Capaz de manejar elementos XML complejos y anidados.

## Estructura del Código

### Clases y Objetos

1. **Clase Base `XMLElement`**:
   - **Descripción**: `XMLElement` es la clase base para representar cualquier elemento XML.
   - **Atributos**: 
     - `name`: El nombre del elemento.
     - `attributes`: Un diccionario de atributos del elemento.
   - **Métodos**:
     - `__init__(self, name, attributes)`: Constructor para inicializar el nombre y los atributos del elemento.
     - `display(self, indent=0)`: Método para imprimir el elemento. Se puede sobrescribir en clases derivadas para personalizar la salida.

```python
class XMLElement:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def display(self, indent=0):
        attrs = ", ".join(f"{k}: {v}" for k, v in self.attributes.items())
        print(' ' * indent + f"Element: {self.name}, Attributes: {{{attrs}}}")
```

2. **Clase `SimpleElement`**:
   - **Descripción**: `SimpleElement` representa elementos XML que no tienen elementos hijos.
   - **Herencia**: Hereda de `XMLElement`.

```python
class SimpleElement(XMLElement):
    def __init__(self, name, attributes):
        super().__init__(name, attributes)
```

3. **Clase `ComplexElement`**:
   - **Descripción**: `ComplexElement` representa elementos XML que pueden contener otros elementos hijos.
   - **Herencia**: Hereda de `XMLElement`.
   - **Atributos Adicionales**:
     - `children`: Lista de elementos hijos.
   - **Métodos**:
     - `add_child(self, child)`: Método para agregar un hijo a la lista de hijos.
     - `display(self, indent=0)`: Sobrescribe el método `display` de `XMLElement` para también imprimir los hijos, demostrando **polimorfismo**.

```python
class ComplexElement(XMLElement):
    def __init__(self, name, attributes):
        super().__init__(name, attributes)
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, indent=0):
        super().display(indent)
        for child in self.children:
            child.display(indent + 2)
```

### Polimorfismo

El polimorfismo en este código se manifiesta en el método `display`:

- **Polimorfismo**: `display` es un método que se define en `XMLElement` y se sobrescribe en `ComplexElement` para añadir funcionalidad adicional (mostrar hijos).

### Funciones Auxiliares

1. **Función `parse_element`**:
   - **Descripción**: Función recursiva que construye objetos `SimpleElement` o `ComplexElement` según corresponda.
   - **Uso de POO**: Crea instancias de `XMLElement` (y sus subclases) y construye una estructura jerárquica de objetos.

```python
def parse_element(element):
    attributes = element.attrib
    if list(element):
        complex_element = ComplexElement(element.tag.split('}')[-1], attributes)
        for child in element:
            complex_element.add_child(parse_element(child))
        return complex_element
    else:
        return SimpleElement(element.tag.split('}')[-1], attributes)
```

2. **Función `process_xml`**:
   - **Descripción**: Función principal que lee y procesa el archivo XML.
   - **Uso de POO**: Inicializa el árbol de objetos XML y llama al método `display` del objeto raíz para imprimir la estructura.

```python
def process_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    root_element = parse_element(root)
    root_element.display()
```

### Ejecución del Programa

Para ejecutar el programa, simplemente usa el siguiente comando:

```bash
python parser.py
```

Asegúrate de tener el archivo XML (`schema.xml`) en el mismo directorio que el script de Python.

### Ejemplo de Output

Al ejecutar el programa con el archivo XML `schema.xml`, el output en consola sería:

```
Element: schema, Attributes: {}
  Element: element, Attributes: {name: purchaseOrder, type: PurchaseOrderType}
  Element: element, Attributes: {name: comment, type: xsd:string}
  Element: complexType, Attributes: {name: PurchaseOrderType}
    Element: sequence, Attributes: {}
      Element: element, Attributes: {name: shipTo, type: Address}
      Element: element, Attributes: {name: billTo, type: Address}
      Element: element, Attributes: {ref: comment, minOccurs: 0}
      Element: element, Attributes: {name: items, type: Items}
    Element: attribute, Attributes: {name: orderDate, type: xsd:date}
  Element: complexType, Attributes: {name: Address}
    Element: sequence, Attributes: {}
      Element: element, Attributes: {name: name, type: xsd:string}
      Element: element, Attributes: {name: street, type: xsd:string}
      Element: element, Attributes: {name: city, type: xsd:string}
      Element: element, Attributes: {name: zip, type: xsd:decimal}
  Element: complexType, Attributes: {name: Items}
    Element: sequence, Attributes: {}
      Element: element, Attributes: {name: item, minOccurs: 0, maxOccurs: unbounded}
        Element: complexType, Attributes: {}
          Element: sequence, Attributes: {}
            Element: element, Attributes: {name: product, type: xsd:string}
            Element: element, Attributes: {name: quantity, type: xsd:integer}
            Element: element, Attributes: {name: price, type: xsd:decimal}
```

Este output representa la estructura del archivo XML, mostrando cada elemento y sus atributos, con una indentación que refleja la jerarquía de los elementos.
