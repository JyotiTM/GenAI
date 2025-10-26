from dotenv import load_dotenv
load_dotenv()

from langgraph.checkpoint.memory import InMemorySaver


from langgraph.prebuilt import create_react_agent

checkpointer = InMemorySaver()

agent = create_react_agent(

   model="openai:gpt-4o-mini",
   tools=[],
   checkpointer=checkpointer,
   prompt="You are a helpful assistant" 
)

   
config = {"configurable":{"thread_id":"1"}}


# Run the agents
response = agent.invoke(
   {"messages": [{"role": "user", "content": "what are large language models"}]},
   config = config
)
print(response["messages"][-1])



print("-------------------------------------")
response = agent.invoke(
{"messages":[{"role":"user","content":"where are they used"}]},
config = config

)
print(response["messages"][-1])
