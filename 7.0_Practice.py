import arcade
arcade.open_window(600,600,"My Art")
arcade.set_background_color((255,0,255))
arcade.start_render()
#rectangles
arcade.draw_lrtb_rectangle_filled(200,300,300,0,(0,0,0))
arcade.draw_rectangle_filled(300,300,400,400,(255,255,0,100),45)
arcade.draw_rectangle_outline(300,300,400,400,(0,0,255),15,45)
#points/lines
arcade.draw_point(300,300,(255,255,255),30)
arcade.draw_line(100,100,500,500,(255,0,0),5)
#circles/ellipses
arcade.draw_circle_filled(300,300,50,(0,0,0,75))
arcade.draw_circle_outline(300,300,50,(0,0,0),5)
arcade.draw_ellipse_filled(400,400,100,50,(100,0,100),45)
#polygons
point_list=((100,100),(120,400),(200,400),(300,150))
arcade.draw_polygon_filled(point_list,(90,187,239))
#text
arcade.draw_text("PyCasso",100,550,arcade.color.INDEPENDENCE,20)

for i in range(0,610,20):
    arcade.draw_rectangle_filled(i,60,10,30,(25,55,69))
radius = 50
y = 50
for i in range(3):
    arcade.draw_circle_filled(100,50,50,(39,218,183))
    y = y+1.8*radius
    radius = radius*.8

#images
# mypic = arcade.load_texture("python.png")
# arcade.draw_texture_rectangle(550,100,mypic.width,mypic.height,mypic,40,200)

for i in range(0,610,20):
    arcade.draw_rectangle_filled(i,60,10,30,(25,55,69))
arcade.finish_render()
arcade.run()