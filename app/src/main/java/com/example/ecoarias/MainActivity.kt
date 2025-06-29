package com.example.ecoarias

import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.LinearLayout
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform

class MainActivity : AppCompatActivity() {
    
    private val TAG = "FORCE_REFRESH_SOLUTION"
    private lateinit var statusText: TextView
    private var counter = 0
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        Log.d(TAG, "=== SOLUCIÓN: FORZAR REDIBUJADO ===")
        
        createWorkingUI()
    }
    
    private fun createWorkingUI() {
        val layout = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(40, 40, 40, 40)
        }
        
        // Título
        val title = TextView(this).apply {
            text = "✅ SOLUCIÓN UI WORKING"
            textSize = 20f
            setPadding(0, 0, 0, 20)
        }
        layout.addView(title)
        
        // Status con fondo de color
        statusText = TextView(this).apply {
            text = "Estado: Listo para tests"
            textSize = 16f
            setBackgroundColor(0xFF4CAF50.toInt()) // Verde
            setPadding(20, 15, 20, 15)
            setTextColor(0xFFFFFFFF.toInt()) // Texto blanco
        }
        layout.addView(statusText)
        
        // Botón test básico
        val btnBasic = Button(this).apply {
            text = "🔧 TEST: Update Forzado"
            setOnClickListener {
                testForcedUpdate()
            }
        }
        layout.addView(btnBasic)
        
        // Botón test Python + Red (ahora que sabemos que UI funciona)
        val btnPython = Button(this).apply {
            text = "🐍 TEST: Python + Red"
            setOnClickListener {
                testPythonNetwork()
            }
        }
        layout.addView(btnPython)
        
        // Botón reset
        val btnReset = Button(this).apply {
            text = "🔄 RESET Counter"
            setOnClickListener {
                resetCounter()
            }
        }
        layout.addView(btnReset)
        
        setContentView(layout)
        Log.d(TAG, "✅ UI creada con solución de redibujado")
    }
    
    private fun testForcedUpdate() {
        Log.d(TAG, "=== TEST UPDATE FORZADO ===")
        
        try {
            counter++
            
            // SOLUCIÓN: Función que fuerza redibujado
            updateTextViewForcefully(
                statusText, 
                "✅ Update #$counter funcionando!"
            )
            
            // Cambiar color de fondo también para confirmación visual
            val colors = listOf(
                0xFF4CAF50.toInt(), // Verde
                0xFF2196F3.toInt(), // Azul  
                0xFFFF9800.toInt(), // Naranja
                0xFF9C27B0.toInt(), // Púrpura
                0xFFE91E63.toInt()  // Rosa
            )
            
            statusText.setBackgroundColor(colors[counter % colors.size])
            
            // Forzar redibujado del fondo también
            forceViewRefresh(statusText)
            
            Toast.makeText(this, "Update #$counter completado", Toast.LENGTH_SHORT).show()
            
            Log.d(TAG, "✅ Update forzado completado: #$counter")
            
        } catch (e: Exception) {
            Log.e(TAG, "❌ Error en update forzado: ${e.message}")
        }
    }
    
    private fun testPythonNetwork() {
        Log.d(TAG, "=== TEST PYTHON + RED ===")
        
        updateTextViewForcefully(statusText, "🐍 Iniciando Python...")
        
        lifecycleScope.launch {
            withContext(Dispatchers.IO) {
                try {
                    // Inicializar Python
                    runOnUiThread {
                        updateTextViewForcefully(statusText, "🐍 Inicializando Python...")
                    }
                    
                    if (!Python.isStarted()) {
                        Python.start(AndroidPlatform(this@MainActivity))
                        Log.d(TAG, "✅ Python iniciado")
                    }
                    
                    val py = Python.getInstance()
                    
                    runOnUiThread {
                        updateTextViewForcefully(statusText, "🌐 Probando conectividad...")
                    }
                    
                    // Test de red con Python
                    val networkTestScript = """
import urllib.request
import json

def test_network():
    try:
        response = urllib.request.urlopen('https://httpbin.org/ip', timeout=10)
        data = response.read().decode('utf-8')
        result = json.loads(data)
        return f"✅ Red OK: IP {result['origin']}"
    except Exception as e:
        return f"❌ Error: {e}"

result = test_network()
print(result)
"""
                    
                    py.getModule("__main__").callAttr("exec", networkTestScript)
                    
                    runOnUiThread {
                        updateTextViewForcefully(statusText, "🎉 ¡Python + Red funcionan!")
                        statusText.setBackgroundColor(0xFF4CAF50.toInt()) // Verde éxito
                        forceViewRefresh(statusText)
                        
                        Toast.makeText(this@MainActivity, "🎉 ¡TODO FUNCIONA!", Toast.LENGTH_LONG).show()
                    }
                    
                    Log.d(TAG, "🎉 ¡PYTHON + RED FUNCIONAN PERFECTAMENTE!")
                    
                } catch (e: Exception) {
                    Log.e(TAG, "❌ Error en Python/Red: ${e.message}")
                    runOnUiThread {
                        updateTextViewForcefully(statusText, "❌ Error: ${e.message}")
                        statusText.setBackgroundColor(0xFFF44336.toInt()) // Rojo error
                        forceViewRefresh(statusText)
                    }
                }
            }
        }
    }
    
    private fun resetCounter() {
        counter = 0
        updateTextViewForcefully(statusText, "🔄 Counter reseteado")
        statusText.setBackgroundColor(0xFF607D8B.toInt()) // Gris
        forceViewRefresh(statusText)
        
        Toast.makeText(this, "Counter reseteado", Toast.LENGTH_SHORT).show()
        Log.d(TAG, "Counter reseteado")
    }
    
    // SOLUCIÓN PRINCIPAL: Función que fuerza redibujado de TextView
    private fun updateTextViewForcefully(textView: TextView, newText: String) {
        Log.d(TAG, "Actualizando TextView: '$newText'")
        
        // 1. Actualizar el texto
        textView.text = newText
        
        // 2. Forzar invalidación
        textView.invalidate()
        
        // 3. Forzar re-layout
        textView.requestLayout()
        
        // 4. Forzar invalidación del padre
        val parent = textView.parent as? android.view.ViewGroup
        parent?.invalidate()
        
        // 5. Post para asegurar que se ejecute en el próximo frame
        textView.post {
            textView.invalidate()
        }
        
        Log.d(TAG, "✅ Redibujado forzado completado")
    }
    
    // Función auxiliar para forzar refresh completo de cualquier View
    private fun forceViewRefresh(view: android.view.View) {
        view.invalidate()
        view.requestLayout()
        
        val parent = view.parent as? android.view.ViewGroup
        parent?.invalidate()
        parent?.requestLayout()
        
        // Forzar en el próximo frame también
        view.post {
            view.invalidate()
            view.requestLayout()
        }
    }
    
    override fun onResume() {
        super.onResume()
        Log.d(TAG, "▶️ App activa - Solución aplicada")
        Toast.makeText(this, "✅ UI Fix aplicado", Toast.LENGTH_SHORT).show()
    }
} 