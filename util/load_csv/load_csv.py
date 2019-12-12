import pandas as pd


def load_data(path=""):
    """
        Args:
            path: file path for building location data.

        Returns:
            The function will return pandas dataframe for building location file.

    """
    return pd.read_csv(path)
