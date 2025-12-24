from typing import Literal
from transformers import AutoProcessor, AutoModelForCausalLM
from huggingface_hub import login
import typer
import dotenv
import os

app = typer.Typer()

GEMMA_MODEL_ID = "google/functiongemma-270m-it"

DEVELOPER_MESSAGE = {
    "role": "developer",
    "content": "You are a model that can do function calling with the following functions"
}

def get_current_weather(city: str, country: str, unit: Literal["celsius", "fahrenheit"] = "celsius"):
    """
    Gets the current weather in a given location.

    Args:
        city: The city name
        country: The country name
        unit: The unit to return the temperature in. (choices: ["celsius", "fahrenheit"])

    Returns:
        temperature: The current temperature in the given location
        weather: The current weather in the given location
    """
    return {"temperature": 15, "weather": "sunny"}

tools = [
  get_current_weather,
]

@app.command()
def predict():
  print("Loading model...")

  processor = AutoProcessor.from_pretrained(GEMMA_MODEL_ID, device_map="auto")
  model = AutoModelForCausalLM.from_pretrained(GEMMA_MODEL_ID, dtype="auto", device_map="auto")

  print(f"Model loaded. Device: {model.device}")

  message = typer.prompt("Enter a message: ")
  
  prompt = [
    DEVELOPER_MESSAGE,
    {"role": "user", "content": message},
  ]

  inputs = processor.apply_chat_template(prompt, tools=tools, add_generation_prompt=True, return_dict=True, return_tensors="pt")
  output = processor.decode(inputs["input_ids"][0], skip_special_tokens=False)

  out = model.generate(**inputs.to(model.device), pad_token_id=processor.eos_token_id, max_new_tokens=128)
  generated_tokens = out[0][len(inputs["input_ids"][0]):]
  output = processor.decode(generated_tokens, skip_special_tokens=True)

  print(f"Output: {output}")
  print(type(output))

if __name__ == "__main__":
    dotenv.load_dotenv()
    login(token=os.getenv("HUGGINGFACE_API_KEY"))

    app()
