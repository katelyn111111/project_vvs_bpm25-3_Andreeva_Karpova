from manim import *


class point1(Scene):
    def construct(self):
        # Белый фон
        self.camera.background_color = rgb_to_color([248, 249, 250])

        # Создаем прямую (две точки)
        line_start = Dot(point=[-2, 0, 0], color=BLACK)
        line_end = Dot(point=[2, 0, 0], color=BLACK)
        line = Line(line_start.get_center(), line_end.get_center(), color=BLACK)

        # Точка не на прямой
        point = Dot(point=[0, 2, 0], color=BLACK)

        # Черные подписи
        label_start = Text("A", font_size=24, color=BLACK).next_to(line_start, DOWN)
        label_end = Text("B", font_size=24, color=BLACK).next_to(line_end, DOWN)
        label_point = Text("C", font_size=24, color=BLACK).next_to(point, UP)

        # Прямоугольная плоскость через прямую и точку
        # Используем точки прямой и точку для построения прямоугольника
        plane = Polygon(
            line_start.get_center(),  # A
            line_end.get_center(),  # B
            [2, 2, 0],  # Симметричная точка сверху справа
            [0, 2, 0],  # Точка C
            [-2, 2, 0],  # Симметричная точка сверху слева
            color=BLUE,
            fill_opacity=0.3,
            stroke_width=0
        )

        # Анимация
        self.play(Create(line_start), Create(line_end))
        self.play(Create(line))
        self.play(Write(label_start), Write(label_end))
        self.wait(0.3)
        self.play(Create(point))
        self.play(Write(label_point))
        self.wait(0.5)
        self.play(Create(plane))
        self.wait(2)
