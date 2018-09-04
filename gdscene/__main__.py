def tilemap():
    print("Hello, world!")

def main():
    parser = argparse.ArgumentParser(description='Do Something')
    parser.add_argument('-V', '--version', action='version', version='0.1')
    args = parser.parse_args()

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, '')
    main()

