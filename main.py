from agents import Agent, Runner
from connection import config
 
agent = Agent(
    name="Translator",
    instructions="You are a helpful translator. Always translate English sentences into clear and simple Urdu."
)
 
response = Runner.run_sync(
    agent,
    input=f"My name is Ali Abbas.",
    run_config=config
