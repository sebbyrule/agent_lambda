import logging

logging.basicConfig(
    filename="agent_interactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_interaction(agent_id, user_input, response):
    logging.info(f"Agent {agent_id}: User Input: {user_input} | Response: {response}")
