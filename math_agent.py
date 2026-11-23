import os
import json
from openai import OpenAI
from math_tools import add_numbers, sub_numbers, mul_numbers, div_numbers

MODEL = 'gpt-5.5'

client = OpenAI()

TOOLS = [
  {
    "type": "function",
    "name": "add_numbers",
    "description": "Add two numbers.",
    "parameters": {
      "type": "object",
      "properties": {
        "a": {"type": "number"},
        "b": {"type": "number"}
      },
      "required": ["a", "b"],
      "additionalProperties": False
    },
    "strict": True
  },
  {
    "type": "function",
    "name": "sub_numbers",
    "description": "Subtract b from a.",
    "parameters": {
      "type": "object",
      "properties": {
        "a": {"type": "number"},
        "b": {"type": "number"}
      },
      "required": ["a", "b"],
      "additionalProperties": False
    },
    "strict": False
  },
  {
    "type": "function",
    "name": "mul_numbers",
    "description": "Multiply a and b.",
    "parameters": {
      "type": "object",
      "properties": {
        "a": {"type": "number"},
        "b": {"type": "number"}
      },
      "required": ["a", "b"],
      "additionalProperties": False
    },
    "strict": False
  },
  {
    "type": "function",
    "name": "div_numbers",
    "description": "Divide a and b.",
    "parameters": {
      "type": "object",
      "properties": {
        "a": {"type": "number"},
        "b": {"type": "number"}
      },
      "required": ["a", "b"],
      "additionalProperties": False
    },
    "strict": False
  }
]

FUNCTIONS = {
  "add_numbers": add_numbers,
  "sub_numbers": sub_numbers,
  "mul_numbers": mul_numbers,
  "div_numbers": div_numbers
}

def run_agent(question):
  response = client.responses.create(
    model = MODEL,
    instructions = (
      "You are a Math AI Agent. Use add_numbers for addition "
      "and sub_numbers for subtraction. Do not guess "
      "calculation results. Use tools when calculation is needed."
    ),
    input = question,
    tools = TOOLS
  )

  while True:
    calls = [
      item for item in response.output
    ]

    if not calls:
      return response.output_text

    tool_outputs = []

    for call in calls:
      arguments = json.loads(call.arguments)
      function = FUNCTIONS[call.name]
      result = function(**arguments)

      tool_outputs.append({
        "type": "function_call_output",
        "call_id": call.call_id,
        "output": str(result)
      })

    response = client.responses.create(
      model = MODEL,
      instructions = (
        "You are a Math AI Agent. Explain results simply."
      ),
      input = [*response.output, *tool_outputs],
      tools = TOOLS
    )

if __name__ == "__main__":
  question = input("Ask a math question: ")
  print("\nAI Agent Answer: ")
  print(run_agent(question))