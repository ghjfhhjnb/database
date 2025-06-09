import turtle as t
import time
import math as m
import random as r

# 设置画布
t.setup(1.0,1.0)  # todo 此处可以设置窗体的大小比例
t.bgcolor('white')   # 设置背景色
t.title('生日快乐！！！')    # 设置窗口的标题

# todo 此处可以设置绘图速度
t.speed(10)  # 速度
t.delay(10)  # 延迟
# t.tracer(False)  # 一次性出图,便于调试程序使用
t.shape('turtle')  # 设置画笔的形状
# 称呼
t.penup()
t.goto(-500,250)
msg = '边庆羚'
for i in msg:
    t.color('green')
    t.write(i,True,align='left',font=('方正舒体',70,'normal'))
    time.sleep(0.3)
# 大熊
# 左耳
t.color('black')
t.penup()
t.goto(-150,200)
t.setheading(160)
t.begin_fill()
t.pendown()
t.circle(-30,230)
t.setheading(180)
t.circle(37,90)
t.end_fill()
# 右耳
t.penup()
t.goto(60,200)
t.setheading(20)
t.begin_fill()
t.pendown()
t.circle(30,230)
t.setheading(0)
t.circle(-37,90)
t.end_fill()
# 头
t.pensize(5)
t.penup()
t.goto(-113,237)
t.setheading(30)
t.pendown()
t.circle(-134,60)
t.penup()
t.goto(-150,200)
t.setheading(-120)
t.pendown()
t.circle(200,80)
t.penup()
t.goto(60,200)
t.setheading(-60)
t.pendown()
t.circle(-200,80)
t.penup()
t.setheading(210)
t.pendown()
t.circle(-120.60)
# 左眼
t.speed(10)
t.delay(1)
# 眼圈
t.penup()
t.goto(-140,100)
t.setheading(-45)
t.begin_fill()
t.pendown()
a = 0.2
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.1
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.1
        t.lt(3)
        t.fd(a)
t.end_fill()
# 眼白
t.fillcolor("white")
t.penup()
t.goto(-103,125)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(14,360)
t.end_fill()
# 眼珠
t.penup()
t.goto(-102,133)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(6,360)
t.end_fill()
# 右眼
# 眼圈
t.penup()
t.goto(50,100)
t.setheading(45)
t.fillcolor("black")
t.pencolor("black")
t.begin_fill()
t.pendown()
a = 0.2
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.1
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.1
        t.lt(3)
        t.fd(a)
