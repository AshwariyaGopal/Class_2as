# handsoff
# Update the import path if 'agents' is a local file or install the required package if it's external.
# For example, if 'agents.py' is in the same directory:
from agents import Agent, Runner, RunConfig, AsyncOpenAI, OpenAIChatCompletionModel
# Or, if it's a package, ensure it's installed and available in your environment.
# Open ai agents sdk has two tyypes of api
# chatcompletionapi
# responses api by default yeh us
# e hoti ha
# #  
external_client = AsyncOpenAI( #its a provider
    api_key="API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/" # comunicatipon protocol is a api jisko unho ne deploy kiya ha or usko use krna ka way h ha hum use krna hata hai toh woh cloud pe uplaod hona chiaya
)

external_model = OpenAIChatCompletionModel(
    model= "gemini-2.0-flash",
    openai_client = external_client # provider

)

config = RunConfig(
    model=external_model,
    model_provider=external_client,
    tracing_disabled= True # isko tab use kray ga jab openai key use kray ga 

)
Nextjs_agent = Agent(
    name="Mr Assistant",
    instructions = "You are a helpfull assistant that provides information about Nextjs programming language"
    )
Python_agent = Agent(
    name="Python Assistant",    
    instructions = "You are a helpfull assistant that provides information about python programming language")

Tri_agent = Agent(
    name="Tri Assistant",    
    instructions = "You are a helpfull assistant that navigates between Nextjs and Python Assistant to provide the best answer",
    handsoff_agents=[Nextjs_agent, Python_agent] # handsoff agents are the agents that will be used to provide the answer

)
# chalana ke liya runner (ek class ha iska instance banay ga)
# starting_agent, input these are positonal argumane keyvalue pair me hota ha s
result = Runner.run_sync(starting_agent=Tri_agent, input="i want to help regarding python decorators?", run_config= config)
print("Final output",result.final_output)
print("Current Agent", result.last_agent)