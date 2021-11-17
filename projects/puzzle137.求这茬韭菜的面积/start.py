from manimlib import *

COLOR1 = '#75cfb8'  # 蓝绿色
COLOR2 = '#bbdfc8'  # 浅绿色
COLOR3 = '#f0e5d8'  # 灰色
COLOR4 = '#ffc478'  # 橘黄色


def logo(scene):
    img = ImageMobject('./assets/logo.jpg').scale(0.3)
    scene.add(img)
    img.add_updater(lambda x:
                    # scale = scene.camera.frame.get_width()*0.2/
                    x.move_to(
                        scene.camera.frame.get_width() / 2 * RIGHT + scene.camera.frame.get_height() / 2 * UP)
                    .shift(2.4 * LEFT + 0.8 * DOWN)
                    )


class Scene1(Scene):

    def construct(self):
        logo(self)
        rect = Rectangle(width=6, height=4, stroke_color=BLACK)
        line1 = Line(start=[-1, -2, 0], end=[-1, 2, 0], stroke_color=BLACK)
        line2 = Line(start=[1, -2, 0], end=[1, 2, 0], stroke_color=BLACK)
        group1 = VGroup(rect, line1, line2)
        self.add(group1)
        self.wait(1)

        # # 所求图形
        # poly1 = VMobject(fill_color=COLOR4,fill_opacity=0.8)
        # poly1.append_points(Line(end=[1,-2,0], start=[3,-2,0]).get_points())
        # poly1.append_points(Arc(angle=PI/2, arc_center=[-3,-2,0],radius=4).get_points())
        # poly1.append_points(Line(start=[-3,2,0], end=[-1,2,0]).get_points())
        # poly1.append_points(Arc(angle=-PI/2, start_angle=PI/2, arc_center=[-1,-2,0],radius=4).get_points())
        # self.play(FadeIn(poly1))

        # 分割部分
        poly2 = VMobject(fill_color=COLOR1, fill_opacity=0.8, stroke_color=COLOR1)
        poly2.append_points(Line(start=[-3, 2, 0], end=[-1, 2, 0]).get_points())
        poly2.append_points(Line(start=[-1, 2, 0], end=[-1, 2 - (4 - 2 * np.sqrt(3)), 0]).get_points())
        poly2.append_points(Arc(angle=PI / 6, start_angle=PI / 3, arc_center=[-3, -2, 0], radius=4).get_points())

        poly3 = VMobject(fill_color=COLOR1, fill_opacity=0.8, stroke_color=COLOR1)
        poly3.append_points(Line(start=[-1, 2 - (4 - 2 * np.sqrt(3)), 0], end=[-1, 2, 0]).get_points())
        poly3.append_points(Arc(angle=-PI / 6, start_angle=PI / 2, arc_center=[-1, -2, 0], radius=4).get_points())
        poly3.append_points(Line(start=[1, 2 - (4 - 2 * np.sqrt(3)), 0], end=[1, -2, 0]).get_points())
        poly3.append_points(Arc(angle=PI / 3, arc_center=[-3, -2, 0], radius=4).get_points())

        poly4 = VMobject(fill_color=COLOR1, fill_opacity=0.8, stroke_color=COLOR1)
        poly4.append_points(Line(start=[1, -2, 0], end=[3, -2, 0]).get_points())
        poly4.append_points(Arc(angle=PI / 3, arc_center=[-1, -2, 0], radius=4).get_points())
        poly4.append_points(Line(start=[1, 2 - (4 - 2 * np.sqrt(3)), 0], end=[1, -2, 0]).get_points())

        self.play(AnimationGroup(
            FadeIn(poly2),
            FadeIn(poly3),
            FadeIn(poly4)
        ))
        self.wait(3)

        self.play(AnimationGroup(
            poly2.animate.shift(RIGHT * 2),
            poly4.animate.shift(LEFT * 2)
        ))

        self.wait(3)
