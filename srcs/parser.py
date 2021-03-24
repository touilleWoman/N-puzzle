def read_puzzel_file():
    with open("/Users/air/projets/N-puzzle-Algo-A-/npuzzle-3-1.txt") as f:
        lines = f.readlines()
        print(lines)
        puzzel_size = None
        import pdb; pdb.set_trace()

        for line in lines:

            if line.startswith('#'):
                pass
            elif puzzel_size is None: 
                try:
                    puzzel_size = int(line)
                except:
                    Raise SystemExit("Wrong puzzel format, can't find puzzel size")
            else:
                

                
            




if __name__ == '__main__':
    read_puzzel_file()
    