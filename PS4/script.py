from manim import *
import time
# x=[-7,7] y=[-4,4] 14x8
class Intro(Scene):
    def construct(self):
        lines = [
            "2. Consider points $A = (0,a)$ and $B = (1,b)$,",
            "where $a$ and $b$ are positive real numbers.",
            "We want to connect point $A$ to point $B$ with a path",
            "that also touches the $x$-axis at some point $C$.",
            "Let $O = (0,0)$ denote the origin.",
            "Prove that the shortest such path touches the $x$-axis at a point $C$",
            "such that $|\\angle ACO| + |\\angle BCO| = \\pi$."
        ]

        # Create a VGroup of Text or MathTex mobjects
        text_mobjects = VGroup()
        for line in lines:
            # Use MathTex for lines containing math, Text for plain text
            if "$" in line:
                mobj = Tex(line, font_size=22)
            else:
                mobj = Text(line, font_size=22)
            text_mobjects.add(mobj)

        # Arrange lines vertically, aligned left
        text_mobjects.arrange(DOWN, aligned_edge=LEFT)

        # Optional: center the whole block on screen
        text_mobjects.move_to(ORIGIN)

        # Reveal each line slowly
        for line_mobj in text_mobjects:
            self.play(Write(line_mobj, shift=UP), run_time=2.0)
        


class Body(Scene):
    def construct(self):

        a=ValueTracker(4)
        b=ValueTracker(2)
        c=ValueTracker(0.5)
        plane = NumberPlane(
            x_range=[-0.5, 3, 1], 
            y_range=[-0.5, 5, 1],
            x_length=7,         
            y_length=7,
            axis_config={
                "include_tip": True,
                "tip_length": 0.1
            },
            background_line_style={
                "stroke_color": BLUE,
                "stroke_opacity": 0.5,
                "stroke_width": 2
            }
        )
        dot_a = always_redraw(lambda : Dot(plane.coords_to_point(0,a.get_value()),color=RED))
        l_a = always_redraw(lambda : MathTex("(0,a)", font_size=28).next_to(dot_a,UL))
        label_a = always_redraw(lambda : MathTex(f"(0,{a.get_value():.1f})", font_size=28).next_to(dot_a,UL))
        dot_b = always_redraw(lambda : Dot(plane.coords_to_point(1,b.get_value()),color=YELLOW))
        l_b = always_redraw(lambda : MathTex("(1,b)", font_size=28).next_to(dot_b,UL))
        label_b = always_redraw(lambda : MathTex(f"(1,{b.get_value():.1f})", font_size=28).next_to(dot_b,UL))
        dot_c = always_redraw(lambda : Dot(plane.coords_to_point(c.get_value(),0),color=GREEN))
        l_c = always_redraw(lambda : MathTex("(c,0)", font_size=28).next_to(dot_c,UL))
        label_c = always_redraw(lambda : MathTex(f"({c.get_value():.2f},0)", font_size=28).next_to(dot_c,UL))


        plane.add_coordinates(font_size=32)

        self.play(DrawBorderThenFill(plane,run_time=2))
        #draw points + labels a and b
        self.play(DrawBorderThenFill(VGroup(dot_a,dot_b,l_a,l_b)))
        self.play(ReplacementTransform(l_a, label_a), ReplacementTransform(l_b, label_b))
        #move the points around
        self.play(a.animate.set_value(1), b.animate.set_value(3), run_time=1)
        self.play(a.animate.set_value(3), b.animate.set_value(1.5), run_time=1)
        #turn back to a and b form
        l_a.update()
        l_b.update()
        self.play(ReplacementTransform(label_a,l_a), ReplacementTransform(label_b,l_b))
        #add the point c + connect lines + move it around
        self.play(DrawBorderThenFill(VGroup(dot_c,l_c)))
        line_1 = always_redraw(lambda :
            Line(dot_a.get_center(),dot_c.get_center(),stroke_width=2)
            )
        line_2 = always_redraw(lambda : 
            Line(dot_c.get_center(),dot_b.get_center(),stroke_width=2)
            )
        self.play(DrawBorderThenFill(VGroup(line_1, line_2)),ReplacementTransform(l_c,label_c))
        self.add(VGroup(dot_a,dot_b,dot_c))
        self.play(c.animate.set_value(0.75))
        self.play(c.animate.set_value(0.15))
        self.play(c.animate.set_value(0.50))
        l_c.update()
        self.play(ReplacementTransform(label_c, l_c))
        self.play(plane.animate.to_edge(LEFT))
        # write equations
        eq_1 = MathTex("L(c)","=","\sqrt{a^{2}+c^{2}}","+","\sqrt{b^{2}+(1-c)^{2}}", font_size=32)
        eq_1.move_to([4,3,0])
        self.play(DrawBorderThenFill(VGroup(eq_1[0], eq_1[1], eq_1[3])))
        self.play(line_1.animate.set_color(YELLOW), Wiggle(line_1, color=YELLOW, scale_value=1.5))
        self.play(TransformFromCopy(line_1, eq_1[2]), run_time=1.5)
        line_1.set_color(WHITE)
        self.play(line_2.animate.set_color(YELLOW), Wiggle(line_2, color=YELLOW, scale_value=1.5))
        self.play(TransformFromCopy(line_2, eq_1[4]), run_time=1.5)
        line_2.set_color(WHITE)
        self.play(Indicate(eq_1[0], scale_factor = 1.5))
        stuff_1 = Tex("a and b = constants, c = variable. We want to find $L'(c)=0$", font_size=20).move_to([3.7,2.2,0])
        self.play(Write(stuff_1, run_time=3))

        eq_2 = MathTex(
            r"L'(c)", "=",
            r"\frac{1}{2}(",    
            "a",           
            r"^{2}+",            
            "c",               
            r"^{2})^{-1/2}\cdot(2",  
            "c",                 
            r")", 

            "+",

            r"\frac{1}{2}(",  
            "b",              
            r"^{2}+(1-",   
            "c",               
            r")^{2})^{-1/2}\cdot (-2)",
            r"(1-c)",                          
            font_size=22
        )
        eq_2.move_to([3.7,1.4,0])
        zero = MathTex("0").move_to(eq_2[0])
        self.play(TransformFromCopy(eq_1, eq_2), run_time=2)
        self.play(ReplacementTransform(eq_2[0], zero, run_time=2))
        eq_3 = MathTex(r"0=\frac{c}{\sqrt{a^{2}+c^{2}}} - \frac{1-c}{\sqrt{b^{2}+(1-c)^{2}}}", font_size=22).move_to([3.7,0.8,0])
        self.play(TransformFromCopy(eq_2,eq_3, run_time=2))
        eq_4 = MathTex(r"(1 - c)^{2}(a^{2} + c^{2}) = c^{2}(b^{2} + (1 - c)^{2})", font_size=22).move_to([3.7,0.2,0])
        self.play(TransformFromCopy(eq_3,eq_4, run_time=2))
        eq_5 = MathTex(r"a-ac=bc", font_size=22).move_to([3.7,-0.4,0])
        self.play(TransformFromCopy(eq_4,eq_5, run_time=2))
        eq_6 = MathTex(r"c=\frac{a}{a+b}", font_size=22).move_to([3.7,-1,0])
        self.play(TransformFromCopy(eq_5,eq_6, run_time=2))

        self.wait()

