# Auto-Anim Engine: LLM-Driven Mathematical Visualization & Analysis

## Project Overview
This repository explores the capabilities and limitations of automated code generation using large language models, specifically focusing on the Google Generative AI (Gemini) API. The core objective is to programmatically generate mathematical animations via Manim, execute them locally to identify syntax errors or architectural flaws, apply rigorous structural refactoring, and document the debugging pipeline.

The study centers on two foundational mathematical principles:
1. **The Pythagorean Theorem ($a^2 + b^2 = c^2$):** A geometric breakdown that constructs a right-angled triangle, dynamically labels its boundaries, and overlays filled boundary squares to visually validate area equivalence.
2. **Fourier Series Synthesis:** A dynamic plotting canvas illustrating the step-by-step assembly of a square wave by calculating and combining individual harmonic sine functions ($n=1, 3, 5, 7, 9$) with high-contrast color indexing.

---

## Directory Architecture
The workspace rejects a flat structure in favor of a highly modular, decoupled directory layout:

```text
manim-genai-assignment/
├── .gitignore                  # Exclusions for Python runtimes & virtual environments
├── requirements.txt            # System environment packages (manim, numpy, google-generativeai)
├── README.md                   # Core documentation & engineering post-mortem
├── task1_pythagoras/
│   ├── generate_scene.py       # API configuration & prompt engineering execution
│   └── pythagoras.py           # Refactored, production-ready Manim script
└── task2_fourier/
    ├── generate_scene.py       # API configuration & prompt engineering execution
    └── fourier_series.py       # Refactored, production-ready Manim script
Technical Installation & Setup
1. System Prerequisites
Verify that your host machine has the following dependencies configured globally:

Python Engine: Version 3.8 or higher.

FFmpeg Multimedia Framework: Mandatory for Manim's video encoding pipeline. Ensure its binary directory is added to your system's path variables.

LaTeX Toolkit (Optional): e.g., MiKTeX or MacTeX. Note: To ensure maximum portability and eliminate environmental runtime errors (such as WinError 2), all finalized code versions in this repo have been refactored to use standard text arrays instead of standard MathTex blocks.

2. Environment Deployment
Run the following commands in your terminal to clone the codebase and initialize an isolated execution environment:
# Clone project repository
git clone [https://github.com/YOUR_USERNAME/manim-genai-assignment.git](https://github.com/YOUR_USERNAME/manim-genai-assignment.git)
cd manim-genai-assignment

# Provision and activate virtual environment
python -m venv env

# Activation - Windows (PowerShell):
.\env\Scripts\activate

# Activation - macOS / Linux:
source env/bin/activate

# Install package dependencies
pip install -r requirements.txt
3. API Authentication
Before triggering the automated generation scripts, expose your Gemini API credentials to your shell session:

Windows (PowerShell):
$env:GEMINI_API_KEY="YOUR_ACTUAL_API_KEY_HERE"
macOS / Linux (Bash):
export GEMINI_API_KEY="YOUR_ACTUAL_API_KEY_HERE"
Execution Guide
To render the math animations at a low resolution for swift testing and validation, execute the following CLI commands:

Render Task 1 (Pythagorean Theorem):
manim -pql task1_pythagoras/pythagoras.py PythagorasScene
Render Task 2 (Fourier Series Decomposition):
manim -pql task2_fourier/fourier_series.py FourierSeries

Code Post-Mortem & Critical EvaluationTask 1: Geometric Proof of the Pythagorean TheoremEvaluating the raw code directly out of the generative model revealed five structural and logical vulnerabilities:Detected FlawOperational ImpactEngineering SolutionHardcoded LaTeX CompilationMathTex() calls triggered fatal WinError 2 on machines without local LaTeX installations.Replaced mathematical typesetting with native, highly portable Text() strings.Unfilled Geometry OutlinesThe model drew empty square perimeters, failing to convey the spatial concept of area equivalence.Applied explicit .set_fill(color, opacity=0.4) modifiers to all bounding polygons.Static Spatial CoordinatesPositional vectors were absolute arrays (e.g., [2, 1, 0]), causing label overlapping during scaling.Transitioned layout logic to relative hooks using anchor bindings like .next_to(triangle, LEFT).Zero Animation IntervalsThe script rendered visual components instantly without structural pauses, making the video unwatchable.Implemented strategic .wait(1.5) intervals following major presentation milestones.Viewport Layout CollisionsThe primary equation block overlapped the core triangle rendering region due to poor bounding box limits.Shifted formulas away from graphics layers using explicit boundary modifiers like .to_edge(UP, buff=0.5).

Task 2: Harmonic Fourier Series Synthesis
Compiling the raw output from the second model generation exposed severe syntax hallucinations and tracking deficiencies:

API Method Hallucination (Axes.to_center()): The model assumed a non-existent spatial centering function for the coordinate system, causing an immediate AttributeError crash.

Correction: Removed the invocation completely since Manim inherently centers newly instantiated coordinate frameworks around the global origin matrix [0,0,0].

Invalid Argument Chaining Syntax: The LLM attempted to pass positional arguments natively inside a spacing configuration block (term_text.next_to(..., align_to=LEFT)), throwing an unhandled TypeError.

Correction: Decoupled the instructions into two separate, syntactically legal method calls: .next_to(...).align_to(..., LEFT).

Implicit LaTeX Dependency Overhead: Standard axis utility methods like axes.get_x_axis_label() were deployed, which covertly trigger back-end LaTeX requirements.

Correction: Swapped out automated labels for manually initialized, vanilla Text() objects.

Lack of Explanatory Metadata/Index: Multiple harmonic frequency curves were rendered in different colors without an index, leaving the viewer unable to identify which curve matched which specific harmonic.

Correction: Built an on-screen telemetry dashboard (e.g., n = 1, Amp: 4/1π) whose text colors match the active curves.

Visual Artifact Accumulation: Iterative curve updates left older harmonic paths on the screen, cluttering the canvas and obscuring the final composite purple wave.

Correction: Added an explicit canvas cleanup phase using FadeOut(individual_graph) at the conclusion of each loop iteration.


