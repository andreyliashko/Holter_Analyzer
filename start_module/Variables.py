from main_program.Time import Time


class FilesConstant:
    file_directory = "D:/holter_files/2@1951-01-31.edf"
    current_signal = 1
    get_points_in_one_sec = 10
    screen_type = ".pdf"
    text_type = ".txt"


class GraphConstant:
    delta_time = 60
    gen_files_dir = "D:/holter_files/file"
    min_peak_height = 400


class autoDeleteGraphConstant:
    where_to_save_file_direction = "D:/holter_files/auto_delete"


class QRSdelete:
    points_amount = 5
    delta_time = Time(0, 0, 1, 0)
