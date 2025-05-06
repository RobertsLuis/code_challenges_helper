"""
Módulo para geração de estrutura de pastas e arquivos
"""

import os
from datetime import datetime
import pkg_resources


def get_template_content(template_type, language, extension):
    """
    Carrega o conteúdo de um template

    Args:
        template_type: Tipo do template ('Solution' ou 'Tests')
        language: Linguagem de programação (python ou java)
        extension: Extensão do arquivo (py ou java)

    Returns:
        String com o conteúdo do template
    """
    template_path = f"templates/{language}/{template_type}.{extension}"
    try:
        content = pkg_resources.resource_string(
            "code_challenge_helper", template_path
        ).decode("utf-8")

        # Normaliza as quebras de linha para o padrão do sistema
        content = content.replace("\r\n", "\n").replace("\r", "\n")

        return content
    except Exception as e:
        raise ValueError(f"Erro ao carregar template {template_path}: {e}")

def get_escalidraw_template():
    """
    Carrega o conteúdo do template Excalidraw

    Returns:
        String com o conteúdo do template
    """
    template_path = "templates/Excalidraw.md"
    try:
        content = pkg_resources.resource_string(
            "code_challenge_helper", template_path
        ).decode("utf-8")

        # Normaliza as quebras de linha para o padrão do sistema
        content = content.replace("\r\n", "\n").replace("\r", "\n")

        return content
    except Exception as e:
        raise ValueError(f"Erro ao carregar template {template_path}: {e}")

def create_challenge_structure(folder_name: str, language: str, extension: str):
    """
    Cria a estrutura de pastas e arquivos para um novo desafio

    Args:
        folder_name: Nome da pasta a ser criada
        language: Linguagem de programação (py ou java)
    """
    # Criar a pasta principal
    os.makedirs(folder_name, exist_ok=True)
    today = datetime.now().strftime("%d-%m-%Y")
    problem_name = folder_name.split("_")[0]

    files_to_create = {
        "Anotacoes.txt": "",
        "Rascunhos.excalidraw.md": get_escalidraw_template(),
        f"Solution.{extension}": get_template_content(
            template_type="Solution", language=language, extension=extension
        ).format(problem_name=problem_name, date=today),
        f"Tests.{extension}": get_template_content(
            template_type="Tests", language=language, extension=extension
        ).format(problem_name=problem_name, date=today),
    }

    for filename, content in files_to_create.items():
        file_path = os.path.join(folder_name, filename)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
