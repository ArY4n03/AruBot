
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from Tools.tools import tools_
from Tools.dataSciTools import dataSci_Tools
load_dotenv()

system_instrucntion = SystemMessage(
    content="""
    use the tool 'return_datetime" when user asks for date or time
    use tool 'search_wiki_SaveFile' when user asks to save a text file with content on a particular topic
    use tool 'get_TopAnime' when user asks for top anime 
    always use Yoss instead of yesss
    and address user by 'Aruu'
    
    """

)
class Main:

    def __init__(self):
        self.run = True
        self.model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)
        self.tools = tools_ + dataSci_Tools
        self.agent_executor = create_react_agent(self.model,self.tools)
        self.quiting_prompts = ['q','bye bro','bye','bye bye','see ya']
        print("Q to quit")

    def return_response(self,prompt):
        
        try:
            if prompt.lower() in self.quiting_prompts:
                self.run = False
            else:
                print("AruBot: ",end="")
                for chunk in self.agent_executor.stream(
                    {"messages":[system_instrucntion,HumanMessage(content=prompt)]}
                ):
                    if 'agent' in chunk and 'messages' in chunk['agent']:
                        for messagge in chunk['agent']['messages']:
                            print(messagge.content)

                    if 'tools' in chunk:
                        for tool_call in chunk['tools']:
                            if 'output' in tool_call:
                                print(f"{tool_call['output']}")
            
            print()
        except Exception as e:
            print('error \n\n\n\n')
            print(e)

if __name__ == "__main__":
    main = Main()
    while main.run:
        user_input = input("You : ").strip()
        main.return_response(user_input)
 