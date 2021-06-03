#!/bin/python
# coding=utf-8

# from scrapy.conf import settings
# from scrapy.contrib.exporter import CsvItemExporter
from ..settings import *
from scrapy.exporters import CsvItemExporter

# 指定输出到csv文件中字段的顺序，结合setting.py
class itemcsvexporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        # delimiter = settings.get('CSV_DELIMITER', ',')
        # kwargs['delimiter'] = delimiter
        kwargs['delimiter'] = CSV_DELIMITER

        # fields_to_export = settings.get('FIELDS_TO_EXPORT', [])
        fields_to_export = FIELDS_TO_EXPORT
        if fields_to_export:
            kwargs['fields_to_export'] = fields_to_export

        super(itemcsvexporter, self).__init__(*args, **kwargs)
