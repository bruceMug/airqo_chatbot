import system_prompt

BOS, EOS = "<s>", "</s>"
B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
DEFAULT_SYSTEM_PROMPT = system_prompt.system_prompt

def format_to_llama_chat_style(history) -> str:
    
    return prompt