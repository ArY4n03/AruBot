from langchain.tools import tool
import datetime
from .webTools import *

def generate_txtFile(content):
    "Save a content as text file"
    with open("File.txt","w") as file:
        file.write(content)
    

@tool
def return_datetime():
    "Returns todays date"
    return f"{datetime.date}"

@tool
def evaluate(exp:str):
    "evaluate a mathematical expression"
    return f"{exp} = {eval(exp)}"

@tool
def search_wiki_SaveFile(topic):
    """Searches wikipedia for a topic and store its content on text file"""
    content = search_wiki(topic)
    generate_txtFile(content)

    return "Search done and file saved"


tools_ = [return_datetime,search_wiki_SaveFile,evaluate,get_TopAnime]