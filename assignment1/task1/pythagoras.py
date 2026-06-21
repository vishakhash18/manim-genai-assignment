from manim import *

class GeometricPythagoras(Scene):
    def construct(self):
        # --- 1. Coordinate Setup for Right-Angled Geometry ---
        # Shifted origin points slightly to randomize vector parameters
        pt_origin = LEFT * 0.5 + DOWN * 0.5
        pt_base = pt_origin + RIGHT * 4
        pt_height = pt_origin + UP * 3

        # --- 2. Construct Vector Bound Elements ---
        edge_base = Line(pt_origin, pt_base, color=BLUE)
        edge_height = Line(pt_origin, pt_height, color=RED)
        edge_hypot = Line(pt_height, pt_base, color=GREEN)

        # Main shape polygon definition
        core_triangle = Polygon(pt_origin, pt_base, pt_height, stroke_width=2.5, fill_opacity=0.15, fill_color=GRAY)

        # Structural layout tracking indicator for right angle
        perpendicular_bracket = RightAngle(edge_base, edge_height, length=0.35, color=YELLOW)

        # --- 3. Text Representation Assets (Bypassing external LaTeX dependencies) ---
        side_label_a = Text("a", color=RED).next_to(edge_height, LEFT, buff=0.25)
        side_label_b = Text("b", color=BLUE).next_to(edge_base, DOWN, buff=0.25)
        side_label_c = Text("c", color=GREEN).next_to(edge_hypot, UR, buff=0.15)

        # --- 4. Render Layout Boundary Squares ---
        # Base tracking boundary shape (b)
        poly_square_b = Square(side_length=4, stroke_color=BLUE, fill_color=BLUE, fill_opacity=0.25)
        poly_square_b.next_to(edge_base, DOWN, buff=0)

        # Vertical tracking boundary shape (a)
        poly_square_a = Square(side_length=3, stroke_color=RED, fill_color=RED, fill_opacity=0.25)
        poly_square_a.next_to(edge_height, LEFT, buff=0)

        # Hypotenuse tracking boundary shape (c)
        poly_square_c = Square(side_length=5, stroke_color=GREEN, fill_color=GREEN, fill_opacity=0.25)
        inclination_theta = edge_hypot.get_angle()
        poly_square_c.rotate(inclination_theta)
        
        # Position mapping using math coordinates translation vector calculation
        poly_square_c.move_to(edge_hypot.get_center()).shift(UP * 1.2 + RIGHT * 1.6)

        # --- 5. Mathematical Identity Banner ---
        theorem_banner = Text("a² + b² = c²", t2c={"a²": RED, "b²": BLUE, "c²": GREEN})
        theorem_banner.to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.5)

        # --- 6. Execution Runtime Timeline ---
        # Display heading banner
        self.play(Write(theorem_banner))
        self.wait(0.4)

        # Generate core geometry and reference components simultaneously
        self.play(
            Create(core_triangle), 
            Create(perpendicular_bracket),
            run_time=1.2
        )
        
        # Animate annotations together
        self.play(
            Write(side_label_a), 
            Write(side_label_b), 
            Write(side_label_c)
        )
        self.wait(0.8)

        # Sequential area representation animation
        self.play(FadeIn(poly_square_a, shift=LEFT), run_time=1.2)
        self.play(FadeIn(poly_square_b, shift=DOWN), run_time=1.2)
        self.play(FadeIn(poly_square_c, shift=UR), run_time=1.4)
        
        self.wait(2.5)
