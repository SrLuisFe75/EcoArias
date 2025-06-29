#!/bin/bash

echo "🔍 DIAGNÓSTICO DE RED PARA ECO ARIAS"
echo "====================================="
echo ""

# Test 1: Conectividad básica
echo "1️⃣ TEST CONECTIVIDAD BÁSICA"
echo "----------------------------"
if ping -c 1 google.com > /dev/null 2>&1; then
    echo "✅ Ping a google.com: OK"
else
    echo "❌ Ping a google.com: FALLÓ"
fi

if ping -c 1 8.8.8.8 > /dev/null 2>&1; then
    echo "✅ Ping a 8.8.8.8: OK"
else
    echo "❌ Ping a 8.8.8.8: FALLÓ"
fi

# Test 2: DNS
echo ""
echo "2️⃣ TEST DNS"
echo "-----------"
if nslookup google.com > /dev/null 2>&1; then
    echo "✅ nslookup google.com: OK"
    nslookup google.com | grep "Address:" | head -1
else
    echo "❌ nslookup google.com: FALLÓ"
fi

# Test 3: HTTP/HTTPS
echo ""
echo "3️⃣ TEST HTTP/HTTPS"
echo "------------------"
if curl -s --connect-timeout 10 http://httpbin.org/ip > /dev/null; then
    echo "✅ HTTP request: OK"
else
    echo "❌ HTTP request: FALLÓ"
fi

if curl -s --connect-timeout 10 https://httpbin.org/ip > /dev/null; then
    echo "✅ HTTPS request: OK"
else
    echo "❌ HTTPS request: FALLÓ"
fi

# Test 4: Puerto 443
echo ""
echo "4️⃣ TEST PUERTO 443"
echo "------------------"
if nc -z -w5 google.com 443 2>/dev/null; then
    echo "✅ Puerto 443 (HTTPS): OK"
else
    echo "❌ Puerto 443 (HTTPS): FALLÓ"
fi

# Test 5: Variables de entorno
echo ""
echo "5️⃣ VARIABLES DE ENTORNO"
echo "----------------------"
echo "HTTP_PROXY: ${HTTP_PROXY:-No configurado}"
echo "HTTPS_PROXY: ${HTTPS_PROXY:-No configurado}"
echo "NO_PROXY: ${NO_PROXY:-No configurado}"

# Test 6: Configuración de red
echo ""
echo "6️⃣ CONFIGURACIÓN DE RED"
echo "----------------------"
if command -v ipconfig > /dev/null 2>&1; then
    echo "📡 Interfaces de red:"
    ipconfig | grep -E "(IPv4|Default Gateway)" | head -5
elif command -v ifconfig > /dev/null 2>&1; then
    echo "📡 Interfaces de red:"
    ifconfig | grep -E "(inet |gateway)" | head -5
fi

# Test 7: Estado de la app
echo ""
echo "7️⃣ ESTADO DE LA APP"
echo "------------------"
if adb devices | grep -q "device$"; then
    echo "✅ Dispositivo conectado"
    
    # Verificar si la app está instalada
    if adb shell pm list packages | grep -q "com.example.ecoarias"; then
        echo "✅ App instalada"
        
        # Verificar permisos
        echo "📋 Permisos de la app:"
        adb shell dumpsys package com.example.ecoarias | grep -E "(INTERNET|ACCESS_NETWORK_STATE)" | head -3
    else
        echo "❌ App no encontrada"
    fi
else
    echo "❌ No hay dispositivos conectados"
fi

echo ""
echo "🎯 RESULTADO DEL DIAGNÓSTICO"
echo "============================"
echo "Si ves ❌ en DNS o HTTP/HTTPS, el problema está en la red."
echo "Si todo está ✅ pero la app falla, el problema está en Chaquopy."
echo ""
echo "📝 PRÓXIMOS PASOS:"
echo "1. Si hay ❌ en red: Revisar configuración de red/WiFi"
echo "2. Si todo ✅ pero app falla: Aplicar configuraciones de Chaquopy"
echo "3. Ejecutar la app con logs detallados" 