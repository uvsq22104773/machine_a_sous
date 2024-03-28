import tkinter as tk
from random import randint

root = tk.Tk()
root.title('777')
canvas = tk.Canvas(root, width=500, height=500)
canvas.grid()

canvas.create_rectangle(160, 218, 345, 223, fill='grey65', outline='grey65')
canvas.create_rectangle(160, 228, 345, 223, fill='grey88', outline='grey88')
canvas.create_rectangle(160, 268, 345, 288, fill='grey90', outline='grey90')
canvas.create_rectangle(160, 288, 345, 298, fill='grey85', outline='grey85')
canvas.create_rectangle(160, 298, 345, 308, fill='grey73', outline='grey73')
canvas.create_rectangle(160, 308, 345, 313, fill='grey65', outline='grey65')

apple1=[
    canvas.create_rectangle(184, 279, 199, 282, fill='black', outline='black'),
    canvas.create_rectangle(181, 276, 184, 279, fill='black', outline='black'),
    canvas.create_rectangle(199, 276, 202, 279, fill='black', outline='black'),
    canvas.create_rectangle(178, 273, 181, 276, fill='black', outline='black'),
    canvas.create_rectangle(202, 273, 205, 276, fill='black', outline='black'),
    canvas.create_rectangle(175, 261, 178, 273, fill='black', outline='black'),
    canvas.create_rectangle(205, 261, 208, 273, fill='black', outline='black'),
    canvas.create_rectangle(178, 258, 181, 261, fill='black', outline='black'),
    canvas.create_rectangle(202, 258, 205, 261, fill='black', outline='black'),
    canvas.create_rectangle(181, 255, 190, 258, fill='black', outline='black'),
    canvas.create_rectangle(193, 255, 202, 258, fill='black', outline='black'),
    canvas.create_rectangle(187, 252, 190, 255, fill='black', outline='black'),
    canvas.create_rectangle(202, 252, 205, 255, fill='black', outline='black'),
    canvas.create_rectangle(190, 249, 193, 252, fill='black', outline='black'),
    canvas.create_rectangle(205, 249, 208, 252, fill='black', outline='black'),
    canvas.create_rectangle(193, 246, 205, 249, fill='black', outline='black'),
    canvas.create_rectangle(184, 258, 196, 276, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(178, 261, 199, 273, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(199, 264, 202, 270, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(181, 258, 184, 261, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(181, 273, 184, 276, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(184, 276, 199, 279, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(196, 273, 202, 276, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(199, 270, 205, 273, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(202, 264, 205, 270, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(199, 261, 205, 264, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(196, 258, 202, 261, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(193, 249, 196, 252, fill='tomato3', outline='tomato3'),
    canvas.create_rectangle(190, 255, 193, 258, fill='tomato4', outline='tomato4'),
    canvas.create_rectangle(190, 252, 193, 255, fill='tomato3', outline='tomato3'),
    canvas.create_rectangle(196, 249, 202, 252, fill='green3', outline='green3'),
    canvas.create_rectangle(193, 252, 202, 255, fill='green4', outline='green4'),
    canvas.create_rectangle(202, 249, 205, 252, fill='green4', outline='green4'),
    canvas.create_rectangle(181, 261, 183, 263, fill='white', outline='white'),
    canvas.create_rectangle(184, 264, 186, 266, fill='white', outline='white'),
    canvas.create_rectangle(190, 258, 193, 261, fill='black', outline='black'),
    canvas.create_rectangle(190, 261, 193, 264, fill='firebrick1', outline='firebrick1'),
]

apple2=[
    canvas.create_rectangle(244, 279, 259, 282, fill='black', outline='black'),
    canvas.create_rectangle(241, 276, 244, 279, fill='black', outline='black'),
    canvas.create_rectangle(259, 276, 262, 279, fill='black', outline='black'),
    canvas.create_rectangle(238, 273, 241, 276, fill='black', outline='black'),
    canvas.create_rectangle(262, 273, 265, 276, fill='black', outline='black'),
    canvas.create_rectangle(235, 261, 238, 273, fill='black', outline='black'),
    canvas.create_rectangle(265, 261, 268, 273, fill='black', outline='black'),
    canvas.create_rectangle(238, 258, 241, 261, fill='black', outline='black'),
    canvas.create_rectangle(262, 258, 265, 261, fill='black', outline='black'),
    canvas.create_rectangle(241, 255, 250, 258, fill='black', outline='black'),
    canvas.create_rectangle(253, 255, 262, 258, fill='black', outline='black'),
    canvas.create_rectangle(247, 252, 250, 255, fill='black', outline='black'),
    canvas.create_rectangle(262, 252, 265, 255, fill='black', outline='black'),
    canvas.create_rectangle(250, 249, 253, 252, fill='black', outline='black'),
    canvas.create_rectangle(265, 249, 268, 252, fill='black', outline='black'),
    canvas.create_rectangle(253, 246, 265, 249, fill='black', outline='black'),
    canvas.create_rectangle(244, 258, 256, 276, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(238, 261, 259, 273, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(259, 264, 262, 270, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(241, 258, 244, 261, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(241, 273, 244, 276, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(244, 276, 259, 279, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(256, 273, 262, 276, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(259, 270, 265, 273, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(262, 264, 265, 270, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(259, 261, 265, 264, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(256, 258, 262, 261, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(253, 249, 256, 252, fill='tomato3', outline='tomato3'),
    canvas.create_rectangle(250, 255, 253, 258, fill='tomato4', outline='tomato4'),
    canvas.create_rectangle(250, 252, 253, 255, fill='tomato3', outline='tomato3'),
    canvas.create_rectangle(256, 249, 262, 252, fill='green3', outline='green3'),
    canvas.create_rectangle(253, 252, 262, 255, fill='green4', outline='green4'),
    canvas.create_rectangle(262, 249, 265, 252, fill='green4', outline='green4'),
    canvas.create_rectangle(241, 261, 243, 263, fill='white', outline='white'),
    canvas.create_rectangle(244, 264, 246, 266, fill='white', outline='white'),
    canvas.create_rectangle(250, 258, 253, 261, fill='black', outline='black'),
    canvas.create_rectangle(250, 261, 253, 264, fill='firebrick1', outline='firebrick1'),
]

apple3=[
    canvas.create_rectangle(304, 279, 319, 282, fill='black', outline='black'),
    canvas.create_rectangle(301, 276, 304, 279, fill='black', outline='black'),
    canvas.create_rectangle(319, 276, 322, 279, fill='black', outline='black'),
    canvas.create_rectangle(298, 273, 301, 276, fill='black', outline='black'),
    canvas.create_rectangle(322, 273, 325, 276, fill='black', outline='black'),
    canvas.create_rectangle(295, 261, 298, 273, fill='black', outline='black'),
    canvas.create_rectangle(315, 261, 328, 273, fill='black', outline='black'),
    canvas.create_rectangle(298, 258, 301, 261, fill='black', outline='black'),
    canvas.create_rectangle(322, 258, 325, 261, fill='black', outline='black'),
    canvas.create_rectangle(301, 255, 310, 258, fill='black', outline='black'),
    canvas.create_rectangle(313, 255, 322, 258, fill='black', outline='black'),
    canvas.create_rectangle(307, 252, 310, 255, fill='black', outline='black'),
    canvas.create_rectangle(322, 252, 325, 255, fill='black', outline='black'),
    canvas.create_rectangle(310, 249, 313, 252, fill='black', outline='black'),
    canvas.create_rectangle(325, 249, 328, 252, fill='black', outline='black'),
    canvas.create_rectangle(313, 246, 325, 249, fill='black', outline='black'),
    canvas.create_rectangle(304, 258, 316, 276, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(298, 261, 319, 273, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(319, 264, 322, 270, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(301, 258, 304, 261, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(301, 273, 304, 276, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(304, 276, 319, 279, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(316, 273, 322, 276, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(319, 270, 325, 273, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(322, 264, 325, 270, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(319, 261, 325, 264, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(316, 258, 322, 261, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(313, 249, 316, 252, fill='tomato3', outline='tomato3'),
    canvas.create_rectangle(310, 255, 313, 258, fill='tomato4', outline='tomato4'),
    canvas.create_rectangle(310, 252, 313, 255, fill='tomato3', outline='tomato3'),
    canvas.create_rectangle(316, 249, 322, 252, fill='green3', outline='green3'),
    canvas.create_rectangle(313, 252, 322, 255, fill='green4', outline='green4'),
    canvas.create_rectangle(322, 249, 325, 252, fill='green4', outline='green4'),
    canvas.create_rectangle(301, 261, 303, 263, fill='white', outline='white'),
    canvas.create_rectangle(304, 264, 306, 266, fill='white', outline='white'),
    canvas.create_rectangle(310, 258, 313, 261, fill='black', outline='black'),
    canvas.create_rectangle(310, 261, 313, 264, fill='firebrick1', outline='firebrick1'),
]


cherry1=[
    canvas.create_rectangle(192, 263, 195, 266, fill='black', outline='black'),
    canvas.create_rectangle(195, 260, 198, 263, fill='black', outline='black'),
    canvas.create_rectangle(192, 254, 195, 260, fill='black', outline='black'),
    canvas.create_rectangle(189, 254, 192, 257, fill='black', outline='black'),
    canvas.create_rectangle(186, 257, 189, 266, fill='black', outline='black'),
    canvas.create_rectangle(189, 266, 192, 269, fill='black', outline='black'),
    canvas.create_rectangle(192, 245, 198, 248, fill='black', outline='black'),
    canvas.create_rectangle(198, 248, 201, 260, fill='black', outline='black'),
    canvas.create_rectangle(201, 260, 204, 263, fill='black', outline='black'),
    canvas.create_rectangle(204, 263, 207, 266, fill='black', outline='black'),
    canvas.create_rectangle(207, 266, 210, 275, fill='black', outline='black'),
    canvas.create_rectangle(204, 275, 207, 278, fill='black', outline='black'),
    canvas.create_rectangle(195, 278, 204, 281, fill='black', outline='black'),
    canvas.create_rectangle(192, 275, 195, 278, fill='black', outline='black'),
    canvas.create_rectangle(189, 278, 192, 281, fill='black', outline='black'),
    canvas.create_rectangle(180, 281, 189, 284, fill='black', outline='black'),
    canvas.create_rectangle(177, 278, 180, 281, fill='black', outline='black'),
    canvas.create_rectangle(174, 269, 177, 278, fill='black', outline='black'),
    canvas.create_rectangle(177, 266, 180, 269, fill='black', outline='black'),
    canvas.create_rectangle(180, 257, 183, 266, fill='black', outline='black'),
    canvas.create_rectangle(183, 254, 186, 257, fill='black', outline='black'),
    canvas.create_rectangle(186, 251, 189, 254, fill='black', outline='black'),
    canvas.create_rectangle(189, 248, 192, 251, fill='black', outline='black'),
    canvas.create_rectangle(192, 248, 198, 251, fill='tomato3', outline='tomato3'),
    canvas.create_rectangle(189, 251, 192, 254, fill='tomato3', outline='tomato3'),
    canvas.create_rectangle(192, 251, 198, 254, fill='tomato4', outline='tomato4'),
    canvas.create_rectangle(186, 254, 189, 257, fill='green3', outline='green3'),
    canvas.create_rectangle(183, 257, 186, 266, fill='green3', outline='green3'),
    canvas.create_rectangle(180, 266, 189, 278, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(177, 269, 192, 275, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(180, 278, 189, 281, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(177, 275, 180, 278, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(189, 275, 192, 278, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(183, 266, 186, 269, fill='green4', outline='green4'),
    canvas.create_rectangle(195, 254, 198, 260, fill='green3', outline='green3'),
    canvas.create_rectangle(198, 260, 201, 263, fill='green3', outline='green3'),
    canvas.create_rectangle(195, 263, 204, 272, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(192, 266, 195, 269, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(204, 266, 207, 272, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(199, 272, 204, 275, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(192, 269, 195, 275, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(195, 272, 198, 278, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(198, 275, 204, 278, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(204, 272, 207, 275, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(198, 263, 201, 266, fill='green4', outline='green4'),
    canvas.create_rectangle(180, 269, 182, 271, fill='white', outline='white'),
    canvas.create_rectangle(183, 272, 185, 274, fill='white', outline='white'),
    canvas.create_rectangle(195, 266, 197, 268, fill='white', outline='white'),
]

cherry2=[
    canvas.create_rectangle(252, 263, 255, 266, fill='black', outline='black'),
    canvas.create_rectangle(255, 260, 258, 263, fill='black', outline='black'),
    canvas.create_rectangle(252, 254, 255, 260, fill='black', outline='black'),
    canvas.create_rectangle(249, 254, 252, 257, fill='black', outline='black'),
    canvas.create_rectangle(246, 257, 249, 266, fill='black', outline='black'),
    canvas.create_rectangle(249, 266, 252, 269, fill='black', outline='black'),
    canvas.create_rectangle(252, 245, 258, 248, fill='black', outline='black'),
    canvas.create_rectangle(258, 248, 261, 260, fill='black', outline='black'),
    canvas.create_rectangle(261, 260, 264, 263, fill='black', outline='black'),
    canvas.create_rectangle(264, 263, 267, 266, fill='black', outline='black'),
    canvas.create_rectangle(267, 266, 270, 275, fill='black', outline='black'),
    canvas.create_rectangle(264, 275, 267, 278, fill='black', outline='black'),
    canvas.create_rectangle(255, 278, 264, 281, fill='black', outline='black'),
    canvas.create_rectangle(252, 275, 255, 278, fill='black', outline='black'),
    canvas.create_rectangle(249, 278, 252, 281, fill='black', outline='black'),
    canvas.create_rectangle(240, 281, 249, 284, fill='black', outline='black'),
    canvas.create_rectangle(237, 278, 240, 281, fill='black', outline='black'),
    canvas.create_rectangle(234, 269, 237, 278, fill='black', outline='black'),
    canvas.create_rectangle(237, 266, 240, 269, fill='black', outline='black'),
    canvas.create_rectangle(240, 257, 243, 266, fill='black', outline='black'),
    canvas.create_rectangle(243, 254, 246, 257, fill='black', outline='black'),
    canvas.create_rectangle(246, 251, 249, 254, fill='black', outline='black'),
    canvas.create_rectangle(249, 248, 252, 251, fill='black', outline='black'),
    canvas.create_rectangle(252, 248, 258, 251, fill='tomato3', outline='tomato3'),
    canvas.create_rectangle(249, 251, 252, 254, fill='tomato3', outline='tomato3'),
    canvas.create_rectangle(252, 251, 258, 254, fill='tomato4', outline='tomato4'),
    canvas.create_rectangle(246, 254, 249, 257, fill='green3', outline='green3'),
    canvas.create_rectangle(243, 257, 246, 266, fill='green3', outline='green3'),
    canvas.create_rectangle(240, 266, 249, 278, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(237, 269, 252, 275, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(240, 278, 249, 281, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(237, 275, 240, 278, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(249, 275, 252, 278, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(243, 266, 246, 269, fill='green4', outline='green4'),
    canvas.create_rectangle(255, 254, 258, 260, fill='green3', outline='green3'),
    canvas.create_rectangle(258, 260, 261, 263, fill='green3', outline='green3'),
    canvas.create_rectangle(255, 263, 264, 272, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(252, 266, 255, 269, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(264, 266, 267, 272, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(259, 272, 264, 275, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(252, 269, 255, 275, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(255, 272, 258, 278, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(258, 275, 264, 278, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(264, 272, 267, 275, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(258, 263, 261, 266, fill='green4', outline='green4'),
    canvas.create_rectangle(240, 269, 242, 271, fill='white', outline='white'),
    canvas.create_rectangle(243, 272, 245, 274, fill='white', outline='white'),
    canvas.create_rectangle(255, 266, 257, 268, fill='white', outline='white'),
]

cherry3=[
    canvas.create_rectangle(312, 263, 315, 266, fill='black', outline='black'),
    canvas.create_rectangle(315, 260, 318, 263, fill='black', outline='black'),
    canvas.create_rectangle(312, 254, 315, 260, fill='black', outline='black'),
    canvas.create_rectangle(309, 254, 312, 257, fill='black', outline='black'),
    canvas.create_rectangle(306, 257, 309, 266, fill='black', outline='black'),
    canvas.create_rectangle(309, 266, 312, 269, fill='black', outline='black'),
    canvas.create_rectangle(312, 245, 318, 248, fill='black', outline='black'),
    canvas.create_rectangle(318, 248, 321, 260, fill='black', outline='black'),
    canvas.create_rectangle(321, 260, 324, 263, fill='black', outline='black'),
    canvas.create_rectangle(324, 263, 327, 266, fill='black', outline='black'),
    canvas.create_rectangle(327, 266, 330, 275, fill='black', outline='black'),
    canvas.create_rectangle(324, 275, 327, 278, fill='black', outline='black'),
    canvas.create_rectangle(315, 278, 324, 281, fill='black', outline='black'),
    canvas.create_rectangle(312, 275, 315, 278, fill='black', outline='black'),
    canvas.create_rectangle(309, 278, 312, 281, fill='black', outline='black'),
    canvas.create_rectangle(300, 281, 309, 284, fill='black', outline='black'),
    canvas.create_rectangle(297, 278, 300, 281, fill='black', outline='black'),
    canvas.create_rectangle(294, 269, 297, 278, fill='black', outline='black'),
    canvas.create_rectangle(297, 266, 300, 269, fill='black', outline='black'),
    canvas.create_rectangle(300, 257, 303, 266, fill='black', outline='black'),
    canvas.create_rectangle(303, 254, 306, 257, fill='black', outline='black'),
    canvas.create_rectangle(306, 251, 309, 254, fill='black', outline='black'),
    canvas.create_rectangle(309, 248, 312, 251, fill='black', outline='black'),
    canvas.create_rectangle(312, 248, 318, 251, fill='tomato3', outline='tomato3'),
    canvas.create_rectangle(309, 251, 312, 254, fill='tomato3', outline='tomato3'),
    canvas.create_rectangle(312, 251, 318, 254, fill='tomato4', outline='tomato4'),
    canvas.create_rectangle(306, 254, 309, 257, fill='green3', outline='green3'),
    canvas.create_rectangle(303, 257, 306, 266, fill='green3', outline='green3'),
    canvas.create_rectangle(300, 266, 309, 278, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(297, 269, 312, 275, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(300, 278, 309, 281, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(297, 275, 300, 278, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(309, 275, 312, 278, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(303, 266, 306, 269, fill='green4', outline='green4'),
    canvas.create_rectangle(315, 254, 318, 260, fill='green3', outline='green3'),
    canvas.create_rectangle(318, 260, 321, 263, fill='green3', outline='green3'),
    canvas.create_rectangle(315, 263, 324, 272, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(312, 266, 315, 269, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(324, 266, 327, 272, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(319, 272, 324, 275, fill='firebrick1', outline='firebrick1'),
    canvas.create_rectangle(312, 269, 315, 275, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(315, 272, 318, 278, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(318, 275, 324, 278, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(324, 272, 327, 275, fill='firebrick3', outline='firebrick3'),
    canvas.create_rectangle(318, 263, 321, 266, fill='green4', outline='green4'),
    canvas.create_rectangle(300, 269, 302, 271, fill='white', outline='white'),
    canvas.create_rectangle(303, 272, 305, 274, fill='white', outline='white'),
    canvas.create_rectangle(315, 266, 317, 268, fill='white', outline='white'),
]

meat1=[
    canvas.create_rectangle(174, 253, 177, 274, fill='black', outline='black'),
    canvas.create_rectangle(177, 250, 180, 253, fill='black', outline='black'),
    canvas.create_rectangle(180, 247, 186, 250, fill='black', outline='black'),
    canvas.create_rectangle(186, 250, 189, 253, fill='black', outline='black'),
    canvas.create_rectangle(189, 253, 195, 256, fill='black', outline='black'),
    canvas.create_rectangle(195, 256, 201, 259, fill='black', outline='black'),
    canvas.create_rectangle(201, 259, 204, 262, fill='black', outline='black'),
    canvas.create_rectangle(204, 262, 207, 265, fill='black', outline='black'),
    canvas.create_rectangle(207, 265, 210, 274, fill='black', outline='black'),
    canvas.create_rectangle(204, 274, 207, 277, fill='black', outline='black'),
    canvas.create_rectangle(201, 277, 204, 280, fill='black', outline='black'),
    canvas.create_rectangle(180, 277, 183, 280, fill='black', outline='black'),
    canvas.create_rectangle(177, 274, 180, 277, fill='black', outline='black'),
    canvas.create_rectangle(192, 277, 201, 281, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(183, 277, 192, 281, fill='LightSalmon4', outline='LightSalmon4'),
    canvas.create_rectangle(180, 271, 183, 277, fill='LightSalmon4', outline='LightSalmon4'),
    canvas.create_rectangle(177, 268, 180, 274, fill='LightSalmon4', outline='LightSalmon4'),
    canvas.create_rectangle(204, 268, 207, 274, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(201, 271, 204, 277, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(183, 274, 201, 277, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(177, 253, 180, 268, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(180, 268, 183, 271, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(183, 271, 201, 274, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(201, 268, 204, 271, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(204, 265, 207, 268, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(201, 262, 204, 265, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(195, 259, 201, 262, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(189, 256, 195, 259, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(186, 253, 189, 256, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(180, 250, 186, 253, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(183, 262, 201, 271, fill='brown1', outline='brown1'),
    canvas.create_rectangle(180, 253, 183, 268, fill='brown1', outline='brown1'),
    canvas.create_rectangle(183, 259, 186, 253, fill='brown1', outline='brown1'),
    canvas.create_rectangle(186, 262, 189, 256, fill='brown1', outline='brown1'),
    canvas.create_rectangle(189, 259, 195, 262, fill='brown1', outline='brown1'),
    canvas.create_rectangle(201, 265, 204, 268, fill='brown1', outline='brown1'),
    canvas.create_rectangle(193, 265, 195, 267, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(190, 265, 192, 267, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(187, 262, 189, 264, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(184, 259, 186, 261, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(184, 262, 186, 264, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(183, 281, 201, 283, fill='black', outline='black')
]

meat2=[
    canvas.create_rectangle(234, 253, 237, 274, fill='black', outline='black'),
    canvas.create_rectangle(237, 250, 240, 253, fill='black', outline='black'),
    canvas.create_rectangle(240, 247, 246, 250, fill='black', outline='black'),
    canvas.create_rectangle(246, 250, 249, 253, fill='black', outline='black'),
    canvas.create_rectangle(249, 253, 255, 256, fill='black', outline='black'),
    canvas.create_rectangle(255, 256, 261, 259, fill='black', outline='black'),
    canvas.create_rectangle(261, 259, 264, 262, fill='black', outline='black'),
    canvas.create_rectangle(264, 262, 267, 265, fill='black', outline='black'),
    canvas.create_rectangle(267, 265, 270, 274, fill='black', outline='black'),
    canvas.create_rectangle(264, 274, 267, 277, fill='black', outline='black'),
    canvas.create_rectangle(261, 277, 264, 280, fill='black', outline='black'),
    canvas.create_rectangle(240, 277, 243, 280, fill='black', outline='black'),
    canvas.create_rectangle(237, 274, 240, 277, fill='black', outline='black'),
    canvas.create_rectangle(252, 277, 261, 281, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(243, 277, 252, 281, fill='LightSalmon4', outline='LightSalmon4'),
    canvas.create_rectangle(240, 271, 243, 277, fill='LightSalmon4', outline='LightSalmon4'),
    canvas.create_rectangle(237, 268, 240, 274, fill='LightSalmon4', outline='LightSalmon4'),
    canvas.create_rectangle(264, 268, 267, 274, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(261, 271, 264, 277, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(243, 274, 261, 277, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(237, 253, 240, 268, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(240, 268, 243, 271, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(243, 271, 261, 274, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(261, 268, 264, 271, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(264, 265, 267, 268, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(261, 262, 264, 265, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(255, 259, 261, 262, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(249, 256, 255, 259, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(246, 253, 249, 256, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(240, 250, 246, 253, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(243, 262, 261, 271, fill='brown1', outline='brown1'),
    canvas.create_rectangle(240, 253, 243, 268, fill='brown1', outline='brown1'),
    canvas.create_rectangle(243, 259, 246, 253, fill='brown1', outline='brown1'),
    canvas.create_rectangle(246, 262, 249, 256, fill='brown1', outline='brown1'),
    canvas.create_rectangle(249, 259, 255, 262, fill='brown1', outline='brown1'),
    canvas.create_rectangle(261, 265, 264, 268, fill='brown1', outline='brown1'),
    canvas.create_rectangle(253, 265, 255, 267, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(250, 265, 252, 267, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(247, 262, 249, 264, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(244, 259, 246, 261, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(244, 262, 246, 264, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(243, 281, 261, 283, fill='black', outline='black')
]

meat3=[
    canvas.create_rectangle(294, 253, 297, 274, fill='black', outline='black'),
    canvas.create_rectangle(297, 250, 300, 253, fill='black', outline='black'),
    canvas.create_rectangle(300, 247, 306, 250, fill='black', outline='black'),
    canvas.create_rectangle(306, 250, 309, 253, fill='black', outline='black'),
    canvas.create_rectangle(309, 253, 315, 256, fill='black', outline='black'),
    canvas.create_rectangle(315, 256, 321, 259, fill='black', outline='black'),
    canvas.create_rectangle(321, 259, 324, 262, fill='black', outline='black'),
    canvas.create_rectangle(324, 262, 327, 265, fill='black', outline='black'),
    canvas.create_rectangle(327, 265, 330, 274, fill='black', outline='black'),
    canvas.create_rectangle(324, 274, 327, 277, fill='black', outline='black'),
    canvas.create_rectangle(321, 277, 324, 280, fill='black', outline='black'),
    canvas.create_rectangle(300, 277, 303, 280, fill='black', outline='black'),
    canvas.create_rectangle(297, 274, 300, 277, fill='black', outline='black'),
    canvas.create_rectangle(312, 277, 321, 281, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(303, 277, 312, 281, fill='LightSalmon4', outline='LightSalmon4'),
    canvas.create_rectangle(300, 271, 303, 277, fill='LightSalmon4', outline='LightSalmon4'),
    canvas.create_rectangle(297, 268, 300, 274, fill='LightSalmon4', outline='LightSalmon4'),
    canvas.create_rectangle(324, 268, 327, 274, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(321, 271, 324, 277, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(303, 274, 321, 277, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(297, 253, 300, 268, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(300, 268, 303, 271, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(303, 271, 321, 274, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(321, 268, 324, 271, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(324, 265, 327, 268, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(321, 262, 324, 265, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(315, 259, 321, 262, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(309, 256, 315, 259, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(306, 253, 309, 256, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(300, 250, 306, 253, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(303, 262, 321, 271, fill='brown1', outline='brown1'),
    canvas.create_rectangle(300, 253, 303, 268, fill='brown1', outline='brown1'),
    canvas.create_rectangle(303, 259, 306, 253, fill='brown1', outline='brown1'),
    canvas.create_rectangle(306, 262, 309, 256, fill='brown1', outline='brown1'),
    canvas.create_rectangle(309, 259, 315, 262, fill='brown1', outline='brown1'),
    canvas.create_rectangle(321, 265, 324, 268, fill='brown1', outline='brown1'),
    canvas.create_rectangle(313, 265, 315, 267, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(310, 265, 312, 267, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(307, 262, 309, 264, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(304, 259, 306, 261, fill='wheat1', outline='wheat1'),
    canvas.create_rectangle(304, 262, 306, 264, fill='LightSalmon3', outline='LightSalmon3'),
    canvas.create_rectangle(303, 281, 321, 283, fill='black', outline='black')
]

gold_coin1=[
    canvas.create_rectangle(187, 248, 196, 251, fill='black', outline='black'),
    canvas.create_rectangle(196, 251, 202, 254, fill='black', outline='black'),
    canvas.create_rectangle(202, 254, 205, 260, fill='black', outline='black'),
    canvas.create_rectangle(205, 260, 208, 269, fill='black', outline='black'),
    canvas.create_rectangle(202, 269, 205, 275, fill='black', outline='black'),
    canvas.create_rectangle(196, 275, 202, 278, fill='black', outline='black'),
    canvas.create_rectangle(187, 278, 196, 281, fill='black', outline='black'),
    canvas.create_rectangle(181, 275, 187, 278, fill='black', outline='black'),
    canvas.create_rectangle(178, 269, 181, 275, fill='black', outline='black'),
    canvas.create_rectangle(175, 260, 178, 269, fill='black', outline='black'),
    canvas.create_rectangle(178, 254, 181, 260, fill='black', outline='black'),
    canvas.create_rectangle(181, 251, 187, 254, fill='black', outline='black'),
    canvas.create_rectangle(187, 275, 196, 278, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(181, 272, 187, 275, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(181, 269, 184, 272, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(178, 260, 181, 269, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(196, 272, 202, 275, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(199, 269, 202, 272, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(187, 251, 196, 254, fill='white', outline='white'),
    canvas.create_rectangle(181, 254, 187, 257, fill='white', outline='white'),
    canvas.create_rectangle(181, 257, 184, 260, fill='white', outline='white'),
    canvas.create_rectangle(196, 254, 202, 257, fill='white', outline='white'),
    canvas.create_rectangle(199, 257, 202, 260, fill='white', outline='white'),
    canvas.create_rectangle(202, 260, 205, 269, fill='white', outline='white'),
    canvas.create_rectangle(181, 260, 202, 269, fill='light goldenrod', outline='light goldenrod'),
    canvas.create_rectangle(184, 257, 199, 260, fill='light goldenrod', outline='light goldenrod'),
    canvas.create_rectangle(187, 254, 196, 257, fill='light goldenrod', outline='light goldenrod'),
    canvas.create_rectangle(184, 269, 199, 272, fill='light goldenrod', outline='light goldenrod'),
    canvas.create_rectangle(187, 272, 196, 275, fill='light goldenrod', outline='light goldenrod'),
    canvas.create_rectangle(187, 261, 189, 268, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(190, 269, 192, 271, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(193, 261, 195, 268, fill='white', outline='white'),
    canvas.create_rectangle(190, 258, 192, 260, fill='white', outline='white')
]

gold_coin2=[
    canvas.create_rectangle(247, 248, 256, 251, fill='black', outline='black'),
    canvas.create_rectangle(256, 251, 262, 254, fill='black', outline='black'),
    canvas.create_rectangle(262, 254, 265, 260, fill='black', outline='black'),
    canvas.create_rectangle(265, 260, 268, 269, fill='black', outline='black'),
    canvas.create_rectangle(262, 269, 265, 275, fill='black', outline='black'),
    canvas.create_rectangle(256, 275, 262, 278, fill='black', outline='black'),
    canvas.create_rectangle(247, 278, 256, 281, fill='black', outline='black'),
    canvas.create_rectangle(241, 275, 247, 278, fill='black', outline='black'),
    canvas.create_rectangle(238, 269, 241, 275, fill='black', outline='black'),
    canvas.create_rectangle(235, 260, 238, 269, fill='black', outline='black'),
    canvas.create_rectangle(238, 254, 241, 260, fill='black', outline='black'),
    canvas.create_rectangle(241, 251, 247, 254, fill='black', outline='black'),
    canvas.create_rectangle(247, 275, 256, 278, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(241, 272, 247, 275, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(241, 269, 244, 272, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(238, 260, 241, 269, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(256, 272, 262, 275, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(259, 269, 262, 272, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(247, 251, 256, 254, fill='white', outline='white'),
    canvas.create_rectangle(241, 254, 247, 257, fill='white', outline='white'),
    canvas.create_rectangle(241, 257, 244, 260, fill='white', outline='white'),
    canvas.create_rectangle(256, 254, 262, 257, fill='white', outline='white'),
    canvas.create_rectangle(259, 257, 262, 260, fill='white', outline='white'),
    canvas.create_rectangle(262, 260, 265, 269, fill='white', outline='white'),
    canvas.create_rectangle(241, 260, 262, 269, fill='light goldenrod', outline='light goldenrod'),
    canvas.create_rectangle(244, 257, 259, 260, fill='light goldenrod', outline='light goldenrod'),
    canvas.create_rectangle(247, 254, 256, 257, fill='light goldenrod', outline='light goldenrod'),
    canvas.create_rectangle(244, 269, 259, 272, fill='light goldenrod', outline='light goldenrod'),
    canvas.create_rectangle(247, 272, 256, 275, fill='light goldenrod', outline='light goldenrod'),
    canvas.create_rectangle(247, 261, 249, 268, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(250, 269, 252, 271, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(253, 261, 255, 268, fill='white', outline='white'),
    canvas.create_rectangle(250, 258, 252, 260, fill='white', outline='white')
]

gold_coin3=[
    canvas.create_rectangle(307, 248, 316, 251, fill='black', outline='black'),
    canvas.create_rectangle(316, 251, 322, 254, fill='black', outline='black'),
    canvas.create_rectangle(322, 254, 325, 260, fill='black', outline='black'),
    canvas.create_rectangle(325, 260, 328, 269, fill='black', outline='black'),
    canvas.create_rectangle(322, 269, 325, 275, fill='black', outline='black'),
    canvas.create_rectangle(316, 275, 322, 278, fill='black', outline='black'),
    canvas.create_rectangle(307, 278, 316, 281, fill='black', outline='black'),
    canvas.create_rectangle(301, 275, 307, 278, fill='black', outline='black'),
    canvas.create_rectangle(298, 269, 301, 275, fill='black', outline='black'),
    canvas.create_rectangle(295, 260, 298, 269, fill='black', outline='black'),
    canvas.create_rectangle(298, 254, 301, 260, fill='black', outline='black'),
    canvas.create_rectangle(301, 251, 307, 254, fill='black', outline='black'),
    canvas.create_rectangle(307, 275, 316, 278, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(301, 272, 307, 275, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(301, 269, 304, 272, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(298, 260, 301, 269, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(316, 272, 322, 275, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(319, 269, 322, 272, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(307, 251, 316, 254, fill='white', outline='white'),
    canvas.create_rectangle(301, 254, 307, 257, fill='white', outline='white'),
    canvas.create_rectangle(301, 257, 304, 260, fill='white', outline='white'),
    canvas.create_rectangle(316, 254, 322, 257, fill='white', outline='white'),
    canvas.create_rectangle(319, 257, 322, 260, fill='white', outline='white'),
    canvas.create_rectangle(322, 260, 325, 269, fill='white', outline='white'),
    canvas.create_rectangle(301, 260, 322, 269, fill='light goldenrod', outline='light goldenrod'),
    canvas.create_rectangle(304, 257, 319, 260, fill='light goldenrod', outline='light goldenrod'),
    canvas.create_rectangle(307, 254, 316, 257, fill='light goldenrod', outline='light goldenrod'),
    canvas.create_rectangle(304, 269, 319, 272, fill='light goldenrod', outline='light goldenrod'),
    canvas.create_rectangle(307, 272, 316, 275, fill='light goldenrod', outline='light goldenrod'),
    canvas.create_rectangle(307, 261, 309, 268, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(310, 269, 312, 271, fill='goldenrod2', outline='goldenrod2'),
    canvas.create_rectangle(313, 261, 315, 268, fill='white', outline='white'),
    canvas.create_rectangle(310, 258, 312, 260, fill='white', outline='white')
]

silver_coin1=[
    canvas.create_rectangle(187, 248, 196, 251, fill='black', outline='black'),
    canvas.create_rectangle(196, 251, 202, 254, fill='black', outline='black'),
    canvas.create_rectangle(202, 254, 205, 260, fill='black', outline='black'),
    canvas.create_rectangle(205, 260, 208, 269, fill='black', outline='black'),
    canvas.create_rectangle(202, 269, 205, 275, fill='black', outline='black'),
    canvas.create_rectangle(196, 275, 202, 278, fill='black', outline='black'),
    canvas.create_rectangle(187, 278, 196, 281, fill='black', outline='black'),
    canvas.create_rectangle(181, 275, 187, 278, fill='black', outline='black'),
    canvas.create_rectangle(178, 269, 181, 275, fill='black', outline='black'),
    canvas.create_rectangle(175, 260, 178, 269, fill='black', outline='black'),
    canvas.create_rectangle(178, 254, 181, 260, fill='black', outline='black'),
    canvas.create_rectangle(181, 251, 187, 254, fill='black', outline='black'),
    canvas.create_rectangle(187, 275, 196, 278, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(181, 272, 187, 275, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(181, 269, 184, 272, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(178, 260, 181, 269, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(196, 272, 202, 275, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(199, 269, 202, 272, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(187, 251, 196, 254, fill='white', outline='white'),
    canvas.create_rectangle(181, 254, 187, 257, fill='white', outline='white'),
    canvas.create_rectangle(181, 257, 184, 260, fill='white', outline='white'),
    canvas.create_rectangle(196, 254, 202, 257, fill='white', outline='white'),
    canvas.create_rectangle(199, 257, 202, 260, fill='white', outline='white'),
    canvas.create_rectangle(202, 260, 205, 269, fill='white', outline='white'),
    canvas.create_rectangle(181, 260, 202, 269, fill='LightSteelBlue1', outline='LightSteelBlue1'),
    canvas.create_rectangle(184, 257, 199, 260, fill='LightSteelBlue1', outline='LightSteelBlue1'),
    canvas.create_rectangle(187, 254, 196, 257, fill='LightSteelBlue1', outline='LightSteelBlue1'),
    canvas.create_rectangle(184, 269, 199, 272, fill='LightSteelBlue1', outline='LightSteelBlue1'),
    canvas.create_rectangle(187, 272, 196, 275, fill='LightSteelBlue1', outline='LightSteelBlue1'),
    canvas.create_rectangle(187, 261, 189, 268, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(190, 269, 192, 271, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(193, 261, 195, 268, fill='white', outline='white'),
    canvas.create_rectangle(190, 258, 192, 260, fill='white', outline='white')
]

silver_coin2=[
    canvas.create_rectangle(247, 248, 256, 251, fill='black', outline='black'),
    canvas.create_rectangle(256, 251, 262, 254, fill='black', outline='black'),
    canvas.create_rectangle(262, 254, 265, 260, fill='black', outline='black'),
    canvas.create_rectangle(265, 260, 268, 269, fill='black', outline='black'),
    canvas.create_rectangle(262, 269, 265, 275, fill='black', outline='black'),
    canvas.create_rectangle(256, 275, 262, 278, fill='black', outline='black'),
    canvas.create_rectangle(247, 278, 256, 281, fill='black', outline='black'),
    canvas.create_rectangle(241, 275, 247, 278, fill='black', outline='black'),
    canvas.create_rectangle(238, 269, 241, 275, fill='black', outline='black'),
    canvas.create_rectangle(235, 260, 238, 269, fill='black', outline='black'),
    canvas.create_rectangle(238, 254, 241, 260, fill='black', outline='black'),
    canvas.create_rectangle(241, 251, 247, 254, fill='black', outline='black'),
    canvas.create_rectangle(247, 275, 256, 278, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(241, 272, 247, 275, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(241, 269, 244, 272, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(238, 260, 241, 269, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(256, 272, 262, 275, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(259, 269, 262, 272, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(247, 251, 256, 254, fill='white', outline='white'),
    canvas.create_rectangle(241, 254, 247, 257, fill='white', outline='white'),
    canvas.create_rectangle(241, 257, 244, 260, fill='white', outline='white'),
    canvas.create_rectangle(256, 254, 262, 257, fill='white', outline='white'),
    canvas.create_rectangle(259, 257, 262, 260, fill='white', outline='white'),
    canvas.create_rectangle(262, 260, 265, 269, fill='white', outline='white'),
    canvas.create_rectangle(241, 260, 262, 269, fill='LightSteelBlue1', outline='LightSteelBlue1'),
    canvas.create_rectangle(244, 257, 259, 260, fill='LightSteelBlue1', outline='LightSteelBlue1'),
    canvas.create_rectangle(247, 254, 256, 257, fill='LightSteelBlue1', outline='LightSteelBlue1'),
    canvas.create_rectangle(244, 269, 259, 272, fill='LightSteelBlue1', outline='LightSteelBlue1'),
    canvas.create_rectangle(247, 272, 256, 275, fill='LightSteelBlue1', outline='LightSteelBlue1'),
    canvas.create_rectangle(247, 261, 249, 268, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(250, 269, 252, 271, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(253, 261, 255, 268, fill='white', outline='white'),
    canvas.create_rectangle(250, 258, 252, 260, fill='white', outline='white')
]

silver_coin3=[
    canvas.create_rectangle(307, 248, 316, 251, fill='black', outline='black'),
    canvas.create_rectangle(316, 251, 322, 254, fill='black', outline='black'),
    canvas.create_rectangle(322, 254, 325, 260, fill='black', outline='black'),
    canvas.create_rectangle(325, 260, 328, 269, fill='black', outline='black'),
    canvas.create_rectangle(322, 269, 325, 275, fill='black', outline='black'),
    canvas.create_rectangle(316, 275, 322, 278, fill='black', outline='black'),
    canvas.create_rectangle(307, 278, 316, 281, fill='black', outline='black'),
    canvas.create_rectangle(301, 275, 307, 278, fill='black', outline='black'),
    canvas.create_rectangle(298, 269, 301, 275, fill='black', outline='black'),
    canvas.create_rectangle(295, 260, 298, 269, fill='black', outline='black'),
    canvas.create_rectangle(298, 254, 301, 260, fill='black', outline='black'),
    canvas.create_rectangle(301, 251, 307, 254, fill='black', outline='black'),
    canvas.create_rectangle(307, 275, 316, 278, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(301, 272, 307, 275, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(301, 269, 304, 272, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(298, 260, 301, 269, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(316, 272, 322, 275, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(319, 269, 322, 272, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(307, 251, 316, 254, fill='white', outline='white'),
    canvas.create_rectangle(301, 254, 307, 257, fill='white', outline='white'),
    canvas.create_rectangle(301, 257, 304, 260, fill='white', outline='white'),
    canvas.create_rectangle(316, 254, 322, 257, fill='white', outline='white'),
    canvas.create_rectangle(319, 257, 322, 260, fill='white', outline='white'),
    canvas.create_rectangle(322, 260, 325, 269, fill='white', outline='white'),
    canvas.create_rectangle(301, 260, 322, 269, fill='LightSteelBlue1', outline='LightSteelBlue1'),
    canvas.create_rectangle(304, 257, 319, 260, fill='LightSteelBlue1', outline='LightSteelBlue1'),
    canvas.create_rectangle(307, 254, 316, 257, fill='LightSteelBlue1', outline='LightSteelBlue1'),
    canvas.create_rectangle(304, 269, 319, 272, fill='LightSteelBlue1', outline='LightSteelBlue1'),
    canvas.create_rectangle(307, 272, 316, 275, fill='LightSteelBlue1', outline='LightSteelBlue1'),
    canvas.create_rectangle(307, 261, 309, 268, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(310, 269, 312, 271, fill='LightSteelBlue3', outline='LightSteelBlue3'),
    canvas.create_rectangle(313, 261, 315, 268, fill='white', outline='white'),
    canvas.create_rectangle(310, 258, 312, 260, fill='white', outline='white')
]

diamond1=[
    canvas.create_rectangle(186, 280, 198, 283, fill='black', outline='black'),
    canvas.create_rectangle(183, 277, 186, 280, fill='black', outline='black'),
    canvas.create_rectangle(180, 274, 183, 277, fill='black', outline='black'),
    canvas.create_rectangle(177, 256, 180, 274, fill='black', outline='black'),
    canvas.create_rectangle(180, 253, 183, 256, fill='black', outline='black'),
    canvas.create_rectangle(183, 250, 186, 253, fill='black', outline='black'),
    canvas.create_rectangle(186, 247, 198, 250, fill='black', outline='black'),
    canvas.create_rectangle(198, 250, 201, 253, fill='black', outline='black'),
    canvas.create_rectangle(201, 253, 204, 256, fill='black', outline='black'),
    canvas.create_rectangle(204, 256, 207, 274, fill='black', outline='black'),
    canvas.create_rectangle(201, 274, 204, 277, fill='black', outline='black'),
    canvas.create_rectangle(198, 277, 201, 280, fill='black', outline='black'),
    canvas.create_rectangle(198, 271, 204, 274, fill='DeepSkyBlue2', outline='DeepSkyBlue2'),
    canvas.create_rectangle(198, 274, 201, 277, fill='DeepSkyBlue2', outline='DeepSkyBlue2'),
    canvas.create_rectangle(180, 256, 186, 259, fill='cornflower blue', outline='cornflower blue'),
    canvas.create_rectangle(183, 253, 186, 256, fill='cornflower blue', outline='cornflower blue'),
    canvas.create_rectangle(198, 256, 204, 262, fill='white', outline='white'),
    canvas.create_rectangle(198, 253, 201, 256, fill='white', outline='white'),
    canvas.create_rectangle(186, 250, 198, 259, fill='cyan', outline='cyan'),
    canvas.create_rectangle(198, 262, 204, 271, fill='cyan', outline='cyan'),
    canvas.create_rectangle(180, 271, 186, 274, fill='RoyalBlue3', outline='RoyalBlue3'),
    canvas.create_rectangle(183, 274, 186, 277, fill='RoyalBlue3', outline='RoyalBlue3'),
    canvas.create_rectangle(180, 259, 186, 271, fill='DeepSkyBlue2', outline='DeepSkyBlue2'),
    canvas.create_rectangle(186, 271, 198, 280, fill='RoyalBlue4', outline='RoyalBlue4'),
    canvas.create_rectangle(186, 259, 198, 271, fill='RoyalBlue3', outline='RoyalBlue3'),
    canvas.create_rectangle(192, 259, 198, 265, fill='white', outline='white'),
    canvas.create_rectangle(190, 265, 192, 267, fill='white', outline='white'),
]

diamond2=[
    canvas.create_rectangle(246, 280, 258, 283, fill='black', outline='black'),
    canvas.create_rectangle(243, 277, 246, 280, fill='black', outline='black'),
    canvas.create_rectangle(240, 274, 243, 277, fill='black', outline='black'),
    canvas.create_rectangle(237, 256, 240, 274, fill='black', outline='black'),
    canvas.create_rectangle(240, 253, 243, 256, fill='black', outline='black'),
    canvas.create_rectangle(243, 250, 246, 253, fill='black', outline='black'),
    canvas.create_rectangle(246, 247, 258, 250, fill='black', outline='black'),
    canvas.create_rectangle(258, 250, 261, 253, fill='black', outline='black'),
    canvas.create_rectangle(261, 253, 264, 256, fill='black', outline='black'),
    canvas.create_rectangle(264, 256, 267, 274, fill='black', outline='black'),
    canvas.create_rectangle(261, 274, 264, 277, fill='black', outline='black'),
    canvas.create_rectangle(258, 277, 261, 280, fill='black', outline='black'),
    canvas.create_rectangle(258, 271, 264, 274, fill='DeepSkyBlue2', outline='DeepSkyBlue2'),
    canvas.create_rectangle(258, 274, 261, 277, fill='DeepSkyBlue2', outline='DeepSkyBlue2'),
    canvas.create_rectangle(240, 256, 246, 259, fill='cornflower blue', outline='cornflower blue'),
    canvas.create_rectangle(243, 253, 246, 256, fill='cornflower blue', outline='cornflower blue'),
    canvas.create_rectangle(258, 256, 264, 262, fill='white', outline='white'),
    canvas.create_rectangle(258, 253, 261, 256, fill='white', outline='white'),
    canvas.create_rectangle(246, 250, 258, 259, fill='cyan', outline='cyan'),
    canvas.create_rectangle(258, 262, 264, 271, fill='cyan', outline='cyan'),
    canvas.create_rectangle(240, 271, 246, 274, fill='RoyalBlue3', outline='RoyalBlue3'),
    canvas.create_rectangle(243, 274, 246, 277, fill='RoyalBlue3', outline='RoyalBlue3'),
    canvas.create_rectangle(240, 259, 246, 271, fill='DeepSkyBlue2', outline='DeepSkyBlue2'),
    canvas.create_rectangle(246, 271, 258, 280, fill='RoyalBlue4', outline='RoyalBlue4'),
    canvas.create_rectangle(246, 259, 258, 271, fill='RoyalBlue3', outline='RoyalBlue3'),
    canvas.create_rectangle(252, 259, 258, 265, fill='white', outline='white'),
    canvas.create_rectangle(250, 265, 252, 267, fill='white', outline='white'),
]

diamond3=[
    canvas.create_rectangle(306, 280, 318, 283, fill='black', outline='black'),
    canvas.create_rectangle(303, 277, 306, 280, fill='black', outline='black'),
    canvas.create_rectangle(300, 274, 303, 277, fill='black', outline='black'),
    canvas.create_rectangle(297, 256, 300, 274, fill='black', outline='black'),
    canvas.create_rectangle(300, 253, 303, 256, fill='black', outline='black'),
    canvas.create_rectangle(303, 250, 306, 253, fill='black', outline='black'),
    canvas.create_rectangle(306, 247, 318, 250, fill='black', outline='black'),
    canvas.create_rectangle(318, 250, 321, 253, fill='black', outline='black'),
    canvas.create_rectangle(321, 253, 324, 256, fill='black', outline='black'),
    canvas.create_rectangle(324, 256, 327, 274, fill='black', outline='black'),
    canvas.create_rectangle(321, 274, 324, 277, fill='black', outline='black'),
    canvas.create_rectangle(318, 277, 321, 280, fill='black', outline='black'),
    canvas.create_rectangle(318, 271, 324, 274, fill='DeepSkyBlue2', outline='DeepSkyBlue2'),
    canvas.create_rectangle(318, 274, 321, 277, fill='DeepSkyBlue2', outline='DeepSkyBlue2'),
    canvas.create_rectangle(300, 256, 306, 259, fill='cornflower blue', outline='cornflower blue'),
    canvas.create_rectangle(303, 253, 306, 256, fill='cornflower blue', outline='cornflower blue'),
    canvas.create_rectangle(318, 256, 324, 262, fill='white', outline='white'),
    canvas.create_rectangle(318, 253, 321, 256, fill='white', outline='white'),
    canvas.create_rectangle(306, 250, 318, 259, fill='cyan', outline='cyan'),
    canvas.create_rectangle(318, 262, 324, 271, fill='cyan', outline='cyan'),
    canvas.create_rectangle(300, 271, 306, 274, fill='RoyalBlue3', outline='RoyalBlue3'),
    canvas.create_rectangle(303, 274, 306, 277, fill='RoyalBlue3', outline='RoyalBlue3'),
    canvas.create_rectangle(300, 259, 306, 271, fill='DeepSkyBlue2', outline='DeepSkyBlue2'),
    canvas.create_rectangle(306, 271, 318, 280, fill='RoyalBlue4', outline='RoyalBlue4'),
    canvas.create_rectangle(306, 259, 318, 271, fill='RoyalBlue3', outline='RoyalBlue3'),
    canvas.create_rectangle(312, 259, 318, 265, fill='white', outline='white'),
    canvas.create_rectangle(310, 265, 312, 267, fill='white', outline='white'),
]

seven1=[
    canvas.create_rectangle(183, 278, 198, 281, fill='black', outline='black'),
    canvas.create_rectangle(195, 269, 198, 278, fill='black', outline='black'),
    canvas.create_rectangle(198, 263, 201, 272, fill='black', outline='black'),
    canvas.create_rectangle(201, 248, 204, 266, fill='black', outline='black'),
    canvas.create_rectangle(180, 248, 201, 251, fill='black', outline='black'),
    canvas.create_rectangle(180, 251, 183, 263, fill='black', outline='black'),
    canvas.create_rectangle(183, 260, 192, 263, fill='black', outline='black'),
    canvas.create_rectangle(189, 257, 192, 260, fill='black', outline='black'),
    canvas.create_rectangle(186, 263, 189, 269, fill='black', outline='black'),
    canvas.create_rectangle(183, 266, 186, 278, fill='black', outline='black'),
    canvas.create_rectangle(183, 251, 189, 257, fill='red2', outline='red2'),
    canvas.create_rectangle(183, 257, 189, 260, fill='red4', outline='red4'),
    canvas.create_rectangle(189, 254, 192, 257, fill='red4', outline='red4'),
    canvas.create_rectangle(198, 260, 201, 263, fill='red4', outline='red4'),
    canvas.create_rectangle(195, 266, 198, 269, fill='red4', outline='red4'),
    canvas.create_rectangle(186, 275, 195, 278, fill='red4', outline='red4'),
    canvas.create_rectangle(189, 263, 195, 275, fill='red3', outline='red3'),
    canvas.create_rectangle(186, 269, 189, 275, fill='red3', outline='red3'),
    canvas.create_rectangle(192, 251, 198, 266, fill='red3', outline='red3'),
    canvas.create_rectangle(189, 251, 192, 254, fill='red3', outline='red3'),
    canvas.create_rectangle(198, 251, 201, 260, fill='red3', outline='red3'),
]

seven2=[
    canvas.create_rectangle(243, 278, 258, 281, fill='black', outline='black'),
    canvas.create_rectangle(255, 269, 258, 278, fill='black', outline='black'),
    canvas.create_rectangle(258, 263, 261, 272, fill='black', outline='black'),
    canvas.create_rectangle(261, 248, 264, 266, fill='black', outline='black'),
    canvas.create_rectangle(240, 248, 261, 251, fill='black', outline='black'),
    canvas.create_rectangle(240, 251, 243, 263, fill='black', outline='black'),
    canvas.create_rectangle(243, 260, 252, 263, fill='black', outline='black'),
    canvas.create_rectangle(249, 257, 252, 260, fill='black', outline='black'),
    canvas.create_rectangle(246, 263, 249, 269, fill='black', outline='black'),
    canvas.create_rectangle(243, 266, 246, 278, fill='black', outline='black'),
    canvas.create_rectangle(243, 251, 249, 257, fill='red2', outline='red2'),
    canvas.create_rectangle(243, 257, 249, 260, fill='red4', outline='red4'),
    canvas.create_rectangle(249, 254, 252, 257, fill='red4', outline='red4'),
    canvas.create_rectangle(258, 260, 261, 263, fill='red4', outline='red4'),
    canvas.create_rectangle(255, 266, 258, 269, fill='red4', outline='red4'),
    canvas.create_rectangle(246, 275, 255, 278, fill='red4', outline='red4'),
    canvas.create_rectangle(249, 263, 255, 275, fill='red3', outline='red3'),
    canvas.create_rectangle(246, 269, 249, 275, fill='red3', outline='red3'),
    canvas.create_rectangle(252, 251, 258, 266, fill='red3', outline='red3'),
    canvas.create_rectangle(249, 251, 252, 254, fill='red3', outline='red3'),
    canvas.create_rectangle(258, 251, 261, 260, fill='red3', outline='red3'),
]

seven3=[
    canvas.create_rectangle(303, 278, 318, 281, fill='black', outline='black'),
    canvas.create_rectangle(315, 269, 318, 278, fill='black', outline='black'),
    canvas.create_rectangle(318, 263, 321, 272, fill='black', outline='black'),
    canvas.create_rectangle(321, 248, 324, 266, fill='black', outline='black'),
    canvas.create_rectangle(300, 248, 321, 251, fill='black', outline='black'),
    canvas.create_rectangle(300, 251, 303, 263, fill='black', outline='black'),
    canvas.create_rectangle(303, 260, 312, 263, fill='black', outline='black'),
    canvas.create_rectangle(309, 257, 312, 260, fill='black', outline='black'),
    canvas.create_rectangle(306, 263, 309, 269, fill='black', outline='black'),
    canvas.create_rectangle(303, 266, 306, 278, fill='black', outline='black'),
    canvas.create_rectangle(303, 251, 309, 257, fill='red2', outline='red2'),
    canvas.create_rectangle(303, 257, 309, 260, fill='red4', outline='red4'),
    canvas.create_rectangle(309, 254, 312, 257, fill='red4', outline='red4'),
    canvas.create_rectangle(318, 260, 321, 263, fill='red4', outline='red4'),
    canvas.create_rectangle(315, 266, 318, 269, fill='red4', outline='red4'),
    canvas.create_rectangle(306, 275, 315, 278, fill='red4', outline='red4'),
    canvas.create_rectangle(309, 263, 315, 275, fill='red3', outline='red3'),
    canvas.create_rectangle(306, 269, 309, 275, fill='red3', outline='red3'),
    canvas.create_rectangle(312, 251, 318, 266, fill='red3', outline='red3'),
    canvas.create_rectangle(309, 251, 312, 254, fill='red3', outline='red3'),
    canvas.create_rectangle(318, 251, 321, 260, fill='red3', outline='red3'),
]

canvas.create_rectangle(170, 0, 335, 95, fill='grey93', outline='grey93')
canvas.create_rectangle(140, 103, 360, 158, fill='SlateBlue4', outline='SlateBlue4')
canvas.create_rectangle(228, 88, 273, 93, fill='goldenrod1', outline='goldenrod1')
canvas.create_rectangle(228, 78, 233, 88, fill='goldenrod1', outline='goldenrod1')
canvas.create_rectangle(268, 78, 273, 88, fill='goldenrod1', outline='goldenrod1')
canvas.create_rectangle(228, 68, 233, 78, fill='gold', outline='gold')
canvas.create_rectangle(268, 68, 273, 78, fill='gold', outline='gold')
canvas.create_rectangle(248, 63, 253, 78, fill='gold', outline='gold')
canvas.create_rectangle(243, 73, 248, 83, fill='gold', outline='gold')
canvas.create_rectangle(253, 73, 258, 83, fill='gold', outline='gold')
canvas.create_rectangle(233, 83, 268, 88, fill='gold', outline='gold')
canvas.create_rectangle(233, 78, 238, 83, fill='gold', outline='gold')
canvas.create_rectangle(263, 78, 268, 83, fill='gold', outline='gold')
canvas.create_rectangle(248, 78, 253, 88, fill='goldenrod1', outline='goldenrod1')
canvas.create_rectangle(140, 98, 360, 103, fill='red4', outline='red4')
canvas.create_rectangle(140, 103, 145, 108, fill='red4', outline='red4')
canvas.create_rectangle(355, 103, 360, 108, fill='red4', outline='red4')
canvas.create_rectangle(135, 103, 140, 158, fill='red4', outline='red4')
canvas.create_rectangle(360, 103, 365, 158, fill='red4', outline='red4')
canvas.create_rectangle(140, 153, 145, 158, fill='red4', outline='red4')
canvas.create_rectangle(355, 153, 360, 158, fill='red4', outline='red4')
canvas.create_rectangle(140, 158, 360, 163, fill='red4', outline='red4')
canvas.create_rectangle(355, 168, 360, 188, fill='red4', outline='red4')
canvas.create_rectangle(145, 168, 150, 188, fill='red4', outline='red4')
canvas.create_rectangle(150, 168, 355, 178, fill='DarkOliveGreen4', outline='DarkOliveGreen4')
canvas.create_rectangle(155, 178, 350, 188, fill='DarkOliveGreen3', outline='DarkOliveGreen3')
canvas.create_rectangle(150, 178, 155, 188, fill='DarkOliveGreen2', outline='DarkOliveGreen2')
canvas.create_rectangle(350, 178, 355, 188, fill='DarkOliveGreen2', outline='DarkOliveGreen2')
canvas.create_rectangle(155, 168, 160, 188, fill='dark olive green', outline='dark olive green')
canvas.create_rectangle(345, 168, 350, 188, fill='dark olive green', outline='dark olive green')
canvas.create_rectangle(145, 343, 150, 428, fill='red4', outline='red4')
canvas.create_rectangle(355, 343, 360, 428, fill='red4', outline='red4')
canvas.create_rectangle(150, 428, 355, 433, fill='red4', outline='red4')
canvas.create_rectangle(160, 353, 345, 418, fill='DarkOliveGreen3', outline='DarkOliveGreen3')
canvas.create_rectangle(150, 343, 355, 353, fill='DarkOliveGreen4', outline='DarkOliveGreen4')
canvas.create_rectangle(150, 353, 160, 428, fill='DarkOliveGreen2', outline='DarkOliveGreen2')
canvas.create_rectangle(345, 353, 355, 428, fill='DarkOliveGreen2', outline='DarkOliveGreen2')
canvas.create_rectangle(160, 418, 345, 428, fill='DarkOliveGreen2', outline='DarkOliveGreen2')
canvas.create_rectangle(160, 343, 165, 418, fill='dark olive green', outline='dark olive green')
canvas.create_rectangle(340, 343, 345, 418, fill='dark olive green', outline='dark olive green')
canvas.create_rectangle(190, 388, 315, 393, fill='dark olive green', outline='dark olive green')
canvas.create_rectangle(185, 383, 190, 388, fill='dark olive green', outline='dark olive green')
canvas.create_rectangle(315, 383, 320, 388, fill='dark olive green', outline='dark olive green')
canvas.create_rectangle(195, 373, 310, 378, fill='dark orange', outline='dark orange')
canvas.create_rectangle(195, 368, 310, 373, fill='chocolate3', outline='chocolate3')
canvas.create_rectangle(185, 358, 320, 368, fill='gold', outline='gold')
canvas.create_rectangle(185, 368, 195, 383, fill='gold', outline='gold')
canvas.create_rectangle(310, 368, 320, 383, fill='gold', outline='gold')
canvas.create_rectangle(190, 378, 315, 388, fill='gold', outline='gold')
canvas.create_rectangle(155, 203, 350, 208, fill='red4', outline='red4')
canvas.create_rectangle(150, 208, 355, 213, fill='red4', outline='red4')
canvas.create_rectangle(155, 323, 350, 328, fill='red4', outline='red4')
canvas.create_rectangle(150, 318, 355, 323, fill='red4', outline='red4')
canvas.create_rectangle(150, 213, 160, 318, fill='red4', outline='red4')
canvas.create_rectangle(345, 213, 355, 318, fill='red4', outline='red4')
canvas.create_rectangle(145, 203, 150, 328, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(135, 198, 140, 333, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(355, 203, 360, 328, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(365, 198, 370, 333, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(150, 203, 355, 198, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(145, 193, 360, 188, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(140, 193, 150, 198, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(355, 193, 365, 198, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(140, 198, 145, 203, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(360, 198, 365, 203, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(150, 203, 155, 208, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(350, 203, 355, 208, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(150, 323, 155, 328, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(350, 323, 355, 328, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(150, 328, 355, 333, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(145, 338, 360, 343, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(140, 333, 150, 338, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(140, 328, 145, 333, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(355, 333, 365, 338, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(360, 328, 365, 333, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(140, 93, 360, 98, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(135, 98, 140, 103, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(360, 98, 365, 103, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(130, 103, 135, 158, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(365, 103, 370, 158, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(135, 158, 140, 163, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(360, 158, 365, 163, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(140, 163, 360, 168, fill='firebrick1', outline='firebrick1')
canvas.create_rectangle(150, 193, 355, 198, fill='red4', outline='red4')
canvas.create_rectangle(145, 198, 150, 203, fill='red4', outline='red4')
canvas.create_rectangle(355, 198, 360, 203, fill='red4', outline='red4')
canvas.create_rectangle(140, 203, 145, 328, fill='red4', outline='red4')
canvas.create_rectangle(360, 203, 365, 328, fill='red4', outline='red4')
canvas.create_rectangle(145, 328, 150, 333, fill='red4', outline='red4')
canvas.create_rectangle(355, 328, 360, 333, fill='red4', outline='red4')
canvas.create_rectangle(150, 333, 355, 338, fill='red4', outline='red4')

canvas.create_rectangle(160, 213, 345, 218, fill='gold', outline='gold')
canvas.create_rectangle(160, 313, 345, 318, fill='gold', outline='gold')

canvas.create_rectangle(160, 218, 165, 313, fill='gold', outline='gold')
canvas.create_rectangle(220, 218, 225, 313, fill='gold', outline='gold')

#canvas.create_rectangle(192.5, 265.5, 192.5, 265.5, fill='black')
#canvas.create_rectangle(252.5, 265.5, 252.5, 265.5, fill='black')
#canvas.create_rectangle(312.5, 265.5, 312.5, 265.5, fill='black')

canvas.create_rectangle(280, 218, 285, 313, fill='gold', outline='gold')
canvas.create_rectangle(340, 218, 345, 313, fill='gold', outline='gold')

canvas.create_rectangle(380, 263, 385, 268, fill='goldenrod1', outline='goldenrod1')
canvas.create_rectangle(370, 248, 375, 283, fill='goldenrod2', outline='goldenrod2')
canvas.create_rectangle(375, 253, 380, 278, fill='goldenrod2', outline='goldenrod2')

light_top=[
    canvas.create_rectangle(150, 93, 155, 98, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(165, 93, 170, 98, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(180, 93, 185, 98, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(195, 93, 200, 98, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(210, 93, 215, 98, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(225, 93, 230, 98, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(240, 93, 245, 98, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(255, 93, 260, 98, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(270, 93, 275, 98, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(285, 93, 290, 98, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(300, 93, 305, 98, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(315, 93, 320, 98, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(330, 93, 335, 98, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(345, 93, 350, 98, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(360, 98, 365, 103, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(365, 113, 370, 118, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(365, 128, 370, 133, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(365, 143, 370, 148, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(360, 158, 365, 163, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(345, 163, 350, 168, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(330, 163, 335, 168, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(315, 163, 320, 168, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(300, 163, 305, 168, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(285, 163, 290, 168, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(270, 163, 275, 168, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(255, 163, 260, 168, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(240, 163, 245, 168, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(225, 163, 230, 168, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(210, 163, 215, 168, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(195, 163, 200, 168, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(180, 163, 185, 168, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(165, 163, 170, 168, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(150, 163, 155, 168, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(135, 158, 140, 163, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(130, 143, 135, 148, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(130, 128, 135, 133, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(130, 113, 135, 118, fill='yellow', outline='firebrick1'),
    canvas.create_rectangle(135, 98, 140, 103, fill='yellow', outline='firebrick1')
]

position_top=[
    (
        (150, 93, 155, 98),
        (165, 93, 170, 98),
        (180, 93, 185, 98),
        (195, 93, 200, 98),
        (210, 93, 215, 98),
        (225, 93, 230, 98),
        (240, 93, 245, 98),
        (255, 93, 260, 98),
        (270, 93, 275, 98),
        (285, 93, 290, 98),
        (300, 93, 305, 98),
        (315, 93, 320, 98),
        (330, 93, 335, 98),
        (345, 93, 350, 98),
        (360, 98, 365, 103),
        (365, 113, 370, 118),
        (365, 128, 370, 133),
        (365, 143, 370, 148),
        (360, 158, 365, 163),
        (345, 163, 350, 168),
        (330, 163, 335, 168),
        (315, 163, 320, 168),
        (300, 163, 305, 168),
        (285, 163, 290, 168),
        (270, 163, 275, 168),
        (255, 163, 260, 168),
        (240, 163, 245, 168),
        (225, 163, 230, 168),
        (210, 163, 215, 168),
        (195, 163, 200, 168),
        (180, 163, 185, 168),
        (165, 163, 170, 168),
        (150, 163, 155, 168),
        (135, 158, 140, 163),
        (130, 143, 135, 148),
        (130, 128, 135, 133),
        (130, 113, 135, 118),
        (135, 98, 140, 103)
    ),
    (
        (155, 93, 160, 98),
        (170, 93, 175, 98),
        (185, 93, 190, 98),
        (200, 93, 205, 98),
        (215, 93, 220, 98),
        (230, 93, 235, 98),
        (245, 93, 250, 98),
        (260, 93, 265, 98),
        (275, 93, 280, 98),
        (290, 93, 295, 98),
        (305, 93, 310, 98),
        (320, 93, 325, 98),
        (335, 93, 340, 98),
        (350, 93, 355, 98),
        (365, 103, 370, 108),
        (365, 118, 370, 123),
        (365, 133, 370, 138),
        (365, 148, 370, 153),
        (355, 163, 360, 168),
        (340, 163, 345, 168),
        (325, 163, 330, 168),
        (310, 163, 315, 168),
        (295, 163, 300, 168),
        (280, 163, 285, 168),
        (265, 163, 270, 168),
        (250, 163, 255, 168),
        (235, 163, 240, 168),
        (220, 163, 225, 168),
        (205, 163, 210, 168),
        (190, 163, 195, 168),
        (175, 163, 180, 168),
        (160, 163, 165, 168),
        (145, 163, 150, 168),
        (130, 153, 135, 158),
        (130, 138, 135, 143),
        (130, 123, 135, 128),
        (130, 108, 135, 113),
        (140, 93, 145, 98)
    ),
    (
        (160, 93, 165, 98),
        (175, 93, 180, 98),
        (190, 93, 195, 98),
        (205, 93, 210, 98),
        (220, 93, 225, 98),
        (235, 93, 240, 98),
        (250, 93, 255, 98),
        (265, 93, 270, 98),
        (280, 93, 285, 98),
        (295, 93, 300, 98),
        (310, 93, 315, 98),
        (325, 93, 330, 98),
        (340, 93, 345, 98),
        (355, 93, 360, 98),
        (365, 108, 370, 113),
        (365, 123, 370, 128),
        (365, 138, 370, 143),
        (365, 153, 370, 158),
        (350, 163, 355, 168),
        (335, 163, 340, 168),
        (320, 163, 325, 168),
        (305, 163, 310, 168),
        (290, 163, 295, 168),
        (275, 163, 280, 168),
        (260, 163, 265, 168),
        (245, 163, 250, 168),
        (230, 163, 235, 168),
        (215, 163, 220, 168),
        (200, 163, 205, 168),
        (185, 163, 190, 168),
        (170, 163, 175, 168),
        (155, 163, 160, 168),
        (140, 163, 145, 168),
        (130, 148, 135, 153),
        (130, 133, 135, 138),
        (130, 118, 135, 123),
        (130, 103, 135, 108),
        (145, 93, 150, 98)
    )
]

def move_top():
    for i in range(len(light_top)):
        canvas.coords(light_top[i], position_top[0][i])
    position_top.append(position_top.pop(0))
    canvas.after(80, move_top)

light_bottom=[
    canvas.create_rectangle(150, 193, 155, 198, fill='yellow', outline='red4'),
    canvas.create_rectangle(165, 193, 170, 198, fill='yellow', outline='red4'),
    canvas.create_rectangle(180, 193, 185, 198, fill='yellow', outline='red4'),
    canvas.create_rectangle(195, 193, 200, 198, fill='yellow', outline='red4'),
    canvas.create_rectangle(210, 193, 215, 198, fill='yellow', outline='red4'),
    canvas.create_rectangle(225, 193, 230, 198, fill='yellow', outline='red4'),
    canvas.create_rectangle(240, 193, 245, 198, fill='yellow', outline='red4'),
    canvas.create_rectangle(255, 193, 260, 198, fill='yellow', outline='red4'),
    canvas.create_rectangle(270, 193, 275, 198, fill='yellow', outline='red4'),
    canvas.create_rectangle(285, 193, 290, 198, fill='yellow', outline='red4'),
    canvas.create_rectangle(300, 193, 305, 198, fill='yellow', outline='red4'),
    canvas.create_rectangle(315, 193, 320, 198, fill='yellow', outline='red4'),
    canvas.create_rectangle(330, 193, 335, 198, fill='yellow', outline='red4'),
    canvas.create_rectangle(345, 193, 350, 198, fill='yellow', outline='red4'),
    canvas.create_rectangle(360, 203, 365, 208, fill='yellow', outline='red4'),
    canvas.create_rectangle(360, 218, 365, 223, fill='yellow', outline='red4'),
    canvas.create_rectangle(360, 233, 365, 238, fill='yellow', outline='red4'),
    canvas.create_rectangle(360, 248, 365, 253, fill='yellow', outline='red4'),
    canvas.create_rectangle(360, 263, 365, 268, fill='yellow', outline='red4'),
    canvas.create_rectangle(360, 278, 365, 283, fill='yellow', outline='red4'),
    canvas.create_rectangle(360, 293, 365, 298, fill='yellow', outline='red4'),
    canvas.create_rectangle(360, 308, 365, 313, fill='yellow', outline='red4'),
    canvas.create_rectangle(355, 328, 360, 333, fill='yellow', outline='red4'),
    canvas.create_rectangle(340, 333, 345, 338, fill='yellow', outline='red4'),
    canvas.create_rectangle(325, 333, 330, 338, fill='yellow', outline='red4'),
    canvas.create_rectangle(310, 333, 315, 338, fill='yellow', outline='red4'),
    canvas.create_rectangle(295, 333, 300, 338, fill='yellow', outline='red4'),
    canvas.create_rectangle(280, 333, 285, 338, fill='yellow', outline='red4'),
    canvas.create_rectangle(265, 333, 270, 338, fill='yellow', outline='red4'),
    canvas.create_rectangle(250, 333, 255, 338, fill='yellow', outline='red4'),
    canvas.create_rectangle(235, 333, 240, 338, fill='yellow', outline='red4'),
    canvas.create_rectangle(220, 333, 225, 338, fill='yellow', outline='red4'),
    canvas.create_rectangle(205, 333, 210, 338, fill='yellow', outline='red4'),
    canvas.create_rectangle(190, 333, 195, 338, fill='yellow', outline='red4'),
    canvas.create_rectangle(175, 333, 180, 338, fill='yellow', outline='red4'),
    canvas.create_rectangle(160, 333, 165, 338, fill='yellow', outline='red4'),
    canvas.create_rectangle(145, 328, 150, 333, fill='yellow', outline='red4'),
    canvas.create_rectangle(140, 313, 145, 318, fill='yellow', outline='red4'),
    canvas.create_rectangle(140, 298, 145, 303, fill='yellow', outline='red4'),
    canvas.create_rectangle(140, 283, 145, 288, fill='yellow', outline='red4'),
    canvas.create_rectangle(140, 268, 145, 273, fill='yellow', outline='red4'),
    canvas.create_rectangle(140, 253, 145, 258, fill='yellow', outline='red4'),
    canvas.create_rectangle(140, 238, 145, 243, fill='yellow', outline='red4'),
    canvas.create_rectangle(140, 223, 145, 228, fill='yellow', outline='red4'),
    canvas.create_rectangle(140, 208, 145, 213, fill='yellow', outline='red4')
]

position_bottom=[
    (
        (150, 193, 155, 198),
        (165, 193, 170, 198),
        (180, 193, 185, 198),
        (195, 193, 200, 198),
        (210, 193, 215, 198),
        (225, 193, 230, 198),
        (240, 193, 245, 198),
        (255, 193, 260, 198),
        (270, 193, 275, 198),
        (285, 193, 290, 198),
        (300, 193, 305, 198),
        (315, 193, 320, 198),
        (330, 193, 335, 198),
        (345, 193, 350, 198),
        (360, 205, 365, 210),
        (360, 220, 365, 225),
        (360, 235, 365, 240),
        (360, 250, 365, 255),
        (360, 265, 365, 270),
        (360, 280, 365, 285),
        (360, 295, 365, 300),
        (360, 310, 365, 315),
        (355, 328, 360, 333),
        (340, 333, 345, 338),
        (325, 333, 330, 338),
        (310, 333, 315, 338),
        (295, 333, 300, 338),
        (280, 333, 285, 338),
        (265, 333, 270, 338),
        (250, 333, 255, 338),
        (235, 333, 240, 338),
        (220, 333, 225, 338),
        (205, 333, 210, 338),
        (190, 333, 195, 338),
        (175, 333, 180, 338),
        (160, 333, 165, 338),
        (145, 328, 150, 333),
        (140, 313, 145, 318),
        (140, 298, 145, 303),
        (140, 283, 145, 288),
        (140, 268, 145, 273),
        (140, 253, 145, 258),
        (140, 238, 145, 243),
        (140, 223, 145, 228),
        (140, 208, 145, 213)
    ),
    (
        (145, 198, 150, 203),
        (160, 193, 165, 198),
        (175, 193, 180, 198),
        (190, 193, 195, 198),
        (205, 193, 210, 198),
        (220, 193, 225, 198),
        (235, 193, 240, 198),
        (250, 193, 255, 198),
        (265, 193, 270, 198),
        (280, 193, 285, 198),
        (295, 193, 300, 198),
        (310, 193, 315, 198),
        (325, 193, 330, 198),
        (340, 193, 345, 198),
        (355, 198, 360, 203),
        (360, 215, 365, 220),
        (360, 230, 365, 235),
        (360, 245, 365, 250),
        (360, 260, 365, 265),
        (360, 275, 365, 280),
        (360, 290, 365, 295),
        (360, 305, 365, 310),
        (360, 320, 365, 325),
        (345, 333, 350, 338),
        (330, 333, 335, 338),
        (315, 333, 320, 338),
        (300, 333, 305, 338),
        (285, 333, 290, 338),
        (270, 333, 275, 338),
        (255, 333, 260, 338),
        (240, 333, 245, 338),
        (225, 333, 230, 338),
        (210, 333, 215, 338),
        (195, 333, 200, 338),
        (180, 333, 185, 338),
        (165, 333, 170, 338),
        (150, 333, 155, 338),
        (140, 318, 145, 323),
        (140, 303, 145, 308),
        (140, 288, 145, 293),
        (140, 273, 145, 278),
        (140, 258, 145, 263),
        (140, 243, 145, 248),
        (140, 228, 145, 233),
        (140, 213, 145, 218)
    ),
    (
        (140, 203, 145, 208),
        (155, 193, 160, 198),
        (170, 193, 175, 198),
        (185, 193, 190, 198),
        (200, 193, 205, 198),
        (215, 193, 220, 198),
        (230, 193, 235, 198),
        (245, 193, 250, 198),
        (260, 193, 265, 198),
        (275, 193, 280, 198),
        (290, 193, 295, 198),
        (305, 193, 310, 198),
        (320, 193, 325, 198),
        (335, 193, 340, 198),
        (350, 193, 355, 198),
        (360, 210, 365, 215),
        (360, 225, 365, 230),
        (360, 240, 365, 245),
        (360, 255, 365, 260),
        (360, 270, 365, 275),
        (360, 285, 365, 290),
        (360, 300, 365, 305),
        (360, 315, 365, 320),
        (350, 333, 355, 338),
        (335, 333, 340, 338),
        (320, 333, 325, 338),
        (305, 333, 310, 338),
        (290, 333, 295, 338),
        (275, 333, 280, 338),
        (260, 333, 265, 338),
        (245, 333, 250, 338),
        (230, 333, 235, 338),
        (215, 333, 220, 338),
        (200, 333, 205, 338),
        (185, 333, 190, 338),
        (170, 333, 175, 338),
        (155, 333, 160, 338),
        (140, 323, 145, 328),
        (140, 308, 145, 313),
        (140, 293, 145, 298),
        (140, 278, 145, 283),
        (140, 263, 145, 268),
        (140, 248, 145, 253),
        (140, 233, 145, 238),
        (140, 218, 145, 223)
    )
]

def move_bottom():
    for i in range(len(light_bottom)):
        canvas.coords(light_bottom[i], position_bottom[0][i])
    position_bottom.append(position_bottom.pop(0))
    canvas.after(80, move_bottom)

grip=[
    canvas.create_rectangle(385, 198, 390, 268, fill='goldenrod1', outline='goldenrod1'),
    canvas.create_rectangle(380, 183, 395, 198, fill='dark red', outline='dark red'),
]

position_grip=[
    (
        (385, 198, 390, 268),
        (380, 183, 395, 198)
    ),
    (
        (385, 208, 390, 268),
        (380, 193, 395, 208)
    ),
    (
        (385, 218, 390, 268),
        (379, 202, 396, 219)
    ),
    (
        (385, 228, 390, 268),
        (379, 212, 396, 229)
    ),
    (
        (385, 238, 390, 268),
        (378, 221, 397, 240)
    ),
    (
        (385, 248, 390, 268),
        (378, 231, 397, 250)
    ),
    (
        (385, 258, 390, 268),
        (377, 240, 398, 261)
    ),
    (
        (385, 258, 390, 268),
        (377, 240, 398, 261)
    ),
    (
        (385, 258, 390, 268),
        (377, 240, 398, 261)
    ),
    (
        (385, 258, 390, 268),
        (377, 240, 398, 261)
    ),
    (
        (385, 258, 390, 268),
        (377, 240, 398, 261)
    ),
    (
        (385, 258, 390, 268),
        (377, 240, 398, 261)
    ),
    (
        (385, 258, 390, 268),
        (377, 240, 398, 261)
    ),
    (
        (385, 258, 390, 268),
        (377, 240, 398, 261)
    ),
    (
        (385, 258, 390, 268),
        (377, 240, 398, 261)
    ),
    (
        (385, 260, 390, 270),
        (377, 255, 398, 276)
    ),
    (
        (385, 263, 390, 273),
        (378, 271, 397, 290)
    ),
    (
        (385, 263, 390, 288),
        (378, 286, 397, 305)
    ),
    (
        (385, 263, 390, 303),
        (379, 302, 396, 319)
    ),
    (
        (385, 263, 390, 318),
        (379, 317, 396, 334)
    ),
    (
        (385, 263, 390, 333),
        (380, 333, 395, 348)
    ),
    (
        (385, 263, 390, 333),
        (380, 333, 395, 348)
    ),
    (
        (385, 263, 390, 333),
        (380, 333, 395, 348)
    ),
    (
        (385, 263, 390, 333),
        (380, 333, 395, 348)
    ),
    (
        (385, 263, 390, 333),
        (380, 333, 395, 348)
    ),
    (
        (385, 263, 390, 333),
        (380, 333, 395, 348)
    ),
    (
        (385, 263, 390, 333),
        (380, 333, 395, 348)
    ),
    (
        (385, 263, 390, 318),
        (380, 318, 395, 333)
    ),
    (
        (385, 263, 390, 303),
        (379, 302, 396, 319)
    ),
    (
        (385, 263, 390, 288),
        (379, 287, 396, 304)
    ),
    (
        (385, 263, 390, 273),
        (378, 271, 397, 290)
    ),
    (
        (385, 253, 390, 271),
        (378, 255, 397, 275)
    ),
    (
        (385, 243, 390, 268),
        (377, 240, 398, 261)
    ),
    (
        (385, 228, 390, 268),
        (377, 226, 398, 245)
    ),
    (
        (385, 213, 390, 268),
        (378, 211, 397, 230)
    ),
    (
        (385, 206, 390, 268),
        (379, 197, 396, 214)
    ),
    (
        (385, 198, 390, 268),
        (380, 183, 395, 198)
    )
]

left=[
    (seven1, 20, [198, 251, 201, 260], 'seven1'),
    (apple1, 2, [190, 261, 193, 264], 'apple1'),
    (gold_coin1, 4, [190, 258, 192, 260], 'gold_coin1'),
    (meet1, 2, [183, 281, 201, 283], 'meet1'),
    (silver_coin1, 4, [190, 258, 192, 260], 'silver_coin1'),
    (cherry1, 2, [195, 266, 197, 268], 'cherry1'),
    (diamond1, 6, [190, 265, 192, 267], 'diamond1')
]

middle=[
    (seven2, 20, [258, 251, 261, 260]),
    (apple2, 2, [250, 261, 253, 264]),
    (gold_coin2, 4, [250, 258, 252, 260]),
    (meet2, 2, [243, 281, 261, 283]),
    (silver_coin2, 4, [250, 258, 252, 260]),
    (cherry2, 2, [255, 266, 257, 268]),
    (diamond2, 6, [250, 265, 252, 267])
]

right=[
    (seven3, 20, [318, 251, 321, 260]),
    (apple3, 2, [310, 261, 313, 264]),
    (gold_coin3, 4, [310, 258, 312, 260]),
    (meet3, 2, [303, 281, 321, 283]),
    (silver_coin3, 4, [310, 258, 312, 260]),
    (cherry3, 2, [315, 266, 317, 268]),
    (diamond3, 6, [310, 265, 312, 267])
]

def randomize(list):
    alea = randint(1, 13)
    for i in range(alea):
        list.append(list.pop(0))

randomize(left)
randomize(middle)
randomize(right)

def initialisation(list):
    for i in range(len(list)):
        for elem in list[i][0]:
            x0, y0, x1, y1 = canvas.coords(elem)
            print(y0, y1)
            canvas.coords(elem, x0, y0-72*i, x1, y1-72*i)

initialisation(left)
initialisation(middle)
initialisation(right)

def reinitia():
    global tour, turn
    turn = [True, True, True]
    tour=0
    root.bind('<space>', start_grip)


turn = [True, True, True]
tour = 0
pixels=0

def move_fruit():
    global tour, pixels
    if turn[0] is True:
        for draw in left:
            if pixels==72:
                left.append(left.pop(0))
            if canvas.coords(draw[0][-1]) == draw[2]:
                if tour > 150:
                        if randint(1, draw[1]) == 1:
                            turn[0]=False
                            tour = 0
            if tour > 300:
                    if canvas.coords(draw[0][-1]) == draw[2]:
                        turn[0]=False
                        tour = 0
            if turn[0] is True:
                for elem in draw[0]:
                    x0, y0, x1, y1=canvas.coords(elem)
                    if y0 > 320:
                        canvas.coords(elem, x0, y0-504, x1, y1-504)
                        x0, y0, x1, y1=canvas.coords(elem)
                    canvas.coords(elem, x0, y0+6, x1, y1+6)
    if turn[1] is True:
        for draw in middle:
            if turn[0] is False:
                if canvas.coords(draw[0][-1]) == draw[2]:
                    if tour > 180:
                            if randint(1, draw[1]) == 1:
                                turn[1]=False
                                tour = 0
                if tour > 350:
                        if canvas.coords(draw[0][-1]) == draw[2]:
                            turn[1]=False
                            tour = 0
            if turn[1] is True:
                for elem in draw[0]:
                    x0, y0, x1, y1=canvas.coords(elem)
                    if y0 > 320:
                        canvas.coords(elem, x0, y0-504, x1, y1-504)
                        x0, y0, x1, y1=canvas.coords(elem)
                    canvas.coords(elem, x0, y0+6, x1, y1+6)
    if turn[2] is True:
        for draw in right:
            if turn[1] is False:
                if canvas.coords(draw[0][-1]) == draw[2]:
                    if tour > 200:
                            if randint(1, draw[1]) == 1:
                                turn[2]=False
                                tour = 0
                if tour > 400:
                        if canvas.coords(draw[0][-1]) == draw[2]:
                            turn[2]=False
                            tour = 0
            if turn[2] is True:
                for elem in draw[0]:
                    x0, y0, x1, y1=canvas.coords(elem)
                    if y0 > 320:
                        canvas.coords(elem, x0, y0-504, x1, y1-504)
                        x0, y0, x1, y1=canvas.coords(elem)
                    canvas.coords(elem, x0, y0+6, x1, y1+6)
        tour += 1
        canvas.after(1, move_fruit)
    else:
        print(left)
        reinitia()

nb = 0
def move_grip():
    global nb
    if nb == len(position_grip)//2:
        move_fruit()
    if nb != len(position_grip):
        for i in range(len(grip)):
            canvas.coords(grip[i], position_grip[0][i])
        position_grip.append(position_grip.pop(0))
        nb += 1
        canvas.after(10, move_grip)

def start_grip(event):
    global nb
    root.unbind('<space>')
    nb = 0
    move_grip()

move_top()
move_bottom()

root.bind('<space>', start_grip)

root.mainloop()
