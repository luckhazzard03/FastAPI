class Estampado:
    def __init__(self, dtf, vinilo, sublimado, textil):
        # Inicializa las propiedades del objeto
        self.dtf = dtf  # Diseño para estampado en DTF
        self.vinilo = vinilo  # Diseño para estampado en vinilo
        self.sublimado = sublimado  # Diseño para estampado en sublimado
        self.textil = textil  # Tipo de textil para decidir el método de estampado

        # Define un diccionario que mapea tipos de textil a métodos de estampado
        self.metodos_estampado = {
            "algodon": self.estampar_algodon,  # Asocia "algodon" al método estampar_algodon
            "poliester": self.estampar_poliester,  # Asocia "poliester" al método estampar_poliester
            "algodon-poliester": self.estampar_algodon_poliester  # Asocia "algodon-poliester" al método estampar_algodon_poliester
        }

    def estampar_algodon(self):
        # Método para estampar en algodón usando DTF
        print(f"Estampando en algodón usar: {self.dtf}")

    def estampar_poliester(self):
        # Método para estampar en poliéster usando sublimado
        print(f"Estampando en poliéster usar: {self.sublimado}")

    def estampar_algodon_poliester(self):
        # Método para estampar en mezcla de algodón y poliéster usando vinilo
        print(f"Estampando en mezcla de algodón y poliéster usar: {self.vinilo}")

    def estampar_en_camiseta(self):
        # Selecciona el método de estampado basado en el tipo de textil
        metodo = self.metodos_estampado.get(self.textil, lambda: print("Tipo de textil no reconocido. No se puede estampar."))
        # Llama al método seleccionado
        metodo()

# Crear instancias y probar el método

# Prueba de estampado en algodón
estampado_algodon = Estampado("DTF", "Vinilo no aplicable", "Sublimado no aplicable", "algodon")
estampado_algodon.estampar_en_camiseta()  # Debería imprimir: "Estampando en algodón usando DTF: Diseño DTF"

# Prueba de estampado en poliéster
estampado_poliester = Estampado("Diseño no aplicable", "Vinilo no aplicable", "Sublimado", "poliester")
estampado_poliester.estampar_en_camiseta()  # Debería imprimir: "Estampando en poliéster usando sublimado: Sublimado"

# Prueba de estampado en mezcla de algodón y poliéster
estampado_mezcla = Estampado("Diseño no aplicable", "Vinilo", "Sublimado no aplicable", "algodon-poliester")
estampado_mezcla.estampar_en_camiseta()  # Debería imprimir: "Estampando en mezcla de algodón y poliéster usando vinilo: Vinilo"

# Prueba de estampado con textil no reconocido
estampado_no_reconocido = Estampado("Diseño no aplicable", "Vinilo no aplicable", "Sublimado no aplicable", "otro_material")
estampado_no_reconocido.estampar_en_camiseta()  # Debería imprimir: "Tipo de textil no reconocido. No se puede estampar."
