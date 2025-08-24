from agents import AgentHooks

class MyAgentHooks(AgentHooks):

 
    async def on_tool_start(self, tool_context, agent,func_tool):
        print(f"🔍 Tool starting: {func_tool.name} ")
    
    