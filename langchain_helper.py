from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, animal_color):
    llm = OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables = ['animal_type','animal_color'],
        template = "I have a {animal_color} {animal_type} pet and I want a cool name for it. Suggest me five cool names for my pet."
    )
    
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="pet_name")

    response = name_chain({'animal_type': animal_type, 'animal_color': animal_color})
    return response
    
def langchain_agent():
    llm = OpenAI(temperature=0.5)

    tools = load_tools(["wikipedia","llm-math"], llm = llm)

    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    results = agent.run(
        "What average age of a dog? Multiply the age by 3."
    )

    print(results)

if __name__ == "__main__":
    langchain_agent()
