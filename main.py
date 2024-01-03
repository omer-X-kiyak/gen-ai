import google.generativeai as genai
import key

genai.configure(api_key=key.api_key)

def main():
    model_name = 'gemini-pro'
    model = genai.GenerativeModel(model_name)

    while True:
        user_input = input("Ask a question (or type 'exit' to end): ")
        if user_input.lower() == 'exit':
            break

        response = model.generate_content(user_input)
        print("Model's response:", response.text)

if __name__ == "__main__":
    main()
