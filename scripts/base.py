#!/usr/bin/python3

import os
import json
import xml.etree.cElementTree as ET
import xml.dom.minidom
import time


class SeedGen:
    
    _DATA_DIRECTORY=""

    def __init__(self):
        return
    
    @classmethod
    def set_data_directory(cls, data_directory=None):
        SeedGen._DATA_DIRECTORY = data_directory

    @classmethod
    def get_json_data(cls, file_name):
        with open(SeedGen._DATA_DIRECTORY+file_name) as f:
            return json.load(f)

    @classmethod
    def get_txt_data(cls, file_name):
        with open(SeedGen._DATA_DIRECTORY+file_name) as f:
            return f.read().split('\n')

    @classmethod
    def array_of_dict_to_list(cls, data_array, key):
        data_list = []
        for data_item in data_array:
            data_list.append(data_item[key])
        return data_list

    @classmethod
    def tuple_to_xml(cls, data_list, table_name):
        tmp_file_name = str(int(time.time()))+".xml"
        table = ET.Element("table", name=table_name)
        for data in data_list:
            ET.SubElement(table, "row",data)
        
        users_xml = ET.ElementTree(table)
        users_xml.write(SeedGen._DATA_DIRECTORY+tmp_file_name)
        
        return tmp_file_name

    @classmethod
    def write_pretty_xml(cls, serializ_data_file, file_name):
        dom = xml.dom.minidom.parse(SeedGen._DATA_DIRECTORY+serializ_data_file)
        pretty_xml_as_string = dom.toprettyxml()
        with open(SeedGen._DATA_DIRECTORY+file_name, '+w') as f:
            f.write(pretty_xml_as_string)
        
        os.remove(SeedGen._DATA_DIRECTORY+serializ_data_file)
