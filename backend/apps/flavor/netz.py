import csv
import re
import pandas as pd


class Parse:
    REPLACE_STRINGS = ["##", "s:1|"]
    csvfile = []
    _xy = None
    _meta = None

    def __init__(self, file, delimter=None):
        self.file = file
        self.delimiter = delimter

    def base(self):
        if isinstance(self.file, str):
            _file = open(self.file)
        else:
            _file = self.file
        if self.delimiter is None:
            self.delimiter = ";"
        import chardet

        decode = chardet.detect(self.file).get("encoding")
        self.file = self.file.decode(decode).splitlines()
        self.csvfile = [
            line for line in csv.reader(self.file, delimiter=self.delimiter) if line
        ]

    def meta(self):
        if self._meta:
            return self._meta
        if not self.csvfile:
            self.base()
        meta_fields = ["RANGE", "SAMPLE", "PROJECT", "SAMPLE MASS /mg"]
        meta_dict = {}
        for field in meta_fields:
            meta_dict[f"{field}"] = [
                x[0]
                for x in map(
                    lambda line_item: re.findall(f"(?<=#{field}:).*$", line_item[0]),
                    self.csvfile,
                )
                if x
            ][0]
            if field == "RANGE":
                meta_dict["RANGE"] = [
                    x for x in re.findall(r"[\d,]*", meta_dict["RANGE"]) if x
                ]
        self._meta = meta_dict
        return self._meta

    def xy(self):
        if self._xy:
            return self._xy
        if not self.csvfile:
            self.base()
        index, columns = [
            (index, line)
            for (index, line) in enumerate(self.csvfile)
            for x in line
            if re.match("##", x)
        ][0]
        for field in self.REPLACE_STRINGS:
            columns = list(map(lambda x: x.replace(f"{field}", ""), columns))
        data = list(zip(*self.csvfile[index + 1 :]))
        data_dict = dict(zip(columns, data))
        self._xy = data_dict
        return self._xy

    def pure(self):
        keys = [x for x in list(self.xy().keys()) if re.search("QMID", x)]
        data = {key: self.xy()[key] for key in keys}
        tops = pd.DataFrame(data)
        top_values = tops.describe()
        top_qmids = top_values.sort_values(by="top", axis=1).iloc[:, :5].columns.values
        name = self.meta().get("SAMPLE")
        if name:
            return list(top_qmids)
        else:
            return None
