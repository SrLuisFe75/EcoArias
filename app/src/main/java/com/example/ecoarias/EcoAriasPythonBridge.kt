package com.example.ecoarias

import com.chaquo.python.PyObject
import com.chaquo.python.Python

/**
 * EcoAriasPythonBridge
 * Puente seguro para interactuar con los módulos Python de Eco Arias.
 * REGLA #1: JAMÁS modificar los archivos Python base desde aquí. Solo ejecutar y obtener resultados.
 * Todos los módulos de IA deben ser llamados a través de este bridge.
 */
object EcoAriasPythonBridge {
    private val py: Python = Python.getInstance()

    /**
     * Ejecuta una función de un módulo Python y retorna el resultado.
     * @param moduleName Nombre del archivo Python (sin .py)
     * @param functionName Nombre de la función a ejecutar
     * @param args Argumentos para la función
     * @return Resultado de la función Python
     */
    fun callPythonFunction(moduleName: String, functionName: String, vararg args: Any?): PyObject? {
        // NO modificar archivos, solo ejecutar funciones
        val module = py.getModule(moduleName)
        return module.callAttr(functionName, *args)
    }

    // Ejemplo de uso:
    // val result = EcoAriasPythonBridge.callPythonFunction("LocalIntelligenceEngine", "procesarComando", "Hola IA")
} 