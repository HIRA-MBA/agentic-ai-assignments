from agents import AgentHooks,RunContextWrapper

class MyAgentHooks(AgentHooks):
    async def on_tool_start(
        self, context: RunContextWrapper, agent, tool
    ) -> None:
        print(f"🛠 Tool started: {tool.name}")

    async def on_tool_end(
        self, context: RunContextWrapper, agent , tool, output
    ) -> None:
        print(f"✅ Tool finished: {tool.name}, output={output}")