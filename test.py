from anthro_lib import ANTHRO

if __name__ == "__main__":
	## Load new ANTHRO object and Process from list of texts
	anthro = ANTHRO()
	text = text = ['democrats', 'demokrats', 'democRATs', 'republicans', 'repubLIEcans', 'republiCUNTs']
	anthro.process(text)
	anthro.statistics()
	anthro.save('./saved')

	## Test
	print(anthro.get_similars('democrats', level=1, distance=5, strict=False))
	print(anthro.get_similars('republicans', level=1, distance=5, strict=False))

	## Load ANTHRO dictionary from external folder
	anthro = ANTHRO()
	anthro.load('./ANTHRO_Data_V1.0')

	## Test
	print(anthro.get_similars('presidents', level=1, distance=5, strict=True))
	print(anthro.get_similars('biden', level=1, distance=5, strict=True))
	print(anthro.get_similars('trump', level=1, distance=5, strict=True))

