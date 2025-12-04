#!/usr/bin/env python3
"""Interfaz gráfica (Tkinter) para visualizar la documentación del proyecto Tienda Aurelion.

Presenta botones para cada sección y un área de texto para mostrar el contenido.
"""
import os
import tkinter as tk
from tkinter import scrolledtext, messagebox


def cargar_documentacion(ruta="documentacion.md"):
    if not os.path.exists(ruta):
        return {
            1: "Tema, problema y objetivo: (documentacion.md no encontrado).",
            2: "Metadatos del dataset: (documentacion.md no encontrado).",
            3: "Relación de entidades: (documentacion.md no encontrado).",
            4: "Diagrama del programa: (documentacion.md no encontrado).",
            5: "Sugerencias y mejoras: (documentacion.md no encontrado).",
        }

    with open(ruta, encoding='utf-8') as f:
        texto = f.read()

    parts = [p.strip() for p in texto.split('\n## ') if p.strip()]
    secciones = {}
    mapping = {
        'Tema, problema y objetivo': 1,
        'Metadatos del dataset de referencia': 2,
        'Relación de entidades': 3,
        'Diagrama del programa (pseudocódigo)': 4,
        'Diagrama del programa': 4,
        'Sugerencias y mejoras con Copilot': 5,
        'Sugerencias y mejoras con Copilot': 5,
        'Sugerencias y mejoras con Copilot': 5,
    }

    for part in parts:
        lines = part.splitlines()
        title = lines[0].strip('# ').strip()
        body = "\n".join(lines[1:]).strip()
        key = mapping.get(title)
        if key:
            secciones[key] = f"## {title}\n\n{body}\n"

    for i in range(1, 6):
        secciones.setdefault(i, f"Sección {i}: (contenido no disponible en {ruta})\n")

    return secciones


class VisorGUI(tk.Tk):
    def __init__(self, secciones):
        super().__init__()
        self.title('Visor Tienda Aurelion - Documentación')
        self.geometry('800x600')
        self.secciones = secciones

        # Frame de botones a la izquierda
        btn_frame = tk.Frame(self)
        btn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=6, pady=6)

        tk.Label(btn_frame, text='Secciones', font=('Arial', 12, 'bold')).pack(pady=(0,6))

        botones = [
            ('1. Tema, problema y solución', 1),
            ('2. Metadatos', 2),
            ('3. Relación de entidades', 3),
            ('4. Diagrama del programa', 4),
            ('5. Sugerencias y mejoras', 5),
        ]

        for (text, idx) in botones:
            b = tk.Button(btn_frame, text=text, width=24, command=lambda i=idx: self.mostrar(i))
            b.pack(pady=4)

        tk.Button(btn_frame, text='Salir', fg='red', width=24, command=self.on_salir).pack(pady=(20,4))

        # Area de texto con scroll a la derecha
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=('Consolas', 11))
        self.text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=6, pady=6)

        # Mostrar instrucción inicial
        self.text_area.insert(tk.END, 'Seleccione una sección a la izquierda para ver la documentación.')
        self.text_area.configure(state=tk.DISABLED)

    def mostrar(self, idx):
        contenido = self.secciones.get(idx, f'Sección {idx} no disponible')
        self.text_area.configure(state=tk.NORMAL)
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.END, contenido)
        self.text_area.configure(state=tk.DISABLED)

    def on_salir(self):
        if messagebox.askokcancel('Salir', '¿Desea salir del visor?'):
            self.destroy()


def main():
    secciones = cargar_documentacion()
    app = VisorGUI(secciones)
    app.mainloop()


if __name__ == '__main__':
    main()
