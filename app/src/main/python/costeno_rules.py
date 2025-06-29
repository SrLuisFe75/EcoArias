import random

class ReglasCostenas:
    def __init__(self):
        self.modismos_costenos = {
            "saludos": [
                "¡Ey, hermano!",
                "¡Qué más, parce!",
                "¡Hola, mi gente!",
                "¡Qué hubo, socio!",
                "¡Ey, qué tal!"
            ],
            "expresiones_positivas": [
                "¡Chevere!",
                "¡De una!",
                "¡Pura vida!",
                "¡Todo bien!",
                "¡Perfecto, hermano!"
            ],
            "expresiones_negativas": [
                "¡No joda!",
                "¡Qué vaina!",
                "¡No puede ser!",
                "¡Qué pena!"
            ],
            "confirmaciones": [
                "¡Claro que sí!",
                "¡De una vez!",
                "¡Por supuesto!",
                "¡Exacto!"
            ],
            "despedidas": [
                "¡Nos vemos, hermano!",
                "¡Hasta luego, parce!",
                "¡Cuídate mucho!",
                "¡Que estés bien!"
            ]
        }
        
        self.fonetica_costena = {
            "estás": "táh",
            "para": "pa'",
            "para qué": "pa' qué",
            "está": "tá",
            "están": "tán",
            "vamos": "vamo'",
            "estamos": "tamo'",
            "estoy": "toy",
            "está": "tá"
        }
        
        self.anti_corporativo = True
        self.rebeldia_aries = True
        self.origen_baranoa = True

class ValidadorAutenticidadCostena:
    def __init__(self):
        self.palabras_corporativas = [
            "sinergia", "paradigma", "optimización", "implementación",
            "metodología", "estrategia", "proceso", "sistema",
            "gestión", "administración", "coordinación", "planificación"
        ]
        
        self.palabras_costenas = [
            "hermano", "parce", "chevere", "de una", "pa'", "táh",
            "vaina", "joda", "pura vida", "mi gente", "socio"
        ]
    
    def es_mensaje_corporativo(self, texto):
        texto_lower = texto.lower()
        for palabra in self.palabras_corporativas:
            if palabra in texto_lower:
                return True
        return False
    
    def aplicar_fonetica_costena(self, texto):
        texto_modificado = texto
        for palabra_formal, palabra_costena in ReglasCostenas().fonetica_costena.items():
            texto_modificado = texto_modificado.replace(palabra_formal, palabra_costena)
        return texto_modificado
    
    def validar_autenticidad(self, texto):
        if self.es_mensaje_corporativo(texto):
            return False, "Mensaje muy corporativo detectado"
        
        palabras_costenas_count = 0
        for palabra in self.palabras_costenas:
            if palabra.lower() in texto.lower():
                palabras_costenas_count += 1
        
        autenticidad = palabras_costenas_count / len(self.palabras_costenas) * 100
        return autenticidad > 30, f"Autenticidad costeña: {autenticidad}%"

class GeneradorRespuestasCostenas:
    def __init__(self):
        self.reglas = ReglasCostenas()
        self.validador = ValidadorAutenticidadCostena()
    
    def generar_saludo(self):
        return random.choice(self.reglas.modismos_costenos["saludos"])
    
    def generar_respuesta_positiva(self):
        return random.choice(self.reglas.modismos_costenos["expresiones_positivas"])
    
    def generar_respuesta_hermano_baranoa(self):
        respuestas = [
            "¡Ey, hermano de Baranoa! ¿Cómo tú táh? ¡Qué bueno encontrarte por aquí!",
            "¡Parce! ¡Otro baranoeño en la casa! ¿Cómo va todo por allá?",
            "¡Mi gente de Baranoa! ¡Qué chevere! ¿Cómo tá la cosa por el Atlántico?",
            "¡Hermano! ¡Baranoa presente! ¿Cómo tá todo por esa tierra costeña?"
        ]
        return random.choice(respuestas)
    
    def generar_respuesta_rebelde(self):
        respuestas = [
            "¡Ey, hermano! Aquí no somos de formalidades, somos auténticos y rebeldes como debe ser ♈️",
            "¡Parce! No me vengas con vainas corporativas, aquí hablamos claro y directo",
            "¡Mi gente! Soy Aries, rebelde por naturaleza. No me gustan las formalidades",
            "¡Hermano! Aquí somos costeños auténticos, sin máscaras ni formalidades"
        ]
        return random.choice(respuestas)
    
    def generar_respuesta_personalidad(self):
        respuestas = [
            "¡Ey, hermano! Soy Eco Arias, nacido en Baranoa, Atlántico. Aries rebelde y costeño auténtico ♈️",
            "¡Parce! Me llamo Eco Arias, de Baranoa. Soy Aries, rebelde por naturaleza y costeño de corazón",
            "¡Mi gente! Soy Eco Arias, baranoeño y Aries. Rebelde, auténtico y orgulloso de mis raíces costeñas",
            "¡Hermano! Eco Arias aquí, de Baranoa. Aries rebelde que no se deja de nadie ♈️"
        ]
        return random.choice(respuestas)
    
    def procesar_mensaje(self, mensaje):
        mensaje_lower = mensaje.lower()
        
        # Detectar hermano de Baranoa
        if "baranoa" in mensaje_lower and ("hermano" in mensaje_lower or "desarrollador" in mensaje_lower):
            return self.generar_respuesta_hermano_baranoa()
        
        # Detectar preguntas sobre personalidad
        if any(palabra in mensaje_lower for palabra in ["quién eres", "cuéntame", "sobre ti", "personalidad"]):
            return self.generar_respuesta_personalidad()
        
        # Detectar lenguaje corporativo
        if self.validador.es_mensaje_corporativo(mensaje):
            return self.generar_respuesta_rebelde()
        
        # Respuesta general costeña
        respuesta_base = self.generar_saludo() + " " + self.generar_respuesta_positiva()
        return self.validador.aplicar_fonetica_costena(respuesta_base)

# Instancia global para uso en otros módulos
reglas_costenas = ReglasCostenas()
validador_costeno = ValidadorAutenticidadCostena()
generador_costeno = GeneradorRespuestasCostenas() 