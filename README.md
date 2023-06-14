# Holter_Analyzer
Program description: this program can help users to open Holter edf files with graphic presentation with opprotunity to save any interval segments and save this data to input file folder.

## First setup:
Firstly you need to import project to your program environment. Next steps:
1. **Open project terminal.** You need to write next command:
  pip --version
2. **Import needed dependencies.** If first command executed successfuly, you can write next command:
  pip install numpy
  pip install matplotlib
  pip install pyedflib
3.** Write full ways to files you want to open.** To make this open with editor file: Holter_Analyzer/start_module/Variables.py and modify next field:
  file_directory = "Copy path to patient holter file here as a text"
  gen_files_dir = "Copy path to empty folder where program will save all info"
4. **Open file:** Holter_Analyzer/start_module/main.py and click **"run main.py".** If all will be ok, after 10-20 seconds you can see console logs
**!Important!** path to the files can not contains cyrillic characters
## Main Menu:
![image](https://github.com/andreyliashko/Holter_Analyzer/assets/47381064/029fb701-cb2c-4ad6-95bb-52f416e5e89a)
1. Main menu
![image](https://github.com/andreyliashko/Holter_Analyzer/assets/47381064/ce93b797-5a62-445d-872f-d49a3b12f9e1)
At the top of the screen you can see graphic scale, what show when this point was registrated.

2. Additional menu
![image](https://github.com/andreyliashko/Holter_Analyzer/assets/47381064/bf1fde1e-9f60-4107-92b0-f1a638ab12c4)
This is python default tools. Here you can scroll heart rhytm, increase and reduce graphic segments, highlight some needed segments.
## Custom setup:
You can modify some setting. To make it, open file: Holter_Analyzer/start_module/Variables.py and change next variables:
 
 1. current_signal = 1 - you can choose what signal will be opened at startup. This variable must be positive integer,and can not be more than signal amount of current file
 2. get_points_in_one_sec = 10 - this variable controls how much data you want to use. Holter files can contain more than 400 points per second, to solve it user can write how many points he/she wants to ignore(for  this value equal to 10 program will use 1 point and ignor next 9). Choose this value multiple to points in one second.
 3. delta_time = 60 - this is period of interval, what describe how many minutes will be displayed at screen. You can choose  this value from 1 minute to 60 minutes. Value must be positive, multiple to 60. Do not recommend to use value more than 60 minutes.
 4. NOT RECCOMEND TO MODIFY
  screen_type = ".pdf"
  text_type = ".txt"
  This value show what object type will be, when user will save some info.
