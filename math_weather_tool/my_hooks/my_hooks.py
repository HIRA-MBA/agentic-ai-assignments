from agents import AgentHooks,RunContextWrapper,Agent,Tool

class Hooks(AgentHooks):

    async def on_tool_start(self, context: RunContextWrapper, agent: Agent, tool: Tool) -> None:
        print(f'{tool.name} starts')
