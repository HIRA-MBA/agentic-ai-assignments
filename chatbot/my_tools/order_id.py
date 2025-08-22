
from agents import FunctionTool
import random
from pydantic import BaseModel, Field, ValidationError

STATUSES = ["Order placed", "Shipped", "In transit", "Out for delivery", "Delivered"]

class OrderID(BaseModel):
    # Enforce range right in the schema: 100–1000 inclusive
    order_id: int = Field(..., ge=100, le=1000)

async def get_order_status_func(ctx, args: str):
    """
    args is a JSON string the model passes per the schema.
    Example: '{"order_id": 145}'
    """
    try:
        obj = OrderID.model_validate_json(args)
    except ValidationError:
        return {
            "valid": False,
            "error": "Please provide a numeric order ID between 100 and 1000 (e.g., {\"order_id\": 145})."
        }

    return {
        "valid": True,
        "order_id": obj.order_id,
        "status": random.choice(STATUSES)
    }

get_order_status = FunctionTool(
    name="get_order_status",
    description="Return shipping status for a valid order_id (100–1000).",
    params_json_schema=OrderID.model_json_schema(),
    on_invoke_tool=get_order_status_func,
    # ⛔️ Do NOT gate this tool on context; let the model pass args directly.
    # is_enabled is omitted so the tool is always callable by the agent that owns it.
)


