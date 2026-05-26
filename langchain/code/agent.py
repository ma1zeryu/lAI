from langchain.agents import create_agent
from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """获取指定城市的天气。"""
    return f"{city}今天天气很好！"

agent = create_agent(
    model="deepseek:deepseek-chat",
    tools=[get_weather],
    system_prompt="你是一个乐于助人的助手。凡是用户询问天气时，必须调用工具，不要凭空编造答案。",
)

# 运行代理
result = agent.invoke(
    {"messages": [{"role": "user", "content": "纽约天气怎么样"}]}
)

# print(result)

# 只提取并打印最后的回复内容
last_message = result["messages"][-1]
print(f"助手: {last_message.content}")