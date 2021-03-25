def parser(file):
    """parse puzzel file and return a list containing rows of matrix"""
    
    with open(file) as f:
        lines = f.readlines()
        print(lines)

        puzzel_size = None
        matrix = []

        for line in lines:
            if line.startswith("#"):
                pass
            elif puzzel_size is None:
                try:
                    puzzel_size = int(line)
                except:
                    raise ValueError("Wrong format: can't find puzzel size")
            else:
                row = [int(x) for x in line.split() if x.isdigit()]
                if len(row) != puzzel_size:
                    raise ValueError("Wrong format: matrix column nb wrong")
                matrix.append(row)
        if len(matrix) != puzzel_size:
            raise ValueError("Wrong format: matrix row nb wrong")

    print(matrix)
    return matrix
