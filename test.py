import os

def file_name(file_dir):
    L = []
    for dirs in os.walk[1](file_dir):
        for dirItem in dirs:
            print("[INFO] dealing with directory {}".format(dirItem))
           # for files in os.walk[2](dirs):
           #     if os.path.splitext(files)[1] = '.mat':
           #         L.append(os.path.join()


           # if os.path.splittext(fileItem)[1] == '.mat':
           #     L.append(os.path.join(root, fileItem))
       # return L

DATA_PATH = "./datasets"
file_name(DATA_PATH)
