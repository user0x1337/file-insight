#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


def calc_file_stats(filename, size_bytes=None):
    with open(filename, 'rb') as f:
        data = bytearray(f.read(size_bytes))
    data = np.frombuffer(data, np.uint8)
    byte_frequencies = []
    for i in range(0, 255):
        byte_frequencies.append(len(data[np.where(data == i)]))

    byte_frequencies = np.array(byte_frequencies)
    plt.hist(data, bins=range(0, 256))

    return byte_frequencies.mean(), byte_frequencies.std()


def start():
    mean, std = calc_file_stats("/home/user/Pictures/fSQPGU.png", size_bytes=10000)
    std_percent = int((1 - std/mean) * 10000)/100
    print(f"Mean: {mean}, Std: {std}; Is encrypted: {'probably yes' if std_percent > 90 else 'probably not'} "
          f"(Prediction: {max(std_percent, 0)}%)")

    plt.show()


if __name__ == "__main__":
    start()
