import os, time

def play_ascii_frames(folder = "ascii_frames", delay = 0.1):
    frames = sorted(f for f in os.listdir(folder) if f.endswith(".txt"))
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
        with open(os.path.join(folder, frame), encoding = "utf-8") as f:
            print(f.read())
        time.sleep(delay)

if __name__ == "__main__":
    play_ascii_frames()