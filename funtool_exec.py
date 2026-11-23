from langchain_openai import ChatOpenAI
from mytool import add_numbers, mul_numbers, sub_numbers, div_numbers

llm = ChatOpenAI(model = 'gpt-6-astra')

llm_with_tool = llm.bind_tools([add_numbers, mul_numbers, sub_numbers, div_numbers])

response = llm_with_tool.invoke('What is 125 + 345? Use the tool add_numbers.')

print("Text: ", response.content)
print("Tool Requests: ", response.tool_calls)

for call in response.tool_calls:
  if call['name'] == 'add_numbers':
    result = add_numbers.invoke(call['args'])
    print('Python result: ', result)