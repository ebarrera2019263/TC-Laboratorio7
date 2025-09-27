import re
import sys
from typing import Dict, List, Set

# Regex mejorada: acepta secuencias de símbolos (A-Z, a-z, 0-9, ε)
REGEX = re.compile(r"^[A-Z]\s*->\s*([A-Z0-9a-zε]+)(\s*\|\s*([A-Z0-9a-zε]+))*$")

def leer_gramatica(ruta: str) -> Dict[str, List[List[str]]]:
    """
    Lee un archivo de gramática y valida cada producción con regex.
    Retorna un diccionario con las producciones.
    """
    gramatica = {}
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not REGEX.match(linea):
                raise ValueError(f"❌ Producción inválida: {linea}")
            izquierda, derecha = linea.split("->")
            izquierda = izquierda.strip()
            producciones = [list(p.strip()) for p in derecha.split("|")]
            gramatica.setdefault(izquierda, []).extend(producciones)
    return gramatica

def encontrar_anulables(gramatica: Dict[str, List[List[str]]]) -> Set[str]:
    """
    Encuentra los no terminales anulables (que producen ε).
    """
    anulables = set()
    cambio = True
    while cambio:
        cambio = False
        for no_terminal, producciones in gramatica.items():
            for prod in producciones:
                if all(simbolo in anulables or simbolo == "ε" for simbolo in prod):
                    if no_terminal not in anulables:
                        anulables.add(no_terminal)
                        cambio = True
    return anulables

def eliminar_epsilon(gramatica: Dict[str, List[List[str]]]) -> Dict[str, List[List[str]]]:
    """
    Elimina producciones ε de la gramática.
    """
    anulables = encontrar_anulables(gramatica)
    print(f"⚡ Símbolos anulables: {anulables}")

    nueva_gramatica = {}
    for nt, producciones in gramatica.items():
        nuevas = []
        for prod in producciones:
            if prod == ["ε"]:
                continue  # eliminamos epsilon directo
            opciones = [[]]

            for simbolo in prod:
                temp = []
                if simbolo in anulables:
                    # conservar o eliminar el símbolo
                    for opcion in opciones:
                        temp.append(opcion + [simbolo])
                        temp.append(opcion)
                else:
                    for opcion in opciones:
                        temp.append(opcion + [simbolo])
                opciones = temp

            # quitar duplicados y vacíos
            for o in opciones:
                if o and o not in nuevas:
                    nuevas.append(o)
        nueva_gramatica[nt] = nuevas
    return nueva_gramatica

def imprimir_gramatica(gramatica: Dict[str, List[List[str]]], titulo="Gramática"):
    """
    Imprime la gramática en formato legible.
    """
    print(f"\n📘 {titulo}")
    for nt, producciones in gramatica.items():
        derechos = ["".join(p) for p in producciones]
        print(f"{nt} -> {' | '.join(derechos)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo_gramatica>")
        sys.exit(1)

    archivo = sys.argv[1]
    print(f"📂 Cargando gramática desde {archivo}...\n")

    gramatica = leer_gramatica(archivo)
    imprimir_gramatica(gramatica, "Gramática Original")

    nueva = eliminar_epsilon(gramatica)
    imprimir_gramatica(nueva, "Gramática sin ε-producciones")