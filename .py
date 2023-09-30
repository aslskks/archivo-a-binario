import tkinter as tk
from tkinter import filedialog

# Función para traducir texto a binario
def texto_a_binario(texto):
    binario = ' '.join(format(ord(char), '08b') for char in texto)
    return binario

# Función para abrir un archivo y realizar la traducción
def abrir_archivo():
    archivo_entrada = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo_entrada:
        try:
            # Abrir el archivo de entrada en modo lectura
            with open(archivo_entrada, 'r') as entrada:
                contenido = entrada.read()

            # Traducir el contenido a binario
            contenido_binario = texto_a_binario(contenido)

            archivo_salida = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Archivos binarios", "*.bin")])

            if archivo_salida:
                # Guardar el contenido binario en un archivo binario
                with open(archivo_salida, 'wb') as salida:
                    salida.write(contenido_binario.encode())

                mensaje.config(text=f'El archivo "{archivo_entrada}" ha sido traducido y guardado en "{archivo_salida}".')

        except FileNotFoundError:
            mensaje.config(text=f'No se pudo encontrar el archivo "{archivo_entrada}".')

        except Exception as e:
            mensaje.config(text=f'Ocurrió un error: {e}')

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Traductor de Texto a Binario")

# Botón para abrir el archivo
boton_abrir = tk.Button(ventana, text="Abrir Archivo", command=abrir_archivo)
boton_abrir.pack(pady=20)

# Etiqueta para mostrar mensajes
mensaje = tk.Label(ventana, text="")
mensaje.pack()

# Iniciar la aplicación
ventana.mainloop()
