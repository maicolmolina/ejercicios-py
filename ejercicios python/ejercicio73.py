"""
crear una clase libro
atributos
titulo, autor, aditorial, año de publicidad
metodo
constructor para inicializar los atributos
"""
class libro:
    def _init_(self, titulo, autor, editorial, anio_publicacion):
        self.titulo=titulo
        self.autor=autor
        self.editorial=editorial
        self.anio_publicacion=anio_publicacion
    
mi_libro = libro("cien años de soledad",
                 "gabriel garcia marquez",
                 "no la conozco",
                 "100")
print(mi_libro.__dict__)


        