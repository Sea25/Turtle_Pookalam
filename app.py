from flask import Flask, Response
from flask_cors import CORS
from svg_turtle import SvgTurtle

app = Flask(__name__)
CORS(app)

def draw_pookalam_svg() -> str:
    t = SvgTurtle(width=800, height=800)
    t.speed(0)

    def filled_circle(r, color):
        t.penup()
        t.goto(0, -r)
        t.setheading(0)
        t.pendown()
        t.color(color, color)
        t.begin_fill()
        t.circle(r)
        t.end_fill()

    def ring(outer, inner, color):
        filled_circle(outer, color)
        if inner > 0:
            filled_circle(inner, "#ffffff")

    def petal_ring(center_r, arc_r, count, color, extent=90):
        t.color(color, color)
        for i in range(count):
            t.penup()
            t.home()
            t.setheading(i * (360 / count))
            t.forward(center_r)
            t.pendown()
            t.begin_fill()
            t.left(90)
            t.circle(arc_r, extent)
            t.left(180 - extent)
            t.circle(arc_r, extent)
            t.end_fill()

    # 🌸 Pookalam layers
    filled_circle(360, "#FEF3C7")  # base
    ring(300, 260, "#FDE68A")
    petal_ring(260, 80, 18, "#FCA5A5", 80)
    ring(220, 180, "#FDBA74")
    petal_ring(180, 60, 24, "#FBBF24", 80)
    ring(150, 120, "#86EFAC")
    petal_ring(120, 40, 24, "#60A5FA", 90)
    ring(95, 70, "#D8B4FE")
    filled_circle(55, "#F43F5E")  # center

    # ✅ FIX: use to_svg()
    svg = t.to_svg()
    return svg

@app.get("/pookalam.svg")
def pookalam_svg():
    svg = draw_pookalam_svg()
    return Response(svg, mimetype="image/svg+xml")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
