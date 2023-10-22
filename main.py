import json

import quart
import quart_cors
from quart import request
from rulzai import RulzAI

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

# Instantiate your Rulz-AI model
rulz_ai_model = RulzAI()

@app.post("/generate")
async def generate_text():
    request_data = await request.get_json(force=True)
    input_text = request_data["input_text"]
    
    # Call your Rulz-AI model to generate the desired text based on the input
    generated_text = rulz_ai_model.generate_text(input_text)
    
    return quart.Response(response=json.dumps({"generated_text": generated_text}), status=200)

# Other necessary routes and functions for your Rulz-AI integration

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
