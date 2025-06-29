// BUSCAR esta línea:
val result = python.getModule("ConsciousnessEngine")

// REEMPLAZAR por:
val result = python.getModule("ECO_ARIAS_ORCHESTRATOR")
    .callAttr("chat_with_eco_arias", userInput)