t.end_fill()
# 眼白
t.fillcolor("white")
t.penup()
t.goto(13,125)
t.setheading(0)
t.begin_fill()
t.circle(14,360)
t.end_fill()
# 眼珠
t.penup()
t.goto(12,133)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(6,360)
t.end_fill()
# 鼻子
t.speed(2)
t.delay(2)
t.pencolor("black")
t.fillcolor("black")
t.penup()
t.goto(-55,133)
t.begin_fill()
t.pendown()
t.fd(20)
t.seth(-120)
t.fd(20)
t.end_fill()
# 嘴
t.penup()
t.goto(-70,110)
t.setheading(-30)
t.fillcolor("red")
t.begin_fill()
t.pendown()
t.circle(50,60)
t.setheading(-120)
t.circle(-100,15)
t.circle(-15,90)
t.circle(-100,15)
t.end_fill()
# 四肢
# 左臂
t.penup()
t.goto(-175, 100)
t.fillcolor("black")
t.begin_fill()
t.setheading(-120)
t.pendown()
t.fd(100)
t.setheading(-110)
t.circle(20, 180)
t.fd(30)
t.circle(-5, 160)
t.end_fill()
# 右臂
t.penup()
t.goto(85, 100)
t.setheading(60)
t.begin_fill()
t.pendown()
t.fd(100)
t.setheading(70)
t.circle(20, 180)
t.fd(30)
t.circle(-5, 160)
t.end_fill()
# 小红心
t.penup()
t.pencolor("red")
t.fillcolor('red')
t.goto(105, 200)
t.begin_fill()
t.pendown()
t.circle(-5, 180)
t.setheading(90)
t.circle(-5, 180)
t.setheading(-120)
t.fd(17)
t.penup()
t.goto(105, 200)
t.pendown()
t.setheading(-60)
t.fd(17)
t.end_fill()
t.pencolor("black")
t.fillcolor("black")
# 左腿
t.penup()
t.goto(-120, -45)
t.begin_fill()
t.pendown()
t.setheading(-90)
t.circle(-140, 20)
t.circle(5, 109)
t.fd(30)
t.circle(10, 120)
t.setheading(90)
t.circle(-140, 10)
t.end_fill()
# 右腿
t.penup()
t.goto(30, -45)
t.begin_fill()
t.pendown()
t.setheading(-90)
t.circle(140, 20)
t.circle(-5, 109)
t.fd(30)
t.circle(-10, 120)
t.setheading(90)
t.circle(140, 10)
t.end_fill()
# 冰糖外壳
t.pensize(3)
t.penup()
t.goto(-160, 195)
t.setheading(160)
t.pendown()
t.circle(-40, 230)
t.setheading(30)
t.circle(-134, 58)
t.setheading(60)
t.circle(-40, 215)
t.setheading(-60)
t.fd(15)
t.circle(2, 200)
t.setheading(65)
t.fd(30)
t.circle(-25, 180)
t.fd(100)
t.circle(2, 25)
t.circle(-200, 47)
t.circle(2, 60)
t.circle(140, 23)
t.circle(-2, 90)
t.setheading(180)
t.fd(70)
t.circle(-2, 90)
t.fd(30)
t.setheading(-160)
t.circle(-100, 35)
t.setheading(-90)
t.fd(30)
t.circle(-2, 90)
t.fd(70)
t.circle(-2, 90)
t.setheading(60)
t.circle(140, 30)
t.circle(2, 45)
t.circle(-200, 19)
t.circle(2, 130)
t.fd(30)
t.circle(-25, 180)
t.fd(100)
t.setheading(90)
t.circle(-200, 30)
# 冰糖面罩
t.speed(1)
t.delay(0)
t.pensize(3)
t.penup()
t.goto(65, 120)
t.setheading(90)
t.pendown()
t.pencolor("red")
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:  # 控制a的变化
        a = a + 0.25
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.25
        t.lt(3)
        t.fd(a)
