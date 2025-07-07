from fastapi import FastAPI, Request
from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import SpacyNlpEngine, NlpEngineProvider
from pydantic import BaseModel
import json

app = FastAPI()

# Vlastní NLP engine s menším modelem
config = {
    "nlp_engine_name": "spacy",
    "models": [{"lang_code": "en", "model_name": "en_core_web_sm"}]
}
provider = NlpEngineProvider(nlp_configuration=config)
nlp_engine = provider.create_engine()
analyzer = AnalyzerEngine(nlp_engine=nlp_engine)

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze(input: TextInput):
    results = analyzer.analyze(text=input.text, language="en")
    entities = list({res.entity_type for res in results})
    snippet = input.text[:300]
    return {"entities": entities, "snippet": snippet}
