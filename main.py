from fastapi import FastAPI, Request
from presidio_analyzer import AnalyzerEngine
from pydantic import BaseModel

app = FastAPI()
analyzer = AnalyzerEngine()

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze(input: TextInput):
    results = analyzer.analyze(text=input.text, language="en")
    entities = list({res.entity_type for res in results})
    snippet = input.text[:300]
    return {"entities": entities, "snippet": snippet}
