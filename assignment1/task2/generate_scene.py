import os
from google import genai

# Establish connection with the Gemini Generative Engine
ai_engine_client = genai.Client()

# Core prompt configuration block mapped directly to project constraints
fourier_prompt = """
Write a complete, working Python script using the Manim Community library (`manim`).
The goal is to create a scene that visualizes Fourier Series Decomposition.

Requirements:
1. Demonstrate how a square wave is built up by summing sine harmonics.
2. Show at least the first 5 terms of the Fourier series.
3. Draw each individual wave component in a different color.
4. Show the cumulative sum updating step-by-step on screen.
5. Ensure appropriate use of axes, labels, a legend, and an on-screen title.

Return ONLY the raw executable Python code inside a single standard markdown code block. Do not include any extra introductory or concluding text.
"""

print("[API Query] Dispatching Fourier analysis criteria to Gemini models...")

# Execute text content request through the flash endpoint
model_callback = ai_engine_client.models.generate_content(
    model='gemini-2.5-flash',
    contents=fourier_prompt,
)

destination_path = "task2_fourier/fourier_series.py"
raw_callback_payload = model_callback.text

# Parsing logic to clean and pull code block fields cleanly
if "```python" in raw_callback_payload:
    extracted_source_block = raw_callback_payload.split("```python")[1].split("```")[0]
elif "```" in raw_callback_payload:
    extracted_source_block = raw_callback_payload.split("```")[1].split("```")[0]
else:
    extracted_source_block = raw_callback_payload

finalized_script_content = extracted_source_block.strip()

# Safely open system stream and sync file data buffer to drive
with open(destination_path, "w", encoding="utf-8") as disk_file:
    disk_file.write(finalized_script_content)

print(f"[Storage Log] Render logic stream saved at pipeline point: {destination_path}")
