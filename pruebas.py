from dict import diccionario_datos
import functions_ift as f


nombre = "TD_LINEAS_INTMOVIL_ITE_VA"
prueba = f.download_files(nombre)
prueba_tweaked = f.tweak_df(prueba,diccionario_datos['Tabla_Lineas']['tweak_columns'],diccionario_datos['Tabla_Lineas']['schema'])
print(prueba_tweaked)