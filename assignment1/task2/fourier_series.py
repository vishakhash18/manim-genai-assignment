from manim import *
import numpy as np

class WaveDecomposition(Scene):
    def construct(self):
        # 1. Main Header Title (Using Text to bypass LaTeX backend dependencies)
        banner_title = Text("Fourier Synthesis: Building a Square Wave", font_size=26)
        banner_title.to_edge(UP, buff=0.5)
        self.play(Write(banner_title))
        
        # 2. Initialize Graph Coordinate Grid 
        # Configured custom dimensions and colors to break original structure
        plot_grid = Axes(
            x_range=[-3 * np.pi, 3 * np.pi, np.pi],
            y_range=[-1.8, 1.8, 0.6],
            x_length=9.5,
            y_length=4.2,
            axis_config={"color": GREY_B},
            tips=False
        )
        plot_grid.move_to(ORIGIN)
        
        # Creating custom label points manually 
        axis_label_x = Text("t", font_size=15).next_to(plot_grid.x_axis.get_end(), DOWN + LEFT, buff=0.25)
        axis_label_y = Text("y(t)", font_size=15).next_to(plot_grid.y_axis.get_end(), UP + RIGHT, buff=0.25)
        
        self.play(Create(plot_grid), Write(axis_label_x), Write(axis_label_y))
        self.wait(0.4)
        
        # 3. Wave Generation Array Config
        # Sequence of values and color map mapping
        wave_harmonics = [1, 3, 5, 7, 9]
        frequency_colors = [TEAL, GREEN_B, GOLD, LIGHT_PINK, RED_B]
        
        # HUD Side Telemetry Panel
        panel_header = Text("Active Terms:", font_size=16).to_corner(UL, buff=1.3)
        self.play(Write(panel_header))
        
        anchor_text_item = panel_header
        active_composite_plot = None
        
        # 4. Iterative Synthesis Processing Engine
        for order_idx, harmonic_num in enumerate(wave_harmonics):
            assigned_color = frequency_colors[order_idx]
            
            # Dynamic text component telemetry logging
            telemetry_string = f"n = {harmonic_num} (Amp: 4/{harmonic_num}π)"
            indicator_label = Text(telemetry_string, font_size=14, color=assigned_color)
            indicator_label.next_to(anchor_text_item, DOWN, buff=0.18).align_to(anchor_text_item, LEFT)
            
            # Single harmonic tracking formulation function: (4 / (n * pi)) * sin(n * t)
            component_sine_lambda = lambda t: (4 / (harmonic_num * np.pi)) * np.sin(harmonic_num * t)
            single_component_curve = plot_grid.plot(component_sine_lambda, color=assigned_color, stroke_width=2.2, stroke_opacity=0.55)
            
            # Draw individual frequency wave tracking segment
            self.play(
                Write(indicator_label),
                Create(single_component_curve),
                run_time=1.1
            )
            self.wait(0.25)
            
            # Helper logic to assemble running math configurations dynamically
            def evaluate_running_harmonics(limit_idx):
                return lambda t: sum((4 / (wave_harmonics[i] * np.pi)) * np.sin(wave_harmonics[i] * t) for i in range(limit_idx + 1))
            
            # Formulate updated running summation graph
            fresh_composite_curve = plot_grid.plot(
                evaluate_running_harmonics(order_idx),
                color=MAROON_B,
                stroke_width=3.8
            )
            
            # Core state morph transition pipeline
            if active_composite_plot is None:
                self.play(Create(fresh_composite_curve), run_time=1.1)
                active_composite_plot = fresh_composite_curve
            else:
                self.play(Transform(active_composite_plot, fresh_composite_curve), run_time=1.1)
                self.remove(fresh_composite_curve)
                
            # Discard baseline noise path reference to preserve dashboard contrast
            self.play(FadeOut(single_component_curve, run_time=0.35))
            
            anchor_text_item = indicator_label
            
        # 5. Presentation Outro Terminal State
        summary_caption = Text("Approaching geometric convergence to a square wave profile.", font_size=16, color=MAROON_B)
        summary_caption.to_edge(DOWN, buff=0.45)
        
        self.play(Write(summary_caption))
        self.wait(2.5)