class Angles(Scene):
    def construct(self):
        eq_1 = MathTex(
            r"\left| \angle ACO \right|",
            r" = \tan\!\left( \frac{a}{\frac{a}{a+b}} \right)",
            font_size=25
        ).move_to([0, 3, 0])
        eq_2 = MathTex(
            r"=\tan(a+b)",
            font_size=25
        ).move_to([0.5, 2.1, 0])
        self.play(Write(eq_1))
        self.play(TransformFromCopy(eq_1[1], eq_2))

        eq_3 = MathTex(
            r"\left| \angle BCM \right|",
            r" = \tan\!\left( \frac{b}{1 - \frac{a}{a+b}} \right)",
            font_size=25
        ).move_to([0, 0.5, 0])
        eq_4 = MathTex(
            r"=\tan(a+b)",
            font_size=25
        ).move_to([0.4, -0.4, 0])
        self.play(Write(eq_3))
        self.play(TransformFromCopy(eq_3[1], eq_4))

        eq_5 = Tex(
            r"Since $|\angle ACO| = |\angle BCM|$ and $|\angle BCM| + |\angle BCO| = \pi$",
            font_size=25
        ).move_to([0.4, -1.5, 0])
        eq_6 = Tex(
            r"Therefore, $|\angle ACO | + |\angle BCO | = \pi$",
            font_size=25
        ).move_to([0.4, -2.2, 0])
        self.play(Write(eq_5))
        self.play(Write(eq_6))
        
        
        self.wait()






