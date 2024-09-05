import pandas as pd


def read_excel(file, **kwargs) -> list:
    """
    读取表格数据，处理后返回。格式如下
    [{column1: value1, column2: value2},
    {column1: value3, column2: value4},
    {column1: value5, column2: value6}]，
    表格第 1 行为表头，不作为列表项。
    :param file: 要读取的Excel数据文件
    :param kwargs:
    :return: 读取后的表格数据。
    """
    data = []
    try:
        excel_data = pd.read_excel(file, **kwargs)
        data = excel_data.to_dict("records")
        print(data)
    finally:
        return data

