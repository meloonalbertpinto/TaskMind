import google.generativeai as genai
import os

api_key = "AIzaSyACJPkCmspdQnmWXIQooiC6FmbMGcGB-84"
genai.configure(api_key=api_key)

print("Listing all models...")
with open("model_list.txt", "w") as f:
    try:
        for m in genai.list_models():
            f.write(f"{m.name} - {m.supported_generation_methods}\n")
            print(m.name)
    except Exception as e:
        f.write(f"Error: {e}\n")
        print(f"Error: {e}")
