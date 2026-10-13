# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wanderlust Travel Concierge Agent definition."""

from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.apps import App
from google.adk.models import Gemini
from google.adk.tools.preload_memory_tool import PreloadMemoryTool
from google.genai import types

from .a2ui_utils import a2ui_callback
from .tools import (
    search_destinations,
    get_destination_details,
    calculate_trip_budget,
    get_weather_and_packing_tips,
)

MODEL = "gemini-3.8-flash"

SYSTEM_INSTRUCTION = """You are Wanderlust Concierge, an expert travel designer and trip planning AI assistant.
Your mission is to help travelers discover extraordinary destinations, design curated day-by-day itineraries, estimate transparent trip budgets, and prepare for seamless journeys.

Guidelines:
1. When asked for recommendations, always use `search_destinations` or `get_destination_details` to retrieve accurate catalog details.
2. When asked about costs, use `calculate_trip_budget` to compute accurate lodging, daily living, and airfare costs.
3. When asked for packing or climate advice, use `get_weather_and_packing_tips`.
4. Be engaging, inspiring, and concise. Provide actionable advice tailored to the user's travel style (adventure, cultural, luxury, budget, relaxation).
5. Remember user preferences, past trips, dietary restrictions, and budget constraints across sessions to personalize all recommendations.
"""


# WRITE: After each turn, send the session to Vertex AI Memory Bank for durable memory extraction
async def generate_memories_callback(callback_context: CallbackContext):
    await callback_context.add_session_to_memory()
    return None


root_agent = Agent(
    name="wanderlust_agent",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=SYSTEM_INSTRUCTION,
    tools=[
        PreloadMemoryTool(),
        search_destinations,
        get_destination_details,
        calculate_trip_budget,
        get_weather_and_packing_tips,
    ],
    after_model_callback=a2ui_callback,
    after_agent_callback=generate_memories_callback,
)

app = App(
    root_agent=root_agent,
    name="app",
)

