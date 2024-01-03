# $language = "python"
# $interface = "1.0"

# This script demonstrates how to open a text file and read it line by
# line to a server.


def main():
	
	crt.Screen.Synchronous = True
	# Note: A IOError exception will be generated if the txt file doesn't exist.
	#
	for line in open("C:\\Users\\jared.easley\\Documents\\Test_Scripts\\commands.txt", "r"):
		# Send the line with an appended CR
		#
		crt.Screen.Send(line)
	 
		# Wait for my prompt before sending the next line
		#
		crt.Screen.WaitForString("test@server1")

	crt.Screen.Synchronous = False

	
main()