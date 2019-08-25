#!/usr/bin/python3

import os

from pprint import pprint
from base import SeedGen

from random import randrange

DATA_DIRECTORY = os.getcwd()+"/data/posts/"


def main():
    SeedGen.set_data_directory(data_directory=DATA_DIRECTORY)

    uuid_list = SeedGen.get_txt_data(file_name="uuid.txt")
    post_list = SeedGen.get_txt_data(file_name="posts.csv")    
    
    with open(os.getcwd()+"/data/users/uuid.txt") as f:
        user_uuid_list = f.read().split('\n')

    post_data=[]
    for index, uuid in enumerate(uuid_list):
        post_data.append({
            "id":uuid,
            "post":post_list[index],
            "posted_by":user_uuid_list[randrange(len(user_uuid_list))]
        })
    
    SeedGen.write_pretty_xml(SeedGen.tuple_to_xml(data_list=post_data, table_name="posts"),"posts.xml")


if __name__ == "__main__":
    main()
