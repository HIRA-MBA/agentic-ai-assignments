from agents import AgentHooks

class MyHooks(AgentHooks):
    async def on_tool_start(self, context, agent,tool):
        print(f"🛠 Tool started: {tool.name}")

    async def on_tool_end(self, context,agent, tool,result):
        print(f"📦 Tool finished: {tool.name}")  