import re


def read_sequences(file_name):
    labels = []
    sequences = []
    with open(file_name, "r") as f:
        for line in f.read().splitlines():
            if line.startswith(">"):
                labels.append(line[1:])
            else:
                sequences.append(line)
    return list(zip(labels, sequences))


def read_patterns(file_name):
    with open(file_name, "r") as f:
        patterns = f.read().splitlines()
    return patterns


if __name__ == "__main__":
    patterns = read_patterns("patterns.txt")
    sequences = read_sequences("sequences.txt")

    for pattern in patterns:
        print(f"\n{pattern} found in ...")
        for label, sequence in sequences:
            matches = [(m.start(0), m.end(0)) for m in re.finditer(pattern, sequence)]
            if matches != []:
                print(label, matches)
