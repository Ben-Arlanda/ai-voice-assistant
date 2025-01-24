import enum  # Provides support for enumerations, which are used for defining distinct constants
from typing import Annotated  
from livekit.agents import llm  
import logging  
# Configure the logger for the temperature control module
logger = logging.getLogger("temperature-control")
logger.setLevel(logging.INFO)  # Set the logging level to INFO

# Define a Zone enumeration to represent different areas of the house
class Zone(enum.Enum):
    LIVING_ROOM = "living_room"
    BEDROOM = "bedroom"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"

# Define a class for the assistant's temperature control functionality
class AssistantFnc(llm.FunctionContext):
    def __init__(self) -> None:
        super().__init__()  # Initialize the parent class

        # Initialize a dictionary to store default temperatures for each zone
        self._temperature = {
            Zone.LIVING_ROOM: 22,
            Zone.BEDROOM: 20,
            Zone.KITCHEN: 24,
            Zone.BATHROOM: 23,
            Zone.OFFICE: 21,
        }

    # Define an AI-callable function to get the temperature of a specific room
    @llm.ai_callable(description="get the temperature in a specific room")
    def get_temperature(
        self, zone: Annotated[Zone, llm.TypeInfo(description="The specific zone")]
    ):
        logger.info("get temp - zone %s", zone)  
        temp = self._temperature[Zone(zone)]  
        return f"The temperature in the {zone.value} is {temp}C"  

    # Define an AI-callable function to set the temperature of a specific room
    @llm.ai_callable(description="set the temperature in a specific room")
    def set_temperature(
        self,
        zone: Annotated[Zone, llm.TypeInfo(description="The specific zone")],
        temp: Annotated[int, llm.TypeInfo(description="The temperature to set")],
    ):
        logger.info("set temp - zone %s, temp: %s", zone, temp)  # Log the action for debugging
        self._temperature[Zone(zone)] = temp  # Update the temperature for the specified zone
        return f"The temperature in the {zone.value} is now {temp}C"  # Return a confirmation message