from kakadu.pykakadu import PyKakadu

# Define Kakadu Base path
kakadu_base_path = '/Library/Kakadu/8.0.5/bin'

# Initiate an instance of PyKakadu
pykakadu = PyKakadu(kakadu_base_path=kakadu_base_path)

# Define in put and Output Directories
input_dir = '/Users/frank/Documents/PyPI/pykakadu'
output_dir = '/Users/frank/Documents/PyPI/pykakadu'

# Convert BigTiff to JP2
pykakadu.tiff2jp2(input_dir=input_dir, output_dir=output_dir)
