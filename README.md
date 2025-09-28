# 🧮 Laboratorio 7 – Teoría de la Computación

Erick Barrera 22934 
# 🧮 Laboratorio 7 – link video en yt

https://youtu.be/ixdlxViwsyE



## 📌 Descripción
Este laboratorio aborda la **eliminación de producciones épsilon en gramáticas libres de contexto (GLC)**.  

Se divide en dos partes principales:

1. **Problema 1 (Implementación en Python):**  
   Se desarrolla un programa que:
   - Lee gramáticas desde archivos de texto.
   - Valida las producciones.
   - Detecta símbolos anulables.
   - Elimina producciones épsilon.
   - Genera una gramática equivalente sin épsilon-producciones.

2. **Problema 2 (Ejercicios Teóricos):**  
   Se resuelven paso a paso dos ejercicios de eliminación de épsilon-producciones, utilizando notación formal en **LaTeX** y presentados en un **PDF** adjunto.

---

## 📂 Estructura del Proyecto


TC-Laboratorio7/
│── problema 1/
│   ├── main.py             # Código principal en Python
│   ├── gramatica1.txt      # Gramática válida de prueba
│   ├── gramatica2.txt      # Otra gramática válida de prueba
│   ├── gramatica_error.txt # Gramática inválida (para pruebas de error)
│
│── problema 2/
│   └── lab_7.pdf           # Desarrollo teórico de los ejercicios en LaTeX
│
└── README.md




---

## ▶️ Ejecución del Problema 1

### 1️⃣ Entrar a la carpeta del problema:
```bash
cd "problema 1"

python3 main.py gramatica1.txt


📂 Cargando gramática desde gramatica1.txt...

📘 Gramática Original
S -> 0A0 | 1B1 | BB
A -> C
B -> S | A
C -> S | ε

⚡ Símbolos anulables: {'S', 'A', 'B', 'C'}

📘 Gramática sin ε-producciones
S -> 0A0 | 00 | 1B1 | 11 | BB | B
A -> C
B -> S | A
C -> S


