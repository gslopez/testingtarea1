Para correr el proyecto:

1 - Instalar robot framework (pip install robotframework)
2 - Instalar Scrapy (pip install scrapy)
2 - cd robotframework
3 - pybot library_test.robot 


En Func.py está la clase (en este caso método) que se quiere probar. 
El archivo library_test.robot es en donde se escriben las pruebas. Este archivo llama metodos de FuncLibrary, quién a su vez usa a Func.


TODO:
- Muchos casos devuelven arreglos vacios. Deberiamos mejorar eso
