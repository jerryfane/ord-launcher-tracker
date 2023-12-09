import argparse
from HashInscriptionChecker import HashInscriptionChecker

def main():
    parser = argparse.ArgumentParser(description="Run Hash Inscription Checker")
    parser.add_argument('--h', type=str, required=True, help='Path to the hash CSV file')
    parser.add_argument('-f', '--filename', type=str, required=True, help='Filename for the output JSON')
    parser.add_argument('-n', '--asset_name', type=str, default="Test", help='Asset name prefix (default: "Test")')

    args = parser.parse_args()

    checker = HashInscriptionChecker(args.h)
    result = checker.run(args.filename, args.asset_name)
    print(result)

if __name__ == '__main__':
    main()