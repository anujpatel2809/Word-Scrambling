# Word-Scrambling
ScramblingModule – Module for scramble word or file
	This module provide facility to scramble words or file.

1)Methods

	1)scrambleFile(file_name)
		This method take a file name as input and generate new scramble file and return path of new scrambled file
	2)scramble(Word)
		This method take word and return scrambled word.

2)Execptions

	1)exception FileNotFoundError :
		Raised when a file or directory is requested but doesn’t exist. Corresponds to errno ENOENT
	2)execption ValueError
		Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as IndexError.
	3)exception BufferError	
		Raised when a buffer related operation cannot be performed.
	4)except EOFError
		Raised when one of the built-in functions (input() or raw_input()) hits an end-of-file condition (EOF) without reading any data. (N.B.: the file.read()and file.readline() methods return an empty string when they hit EOF.)
