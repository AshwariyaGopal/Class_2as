from agents import Agent, Runner , RunConfig, AsyncOpenAI, OpenAIChatCompletionModel 
# Open ai agents sdk has two tyypes of api
# chatcompletionapi
# responses api by default yeh us
# e hoti ha
# #  
external_client = AsyncOpenAI( #its a provider
    api_key="",
    base_url="" # comunicatipon protocol is a api jisko unho ne deploy kiya ha or usko use krna ka way h ha hum use krna hata hai toh woh cloud pe uplaod hona chiaya
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
assistant = Agent(
    name="Mr Assistant",
    instructions = "You are a helpfull assistant that provides"
)
# chalana ke liya runner (ek class ha iska instance banay ga)
# starting_agent, input these are positonal argumane keyvalue pair me hota ha s
result = Runner.run_sync(starting_agent=assistant, input="hi how are you?" , run_config= config)
print(result.final_output)
# agent level config ki , run level ki ha 
# run pip install openai-agents
# uv add openai-agents
# uv run main.py