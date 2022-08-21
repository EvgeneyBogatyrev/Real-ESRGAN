import os

with open("/model/run.sh", 'w') as f:
    f.write("cd ../model\n")
    f.write("python3 setup.py develop\n")

    videos = os.listdir("/dataset")
    for video in videos:
        f.write(f'mkdir /results/{video}\n')
        f.write(f'python3 inference_realesrgan.py -n RealESRGAN_x4plus --input /dataset/{video} --tile 1024 --output /results/{video}\n')
        f.write(f'ffmpeg -y -i /results/{video}/frame%04d.png -c:v libx264rgb -crf 0 /result/{video}.mp4')
        f.write(f'rm -rf /result/{video}')


os.system("chmod 0777 /model/run.sh")
os.system("/model/run.sh")
