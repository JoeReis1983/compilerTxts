#!/usr/bin/env python3
"""
Script para compilar arquivos .txt em um único arquivo e organizá-los em uma pasta separada.
"""

import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Optional

# Configurações
DEFAULT_PATH = Path.home() / "Desktop"
OUTPUT_FILE = "compilado.txt"
BACKUP_FOLDER = "txt rip"
HEADER_SEPARATOR = "#" * 20

def get_txt_files(directory: Path) -> List[str]:
    """
    Lista todos os arquivos .txt em um diretório.
    
    Args:
        directory: Caminho do diretório para buscar os arquivos
        
    Returns:
        Lista com os nomes dos arquivos .txt encontrados
    """
    return [f for f in os.listdir(directory) if f.endswith('.txt')]

def sort_files_by_date(files: List[str], directory: Path) -> List[str]:
    """
    Ordena arquivos por data de modificação (mais antigos primeiro).
    
    Args:
        files: Lista de nomes de arquivos
        directory: Diretório onde os arquivos estão localizados
        
    Returns:
        Lista ordenada de nomes de arquivos
    """
    return sorted(files, key=lambda x: os.path.getmtime(directory / x))

def format_file_header(filename: str, mod_date: datetime) -> str:
    """
    Formata o cabeçalho para cada arquivo no compilado.
    
    Args:
        filename: Nome do arquivo
        mod_date: Data da última modificação
        
    Returns:
        String formatada com o cabeçalho
    """
    formatted_date = mod_date.strftime("%d/%m/%Y %H:%M:%S")
    return f"\n{HEADER_SEPARATOR} {filename} - Última atualização: {formatted_date} {HEADER_SEPARATOR}\n"

def create_compiled_file(files: List[str], directory: Path) -> None:
    """
    Cria o arquivo compilado com o conteúdo de todos os arquivos .txt.
    
    Args:
        files: Lista de arquivos para compilar
        directory: Diretório onde os arquivos estão localizados
    """
    output_path = directory / OUTPUT_FILE
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for filename in files:
            file_path = directory / filename
            mod_time = os.path.getmtime(file_path)
            mod_date = datetime.fromtimestamp(mod_time)
            
            # Escreve o cabeçalho
            output_file.write(format_file_header(filename, mod_date))
            
            # Escreve o conteúdo
            try:
                with open(file_path, 'r', encoding='utf-8') as input_file:
                    output_file.write(input_file.read())
                    output_file.write('\n')
            except Exception as e:
                error_msg = f"\nErro ao ler o arquivo {filename}: {str(e)}\n"
                output_file.write(error_msg)
    
    print(f"Arquivo compilado criado com sucesso: {output_path}")

def move_files_to_backup(files: List[str], directory: Path) -> None:
    """
    Move os arquivos .txt para a pasta de backup.
    
    Args:
        files: Lista de arquivos para mover
        directory: Diretório onde os arquivos estão localizados
    """
    backup_path = directory / BACKUP_FOLDER
    
    # Cria a pasta de backup se não existir
    if not backup_path.exists():
        backup_path.mkdir()
        print(f"Pasta '{BACKUP_FOLDER}' criada em: {backup_path}")
    
    # Move os arquivos
    for filename in files:
        if filename != OUTPUT_FILE:  # Não move o arquivo compilado
            source = directory / filename
            destination = backup_path / filename
            try:
                shutil.move(str(source), str(destination))
                print(f"Arquivo movido: {filename}")
            except Exception as e:
                print(f"Erro ao mover o arquivo {filename}: {str(e)}")

def main() -> None:
    """Função principal que executa todo o processo."""
    # Obtém e ordena os arquivos
    txt_files = get_txt_files(DEFAULT_PATH)
    sorted_files = sort_files_by_date(txt_files, DEFAULT_PATH)
    
    # Cria o arquivo compilado
    create_compiled_file(sorted_files, DEFAULT_PATH)
    
    # Move os arquivos para a pasta de backup
    move_files_to_backup(sorted_files, DEFAULT_PATH)
    
    print("Processo finalizado!")

if __name__ == "__main__":
    main() 