t.pencolor("orange")
t.penup()
t.goto(66, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.255
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.255
        t.lt(3)
        t.fd(a)
t.pencolor("green")
t.penup()
t.goto(67, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.2555
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.2555
        t.lt(3)
        t.fd(a)
t.pencolor("deep sky blue")
t.penup()
t.goto(68, 120)
t.pendown()
a = 1
for i in range(120):
     if 0 <= i < 30 or 60 <= i < 90:
         a = a + 0.25955
         t.lt(3)
         t.fd(a)
     else:
         a = a - 0.25955
         t.lt(3)
         t.fd(a)
t.pencolor("pink")
t.penup()
t.goto(71, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.26
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.26
        t.lt(3)
        t.fd(a)
t.pencolor("purple")
t.penup()
t.goto(72, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.269
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.269
        t.lt(3)
        t.fd(a)
# 五环
t.penup()
t.goto(-55, -10)
t.pendown()
t.pencolor("blue")
t.circle(10)
t.penup()
t.goto(-40, -10)
t.pendown()
t.pencolor("black")
t.circle(10)
t.penup()
t.goto(-25, -10)
t.pendown()
t.pencolor("red")
t.circle(10)
t.penup()
t.goto(-50, -20)
t.pendown()
t.pencolor("yellow")
t.circle(10)
t.penup()
t.goto(-30, -20)
t.pendown()
t.pencolor("green")
t.circle(10)
# HappyBirthday
t.speed(2)
t.delay(2)


def move(angle, length):
    t.penup()
    t.seth(angle)
    t.fd(length)


# prepare
t.penup()
t.fd(-180)
t.seth(90)  # 画笔方向
# t.fd(50)
t.pendown()
t.pensize(10)
t.pencolor("green")
t.seth(0)
t.hideturtle()
t.speed(5)
# 呀
t.fd(100)
# 生
t.pencolor("green")
t.circle(50, 90)
t.circle(50, -30)
t.seth(0)
t.fd(100)
t.fd(-50)
t.left(90)
t.fd(30)
t.fd(-60)
t.left(90)
t.fd(50)
t.fd(-100)
t.fd(50)
t.left(90)
t.fd(50)
t.right(90)
t.fd(60)
t.fd(-120)
# 日
t.penup()
t.fd(-30)
t.pendown()
t.seth(90)
t.fd(100)
t.seth(0)
t.fd(70)
t.seth(-90)
t.fd(50)
t.seth(180)
t.fd(70)
t.seth(-90)
t.fd(50)
t.seth(0)
t.fd(70)
t.seth(90)
t.fd(50)
# 移动
move(0, 30)
# 快
t.pensize(8)
t.circle(30, 15)
t.pendown()
t.circle(30, 60)
t.penup()
t.seth(0)
t.fd(13)
t.seth(90)
t.pendown()
t.fd(40)
t.fd(-50)
t.penup()
t.seth(0)
t.fd(13)
t.pendown()
t.seth(-180)
t.circle(20, -90)
t.circle(20, 90)
t.penup()
t.fd(13)
t.pendown()
t.seth(-90)
t.fd(60)
move(0, 40)
move(90, 80)
t.pendown()
t.seth(0)
t.fd(30)
t.seth(90)
t.fd(30)
t.fd(-30)
t.seth(0)
t.fd(20)
t.seth(-90)
t.fd(35)
t.seth(0)
t.fd(10)
t.fd(-30)
t.seth(90)
t.fd(35)
t.fd(-35)
t.seth(0)
t.fd(-25)
move(-90, 50)
move(180, 25)
t.pendown()
t.seth(0)
t.penup()
t.circle(50, 20)
t.pendown()
t.circle(50, 70)
t.seth(-90)
t.circle(50, 60)
# 移动
move(0, 50)
move(90, 45)
# 乐
t.pensize(10)
t.pendown()
t.fd(40)
t.seth(0)
t.circle(50, 60)
t.circle(50, -25)
move(-90, 15)
t.pendown()
t.fd(30)
t.seth(0)
t.fd(-25)
t.fd(65)
t.fd(-40)
t.seth(-90)
t.fd(60)
t.seth(135)
t.fd(20)
move(135, 10)
t.pendown()
t.seth(-135)
t.fd(20)
move(0, 70)
t.pendown()
t.seth(135)
t.fd(20)
# 署名
t.penup()
t.goto(450, -350)
msg = '——小彭'  # todo 此处可以修改你的署名
for i in msg:
    t.color('green')
    t.write(i, True, align='left', font=('JetBrains Moon', 45, 'normal'))
    time.sleep(0.3)
t.clear()  # 清屏
time.sleep(3)  # 让程序休眠3秒，休息3秒后开始绘制生日蛋糕
# 开始绘制生日蛋糕
t.speed(2)
t.delay(0)


def drawx(a, i):
    angle = m.radians(i)
    return a * m.cos(angle)


def drawy(b, i):
    angle = m.radians(i)
    return b * m.sin(angle)


# 设置背景颜色，窗口位置以及大小
t.bgcolor("#d3dae8")
t.speed(10)
t.pensize(1)
t.penup()
t.goto(150, 0)
t.pendown()
# 1
t.pencolor("white")
t.begin_fill()
for i in range(360):
    x = drawx(150, i)
    y = drawy(60, i)
    t.goto(x, y)
t.fillcolor("#fef5f7")
t.end_fill()
# 2
t.begin_fill()
for i in range(180):
    x = drawx(150, -i)
    y = drawy(70, -i)
    t.goto(x, y)
for i in range(180, 360):
    x = drawx(150, i)
    y = drawy(60, i)
    t.goto(x, y)
t.fillcolor("#f2d7dd")
t.end_fill()
# 3
t.pu()
t.goto(120, 0)
t.pd()
t.begin_fill()
for i in range(360):
    x = drawx(120, i)
    y = drawy(48, i)
    t.goto(x, y)
t.fillcolor("#cbd9f9")
t.end_fill()
# 4
t.begin_fill()
t.pencolor("#fee48c")
for i in range(540):
    x = drawx(120, i)
    y = drawy(48, i) + 70
    t.goto(x, y)
t.goto(-120, 0)
t.fillcolor("#cbd9f9")
t.end_fill()
# 5
t.pu()
t.goto(120, 70)
t.pd()
t.pencolor("#fff0f3")
t.begin_fill()
for i in range(360):
    x = drawx(120, i)
    y = drawy(48, i) + 70
    t.goto(x, y)
t.fillcolor("#fff0f3")
t.end_fill()
# 6
t.pu()
t.goto(110, 70)
t.pd()
t.pencolor("#fff9fb")
t.begin_fill()
for i in range(360):
    x = drawx(110, i)
    y = drawy(44, i) + 70
    t.goto(x, y)
t.fillcolor("#fff9fb")
t.end_fill()
# 7
t.pu()
t.goto(120, 0)
t.pd()
t.begin_fill()
t.pencolor("#ffa79d")
for i in range(180):
    x = drawx(120, -i)
    y = drawy(48, -i) + 10
    t.goto(x, y)
t.goto(-120, 0)
for i in range(180, 360):
    x = drawx(120, i)
    y = drawy(48, i)
    t.goto(x, y)
t.fillcolor("#ffa79d")
t.end_fill()
# 8
t.pu()
t.goto(120, 70)
t.pd()
t.begin_fill()
t.pensize(4)
t.pencolor("#fff0f3")
for i in range(1800):
    x = drawx(120, 0.1 * i)
    y = drawy(-18, i) + 10
    t.goto(x, y)
t.goto(-120, 70)
t.pensize(1)
for i in range(180, 360):
    x = drawx(120, i)
    y = drawy(48, i) + 70
    t.goto(x, y)
t.fillcolor("#fff0f3")
t.end_fill()
# 9
t.pu()
t.goto(80, 70)
t.pd()
t.begin_fill()
t.pencolor("#6f3732")
t.goto(80, 120)
for i in range(180):
    x = drawx(80, i)
    y = drawy(32, i) + 120
    t.goto(x, y)
t.goto(-80, 70)
for i in range(180, 360):
    x = drawx(80, i)
    y = drawy(32, i) + 70
    t.goto(x, y)
t.fillcolor("#6f3732")
t.end_fill()
# 10
t.pu()
t.goto(80, 120)
t.pd()
t.pencolor("#ffaaa0")
t.begin_fill()
for i in range(360):
    x = drawx(80, i)
    y = drawy(32, i) + 120
    t.goto(x, y)
t.fillcolor("#ffaaa0")
t.end_fill()
# 11
t.pu()
t.goto(70, 120)
t.pd()
t.pencolor("#ffc3be")
t.begin_fill()
for i in range(360):
    x = drawx(70, i)
    y = drawy(28, i) + 120
    t.goto(x, y)
t.fillcolor("#ffc3be")
t.end_fill()
# 12
t.pu()
t.goto(80, 120)
t.pd()
t.begin_fill()
t.pensize(3)
t.pencolor("#ffaaa0")
for i in range(1800):
    x = drawx(80, 0.1 * i)
    y = drawy(-12, i) + 80
    t.goto(x, y)
t.goto(-80, 120)
t.pensize(1)
for i in range(180, 360):
    x = drawx(80, i)
    y = drawy(32, i) + 120
    t.goto(x, y)
t.fillcolor("#ffaaa0")
t.end_fill()
# 13
t.pu()
t.goto(64, 120)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawx(4, i) + 60
    y = drawy(1, i) + 120
    t.goto(x, y)
t.goto(64, 170)
for i in range(540):
    x = drawx(4, i) + 60
    y = drawy(1, i) + 170
    t.goto(x, y)
t.goto(56, 120)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(64, 120 + 10 * i)
    t.pu()
    t.goto(56, 120 + 10 * i)
    t.pd()
t.pu()
t.goto(60, 170)
t.pd()
t.goto(60, 180)
t.pensize(1)
#
t.pu()
t.goto(64, 190)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawx(4, i) + 60
    y = drawy(10, i) + 190
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
# 14
t.pu()
t.goto(-56, 120)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawx(4, i) - 60
    y = drawy(1, i) + 120
    t.goto(x, y)
t.goto(-56, 170)
for i in range(540):
    x = drawx(4, i) - 60
    y = drawy(1, i) + 170
    t.goto(x, y)
t.goto(-64, 120)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(-56, 120 + 10 * i)
    t.pu()
    t.goto(-64, 120 + 10 * i)
    t.pd()
t.pu()
t.goto(-60, 170)
t.pd()
t.goto(-60, 180)
t.pensize(1)
#
t.pu()
t.goto(-56, 190)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawx(4, i) - 60
    y = drawy(10, i) + 190
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
# 15
t.pu()
t.goto(0, 130)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawx(4, i)
    y = drawy(1, i) + 130
    t.goto(x, y)
t.goto(4, 180)
for i in range(540):
    x = drawx(4, i)
    y = drawy(1, i) + 180
    t.goto(x, y)
t.goto(-4, 130)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(4, 130 + 10 * i)
    t.pu()
    t.goto(-4, 130 + 10 * i)
    t.pd()
t.pu()
t.goto(0, 180)
t.pd()
t.goto(0, 190)
t.pensize(1)
#
t.pu()
t.goto(4, 200)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawx(4, i)
    y = drawy(10, i) + 200
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
# 16
t.pu()
t.goto(30, 110)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawx(4, i) + 30
    y = drawy(1, i) + 110
    t.goto(x, y)
t.goto(34, 160)
for i in range(540):
    x = drawx(4, i) + 30
    y = drawy(1, i) + 160
    t.goto(x, y)
t.goto(26, 110)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(34, 110 + 10 * i)
    t.pu()
    t.goto(26, 110 + 10 * i)
    t.pd()
t.pu()
t.goto(30, 160)
t.pd()
t.goto(30, 170)
t.pensize(1)
#
t.pu()
t.goto(34, 180)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawx(4, i) + 30
    y = drawy(10, i) + 180
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
# 17
t.pu()
t.goto(-30, 110)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawx(4, i) - 30
    y = drawy(1, i) + 110
    t.goto(x, y)
t.goto(-26, 160)
for i in range(540):
    x = drawx(4, i) - 30
    y = drawy(1, i) + 160
    t.goto(x, y)
t.goto(-34, 110)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(-26, 110 + 10 * i)
    t.pu()
    t.goto(-34, 110 + 10 * i)
    t.pd()
t.pu()
t.goto(-30, 160)
t.pd()
t.goto(-30, 170)
t.pensize(1)
#
t.pu()
t.goto(-26, 180)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawx(4, i) - 30
    y = drawy(10, i) + 180
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
# 随机
color = ["#e28cb9", "#805a8c", "#eaa989", "#6e90b7", "#b8b68f", "#e174b5", "#cf737c", "#7c8782"]
for i in range(80):
    t.pu()
    x = r.randint(-120, 120)
    y = r.randint(-25, 30)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])
for i in range(40):
    t.pu()
    x = r.randint(-90, 90)
    y = r.randint(-35, 10)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])
for i in range(40):
    t.pu()
    x = r.randint(-80, 80)
    y = r.randint(60, 90)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])
for i in range(30):
    t.pu()
    x = r.randint(-50, 50)
    y = r.randint(45, 70)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])
for i in range(50):
    t.pu()
    x = r.randint(-500, 500)
    y = r.randint(120, 300)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(3, 5), color[r.randint(0, 7)])
t.seth(90)
t.pu()
t.goto(0, 0)
t.fd(210)
t.left(90)
t.fd(170)
t.pd()
t.write("边庆羚，Happy Birthday", font=("Curlz MT",50))  # todo 此处可以修改画完蛋糕以后显示的文字
t.done()





