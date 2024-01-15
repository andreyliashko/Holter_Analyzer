from main_program.Time import Time


class FilesConstant:
    file_directory = "/home/andrii/Documents/holter/files/2@1951-01-31.edf"
    current_signal = 1
    get_points_in_one_sec = 10
    screen_type = ".pdf"
    text_type = ".txt"


class GraphConstant:
    delta_time = 60
    gen_files_dir = "/home/andrii/Documents/holter/encrypted"
    min_peak_height = 400


class autoDeleteGraphConstant:
    where_to_save_file_direction = "/home/andrii/Documents/holter/auto_delete"


class QRSDelete:
    points_amount = 4
    delta_time = Time(0, 0, 1, 0)
