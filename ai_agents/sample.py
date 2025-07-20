import asyncio
try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

import os
from dotenv import load_dotenv

# Semantic Kernel imports
from semantic_kernel import Kernel
from semantic_kernel.agents import Agent, ChatCompletionAgent, ChatHistoryAgentThread
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.open_ai import AzureChatPromptExecutionSettings
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.contents import ChatMessageContent, TextContent, ImageContent
from semantic_kernel.contents.utils.author_role import AuthorRole
from semantic_kernel.functions import kernel_function



class RestaurantMenuPlugin:
    """A plugin that provides restaurant menu information."""

    @kernel_function(description="Get today's special menu items.")
    def get_specials(self) -> Annotated[str, "Returns today's special menu items."]:
        return """
        🍲 Special Soup: Clam Chowder
        🥗 Special Salad: Caesar Salad with Grilled Chicken
        🍹 Special Drink: Fresh Mint Lemonade
        🍰 Special Dessert: Chocolate Lava Cake
        """

    @kernel_function(description="Get the price of a specific menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        # In a real application, this would query a database
        prices = {
            "clam chowder": "$12.99",
            "caesar salad": "$14.99",
            "mint lemonade": "$4.99",
            "chocolate lava cake": "$8.99"
        }
        
        item_key = menu_item.lower()
        return prices.get(item_key, "$9.99")  # Default price

    @kernel_function(description="Check if a menu item is available.")
    def check_availability(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns availability status."]:
        # Simulate checking availability
        available_items = ["clam chowder", "caesar salad", "mint lemonade", "chocolate lava cake"]
        item_key = menu_item.lower()
        
        if item_key in available_items:
            return f"✅ {menu_item} is available!"
        else:
            return f"❌ {menu_item} is not available today."


async def main() -> None:
    # Kernel can be used to share any plugin between any agent.
    # Globally register the plugins
    kernel = Kernel()

    # Chat completion
    chat_completion = AzureChatCompletion(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    )

    # add the service to kernel
    kernel.add_service(chat_completion)

    kernel.add_plugin(
        RestaurantMenuPlugin,
        plugin_name="Resturant",
    )

    # Create execution settings (optional - for controlling temperature, max tokens, etc.)
    execution_settings = AzureChatPromptExecutionSettings(
        max_completion_tokens=2000
    )
    execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

    # Create a simple chat history
    chat_history = ChatHistory()

    user_input = None
    while True:
        
        user_input = input("User > ")

        if user_input == "exit":
            break

        chat_history.add_user_message(user_input)

        # Get a response from the AI
        response = await chat_completion.get_chat_message_content(
            chat_history=chat_history, 
            settings=execution_settings,
            kernel=kernel
        )

        print(f"AI Response: {response.content}")

        chat_history.add_message(response)


if __name__ == '__main__':
    asyncio.run(main())