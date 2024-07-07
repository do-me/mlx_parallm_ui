from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import FileResponse 

from mlx_parallm.utils import load, batch_generate

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    model: str
    prompts: list[str]
    context: str
    max_tokens: int

@app.post("/process_data")
def process_data(data: InputData):
    try:
        print(data)
        formatted_prompts = [f"{i}/nContext: {data.context}" for i in data.prompts]
        print(formatted_prompts)
        
        model, tokenizer = load(data.model)  # Load the model specified in the request
        responses = batch_generate(model, tokenizer, prompts=formatted_prompts, max_tokens=data.max_tokens, verbose=False, format_prompts=True, temp=0.0)
        return {'responses': responses}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing data: {str(e)}")

@app.get("/")
async def read_index():
    return FileResponse('index.html')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
