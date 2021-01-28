""" ***************************************************************************
# * File Description:                                                         *
# *                                                                           *
# * Python wrapper for Kakadu V8.0.3for converting BigTiff images to JP2.     *
# *                                                                           *
# * --------------------------------------------------------------------------*
# * AUTHORS(S): Frank Ceballos <frank.ceballos123@gmail.com>                  *
# * --------------------------------------------------------------------------*
# * DATE CREATED: January 27, 2021                                            *
# * LAST UPDATE : ----                                                        *
# * --------------------------------------------------------------------------*
# * NOTES:                                                                    *
# * ************************************************************************"""

# To run bash commands
import glob, os
import subprocess


class PyKakadu:
    """
    The PyKakadu class is used to convert BigTiff into JP2. 
                
    Parameters
    ----------
    
    kakadu_base_path: str
        Base path to the bin folder for Kakadu. In Mac OS this can be found 
        in /Library/Kakadu/8.0.5/bin. This folder contains kdu_compress, 
        kdu_expand, kdu_merge, etc.
        

    Example
    -------
    
    
    Attributes
    ----------
    
    None
    
    Author Information
    ------------------
    
    Frank Ceballos
    LinkedIn: <https://www.linkedin.com/in/frank-ceballos/>
    Date: January 27, 2021
    """

    def __init__(self, kakadu_base_path):
        
        self.kakadu_base_path = kakadu_base_path
    
    def tiff2jp2(self, input_dir, output_dir, rate=1.29, num_threads=6):
        """
        Use this function to convert a BigTiff file into JP2 using Kakadu
        in the backend.
                    
        Parameters
        ----------
        
        kakadu_base_path: str
            Base path to the bin folder for Kakadu. In Mac OS this can be found 
            in /Library/Kakadu/8.0.5/bin. This folder contains kdu_compress, 
            kdu_expand, kdu_merge, etc.
        input_dir: str

        output_dir: str

        rate: float, default=1.29
        
        num_threads: int, default=6
            

        Example
        -------
        
        
        Attributes
        ----------
        
        None
        
        Author Information
        ------------------
        
        Frank Ceballos
        LinkedIn: <https://www.linkedin.com/in/frank-ceballos/>
        Date: January 27, 2021
        """

        # Get all tif files
        files = self.get_files(input_dir)
        num_files = len(files)

        # Print message to User
        self.message(num_files, files)

        # Convert every BigTiff file into JP2
        for file in files:
            # Get filename
            filename = file.split('.')[0]
            print(f'-------------------> Now Converting {file} to JP2 <-------------------')
            CONVERT_TO_JP2_LOSSY = f'kdu_compress -i {file} -o {filename}.jp2 '\
                f'-rate {rate}' + ' Cprecincts={128,128} Cblk={64,64} Corder=RPCL Clayers=1'\
                f' ORGgen_plt=yes -num_threads {num_threads} -flush_period 1024'
            subprocess.run(CONVERT_TO_JP2_LOSSY.split())


    def get_files(self, input_dir):
        """ Get all BigTiff files in a directory"""
        # Change directory to input_dir
        os.chdir(input_dir)

        # Get all tif files
        files = [file for file in glob.glob('*.tif')]

        return files

    def message(self, num_files, files):
        # Print message to User
        print('-----------------------------------------------------------------------')
        message = 'Now running PyKakadu V1.0. Use this free Python wrapper'\
            ' at your own risk.\n'\
            ' Kakadu products are proprietary software applications.'
        print(message)
        print(f'A total of {num_files} BigTiff files are going to be converted to JP2')
        print(f'Here is the list of files that are going to be converted:')
        print(files)