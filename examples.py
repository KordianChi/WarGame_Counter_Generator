import cairo
import math

WIDTH, HEIGHT = 256, 256
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(0.51, 0.38, 0.24)
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
ctx.set_source_rgb(0.35, 0.34, 0.29)
ctx.fill()

ctx.set_source_rgb(0, 0, 0)
ctx.set_font_size(4/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(2/27, 5/27)
ctx.show_text("XXX")

#Draw paramteres of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(4/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(11/54, 24/27)
ctx.show_text("Horrocks")

#create PNG file
surface.write_to_png('HQ_ex.png')

### Mech_Example

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

ctx.set_source_rgb(1.0, 1.0, 1.0)
ctx.set_line_width(0.03)
ctx.move_to(2/9, 3/9)
ctx.line_to(7/9, 6/9)
ctx.stroke()

ctx.set_source_rgb(1.0, 1.0, 1.0)
ctx.set_line_width(0.03)
ctx.move_to(7/9, 3/9)
ctx.line_to(2/9, 6/9)
ctx.stroke()

# Draw number of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(4/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(2/27, 5/27)
ctx.show_text("1 PGR")

#Draw Division/Army Number
ctx.rectangle(19/27, 1/27, 7/27, 5/27)
ctx.set_source_rgb(0.5, 0.1, 0)
ctx.fill()

ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(4/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(39/54, 5/27)
ctx.show_text("AH")

#Draw paramteres of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(5/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(11/54, 24/27)
ctx.show_text("6 - 6 - 9")

#Draw size of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(3/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(1/27, 5/9)
ctx.show_text('III')

#create PNG file
surface.write_to_png('SS_ex.png')

#Inf_Example

WIDTH, HEIGHT = 256, 256
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(0.82, 0.14, 0.023)
ctx.fill()

#draw NATO panzer icon
ctx.rectangle(2/9, 3/9, 5/9, 3/9)
ctx.set_source_rgb(1.0, 1.0, 1.0)  # Solid color
ctx.set_line_width(0.03)
ctx.set_line_join(cairo.LINE_JOIN_ROUND)
ctx.stroke()

ctx.set_source_rgb(1.0, 1.0, 1.0)
ctx.set_line_width(0.03)
ctx.move_to(2/9, 3/9)
ctx.line_to(7/9, 6/9)
ctx.stroke()

ctx.set_source_rgb(1.0, 1.0, 1.0)
ctx.set_line_width(0.03)
ctx.move_to(7/9, 3/9)
ctx.line_to(2/9, 6/9)
ctx.stroke()

# Draw number of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(4/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(2/27, 5/27)
ctx.show_text("183")

#Draw Division/Army Number
ctx.rectangle(19/27, 1/27, 6/27, 5/27)
ctx.set_source_rgb(1, 1, 0)
ctx.fill()

ctx.set_source_rgb(0, 0, 0)
ctx.set_font_size(4/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(20/27, 5/27)
ctx.show_text("38")

#Draw paramteres of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(5/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(11/54, 24/27)
ctx.show_text("3 - 4 - 5")

#Draw size of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(3/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(1/27, 5/9)
ctx.show_text('XX')

#create PNG file
surface.write_to_png('RED_ARMY_ex.png')

### Panzer Example

WIDTH, HEIGHT = 256, 256
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(0.302, 0.3647, 0.3255)
ctx.fill()

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
ctx.show_text("15")

#Draw Division/Army Number
ctx.rectangle(19/27, 1/27, 6/27, 5/27)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

ctx.set_source_rgb(0, 0, 0)
ctx.set_font_size(4/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(20/27, 5/27)
ctx.show_text("11")

#Draw paramteres of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(5/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(11/54, 24/27)
ctx.show_text("7 - 5 - 8")

#Draw size of unit
ctx.set_source_rgb(1, 1, 1)
ctx.set_font_size(3/27)
ctx.select_font_face("Times New Roman",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.move_to(1/27, 5/9)
ctx.show_text('III')

#create PNG file
surface.write_to_png('WEHRMACHT_ex.png')
