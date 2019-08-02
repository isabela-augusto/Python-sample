import os


def extract_name(name):
    return name.split(".")[0]


def read_lines(filename):
    _file = open(os.path.join("data", "meta-data", filename), "rt")
    data = _file.read().split("\n")
    _file.close()
    return data


def read_metadata(filename):
    metadata = []
    for column in read_lines(filename):
        if column:
            values = column.split('\t')
            nome, tipo, desc = values[:3]
            metadata.append(tuple((nome, tipo, desc)))
        return metadata


def main():
    meta = {}
    for meta_data_file in os.listdir(os.path.join("data", "meta-data")):
        table_name = extract_name(meta_data_file)
        meta[table_name] = read_metadata(meta_data_file)

    for key, value in meta.items():
        print(f"Tabela {key}")
        print(" Attributes: ")
        for col in value:
            print(f" {col[1]}: {col[0]} - {col[2]}")


if __name__ == "__main__":
    main()            

        

    