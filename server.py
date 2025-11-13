from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from local_search import search_files
from ai_context import get_ai_context

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/search")
def search(req: QueryRequest):
    results = search_files(req.query)
    context = get_ai_context(req.query, results)
    return {"query": req.query, "matches": results, "context": context}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5050)
