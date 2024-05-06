# ParserXML
## En este codigo se utiliza lo siguiente de POO(Programacion Orientada a objetos(
###Encapsulación:
>os.path.dirname(__file__): os.path.dirname() es un método encapsulado dentro del módulo os. Devuelve el directorio del script actual.
>os.path.join(script_dir, "schema.xml"): os.path.join() es otro método encapsulado dentro del módulo os. Combina script_dir con el nombre del archivo para crear la ruta completa.
###Uso de objetos:
>root es un objeto de la clase ElementTree.Element, que representa el elemento raíz del árbol XML.
>element y complex_type son objetos de la clase ElementTree.Element, que representan elementos XML dentro del árbol XML.
###Herencia:
>ElementTree.Element puede tener subclases que heredan sus métodos y propiedades. Aunque no estás definiendo subclases explícitamente en tu código, el módulo xml.etree.ElementTree puede tener subclases de           ElementTree.Element que están siendo utilizadas.
###Polimorfismo:
>El método findall() en el objeto root y en los objetos element y complex_type muestra polimorfismo de inclusión. Aunque findall() se llama en diferentes contextos, funciona de la misma manera independientemente del objeto al que se llame.
