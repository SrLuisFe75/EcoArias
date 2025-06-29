"""
Script Python para solucionar problemas de red en Chaquopy
"""

import socket
import ssl
import urllib.request
import json
import time
import os
from typing import Dict, Any

class NetworkFixer:
    def __init__(self):
        self.timeout = 30
        self.retries = 3
        self.setup_environment()
    
    def setup_environment(self):
        """Configurar entorno de red para Android"""
        # Configurar timeouts globales
        socket.setdefaulttimeout(self.timeout)
        
        # Configurar SSL para Android
        try:
            # Crear contexto SSL personalizado
            self.ssl_context = ssl.create_default_context()
            self.ssl_context.check_hostname = False
            self.ssl_context.verify_mode = ssl.CERT_NONE
        except Exception as e:
            print(f"Warning: SSL context setup failed: {e}")
    
    def test_connectivity(self) -> Dict[str, Any]:
        """Test completo de conectividad"""
        results = {
            "dns": False,
            "http": False,
            "https": False,
            "dns_manual": False,
            "error": None
        }
        
        try:
            # Test DNS básico
            results["dns"] = self._test_dns()
            
            # Test DNS manual con dnspython
            results["dns_manual"] = self._test_dns_manual()
            
            # Test HTTP
            results["http"] = self._test_http()
            
            # Test HTTPS
            results["https"] = self._test_https()
            
        except Exception as e:
            results["error"] = str(e)
        
        return results
    
    def _test_dns(self) -> bool:
        """Test resolución DNS básica"""
        try:
            socket.gethostbyname('google.com')
            return True
        except Exception as e:
            print(f"DNS básico falló: {e}")
            return False
    
    def _test_dns_manual(self) -> bool:
        """Test resolución DNS manual con dnspython"""
        try:
            import dns.resolver
            result = dns.resolver.resolve('google.com', 'A')
            for ipval in result:
                print(f"DNS manual - IP de google.com: {ipval.to_text()}")
            return True
        except Exception as e:
            print(f"DNS manual falló: {e}")
            return False
    
    def _test_http(self) -> bool:
        """Test conexión HTTP"""
        try:
            response = urllib.request.urlopen(
                'http://httpbin.org/ip', 
                timeout=self.timeout
            )
            return response.getcode() == 200
        except Exception as e:
            print(f"HTTP test falló: {e}")
            return False
    
    def _test_https(self) -> bool:
        """Test conexión HTTPS"""
        try:
            response = urllib.request.urlopen(
                'https://httpbin.org/ip', 
                timeout=self.timeout
            )
            return response.getcode() == 200
        except Exception as e:
            print(f"HTTPS test falló: {e}")
            return False
    
    def resolve_and_request(self, hostname: str, url: str) -> Dict[str, Any]:
        """Resolver hostname manualmente y hacer request con IP"""
        try:
            import dns.resolver
            
            # Resolver IP
            ip = dns.resolver.resolve(hostname, 'A')[0].to_text()
            print(f"IP de {hostname}: {ip}")
            
            # Reemplazar hostname por IP en URL
            url_with_ip = url.replace(hostname, ip)
            print(f"URL con IP: {url_with_ip}")
            
            # Hacer request con Host header
            req = urllib.request.Request(
                url_with_ip, 
                headers={'Host': hostname}
            )
            response = urllib.request.urlopen(req, timeout=self.timeout)
            content = response.read().decode('utf-8')
            
            return {
                "success": True,
                "status_code": response.getcode(),
                "content": content,
                "ip_used": ip
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def make_request(self, url: str, method: str = 'GET', data: dict = None) -> Dict[str, Any]:
        """Hacer request con reintentos y manejo de errores"""
        for attempt in range(self.retries):
            try:
                # Preparar request
                if data:
                    data_encoded = json.dumps(data).encode('utf-8')
                    req = urllib.request.Request(
                        url, 
                        data=data_encoded,
                        headers={'Content-Type': 'application/json'}
                    )
                else:
                    req = urllib.request.Request(url)
                
                req.get_method = lambda: method
                
                # Realizar request
                response = urllib.request.urlopen(req, timeout=self.timeout)
                content = response.read().decode('utf-8')
                
                return {
                    "success": True,
                    "status_code": response.getcode(),
                    "content": content,
                    "headers": dict(response.headers)
                }
                
            except Exception as e:
                if attempt == self.retries - 1:
                    return {
                        "success": False,
                        "error": str(e),
                        "attempt": attempt + 1
                    }
                time.sleep(1)  # Wait before retry
        
        return {"success": False, "error": "Max retries reached"}

# Función helper para usar desde Kotlin
def test_network():
    """Función simple para test desde Kotlin"""
    fixer = NetworkFixer()
    results = fixer.test_connectivity()
    
    print("=== RESULTADOS TEST RED ===")
    print(f"DNS básico: {'✅' if results['dns'] else '❌'}")
    print(f"DNS manual: {'✅' if results['dns_manual'] else '❌'}")
    print(f"HTTP: {'✅' if results['http'] else '❌'}")
    print(f"HTTPS: {'✅' if results['https'] else '❌'}")
    
    if results['error']:
        print(f"Error: {results['error']}")
    
    return results

def make_api_request(url: str):
    """Función para hacer requests API desde Kotlin"""
    fixer = NetworkFixer()
    result = fixer.make_request(url)
    
    if result['success']:
        print(f"✅ Request exitoso: {result['status_code']}")
        return result['content']
    else:
        print(f"❌ Request falló: {result['error']}")
        return None

def test_dns_resolution():
    """Test específico de resolución DNS"""
    fixer = NetworkFixer()
    return fixer._test_dns_manual()

def test_with_ip_resolution(hostname: str, url: str):
    """Test usando resolución manual de IP"""
    fixer = NetworkFixer()
    return fixer.resolve_and_request(hostname, url) 