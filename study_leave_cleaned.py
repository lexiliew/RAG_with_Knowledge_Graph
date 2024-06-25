import textwrap
from langchain.chains import GraphCypherQAChain
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_community.graphs import Neo4jGraph
from neo4j import GraphDatabase
import os
import dotenv

# Database connection setup
load_dotenv('.env', override=True)
NEO4J_URI1 = os.getenv('NEO4J_URI1')
NEO4J_USERNAME1 = os.getenv('NEO4J_USERNAME1')
NEO4J_PASSWORD1 = os.getenv('NEO4J_PASSWORD1')
NEO4J_DATABASE1 = os.getenv('NEO4J_DATABASE1')
print("Connected to Neo4j")

# Define the schema of your graph based on the entities and relationships
graph.refresh_schema()
print(graph.schema)

# Define the template for generating Cypher queries based on the schema and user questions
CYPHER_GENERATION_TEMPLATE = """Task: Generate Cypher statement to 
query a graph database.
Instructions:
Use only the provided relationship types and properties in the 
schema. Do not use any other relationship types or properties that 
are not provided.
Schema:
{schema}
Note: Do not include any explanations or apologies in your responses.
Do not respond to any questions that might ask anything else than 
for you to construct a Cypher statement.
Do not include any text except the generated Cypher statement.
# Who are the staff members eligible for study leave?
MATCH (sm:StaffMember)-[:APPLY_FOR]->(sl:StudyLeave)
WHERE toLower(sl.eligibility) CONTAINS 'eligible'
RETURN sm.title, sm.department

# Which approver is responsible for approving study leave?
MATCH (ap:Approver)-[:APPROVE]->(:StudyLeave)
WHERE toLower(ap.responsibility) CONTAINS 'approve'
RETURN ap.title, ap.responsibility

# What responsibilities does the Vice-President have regarding study leave?
MATCH (ap:Approver)
WHERE toLower(ap.title) CONTAINS 'vice-president'
RETURN ap.responsibility

# What are the entitlements for study leave?
MATCH (sl:StudyLeave)
RETURN sl.entitlement

The question is:
{question}"""



CYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question"], template=CYPHER_GENERATION_TEMPLATE
)
OPENAI_API_KEY=os.getenv("openai_api_key")
# Initialize the GraphCypherQAChain
llm = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0) 
# Initialize the GraphCypherQAChain without formatting the template here
qa_chain = GraphCypherQAChain.from_llm(
    graph=graph,
    llm=llm,
    verbose=True,
    cypher_prompt=CYPHER_GENERATION_PROMPT,
    )
print("QA chain initialized")


def prettyCypherChain(question: str) -> str:
    response = qa_chain.run(question)
    print(textwrap.fill(response, 60))

prettyCypherChain("What are the entitlements for study leave?")
prettyCypherChain("Who are the staff members eligible for study leave?")
prettyCypherChain("What responsibilities does the Vice-President have regarding study leave?")
prettyCypherChain("Which approver is responsible for approving study leave?")
prettyCypherChain("Is the President responsible for reviewing and approving study leave?")


