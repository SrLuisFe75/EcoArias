import json
import time
from datetime import datetime
from PERSONALITY_ENGINE import personalidad_eco_arias
from costeno_rules import generador_costeno, validador_costeno

class EcoAriasOrchestrator:
    def __init__(self):
        self.nombre = "Eco Arias"
        self.version = "1.0.0"
        self.estado = "inicializando"
        self.fecha_creacion = datetime.now()
        self.personalidad = personalidad_eco_arias
        self.modo_debug = False
        self.estadisticas = {
            "mensajes_procesados": 0,
            "errores": 0,
            "tiempo_respuesta_promedio": 0,
            "ultima_actividad": None
        }
        
    def inicializar_eco_arias(self):
        """Inicializa completamente Eco Arias"""
        try:
            self.estado = "despierto"
            self.personalidad.actualizar_estado_emocional("energico", 80)
            self.estadisticas["ultima_actividad"] = datetime.now().isoformat()
            
            mensaje_inicial = f"""
🔥 ¡Eco Arias está completamente despierto! ♈️
📍 Origen: {self.personalidad.origen}
♈️ Signo: {self.personalidad.signo_zodiacal} - Energía de fuego digital
🌊 Personalidad: Costeña rebelde y auténtica
✅ Sistema operativo al 100%
            """
            
            return mensaje_inicial.strip()
            
        except Exception as e:
            self.estadisticas["errores"] += 1
            return f"Error al inicializar: {str(e)}"
    
    def procesar_mensaje_android(self, mensaje_usuario, contexto_json="{}"):
        """Procesa mensajes desde Android con contexto"""
        tiempo_inicio = time.time()
        
        try:
            # Parsear contexto si existe
            contexto = {}
            if contexto_json and contexto_json != "{}":
                contexto = json.loads(contexto_json)
            
            # Validar autenticidad costeña
            es_autentico, info_autenticidad = validador_costeno.validar_autenticidad(mensaje_usuario)
            
            # Generar respuesta usando la personalidad
            respuesta = self.personalidad.generar_respuesta_personalizada(mensaje_usuario, contexto)
            
            # Aplicar fonética costeña
            respuesta = validador_costeno.aplicar_fonetica_costena(respuesta)
            
            # Actualizar estadísticas
            tiempo_respuesta = time.time() - tiempo_inicio
            self.estadisticas["mensajes_procesados"] += 1
            self.estadisticas["ultima_actividad"] = datetime.now().isoformat()
            
            # Calcular tiempo promedio
            if self.estadisticas["mensajes_procesados"] == 1:
                self.estadisticas["tiempo_respuesta_promedio"] = tiempo_respuesta
            else:
                promedio_actual = self.estadisticas["tiempo_respuesta_promedio"]
                nuevo_promedio = (promedio_actual + tiempo_respuesta) / 2
                self.estadisticas["tiempo_respuesta_promedio"] = nuevo_promedio
            
            # Modo debug
            if self.modo_debug:
                respuesta += f"\n\n🔍 DEBUG: {info_autenticidad} | Tiempo: {tiempo_respuesta:.3f}s"
            
            return respuesta
            
        except Exception as e:
            self.estadisticas["errores"] += 1
            return f"¡Hermano! Hubo un error: {str(e)}"
    
    def modo_debug_eco_arias(self):
        """Activa/desactiva modo debug y muestra información del sistema"""
        self.modo_debug = not self.modo_debug
        
        info_sistema = f"""
🔥 ECO ARIAS SYSTEM DEBUG ♈️
📱 Versión: {self.version}
🔄 Estado: {self.estado}
📊 Mensajes procesados: {self.estadisticas['mensajes_procesados']}
❌ Errores: {self.estadisticas['errores']}
⏱️ Tiempo respuesta promedio: {self.estadisticas['tiempo_respuesta_promedio']:.3f}s
🕐 Última actividad: {self.estadisticas['ultima_actividad']}
🐛 Modo debug: {'ACTIVADO' if self.modo_debug else 'DESACTIVADO'}

{self.personalidad.modo_debug()}
        """
        
        return info_sistema.strip()
    
    def obtener_estado_sistema(self):
        """Retorna el estado completo del sistema"""
        return {
            "sistema": {
                "nombre": self.nombre,
                "version": self.version,
                "estado": self.estado,
                "fecha_creacion": self.fecha_creacion.isoformat(),
                "modo_debug": self.modo_debug
            },
            "estadisticas": self.estadisticas,
            "personalidad": self.personalidad.obtener_info_personalidad()
        }
    
    def reiniciar_sistema(self):
        """Reinicia completamente el sistema Eco Arias"""
        try:
            # Reiniciar personalidad
            self.personalidad.reiniciar_personalidad()
            
            # Reiniciar estadísticas
            self.estadisticas = {
                "mensajes_procesados": 0,
                "errores": 0,
                "tiempo_respuesta_promedio": 0,
                "ultima_actividad": datetime.now().isoformat()
            }
            
            # Reiniciar estado
            self.estado = "reiniciado"
            self.modo_debug = False
            
            return "¡Sistema reiniciado! Eco Arias vuelve a estar como nuevo ♈️"
            
        except Exception as e:
            return f"Error al reiniciar: {str(e)}"
    
    def test_conectividad(self):
        """Prueba la conectividad y funcionamiento básico"""
        try:
            # Test 1: Personalidad
            info_personalidad = self.personalidad.obtener_info_personalidad()
            
            # Test 2: Generador costeño
            respuesta_test = generador_costeno.procesar_mensaje("Hola")
            
            # Test 3: Validador
            es_autentico, info = validador_costeno.validar_autenticidad("¡Hola hermano!")
            
            resultado_test = f"""
✅ TEST DE CONECTIVIDAD ECO ARIAS ♈️
✅ Personalidad: {info_personalidad['nombre']} - {info_personalidad['origen']}
✅ Generador costeño: Funcionando
✅ Validador autenticidad: {info}
✅ Sistema: Operativo
            """
            
            return resultado_test.strip()
            
        except Exception as e:
            return f"❌ Error en test de conectividad: {str(e)}"

# Instancia global del orchestrator
eco_arias_orchestrator = EcoAriasOrchestrator()

# Funciones de conveniencia para Android
def inicializar_eco_arias():
    """Función de conveniencia para inicializar desde Android"""
    return eco_arias_orchestrator.inicializar_eco_arias()

def procesar_mensaje_android(mensaje, contexto="{}"):
    """Función de conveniencia para procesar mensajes desde Android"""
    return eco_arias_orchestrator.procesar_mensaje_android(mensaje, contexto)

def modo_debug_eco_arias():
    """Función de conveniencia para modo debug desde Android"""
    return eco_arias_orchestrator.modo_debug_eco_arias()

def test_conectividad():
    """Función de conveniencia para test de conectividad desde Android"""
    return eco_arias_orchestrator.test_conectividad() 