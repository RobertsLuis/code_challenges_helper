"""
Interface de linha de comando para o Code Challenge Helper
"""

import click
import sys
from datetime import datetime
from InquirerPy import inquirer
from .generator import create_challenge_structure

# Texto de ajuda personalizado para exibição
HELP_TEXT = """
Usage: challenge-helper COMMAND [ARGS]...

Code Challenge Helper - Ferramenta para criar estrutura de pastas para estudos.

Options:
  --help  Show this message and exit.

Commands:
  create-resolution  Cria uma nova estrutura de pastas para um desafio de código.
                     Este comando inicia um assistente interativo que solicitará:
                    
                     1. O nome do problema a ser resolvido
                     2. A linguagem de programação desejada (Python ou Java)
                    
                     Após fornecer essas informações, uma nova pasta será criada
                     com arquivos de template prontos para resolver o desafio.
"""


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Code Challenge Helper - Ferramenta para criar estrutura de pastas para estudos."""
    # Mostrar nosso texto personalizado para --help ou quando não há subcomando
    if ctx.invoked_subcommand is None:
        click.echo(HELP_TEXT)
        ctx.exit()


@cli.command(name="create-resolution")
def create_resolution_schema():
    """Cria uma nova estrutura de pastas para um desafio de código."""
    nome_questao = click.prompt("Qual o nome da questão?", type=str)

    valid_languages = {"python": "py", "java": "java", "go": "go"}
    language = inquirer.select(
        message="Em qual linguagem deseja realizar?",
        choices=valid_languages.keys(),
        default="python",
    ).execute()
    extension = valid_languages[language]

    hoje = datetime.now().strftime("%d-%m-%Y")
    folder_name = f"{nome_questao}_{hoje}"

    create_challenge_structure(folder_name, language, extension)
    click.echo(f"\n✅ Estrutura criada com sucesso: {folder_name}")


def main():
    # Se for chamado com --help, use nosso próprio texto de ajuda
    if "--help" in sys.argv or "-h" in sys.argv:
        click.echo(HELP_TEXT)
        return 0
    cli()


if __name__ == "__main__":
    main()
