import random


colors = ["\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m", "\033[0;35m", "\033[0;36m", "\033[0;37m", "\033[0;90m", "\033[0;91m", "\033[0;92m", "\033[0;93m", "\033[0;94m", "\033[0;95m", "\033[0;96m", "\033[0;97m"]

def __getattr__(name):
	if name == "red":
		return "\033[0;31m"
	elif name == "green":
		return "\033[0;32m"
	elif name == "yellow":
		return "\033[0;33m"
	elif name == "blue":
		return "\033[0;34m"
	elif name == "magenta":
		return "\033[0;35m"
	elif name == "cyan":
		return "\033[0;36m"
	elif name == "white":
		return "\033[0;37m"
	elif name == "bright_black":
		return "\033[0;90m"
	elif name == "bright_red":
		return "\033[0;91m"
	elif name == "bright_green":
		return "\033[0;92m"
	elif name == "bright_yellow":
		return "\033[0;93m"
	elif name == "bright_blue":
		return "\033[0;94m"
	elif name == "bright_magenta":
		return "\033[0;95m"
	elif name == "bright_cyan":
		return "\033[0;96m"
	elif name == "bright_white":
		return "\033[0;97m"
	elif name == "highlight_black":
		return "\033[0;40m"
	elif name == "highlight_salmon":
		return "\033[0;41m"
	elif name == "highlight_green":
		return "\033[0;42m"
	elif name == "highlight_olive":
		return "\033[0;43m"
	elif name == "highlight_light_blue":
		return "\033[0;44m"
	elif name == "highlight_purple":
		return "\033[0;45m"
	elif name == "highlight_blue":
		return "\033[0;46m"
	elif name == "highlight_white":
		return "\033[0;47m"
	elif name == "colors" or name == "all":
		return colors
	
	raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

def rand_color():
	return random.choice(colors)

def cprint(color, text, endChar="\n"):
	print(color, text, end=endChar)