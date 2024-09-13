import torch
from transformers import LlamaTokenizer, LlamaForCausalLM


def load_model(model_path):
    # Cargar el tokenizador y el modelo
    tokenizer = LlamaTokenizer.from_pretrained(model_path)
    model = LlamaForCausalLM.from_pretrained(model_path)
    return tokenizer, model


def generate_response(prompt, tokenizer, model):
    # Tokenizar la entrada
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generar la respuesta
    with torch.no_grad():
        outputs = model.generate(
            **inputs, max_length=50
        )  # Ajusta max_length según lo necesites

    # Decodificar la respuesta
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response


def main():
    model_path = "llama-2-7b"  # Ajusta esto según el modelo que estés usando
    tokenizer, model = load_model(model_path)

    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            break
        response = generate_response(prompt, tokenizer, model)
        print(f"LLaMA: {response}")


if __name__ == "__main__":
    main()
