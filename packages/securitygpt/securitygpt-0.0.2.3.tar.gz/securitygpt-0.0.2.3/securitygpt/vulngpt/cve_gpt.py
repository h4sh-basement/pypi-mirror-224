
from schema.schema_cve import CVEStructureJson, CVERemediationJson
from prompts.prompts_vuln import PromptCVERole, PromptCVETask
from chains.chain_generic import chat_complete
from utils import cve_utils

def summmarize_cve(cve_id:str):

    paragraphs = cve_utils.run(cve_id)

    paragraphs_text = ' '.join(paragraphs)

    system_content =  PromptCVERole().return_string
    
    prompt_string = """ 
        your goal is to analyze the text and summarize the text, the return is json.
        """  + paragraphs_text
    
    completion = chat_complete (model = "gpt-3.5-turbo-16k", system_content=system_content, user_content=prompt_string, functions = [CVEStructureJson.openai_schema] ).completion

    #print (completion["choices"][0].message.content)
    #print (completion["choices"][0].message.function_call.arguments)

    return completion["choices"][0].message.function_call.arguments