from prompt_builder import build_prompt

task = "Extract the person's name and project."

data = {
    "name": "Rishitha",
    "project": "Structured LLM Prompt Pipeline"
}

prompt = build_prompt(task, data)

print("Generated Prompt:")
print("-----------------")
print(prompt)