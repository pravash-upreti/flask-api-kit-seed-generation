#!/usr/bin/python3

import os
import uuid as UUID

from pprint import pprint
from base import SeedGen
from random import randrange

DATA_DIRECTORY = os.getcwd()+"/data/users/"


def main():
    SeedGen.set_data_directory(data_directory=DATA_DIRECTORY)

    uuid_list = SeedGen.get_txt_data(file_name="uuid.txt")
    friend_list_data=[]
    for uuid in uuid_list:
        while randrange(len(uuid_list)):
            selected_friend_id = uuid_list[randrange(len(uuid_list))]
            
            # user cannot have itself as a friend
            if selected_friend_id==uuid:
                continue
            
            for friend in friend_list_data:                
                if friend["friend_id"] == selected_friend_id and friend["user_id"] == uuid:
                    break;
            else:
                friend_list_data.append({
                    "id":str(UUID.uuid4()),
                    "user_id":uuid,
                    "friend_id":selected_friend_id
                })
                continue
            break
    
    SeedGen.write_pretty_xml(SeedGen.tuple_to_xml(data_list=friend_list_data, table_name="friend_list"),"friend_list.xml")


if __name__ == "__main__":
    main()
