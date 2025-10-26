from dotenv import load_dotenv
load_dotenv()

# from langgraph.checkpoint.memory import InMemorySaver

from pydantic import BaseModel

from langgraph.prebuilt import create_react_agent

# checkpointer = InMemorySaver()

class MailResponse(BaseModel):
    subject : str
    body : str

agent = create_react_agent(

   model="openai:gpt-4o-mini",
   tools=[],
#    checkpointer=checkpointer,
 response_format = MailResponse,
   prompt="You are a helpful assistant" 
)

   


# Run the agents
response = agent.invoke(
   {"messages": [{"role": "user", "content": "write a mail to my boss stating that I am sick and wont be coming to pffice for 3 days"}]}
   
)
print(response)
print("---------------------------")

print(response["structured_response"])
print("-------------------------")

print(response["structured_response"].subject)
print("---------------------------")
print(response["structured_response"].body)



