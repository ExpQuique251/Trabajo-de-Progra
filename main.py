# Sistema de Gestión de Gimnasio

class Gimnasio:
    def __init__(self):
        self.socios = []  # Lista de socios del gimnasio

    def agregar_socio(self, nombre, edad, tipo_membresia):
        if not self.validar_nombre(nombre):
            raise ValueError("El nombre debe contener solo letras y tener al menos 3 caracteres.")
        if not self.validar_edad(edad):
            raise ValueError("La edad debe ser un número positivo y menor de 120.")
        if tipo_membresia not in ["mensual", "anual"]:
            raise ValueError("Tipo de membresía no válido. Debe ser 'mensual' o 'anual'.")

        socio = {
            "nombre": nombre,
            "edad": edad,
            "tipo_membresia": tipo_membresia
        }
        self.socios.append(socio)
        print(f"Socio {nombre} agregado exitosamente.")

    def validar_nombre(self, nombre):
        return isinstance(nombre, str) and len(nombre) >= 3 and nombre.isalpha()

    def validar_edad(self, edad):
        return isinstance(edad, int) and 0 < edad < 120

    def mostrar_socios(self):
        if not self.socios:
            print("No hay socios registrados.")
            return
        for idx, socio in enumerate(self.socios, start=1):
            print(f"Socio #{idx}: {socio['nombre']}, Edad: {socio['edad']}, Membresía: {socio['tipo_membresia']}")

# Ejemplo de uso
if __name__ == '__main__':
    gimnasio = Gimnasio()
    gimnasio.agregar_socio("Carlos", 30, "mensual")
    gimnasio.agregar_socio("Ana", 25, "anual")
    gimnasio.mostrar_socios()