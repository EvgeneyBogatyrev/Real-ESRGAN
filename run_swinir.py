import os

with open("/model/run_swinir.sh", 'w') as f:
    f.write("cd model\n")
    f.write("python3 setup.py develop\n")

    videos = os.listdir("/dataset")
    for video in videos:
        f.write(f'mkdir /results/{video}\n')
        f.write(f'python3 /model/SwinIR/main_test_swinir.py --task real_sr --model_path /model/experiments/pretrained_models/003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN.pth --folder_lq /dataset/{video} --scale 4 --save_dir /results/{video}\n')

os.system("chmod +x /model/run_swinir.sh")
os.system("/model/run_swinir.sh")
