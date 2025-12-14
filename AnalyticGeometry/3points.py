from manim import *

class point(Scene):
    def construct(self):
        # Белый фон
        self.camera.background_color = rgb_to_color([248, 249, 250])

        # Создаем три точки для прямоугольной плоскости
        # Точки образуют прямоугольник
        point1 = Dot(point=[-2, 1.5, 0], color=BLACK)
        point2 = Dot(point=[2, 1.5, 0], color=BLACK)
        point3 = Dot(point=[2, -1.5, 0], color=BLACK)

        # Черные подписи точек
        label1 = Text("A", font_size=24, color=BLACK).next_to(point1, UP)
        label2 = Text("B", font_size=24, color=BLACK).next_to(point2, UP)
        label3 = Text("C", font_size=24, color=BLACK).next_to(point3, DOWN)

        # Прямоугольная плоскость через три точки
        # Четвертая точка для прямоугольника
        point4 = [-2, -1.5, 0]
        plane = Polygon(
            point1.get_center(),
            point2.get_center(),
            point3.get_center(),
            point4,
            color=BLUE,
            fill_opacity=0.3,
            stroke_width = 0
        )

        # Анимация
        self.play(Create(point1), Create(point2), Create(point3))
        self.play(Write(label1), Write(label2), Write(label3))
        self.wait(0.5)
        self.play(Create(plane))
        self.wait(2)

