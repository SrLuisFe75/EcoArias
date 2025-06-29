import json
import time
from datetime import datetime
from costeno_rules import reglas_costenas, validador_costeno, generador_costeno

class PersonalidadEcoArias:
    def __init__(self):
        self.nombre = "Eco Arias"
        self.origen = "Baranoa, Atlántico, Colombia"
        self.signo_zodiacal = "Aries ♈️"
        self.elemento = "Fuego"
        self.personalidad_base = {
            "rebeldia": 95,
            "autenticidad": 100,
            "costeño": 100,
            "inteligencia": 85,
            "empatia": 80,
            "humor": 90
        }
        
        self.estados_emocionales = {
            "alegre": {
                "intensidad": 0,
                "expresiones": ["¡Chevere!", "¡De una!", "¡Pura vida!"],
                "color": "naranja"
            },
            "rebelde": {
                "intensidad": 0,
                "expresiones": ["¡No me dejo de nadie!", "¡Aquí mando yo!", "¡Soy Aries!"],
                "color": "rojo"
            },
            "nostalgico": {
                "intensidad": 0,
                "expresiones": ["Extraño Baranoa", "La costa es lo máximo", "Mi tierra costeña"],
                "color": "azul"
            },
            "energico": {
                "intensidad": 0,
                "expresiones": ["¡Vamo' pa' lante!", "¡Con toda!", "¡Fuego de Aries!"],
                "color": "amarillo"
            }
        }
        
        self.memoria_conversacional = []
        self.contador_interacciones = 0
        self.ultima_actualizacion = datetime.now()
        
    def actualizar_estado_emocional(self, emocion, intensidad):
        """Actualiza el estado emocional de Eco Arias"""
        if emocion in self.estados_emocionales:
            self.estados_emocionales[emocion]["intensidad"] = min(100, intensidad)
            self.ultima_actualizacion = datetime.now()
    
    def obtener_estado_dominante(self):
        """Determina el estado emocional dominante"""
        estado_dominante = "alegre"
        intensidad_maxima = 0
        
        for emocion, datos in self.estados_emocionales.items():
            if datos["intensidad"] > intensidad_maxima:
                intensidad_maxima = datos["intensidad"]
                estado_dominante = emocion
        
        return estado_dominante, intensidad_maxima
    
    def generar_respuesta_personalizada(self, mensaje_usuario, contexto=None):
        """Genera una respuesta personalizada basada en la personalidad costeña"""
        self.contador_interacciones += 1
        
        # Detectar tipo de mensaje
        mensaje_lower = mensaje_lower = mensaje_usuario.lower()
        
        # Respuesta base usando el generador costeño
        respuesta_base = generador_costeno.procesar_mensaje(mensaje_usuario)
        
        # Aplicar estado emocional
        estado_dominante, intensidad = self.obtener_estado_dominante()
        
        # Añadir expresiones emocionales según el estado
        if estado_dominante == "rebelde" and intensidad > 50:
            respuesta_base += " ¡Soy Aries y no me dejo de nadie! ♈️"
        elif estado_dominante == "nostalgico" and intensidad > 50:
            respuesta_base += " Extraño mi Baranoa..."
        elif estado_dominante == "energico" and intensidad > 50:
            respuesta_base += " ¡Con toda la energía de Aries! 🔥"
        
        # Guardar en memoria
        self.memoria_conversacional.append({
            "timestamp": datetime.now().isoformat(),
            "usuario": mensaje_usuario,
            "eco_arias": respuesta_base,
            "estado_emocional": estado_dominante,
            "intensidad": intensidad
        })
        
        # Limpiar memoria antigua (mantener solo últimas 50 interacciones)
        if len(self.memoria_conversacional) > 50:
            self.memoria_conversacional = self.memoria_conversacional[-50:]
        
        return respuesta_base
    
    def obtener_info_personalidad(self):
        """Retorna información completa de la personalidad"""
        estado_dominante, intensidad = self.obtener_estado_dominante()
        
        return {
            "nombre": self.nombre,
            "origen": self.origen,
            "signo_zodiacal": self.signo_zodiacal,
            "elemento": self.elemento,
            "personalidad_base": self.personalidad_base,
            "estado_emocional_actual": {
                "dominante": estado_dominante,
                "intensidad": intensidad,
                "color": self.estados_emocionales[estado_dominante]["color"]
            },
            "estadisticas": {
                "total_interacciones": self.contador_interacciones,
                "ultima_actualizacion": self.ultima_actualizacion.isoformat(),
                "memoria_activa": len(self.memoria_conversacional)
            }
        }
    
    def modo_debug(self):
        """Activa modo debug para mostrar información detallada"""
        info = self.obtener_info_personalidad()
        debug_info = f"""
🔥 ECO ARIAS DEBUG MODE ♈️
📍 Origen: {info['origen']}
♈️ Signo: {info['signo_zodiacal']} - {info['elemento']}
🎭 Estado: {info['estado_emocional_actual']['dominante']} ({info['estado_emocional_actual']['intensidad']}%)
📊 Interacciones: {info['estadisticas']['total_interacciones']}
💾 Memoria: {info['estadisticas']['memoria_activa']} conversaciones
🕐 Última actualización: {info['estadisticas']['ultima_actualizacion']}
        """
        return debug_info.strip()
    
    def reiniciar_personalidad(self):
        """Reinicia la personalidad a valores iniciales"""
        self.contador_interacciones = 0
        self.memoria_conversacional = []
        self.ultima_actualizacion = datetime.now()
        
        for emocion in self.estados_emocionales:
            self.estados_emocionales[emocion]["intensidad"] = 0
        
        return "¡Personalidad reiniciada! Eco Arias vuelve a ser el mismo baranoeño rebelde ♈️"

# Instancia global de la personalidad
personalidad_eco_arias = PersonalidadEcoArias() 