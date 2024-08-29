class Estampado:
    def __init__(self, dtf, vinilo, sublimado, textil):
        self.dtf = dtf
        self.vinilo = vinilo
        self.sublimado = sublimado
        self.textil = textil  # Se pasa como parámetro para especificar el tipo de camiseta

    def estampar_en_camiseta(self):
        # Verifica el tipo de textil y decide el método de estampado
        if self.textil == "algodon":
            print(f"Estampando en algodón usando DTF: {self.dtf}")
        elif self.textil == "poliester":
            print(f"Estampando en poliéster usando sublimado: {self.sublimado}")
        elif self.textil == "algodon-poliester":
            print(f"Estampando en mezcla de algodón y poliéster usando vinilo: {self.vinilo}")
        else: 
            print("Tipo de textil no reconocido. No se puede estampar.")

# Crear instancias y probar el método
# Prueba de algodón
estampado_algodon = Estampado("Diseño DTF", "Vinilo no aplicable", "Sublimado no aplicable", "algodon")
estampado_algodon.estampar_en_camiseta()        

# Prueba de poliéster
estampado_poliester = Estampado("Diseño no aplicable", "Vinilo no aplicable", "Sublimado", "poliester")
estampado_poliester.estampar_en_camiseta()

# Prueba mezcla de poliéster y algodón
estampado_mezcla = Estampado("Diseño no aplicable", "Vinilo", "Sublimado no aplicable", "algodon-poliester")
estampado_mezcla.estampar_en_camiseta()

# Prueba para textil no reconocido
estampado_no_reconocido = Estampado("Diseño no aplicable", "Vinilo no aplicable", "Sublimado no aplicable", "otro_material")
estampado_no_reconocido.estampar_en_camiseta()
