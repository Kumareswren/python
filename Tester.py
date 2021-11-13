import video_library as lib

class CreateVideo():
    def __init__(self, window):
        window.geometry("750x350")
        window.title("Create Videos")

    def check_video_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)