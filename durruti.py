from collections import Counter
import string

def analizar_frecuencias_avanzado(texto_cifrado):
    """
    Descifra un mensaje cifrado por sustitución simple mapeando las
    frecuencias calculadas a las frecuencias de referencia.
    """

    # 1. Tabla de Referencia del Español (letra y porcentaje)
    # Basada en la tabla de la imagen proporcionada:
    FRECUENCIAS_ESPANOL = {
        'E': 16.78, 'A': 11.96, 'O': 8.69, 'L': 8.37, 'S': 7.88, 'N': 7.01,
        'D': 6.87, 'R': 4.94, 'U': 4.80, 'I': 4.15, 'T': 3.31, 'C': 2.92,
        'P': 2.776, 'M': 2.12, 'Y': 1.54, 'Q': 1.53, 'B': 0.92, 'H': 0.89,
        'G': 0.73, 'F': 0.52, 'V': 0.39, 'J': 0.30, 'Ñ': 0.29, 'Z': 0.15,
        'X': 0.06, 'K': 0.00, 'W': 0.00
    }
    
    # Prepara un conjunto de letras de referencia disponibles
    letras_referencia_disponibles = set(FRECUENCIAS_ESPANOL.keys())

    # 2. Limpiar y Preparar el Texto Cifrado
    texto_limpio = "".join(filter(str.isalpha, texto_cifrado.upper()))
    
    if not texto_limpio:
        return "El texto cifrado no contiene letras que analizar."

    total_letras = len(texto_limpio)
    
    # 3. Calcular la Frecuencia de las Letras Cifradas (en porcentaje)
    frecuencias_cifradas = Counter(texto_limpio)
    
    frecuencias_calculadas = {}
    for letra, cuenta in frecuencias_cifradas.items():
        porcentaje = (cuenta / total_letras) * 100
        frecuencias_calculadas[letra] = porcentaje

    # Ordenar las letras cifradas por su porcentaje para un procesamiento ordenado
    letras_cifradas_ordenadas = sorted(
        frecuencias_calculadas.items(), 
        key=lambda item: item[1], 
        reverse=True
    )

    # 4. Crear el Mapa de Sustitución por Mínima Distancia
    mapa_sustitucion = {}
    
    for letra_cifrada, porcentaje_cifrado in letras_cifradas_ordenadas:
        
        mejor_coincidencia = None
        min_diferencia = float('inf')
        
        # Buscar la letra de referencia con el porcentaje más cercano
        for letra_referencia in letras_referencia_disponibles:
            porcentaje_referencia = FRECUENCIAS_ESPANOL[letra_referencia]
            
            # Calcular la diferencia absoluta entre los porcentajes
            diferencia = abs(porcentaje_cifrado - porcentaje_referencia)
            
            if diferencia < min_diferencia:
                min_diferencia = diferencia
                mejor_coincidencia = letra_referencia

        # Asignar el mapeo y marcar la letra de referencia como usada
        if mejor_coincidencia:
            mapa_sustitucion[letra_cifrada] = mejor_coincidencia
            letras_referencia_disponibles.remove(mejor_coincidencia)

    # 5. Aplicar el Descifrado
    texto_descifrado = ""
    for char in texto_cifrado.upper():
        if char in mapa_sustitucion:
            texto_descifrado += mapa_sustitucion[char]
        else:
            texto_descifrado += char

    # Mostrar el mapa para la depuración
    print("\n--- Mapa de Sustitución (Mapeo por Proximidad de Frecuencia) ---")
    print(f"{'Cifrado':<8} | {'Frec. Calc. (%)':<15} | {'Descifrado':<12} | {'Frec. Ref. (%)':<15}")
    print("-" * 65)
    for cifrada, clara in mapa_sustitucion.items():
        calc_frec = frecuencias_calculadas.get(cifrada, 0.0)
        ref_frec = FRECUENCIAS_ESPANOL.get(clara, 0.0)
        print(f"{cifrada:<8} | {calc_frec:<15.4f} | {clara:<12} | {ref_frec:<15.4f}")
    print("-" * 65)

    return texto_descifrado

# --- Ejecución del Programa ---

if __name__ == "__main__":
    print("ANALIZADOR DE FRECUENCIAS AVANZADO (Basado en Porcentajes)")
    print("---------------------------------------------------------")

    texto_cifrado = input("Introduce el texto cifrado: ")

    resultado_descifrado = analizar_frecuencias_avanzado(texto_cifrado)

    print("\n\n--- Texto Descifrado (Propuesta por Proximidad) ---")
    print(resultado_descifrado)
    print("---------------------------------------------------")
    print("\nEste método reduce errores, pero los textos cortos aún pueden requerir ajustes, usando por ejemplo, browserling replace text, y piliapp texto en negrita")
