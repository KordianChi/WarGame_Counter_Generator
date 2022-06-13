import cairo
import math

tanks_battalion_A = [('I/1', 'A', '8'), ('II/1', 'A', '5'), ('I/2', 'R', '7'),
                   ('II/2', 'R', '7'), ('I/3', 'T', '8'), ('II/3', 'T', '6')]

tanks_battalion_R = [('I/1', 'A', '5'), ('II/1', 'A', '3'), ('I/2', 'R', '4'),
                   ('II/2', 'R', '3'), ('I/3', 'T', '5'), ('II/3', 'T', '4')]

pzg_regiment_A = [('1', 'A', '6'), ('2', 'A', '6'), ('3', 'R', '6'),
                  ('4', 'R', '6'), ('5', 'T', '6'), ('6', 'T', '6')]

pzg_regiment_R = [('1', 'A', '4'), ('2', 'A', '4'), ('3', 'R', '4'),
                  ('4', 'R', '4'), ('5', 'T', '4'), ('6', 'T', '4')]

stug_battalion_A = [('StuG', 'A', '4'), ('StuG', 'R', '4'), ('StuG', 'T', '4')]

stug_battalion_R = [('StuG', 'A', '2'), ('StuG', 'R', '2'), ('StuG', 'T', '2')]

tiger_company_A = [('Tiger', 'A', '3'), ('Tiger', 'R', '3'), ('Tiger', 'T', '3')]

tiger_company_R = [('Tiger', 'A', '2'), ('Tiger', 'R', '2'), ('Tiger', 'T', '2')]


WIDTH, HEIGHT = 256, 256
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

