import pydivert

def main():
    with pydivert.WinDivert("ip") as w:
        for packet in w:
            print(f"Packet: {packet}")

if __name__ == "__main__":
    main()
