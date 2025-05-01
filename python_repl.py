from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import Tool
from langchain_experimental.utilities import PythonREPL
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType

# Load env variables (ensure your GOOGLE_API_KEY is set)
load_dotenv()

# Step 1: Initialize the model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=256,  # Set a reasonable limit
    timeout=None,
    max_retries=2,
)

# Step 2: Initialize Python REPL Tool
python_repl = PythonREPL()
repl_tool = Tool(
    name="python_repl",
    description="A Python shell. Use this to execute Python commands. Input should be a valid Python command. If you want to see the output of a value, you should print it out with `print(...)`.",
    func=python_repl.run,
)

# Step 3: Initialize Agent with the Tool
agent_executor = initialize_agent(
    tools=[repl_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# Step 4: Query in Natural Language
query = "Who is Anun"

# Step 5: Run Agent
response = agent_executor.run(query)
print("\n🔁 Final Response:\n", response)