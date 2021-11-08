from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square() # create a square
        square.rotate(PI /4)

        
        self.play(Create(square))  # show the circle on screen
        self.play(Transform(square,circle))
        self.play(FadeOut(square))  # fade out animation


class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)

        #self.add(numberplane, dot, arrow, origin_text, tip_text)
        self.play(Create(numberplane))
        self.play(Create(origin_text))
        self.play(Create(dot))
        self.play(Create(arrow))
        self.play(Create(tip_text))
        self.wait()

class VismoHouse(Scene):
    def construct(self):
        numberplane = NumberPlane()
        Ab = Dot([-3, 0, 0])
        Bb = Dot([3, 0, 0])
        Cb = Dot([3, 3, 0])
        Db = Dot([-3, 3, 0])
        lAB = Line(Ab,Bb)
        lBC = Line(Bb,Cb)
        lCD = Line(Cb,Db)
        lDA = Line(Db,Ab)


        self.play(Create(numberplane))
        self.play(Create(Ab))
        self.play(Create(Bb))
        self.play(Create(Cb))
        self.play(Create(Db))
        self.play(Create(lAB))
        self.play(Create(lBC))
        self.play(Create(lCD))
        self.play(Create(lDA))
        self.wait()
        