import sys, os
import datetime
sys.path.insert(0,'..')

def main():
    header = '[{}] ({})'.format(os.path.basename(__file__), datetime.datetime.now().time())
    print(header + '\n' + ('='*len(header)))
    # Put quick test code here






if __name__ == '__main__':
    main()