from manim import *


class line(Scene):
    def construct(self):
        # Белый фон
        self.camera.background_color = rgb_to_color([248,249,250])

        # Первая прямая (наклонная)
        line1_start = Dot(point=[-2, -1, 0], color=BLACK)
        line1_end = Dot(point=[2, 1, 0], color=BLACK)
        line1 = Line(line1_start.get_center(), line1_end.get_center(), color=BLACK)

        # Вторая прямая (другая наклонная)
        line2_start = Dot(point=[-1, -2, 0], color=BLACK)
        line2_end = Dot(point=[1, 2, 0], color=BLACK)
        line2 = Line(line2_start.get_center(), line2_end.get_center(), color=BLACK)

        # Точка пересечения
        intersection = Dot(point=[0, 0, 0], color=PURPLE)

        # Черные подписи
        label1_start = Text("A", font_size=24, color=BLACK).next_to(line1_start, LEFT + DOWN)
        label1_end = Text("B", font_size=24, color=BLACK).next_to(line1_end, RIGHT + UP)
        label2_start = Text("C", font_size=24, color=BLACK).next_to(line2_start, LEFT + DOWN)
        label2_end = Text("D", font_size=24, color=BLACK).next_to(line2_end, RIGHT + UP)
        label_int = Text("O", font_size=24, color=BLACK).next_to(intersection, DOWN)

        # Плоскость строится так, чтобы ее края проходили через концы прямых
        # Используем концы прямых как углы плоскости
        plane = Polygon(
            line1_start.get_center(),  # A
            line1_end.get_center(),  # B
            line2_end.get_center(),  # D
            line2_start.get_center(),  # C
            color=BLUE,
            fill_opacity=0.3,
            stroke_width=0
        )

        # Анимация
        # Первая прямая
        self.play(Create(line1_start), Create(line1_end))
        self.play(Create(line1))
        self.play(Write(label1_start), Write(label1_end))

        # Вторая прямая
        self.play(Create(line2_start), Create(line2_end))
        self.play(Create(line2))
        self.play(Write(label2_start), Write(label2_end))

        # Точка пересечения
        self.play(Create(intersection))
        self.play(Write(label_int))

        # Плоскость
        self.wait(0.5)
        self.play(Create(plane))
        self.wait(2)
