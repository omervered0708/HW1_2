import pandas


def load_data(path, features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    new_data = {}
    for key, value in data.items():
        if key in features:
            new_data[key] = value
    data = new_data
    return data

