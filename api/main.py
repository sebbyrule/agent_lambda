from fastapi import FastAPI, HTTPException
from agent.agent import Agent  # Assuming Agent is your core class

app = FastAPI()

# Initialize the agent
agent = Agent()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Agent API"}

@app.post("/agent/respond/")
def agent_respond(prompt: str):
    try:
        response = agent.respond(prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
