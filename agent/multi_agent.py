from agent.agent import Agent

class MultiAgentCoordinator:
    def __init__(self):
        self.agents = {}

    def add_agent(self, agent_id, agent):
        if agent_id in self.agents:
            raise ValueError(f"Agent with ID {agent_id} already exists.")
        self.agents[agent_id] = agent

    def remove_agent(self, agent_id):
        self.agents.pop(agent_id, None)

    def communicate(self, sender_id, receiver_id, message):
        if sender_id not in self.agents or receiver_id not in self.agents:
            raise ValueError("Invalid agent ID(s).")
        response = self.agents[receiver_id].respond(message)
        return response
