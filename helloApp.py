"""Aplicación Gradio para sumar dos números."""

import gradio as gr
from mylib.calculator import add


def sumar(valor1, valor2):
    """Devuelve la suma de dos números."""
    resultado = add(float(valor1), float(valor2))
    return f"El resultado es: {resultado}"


with gr.Blocks() as demo:
    gr.Markdown("## Calculadora de Suma")

    with gr.Row():
        num1 = gr.Number(label="Número 1")
        num2 = gr.Number(label="Número 2")

    boton = gr.Button("Sumar")
    salida = gr.Textbox(label="Resultado")

    boton.click(
        fn=sumar,
        inputs=[num1, num2],
        outputs=salida,
    )  # pylint: disable=no-member

demo.launch()
