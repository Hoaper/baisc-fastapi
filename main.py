from fastapi import FastAPI
import requests
 
app = FastAPI()
 
@app.post("/load_data")
def load_data(data: str):
    
 
    return {"message": "Data loaded successfully."}
 
@app.post("/generate_response")
def generate_response(data: str):
   
    response = requests.post("https://api.openai.com/v1/engines/davinci-codex/completions", 
                             headers={"Authorization": "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"},
                             json={"prompt": data, "max_tokens": 100})
 
    generated_response = response.json()["choices"][0]["text"]
 
    return {"response": generated_response}
 
 
import unittest
from fastapi.testclient import TestClient
 
 #В коде определяется класс модульного тестирования TestFastAPI,
 #  который тестирует два endpoint приложения FastAPI. 
 # Класс наследуется от unittest.TestCase, который предоставляет основу для написания и запуска тестов.
 #  Два метода тестирования, test_load_data_success и test_generate_response_success, отправляют HTTP-запросы POST
 #  к соответствующим конечным точкам и утверждают ожидаемый код состояния ответа и содержимое ответа.
class TestFastAPI(unittest.TestCase):
 
    def setUp(self):
        self.client = TestClient(app)
 
    def test_load_data_success(self):
        
        response = self.client.post("/load_data", json={"data": "Sample data"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Data loaded successfully."})
 
    def test_generate_response_success(self):
        
        response = self.client.post("/generate_response", json={"data": "Sample prompt"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("response", response.json())
 
    def test_load_data_invalid_request(self):
        
        response = self.client.post("/load_data", json={"invalid_key": "Sample data"})
        self.assertEqual(response.status_code, 422)
 
    def test_generate_response_invalid_request(self):
        
        response = self.client.post("/generate_response", json={"invalid_key": "Sample prompt"})
        self.assertEqual(response.status_code, 422)



@app.get("/")
def web_page():
    return """
    <html>
    <body>
    <h1>Welcome to the API!</h1>
    <p>Use the /load_data endpoint to load data for analysis.</p>
    <p>Use the /generate_response endpoint to generate detailed responses using ChatGPT API.</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=8000, host='0.0.0.0')



#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