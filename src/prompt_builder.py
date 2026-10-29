def build_prompt(task: str, data: dict) -> str:
    prompt = f"""
Task: {task}

Input Data:
{data}

Instructions:
- Process the input data carefully.
- Return the result as a valid JSON object.
- Do not include explanations outside the JSON.
"""
    return prompt.strip()