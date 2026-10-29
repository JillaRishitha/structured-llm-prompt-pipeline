import json

from pipeline.json_extractor import extract_json
from validator import validate_json
from prompt_builder import build_prompt


def main():
    sample_response = '{"name": "Rishitha", "project": "Structured LLM Prompt Pipeline"}'

    result = extract_json(sample_response)

    validate_json(result)

    task = "Extract the person's name and project."

    prompt = build_prompt(task, result)

    print("Structured LLM Prompt Pipeline")
    print("------------------------------")

    print("\nGenerated Prompt:")
    print(prompt)

    print("\nJSON validation successful!")
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()