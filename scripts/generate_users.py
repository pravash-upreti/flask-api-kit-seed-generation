#!/usr/bin/python3

import os

from pprint import pprint
from base import SeedGen

DATA_DIRECTORY = os.getcwd()+"/data/users/"


def main():
    SeedGen.set_data_directory(data_directory=DATA_DIRECTORY)

    email_data = SeedGen.get_json_data(file_name="email.json")
    username_data = SeedGen.get_json_data(file_name="username.json")

    uuid_list = SeedGen.get_txt_data(file_name="uuid.txt")
    email_list = SeedGen.array_of_dict_to_list(data_array=email_data, 
                                        key="Email")
    username_list = SeedGen.array_of_dict_to_list(data_array=username_data, 
                                        key="Username")
    users_data=[]
    for index, uuid in enumerate(uuid_list):
        users_data.append({
            "id":uuid,
            "email":email_list[index],
            "username":username_list[index]
        })
    
    SeedGen.write_pretty_xml(SeedGen.tuple_to_xml(data_list=users_data, table_name="users"),"users.xml")


if __name__ == "__main__":
    main()
