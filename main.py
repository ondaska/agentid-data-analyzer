from fastapi import FastAPI
from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import NlpEngineProvider
from pydantic import BaseModel
import spacy
import subprocess

# Stáhne model, pokud ještě není
try:
    spacy.load("en_core_web_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])

# Konfigurace NLP engine
config = {
    "nlp_engine_name": "spacy",
    "models": [{"lang_code": "en", "model_name": "en_core_web_sm"}]
}
provider = NlpEngineProvider(nlp_configuration=config)
nlp_engine = provider.create_engine()
analyzer = AnalyzerEngine(nlp_engine=nlp_engine)

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze(input: TextInput):
    results = analyzer.analyze(text=input.text, language="en")
    entities = list({res.entity_type for res in results})
    snippet = input.text[:300]
    return {"entities": entities, "snippet": snippet}
