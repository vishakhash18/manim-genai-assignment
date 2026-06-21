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

```

## Code Post-Mortem & Critical Evaluation

### Task 1: Geometric Proof of the Pythagorean Theorem

Evaluating the raw code directly out of the generative model revealed five structural and logical vulnerabilities:

| Detected Flaw | Operational Impact | Engineering Solution |
| :--- | :--- | :--- |
| **Hardcoded LaTeX Compilation** | `MathTex()` calls triggered fatal `WinError 2` on machines without local LaTeX installations. | Replaced mathematical typesetting with native, highly portable `Text()` strings. |
| **Unfilled Geometry Outlines** | The model drew empty square perimeters, failing to convey the spatial concept of area equivalence. | Applied explicit `.set_fill(color, opacity=0.4)` modifiers to all bounding polygons. |
| **Static Spatial Coordinates** | Positional vectors were absolute arrays (e.g., `[2, 1, 0]`), causing label overlapping during scaling. | Transitioned layout logic to relative hooks using anchor bindings like `.next_to(triangle, LEFT)`. |
| **Zero Animation Intervals** | The script rendered visual components instantly without structural pauses, making the video unwatchable. | Implemented strategic `.wait(1.5)` intervals following major presentation milestones. |
| **Viewport Layout Collisions** | The primary equation block overlapped the core triangle rendering region due to poor bounding box limits. | Shifted formulas away from graphics layers using explicit boundary modifiers like `.to_edge(UP, buff=0.5)`. |

---

### Task 2: Visualisation of Fourier Series Decomposition

Running the generated Fourier scene exposed critical API syntax hallucinations and readability constraints:

| Detected Flaw | Operational Impact | Engineering Solution |
| :--- | :--- | :--- |
| **API Method Hallucination (`Axes.to_center()`)** | The model assumed a non-existent spatial centering function, causing an immediate `AttributeError` crash. | Removed the invocation completely since Manim inherently centers newly instantiated coordinate frameworks around `[0,0,0]`. |
| **Invalid Argument Chaining Syntax** | Attempted to pass positional arguments natively inside a spacing block (`term_text.next_to(..., align_to=LEFT)`), throwing a `TypeError`. | Decoupled the instructions into two separate, syntactically legal method calls: `.next_to(...).align_to(..., LEFT)`. |
| **Implicit LaTeX Dependency Overhead** | Standard axis utilities like `axes.get_x_axis_label()` were deployed, which covertly trigger back-end LaTeX requirements. | Swapped out automated labels for manually initialized, vanilla `Text()` objects. |
| **Lack of Explanatory Metadata/Index** | Multiple harmonic curves were rendered in different colors without an index, leaving the viewer unable to identify wave properties. | Built an on-screen telemetry dashboard (e.g., `n = 1, Amp: 4/1π`) whose text colors precisely match the active curves. |
| **Visual Artifact Accumulation** | Iterative curve updates left older harmonic paths on the screen, cluttering the canvas and obscuring the final composite wave. | Added an explicit canvas cleanup phase using `FadeOut(individual_graph)` at the conclusion of each loop iteration. |



