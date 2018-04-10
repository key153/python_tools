#-*- encoding:UTF-8 -*-
import xlrd
import xlwt


# open excel file
def open_file(file_name):
	file = xlrd.open_workbook(file_name)
	# 读取第一个sheet
	table = file.sheets()[0]
	nrows = table.nrows
	return table, nrows


# get a col data from table
def get_col_data(table, nrows, col_num):
	list_data = []
	for i in range(1,nrows):
		list_data.append(table.row_values(i)[col_num])
	return list_data


# 获取表格中某一列中重复数据的行号
def get_repeat_data(table, nrows, col_num):
	list_repeat_num = []
	list_data = []
	for i in range(1, nrows):
		if table.row_values(i)[col_num] != '':
			if table.row_values(i)[col_num] in list_data:
				list_repeat_num.append(i-1)
			else:
				list_data.append(table.row_values(i)[col_num])
		else:
			continue
	return list_repeat_num


# change pattern style
def change_pattern(style,pattern_fore_colour):
	pattern = xlwt.Pattern()
	pattern.pattern =pattern.SOLID_PATTERN
	pattern.pattern_fore_colour =pattern_fore_colour
	style.pattern = pattern
	return style


# change fone style
def change_fone(style,colour_index,bold,name,underline):
	font = xlwt.Font()
	font.colour_index = colour_index
	font.bold = bold
	font.name = name
	font.underline = underline #xlwt.Font.UNDERLINE_SINGLE
	style.font = font
	return style


# change alignment style
def change_alignment(style,horz,vert):
	alignment = xlwt.Alignment()
	alignment.horz = horz #xlwt.Alignment.HORZ_CENTER
	alignment.vert = vert #xlwt.Alignment.VERT_CENTER
	style.alignment = alignment
	return style


# change borders style
def change_borders(style,bottom_colour):
	borders = xlwt.Borders()
	borders.left = 1
	borders.right = 1
	borders.top = 1
	borders.bottom = 1
	borders.bottom_colour = bottom_colour #0x3A
	style.borders = borders
	return style


def create_style():
	style = xlwt.XFStyle()
	return style


def type_list(num):
	# type1: Add black border around the cell
	if num ==1:
		return change_borders(create_style(), 0x3A)

	# type2: Add black border around the cell, white background colour,red fone,no underline
	elif num ==2:
		return change_fone(change_pattern(change_borders(create_style(), 0x3A), 0x2A), 0, True, 'Arial',
						xlwt.Font.UNDERLINE_NONE)

	# type3: Add black border around the cell,white background colour, blue fone,single underline
	elif num ==3:
		return change_fone(change_borders(create_style(), 0x3A), 4, False, 'Arial', xlwt.Font.UNDERLINE_SINGLE)

	# type4: Add black border around the cell, bule background colour, white fone.
	elif num == 4:
		return change_alignment(change_fone(change_pattern(change_borders(create_style(), 0x3A), 0x36),1, True, 'Arial',
						xlwt.Font.UNDERLINE_NONE),xlwt.Alignment.HORZ_LEFT,xlwt.Alignment.VERT_CENTER)

	# type5:Add black border around the cell,center in horz and vert
	elif num == 5:
		return change_alignment(change_borders(create_style(), 0x3A),
											   xlwt.Alignment.HORZ_CENTER, xlwt.Alignment.VERT_CENTER)

	#
	elif num ==6:
		return change_pattern(change_fone(change_borders(create_style(), 0x3A),1, True, 'Arial',xlwt.Font.UNDERLINE_NONE),0x10)

	else:
		print "No type to choose."