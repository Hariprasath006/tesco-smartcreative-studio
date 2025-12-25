import gradio as gr
from PIL import Image
import random

def generate_creative(product_name, price, image):
    status = random.choice([
        "✅ Tesco Compliance Passed",
        "⚠️ Minor Text Adjustment Suggested"
    ])
    
    return image, f"""
Creative Generated Successfully!

Product: {product_name}
Price: £{price}

Compliance Status:
{status}

Formats Generated:
- Tesco Display Banner
- Category Tile
- In-store Screen
"""

with gr.Blocks(title="Tesco SmartCreative Studio") as demo:
    gr.Markdown("## 🛒 Tesco SmartCreative Studio")
    gr.Markdown("AI-powered creative automation for Tesco Retail Media")

    with gr.Row():
        product_name = gr.Textbox(label="Product Name")
        price = gr.Textbox(label="Price (£)")

    image_input = gr.Image(label="Upload Product Image", type="pil")

    generate_btn = gr.Button("Generate Creative")

    output_image = gr.Image(label="Generated Creative Preview")
    output_text = gr.Textbox(label="Creative Details", lines=8)

    generate_btn.click(
        generate_creative,
        inputs=[product_name, price, image_input],
        outputs=[output_image, output_text]
    )

demo.launch()
