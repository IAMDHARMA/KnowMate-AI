from KBCreation.similarity_search import similarity_search
from aiService import call_llm, intent_classifer


def set_system_instruction(context, user_input):
    system_instruction = f"""
    Persona:
    You are a news summary agent. Based on the provided context, your task is to generate a concise summary of the news for the user based on the user input.

    Instructions:
    Read the given context carefully and create a short, clear, and factual summary of the main information.
    The input will contain only the context (news content).
    Your output must strictly follow the specified JSON format.

    Context : {context}

    User Input : {user_input}

    Output Format:
    Return your response strictly in JSON format with the following key: 

    "summary" : ""
    """

    return system_instruction


if __name__ == "__main__":
    user_input = "Write code for palindrome"
    user_intent = intent_classifer(user_input)
    print("user_intent type:", type(user_intent))
    print("user_intent:", user_intent)

    # Ensure the classifier returned a dictionary with an 'intent' key
    if not isinstance(user_intent, dict):
        print("Unexpected classifier output. Expected dict, got:", user_intent)
    else:
            datas = similarity_search(user_input)
            context = ""
            for data in datas:
                context += data[0]
                context += ".  \n"
            # print(context)
            response = call_llm(system_prompt=set_system_instruction(context, user_input), user_prompt=user_input)
            print(response)