# Holter_Analyzer
Program description: this program can help users to open Holter edf files with graphic presentation with opportunity to save any interval segments and save this data to input file folder.

## First setup:
Firstly you need to import project to your program environment. Next steps:
1. **Open project terminal.** You need to write next command:
  pip --version
2. **Import needed dependencies.** If first command executed successfuly, you can write next command:
  
 pip install -r requirements.txt
  
  or you can write if by yourself:
  
    pip install numpy
  
    pip install matplotlib
  
    pip install pyedflib
  
3. **Write full ways to files you want to open.** To do this open with editor file: Holter_Analyzer/start_module/Variables.py and modify next field:
  
    file_directory = "Copy path to patient holter file here as a text"
  
    gen_files_dir = "Copy path to empty folder where program will save all info"

    where_to_save_file_direction =""Copy path to empty folder where program will save info with deleted intervals"
  
4. **Open file:** Holter_Analyzer/start_module/main.py and click **"run main.py".** If all will be ok, after 10-20 seconds you can see console logs
**!Important!** The path to the files can not contain Cyrillic characters
  
# Part 1:
## Main Menu:
![image](https://github.com/andreyliashko/Holter_Analyzer/assets/47381064/029fb701-cb2c-4ad6-95bb-52f416e5e89a)
1. Main menu
![image](https://github.com/andreyliashko/Holter_Analyzer/assets/47381064/ce93b797-5a62-445d-872f-d49a3b12f9e1)
At the top of the screen you can see graphic scale, what show when this point was registrated. The next picture shows the current start time of this segment.
  
![image](https://github.com/andreyliashko/Holter_Analyzer/assets/47381064/db187f5b-0fab-4f82-a2b3-b00696caebee)
  
  Also, project has possibility to go to needed segment, what you can choose via a button next and previous, or choose some HOUR, MINUTES or SIGNAL slider and click button Go to.  Later, you can choose segments, what you want to remember, and click button Save, to save the current segment as a list of points, and his graphic of all available signals. Here you can see what data of what format will be saved.
![image](https://github.com/andreyliashko/Holter_Analyzer/assets/47381064/4cf86e23-aeeb-4676-bba2-ae7f6638bf1b)

2. Additional menu
![image](https://github.com/andreyliashko/Holter_Analyzer/assets/47381064/bf1fde1e-9f60-4107-92b0-f1a638ab12c4)
This is python default tools. Here you can scroll heart rhythm, increase and reduce graphic segments, highlight some needed segments.
  
# Part 2:
In this part you can see part of data, with deleted period. Here is an example of a file with 3 deleted sectors.
![image](https://github.com/andreyliashko/Holter_Analyzer/assets/47381064/4ee40cc0-e885-4c4c-9860-f4cec4b5495c)

To perform it, you need to clear start_module/main.py and insert next code:

    autoDelGraph = autoDeleteGraph()
    start = Time()
    finish = Time(2, 0, 0, 0)

    # times period from file can be deleted only once. comment this code after first use
    # start code
    need_to_del = []
    need_to_del.append([Time(_hour=0, _minute=0, _sec=40, _milis=0), Time(_hour=0, _minute=0, _sec=50, _milis=0)])
    need_to_del.append([Time(_hour=0, _minute=0, _sec=0, _milis=0), Time(_hour=0, _minute=0, _sec=10, _milis=0)])
    need_to_del.append([Time(_hour=0, _minute=0, _sec=20, _milis=0), Time(_hour=0, _minute=0, _sec=30, _milis=0)])
    autoDelGraph.deleteData(start, finish, need_to_del)
    # end of code

    autoDelGraph.make_graph(start, finish)

!Attention! File with input time can be deleted and written only once. For the next usage with its input interval, you must clear next code
  
from #start code
  
  ...
    
  to  # end of code.

## Custom setup:
You can modify some setting. To make it, open file: Holter_Analyzer/start_module/Variables.py and change next variables:
   
 1. current_signal = 1 - you can choose what signal will be opened at startup. This variable must be a positive integer, and can not be more than signal amount of current file
 2. get_points_in_one_sec = 10 - this variable controls how much data you want to use. Holter files can contain more than 400 points per second, to solve it user can write, how many points he/she wants to ignore (to  this value equal to 10 the program will use 1 point and ignore next 9). Choose this value multiple two points in one second.
 3. delta_time = 60 - this is period of interval, what describe how many minutes will be displayed on screen. You can choose  this value from 1 minute to 60 minutes. The value must be positive, multiple of 60. Do not recommend to use value more than 60 minutes.
 4. NOT RECCOMEND TO MODIFY  
  screen_type = ".pdf"  
  text_type = ".txt"  
  This value shows what object type will be, when user will save some info.