#draw NATO icon
ctx.rectangle(2/9, 3/9, 5/9, 3/9)
ctx.set_source_rgb(1, 1, 1)  # Solid color
ctx.set_line_width(0.03)
ctx.set_line_join(cairo.LINE_JOIN_ROUND)
ctx.stroke()

ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(4/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(21/54, 30/54)
ctx.show_text("HQ")

# Draw number of unit

ctx.rectangle(3/54, 1/27, 10/27, 5/27)
ctx.set_source_rgb(0.5, 0.1, 0)
ctx.fill()

ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(4/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(2/27, 5/27)
ctx.show_text("II SS")

#Draw paramteres of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(4/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(13/54, 24/27)
ctx.show_text("Hausser")

#create PNG file
surface.write_to_png('HQ_II_SS.png')

WIDTH, HEIGHT = 256, 256
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

#draw NATO icon
ctx.rectangle(2/9, 3/9, 5/9, 3/9)
ctx.set_source_rgb(1.0, 1.0, 1.0)  # Solid color
ctx.set_line_width(0.03)
ctx.set_line_join(cairo.LINE_JOIN_ROUND)
ctx.stroke()

ctx.arc(1/2, 1/2, 1/36, 0, 2*math.pi)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()


    # Draw number of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(4/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(2/27, 5/27)
ctx.show_text('Art II SS')


    #Draw paramteres of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(5/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(11/54, 24/27)
ctx.show_text("5 - 3 - 0")

  #Draw size of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(3/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(1/27, 5/9)
ctx.show_text('X')

    #create PNG file
surface.write_to_png(f'II_SS_Art_A.png')


WIDTH, HEIGHT = 256, 256
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

#draw NATO icon
ctx.rectangle(2/9, 3/9, 5/9, 3/9)
ctx.set_source_rgb(1.0, 1.0, 1.0)  # Solid color
ctx.set_line_width(0.03)
ctx.set_line_join(cairo.LINE_JOIN_ROUND)
ctx.stroke()

ctx.arc(1/2, 1/2, 1/36, 0, 2*math.pi)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()


    # Draw number of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(4/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(2/27, 5/27)
ctx.show_text('Art II SS')

    #Draw paramteres of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(5/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(11/54, 24/27)
ctx.show_text("0 - 1 - 6")

  #Draw size of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(3/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(1/27, 5/9)
ctx.show_text('X')

    #create PNG file
surface.write_to_png(f'II_SS_Art_R.png')

k = 0
for bat in tanks_battalion_A:
    WIDTH, HEIGHT = 256, 256
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()

    #draw Special panzer star
    ctx.arc(24/27, 1/2, 0.03, 0, 2*math.pi)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.01)
    ctx.stroke()

    #draw NATO icon
    ctx.rectangle(2/9, 3/9, 5/9, 3/9)
    ctx.set_source_rgb(1.0, 1.0, 1.0)  # Solid color
    ctx.set_line_width(0.03)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 4/9)
    ctx.line_to(17/27, 4/9)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 5/9)
    ctx.line_to(17/27, 5/9)
    ctx.stroke()

    ctx.arc(10/27, 1/2, 1/18, math.pi/2, -math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    ctx.arc(17/27, 1/2, 1/18, -math.pi/2, math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    # Draw number of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(2/27, 5/27)
    ctx.show_text(bat[0])

    #Draw Division/Army Number
    ctx.rectangle(19/27, 1/27, 5/27, 5/27)
    ctx.set_source_rgb(0.5, 0.1, 0)
    ctx.fill()

    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(20/27, 5/27)
    ctx.show_text(bat[1])

    #Draw paramteres of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(5/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(17/54, 24/27)
    ctx.show_text(bat[2] + " - 7")

    #Draw size of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(3/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(1/27, 5/9)
    ctx.show_text('II')

    #create PNG file
    surface.write_to_png(f'II_SS{k}_Panzer_A.png')
    k+=1

k = 0
for bat in tanks_battalion_R:
    WIDTH, HEIGHT = 256, 256
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()

    # draw Special panzer star
    ctx.arc(24 / 27, 1 / 2, 0.03, 0, 2 * math.pi)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.01)
    ctx.stroke()

    #draw NATO icon
    ctx.rectangle(2/9, 3/9, 5/9, 3/9)
    ctx.set_source_rgb(1.0, 1.0, 1.0)  # Solid color
    ctx.set_line_width(0.03)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 4/9)
    ctx.line_to(17/27, 4/9)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 5/9)
    ctx.line_to(17/27, 5/9)
    ctx.stroke()

    ctx.arc(10/27, 1/2, 1/18, math.pi/2, -math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    ctx.arc(17/27, 1/2, 1/18, -math.pi/2, math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    # Draw number of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(2/27, 5/27)
    ctx.show_text(bat[0])

    #Draw Division/Army Number
    ctx.rectangle(19/27, 1/27, 5/27, 5/27)
    ctx.set_source_rgb(0.5, 0.1, 0)
    ctx.fill()

    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(20/27, 5/27)
    ctx.show_text(bat[1])

    #Draw paramteres of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(5/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(17/54, 24/27)
    ctx.show_text(bat[2] + " - 7")

    #Draw size of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(3/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(1/27, 5/9)
    ctx.show_text('II')

    #create PNG file
    surface.write_to_png(f'II_SS{k}_Panzer_R.png')
    k+=1

k = 0
for reg in pzg_regiment_A:
    WIDTH, HEIGHT = 256, 256
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()

    #draw NATO icon
    ctx.rectangle(2/9, 3/9, 5/9, 3/9)
    ctx.set_source_rgb(1.0, 1.0, 1.0)  # Solid color
    ctx.set_line_width(0.03)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(2 / 9, 3 / 9)
    ctx.line_to(7 / 9, 6 / 9)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(7 / 9, 3 / 9)
    ctx.line_to(2 / 9, 6 / 9)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 4/9)
    ctx.line_to(17/27, 4/9)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 5/9)
    ctx.line_to(17/27, 5/9)
    ctx.stroke()

    ctx.arc(10/27, 1/2, 1/18, math.pi/2, -math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    ctx.arc(17/27, 1/2, 1/18, -math.pi/2, math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    # Draw number of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(2/27, 5/27)
    ctx.show_text(reg[0])

    #Draw Division/Army Number
    ctx.rectangle(19/27, 1/27, 5/27, 5/27)
    ctx.set_source_rgb(0.5, 0.1, 0)
    ctx.fill()

    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(20/27, 5/27)
    ctx.show_text(reg[1])

    #Draw paramteres of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(5/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(17/54, 24/27)
    ctx.show_text(reg[2] + " - 7")

    #Draw size of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(3/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(1/27, 5/9)
    ctx.show_text('III')

    #create PNG file
    surface.write_to_png(f'II_SS{k}_Gred_A.png')
    k+=1

k = 0
for reg in pzg_regiment_R:
    WIDTH, HEIGHT = 256, 256
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()

    #draw NATO icon
    ctx.rectangle(2/9, 3/9, 5/9, 3/9)
    ctx.set_source_rgb(1.0, 1.0, 1.0)  # Solid color
    ctx.set_line_width(0.03)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(2 / 9, 3 / 9)
    ctx.line_to(7 / 9, 6 / 9)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(7 / 9, 3 / 9)
    ctx.line_to(2 / 9, 6 / 9)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 4/9)
    ctx.line_to(17/27, 4/9)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 5/9)
    ctx.line_to(17/27, 5/9)
    ctx.stroke()

    ctx.arc(10/27, 1/2, 1/18, math.pi/2, -math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    ctx.arc(17/27, 1/2, 1/18, -math.pi/2, math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    # Draw number of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(2/27, 5/27)
    ctx.show_text(reg[0])

    #Draw Division/Army Number
    ctx.rectangle(19/27, 1/27, 5/27, 5/27)
    ctx.set_source_rgb(0.5, 0.1, 0)
    ctx.fill()

    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(20/27, 5/27)
    ctx.show_text(reg[1])

    #Draw paramteres of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(5/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(17/54, 24/27)
    ctx.show_text(reg[2] + " - 7")

    #Draw size of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(3/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(1/27, 5/9)
    ctx.show_text('III')

    #create PNG file
    surface.write_to_png(f'II_SS{k}_Gred_R.png')
    k+=1

k = 0
for bat in stug_battalion_A:
    WIDTH, HEIGHT = 256, 256
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()

    # draw Special panzer star
    ctx.arc(24 / 27, 1 / 2, 0.03, 0, 2 * math.pi)
    ctx.set_source_rgb(1, 1, 0)
    ctx.set_line_width(0.01)
    ctx.fill()

    #draw NATO icon
    ctx.rectangle(2/9, 3/9, 5/9, 3/9)
    ctx.set_source_rgb(1.0, 1.0, 1.0)  # Solid color
    ctx.set_line_width(0.03)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.stroke()

    ctx.arc(1/2, 1/2, 1/36, 0, 2*math.pi)
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 4/9)
    ctx.line_to(17/27, 4/9)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 5/9)
    ctx.line_to(17/27, 5/9)
    ctx.stroke()

    ctx.arc(10/27, 1/2, 1/18, math.pi/2, -math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    ctx.arc(17/27, 1/2, 1/18, -math.pi/2, math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    # Draw number of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(2/27, 5/27)
    ctx.show_text(bat[0])

    #Draw Division/Army Number
    ctx.rectangle(19/27, 1/27, 5/27, 5/27)
    ctx.set_source_rgb(0.5, 0.1, 0)
    ctx.fill()

    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(20/27, 5/27)
    ctx.show_text(bat[1])

    #Draw paramteres of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(5/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(17/54, 24/27)
    ctx.show_text(bat[2] + " - 7")

    #Draw size of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(3/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(1/27, 5/9)
    ctx.show_text('II')

    #create PNG file
    surface.write_to_png(f'II_SS{k}_StuG_A.png')
    k+=1

k = 0
for bat in stug_battalion_R:
    WIDTH, HEIGHT = 256, 256
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()

    # draw Special panzer star
    ctx.arc(24 / 27, 1 / 2, 0.03, 0, 2 * math.pi)
    ctx.set_source_rgb(1, 1, 0)
    ctx.set_line_width(0.01)
    ctx.fill()

    #draw NATO icon
    ctx.rectangle(2/9, 3/9, 5/9, 3/9)
    ctx.set_source_rgb(1.0, 1.0, 1.0)  # Solid color
    ctx.set_line_width(0.03)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.stroke()

    ctx.arc(1/2, 1/2, 1/36, 0, 2*math.pi)
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 4/9)
    ctx.line_to(17/27, 4/9)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 5/9)
    ctx.line_to(17/27, 5/9)
    ctx.stroke()

    ctx.arc(10/27, 1/2, 1/18, math.pi/2, -math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    ctx.arc(17/27, 1/2, 1/18, -math.pi/2, math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    # Draw number of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(2/27, 5/27)
    ctx.show_text(bat[0])

    #Draw Division/Army Number
    ctx.rectangle(19/27, 1/27, 5/27, 5/27)
    ctx.set_source_rgb(0.5, 0.1, 0)
    ctx.fill()

    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(20/27, 5/27)
    ctx.show_text(bat[1])

    #Draw paramteres of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(5/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(17/54, 24/27)
    ctx.show_text(bat[2] + " - 7")

    #Draw size of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(3/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(1/27, 5/9)
    ctx.show_text('II')

    #create PNG file
    surface.write_to_png(f'II_SS{k}_StuG_R.png')
    k+=1

k = 0
for comp in tiger_company_A:
    WIDTH, HEIGHT = 256, 256
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()

    #draw Special panzer star
    ctx.arc(24 / 27, 12 / 18, 0.03, 0, 2 * math.pi)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.01)
    ctx.fill()

    ctx.arc(24 / 27, 1 / 2, 0.03, 0, 2 * math.pi)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.01)
    ctx.fill()

    ctx.arc(24/27, 6/18, 0.03, 0, 2*math.pi)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.01)
    ctx.stroke()

    #draw NATO icon
    ctx.rectangle(2/9, 3/9, 5/9, 3/9)
    ctx.set_source_rgb(1.0, 1.0, 1.0)  # Solid color
    ctx.set_line_width(0.03)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 4/9)
    ctx.line_to(17/27, 4/9)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 5/9)
    ctx.line_to(17/27, 5/9)
    ctx.stroke()

    ctx.arc(10/27, 1/2, 1/18, math.pi/2, -math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    ctx.arc(17/27, 1/2, 1/18, -math.pi/2, math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    # Draw number of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(2/27, 5/27)
    ctx.show_text(comp[0])

    #Draw Division/Army Number
    ctx.rectangle(19/27, 1/27, 5/27, 5/27)
    ctx.set_source_rgb(0.5, 0.1, 0)
    ctx.fill()

    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(20/27, 5/27)
    ctx.show_text(comp[1])

    #Draw paramteres of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(5/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(17/54, 24/27)
    ctx.show_text(comp[2] + " - 6")

    #Draw size of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(3/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(2/27, 5/9)
    ctx.show_text('I')

    #create PNG file
    surface.write_to_png(f'II_SS{k}_Tiger_A.png')
    k+=1

k = 0
for comp in tiger_company_R:
    WIDTH, HEIGHT = 256, 256
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()

    #draw Special panzer star
    ctx.arc(24 / 27, 12 / 18, 0.03, 0, 2 * math.pi)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.01)
    ctx.fill()

    ctx.arc(24 / 27, 1 / 2, 0.03, 0, 2 * math.pi)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.01)
    ctx.fill()

    ctx.arc(24/27, 6/18, 0.03, 0, 2*math.pi)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.01)
    ctx.stroke()

    #draw NATO icon
    ctx.rectangle(2/9, 3/9, 5/9, 3/9)
    ctx.set_source_rgb(1.0, 1.0, 1.0)  # Solid color
    ctx.set_line_width(0.03)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 4/9)
    ctx.line_to(17/27, 4/9)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(0.03)
    ctx.move_to(10/27, 5/9)
    ctx.line_to(17/27, 5/9)
    ctx.stroke()

    ctx.arc(10/27, 1/2, 1/18, math.pi/2, -math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    ctx.arc(17/27, 1/2, 1/18, -math.pi/2, math.pi/2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(0.03)
    ctx.stroke()

    # Draw number of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(2/27, 5/27)
    ctx.show_text(comp[0])

    #Draw Division/Army Number
    ctx.rectangle(19/27, 1/27, 5/27, 5/27)
    ctx.set_source_rgb(0.5, 0.1, 0)
    ctx.fill()

    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(4/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(20/27, 5/27)
    ctx.show_text(comp[1])

    #Draw paramteres of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(5/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(17/54, 24/27)
    ctx.show_text(comp[2] + " - 6")

    #Draw size of unit
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_font_size(3/27)
    ctx.select_font_face("Times New Roman",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_BOLD)
    ctx.move_to(2/27, 5/9)
    ctx.show_text('I')

    #create PNG file
    surface.write_to_png(f'II_SS{k}_Tiger_R.png')
    k+=1
