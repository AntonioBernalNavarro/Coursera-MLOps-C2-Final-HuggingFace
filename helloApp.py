import gradio as gr
from mylib.calculator import add

def sumar(num1, num2):
    # Convertimos a float por si Gradio envía strings
    resultado = add(float(num1), float(num2))
    return f"El resultado es: {resultado}"

with gr.Blocks() as demo:
    gr.Markdown("## Calculadora de Suma")
    with gr.Row():
        num1 = gr.Number(label="Número 1")
        num2 = gr.Number(label="Número 2")
    boton = gr.Button("Sumar")
    salida = gr.Textbox(label="Resultado")
    boton.click(fn=sumar, inputs=[num1, num2], outputs=salida)

demo.launch()
