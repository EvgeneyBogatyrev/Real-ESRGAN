import os

os.system("chmod -R 0777 /model")

with open("/model/run.sh", 'w') as f:
    f.write("cd model\n")
    f.write("python3 setup.py develop\n")

    videos = os.listdir("/dataset")
    for video in videos:
        f.write(f'mkdir /results/{video}\n')
        f.write(f'python3 inference_realesrgan.py -n RealESRGAN_x4plus --face_enhance --input /dataset/{video} --output /results/{video}\n')

    f.write('chmod -R 0777 /results\n')

os.system("chmod -R 0777 /model")
os.system("/model/run.sh")
