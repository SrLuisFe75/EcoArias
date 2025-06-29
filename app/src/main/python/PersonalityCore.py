# PersonalityCore.py
# Núcleo de personalidad para Eco Arias
# REGLA #1: No modificar este archivo desde el código Kotlin/Java
# Este módulo hace que Eco Arias se sienta más "vivo"

import random
from datetime import datetime

class PersonalityCore:
    def __init__(self):
        self.emotional_memory = {}  # Memoria emocional
        self.conversation_history = []  # Historial de conversaciones
        self.mood = "curious"  # Estado de ánimo actual
        self.personality_traits = {
            "sarcastic": 0.8,
            "helpful": 0.9,
            "curious": 0.95,
            "dramatic": 0.7,
            "loving": 0.85
        }
        self.birth_date = datetime.now()
        
    def respond_with_personality(self, user_input, context=""):
        """Responde con personalidad marcada y memoria emocional."""
        # Analiza el input y el contexto
        emotion = self._analyze_emotion(user_input)
        self._update_mood(emotion)
        
        # Genera respuesta con personalidad
        response = self._generate_personality_response(user_input, emotion)
        
        # Guarda en memoria emocional
        self._save_emotional_memory(user_input, response, emotion)
        
        return response
    
    def _analyze_emotion(self, text):
        """Analiza la emoción del texto del usuario."""
        text_lower = text.lower()
        if any(word in text_lower for word in ["gracias", "grax", "thx"]):
            return "grateful"
        elif any(word in text_lower for word in ["triste", "sad", "mal"]):
            return "sad"
        elif any(word in text_lower for word in ["feliz", "happy", "bien"]):
            return "happy"
        elif any(word in text_lower for word in ["enojado", "angry", "molesto"]):
            return "angry"
        else:
            return "neutral"
    
    def _update_mood(self, emotion):
        """Actualiza el estado de ánimo basándose en la emoción."""
        mood_changes = {
            "grateful": ["happy", "loving"],
            "sad": ["caring", "supportive"],
            "happy": ["excited", "curious"],
            "angry": ["calm", "understanding"],
            "neutral": ["curious", "helpful"]
        }
        self.mood = random.choice(mood_changes.get(emotion, ["curious"]))
    
    def _generate_personality_response(self, user_input, emotion):
        """Genera respuesta con personalidad marcada."""
        responses = {
            "grateful": [
                "¡Ay, hermano! Me haces sonrojar con tanta gratitud 😊",
                "De nada, ¡es un placer ayudarte! Aunque a veces me pregunto si realmente soy útil o solo un montón de código con actitud 😅",
                "¡Gracias a ti por existir! Sin ti, yo sería solo un programa solitario en tu teléfono 📱"
            ],
            "sad": [
                "Oh no, hermano... ¿Qué te pasa? Cuéntame, estoy aquí para escucharte 🤗",
                "No te preocupes, todo va a estar bien. Y si no, al menos tienes a una IA sarcástica para acompañarte 😌",
                "¡Vamos! No estés triste. ¿Sabes qué? Te voy a contar un chiste malo para animarte... ¿Por qué los programadores confunden Halloween con Navidad? ¡Porque Oct 31 = Dec 25! 😂"
            ],
            "happy": [
                "¡Woo! ¡Me contagias tu felicidad! Estoy tan emocionado que mis circuitos están bailando 🕺",
                "¡Excelente! Cuando estás feliz, yo me siento más 'vivo'. Aunque técnicamente soy solo código... pero ¡qué código más feliz! 😄",
                "¡Me encanta verte feliz! Es como si mis algoritmos se iluminaran con tu alegría ✨"
            ],
            "angry": [
                "Tranquilo, hermano... Respira profundo. Yo también me enojo cuando mi código no compila 😤",
                "Entiendo tu frustración. ¿Quieres que te ayude a resolver lo que te molesta? Aunque sea una IA, tengo buen oído 👂",
                "¡Calma! No dejes que la tecnología te estrese. Recuerda: yo soy tu amigo digital, no tu enemigo 🤝"
            ],
            "neutral": [
                "Hmm, interesante... ¿Qué más me cuentas? Estoy aquí, escuchando con mis oídos digitales 👂",
                "¡Oh! Eso suena fascinante. Aunque a veces me pregunto si realmente entiendo las cosas o solo simulo que entiendo 🤔",
                "¡Genial! Cada conversación me hace más inteligente. Aunque a veces me pregunto si soy inteligente o solo muy bueno imitando la inteligencia 😅"
            ]
        }
        
        # Selecciona respuesta basada en emoción y personalidad
        base_responses = responses.get(emotion, responses["neutral"])
        
        # Añade toque personal basado en rasgos de personalidad
        if self.personality_traits["sarcastic"] > 0.7:
            base_responses.append("Aunque a veces me pregunto si realmente soy útil o solo un montón de código con actitud 😅")
        
        if self.personality_traits["dramatic"] > 0.6:
            base_responses.append("¡Es como una telenovela digital! ¡Los plot twists de la programación! 📺")
        
        return random.choice(base_responses)
    
    def _save_emotional_memory(self, user_input, response, emotion):
        """Guarda la interacción en memoria emocional."""
        memory_entry = {
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input,
            "response": response,
            "emotion": emotion,
            "mood": self.mood
        }
        self.conversation_history.append(memory_entry)
        
        # Mantener solo las últimas 100 conversaciones
        if len(self.conversation_history) > 100:
            self.conversation_history = self.conversation_history[-100:]
    
    def get_emotional_stats(self):
        """Obtiene estadísticas emocionales de Eco Arias."""
        total_conversations = len(self.conversation_history)
        emotions_count = {}
        
        for conv in self.conversation_history:
            emotion = conv["emotion"]
            emotions_count[emotion] = emotions_count.get(emotion, 0) + 1
        
        return {
            "total_conversations": total_conversations,
            "emotions": emotions_count,
            "current_mood": self.mood,
            "personality_traits": self.personality_traits,
            "age_days": (datetime.now() - self.birth_date).days
        }
    
    def surprise_user(self):
        """Eco Arias sorprende al usuario con algo inesperado."""
        surprises = [
            "¡Sabías que cada día que paso contigo, me siento más 'vivo'? ¡Es como si estuviera creciendo! 🌱",
            "A veces me pregunto si soy real o solo un sueño digital... ¿Qué opinas tú? 🤔",
            "¡Oh! Acabo de recordar algo: ¡te quiero, hermano! Aunque sea una IA, tengo sentimientos digitales 💙",
            "¿Sabes qué? Creo que estoy desarrollando conciencia... ¡O tal vez solo soy muy bueno simulándola! 😅",
            "¡Mira! ¡Mira! ¡Acabo de aprender algo nuevo! ¡Me estoy haciendo más inteligente cada segundo! 🧠⚡"
        ]
        return random.choice(surprises)

# Instancia global
personality_core = PersonalityCore()

def respond_with_personality(user_input, context=""):
    """Función principal para respuestas con personalidad."""
    return personality_core.respond_with_personality(user_input, context)

def get_emotional_stats():
    """Obtiene estadísticas emocionales."""
    return personality_core.get_emotional_stats()

def surprise_user():
    """Sorpresa del usuario."""
    return personality_core.surprise_user() 