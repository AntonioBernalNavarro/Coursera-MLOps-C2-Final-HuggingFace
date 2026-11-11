import click
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Cargar el modelo local que está en la carpeta summarizeApp
model = AutoModelForSeq2SeqLM.from_pretrained("summarizeApp")
tokenizer = AutoTokenizer.from_pretrained("summarizeApp")


def resumir_texto(texto: str) -> str:
    # Truncar a 1024 tokens para evitar errores con textos largos
    input_ids = tokenizer.encode(
        texto, return_tensors="pt", truncation=True, max_length=1024
    )
    outputs = model.generate(input_ids, max_length=150, min_length=30, do_sample=False)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


@click.command()
@click.option(
    "--archivo",
    "-f",
    type=click.Path(exists=True),
    help="Ruta al archivo de texto a resumir.",
)
@click.option(
    "--texto",
    "-t",
    type=str,
    help="Texto directo a resumir (alternativo a --archivo).",
)
def cli(archivo, texto):
    """Herramienta CLI para resumir texto usando el modelo de Hugging Face."""
    if archivo:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
    elif texto:
        contenido = texto
    else:
        click.echo("Error: Debes proporcionar --archivo o --texto.", err=True)
        raise click.Abort()

    click.echo("\n--- RESUMEN ---\n")
    click.echo(resumir_texto(contenido))


if __name__ == "__main__":
    # Click supplies the decorated command parameters.
    # pylint: disable=no-value-for-parameter
    cli()
