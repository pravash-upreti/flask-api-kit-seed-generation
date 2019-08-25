#!/usr/bin/python3

import os

from pprint import pprint
from base import SeedGen

from random import randrange

DATA_DIRECTORY = os.getcwd()+"/data/comments/"


def main():
    SeedGen.set_data_directory(data_directory=DATA_DIRECTORY)

    uuid_list = SeedGen.get_txt_data(file_name="uuid.txt")
    comment_list = SeedGen.get_txt_data(file_name="comments.csv")    
    
    with open(os.getcwd()+"/data/posts/uuid.txt") as f:
        post_uuid_list = f.read().split('\n')

    with open(os.getcwd()+"/data/users/uuid.txt") as f:
        user_uuid_list = f.read().split('\n')
    
    # comment 50 % on post
    comment_data = []
    for index in range(len(comment_list)//2):
        post_uuid = post_uuid_list[randrange(len(post_uuid_list))]
        user_uuid = user_uuid_list[randrange(len(user_uuid_list))]
        comment_data.append({
            "comment": comment_list[index],
            "id": uuid_list[index],
            "post_id": post_uuid,
            "commented_by": user_uuid
        })
    
    # comment 50% on comment
    for index in range(len(comment_list)//2,len(comment_list)-1):
        comment_uuid = comment_data[randrange(len(comment_data))]["id"]
        user_uuid = user_uuid_list[randrange(len(user_uuid_list))]
        comment_data.append({
            "comment": comment_list[index],
            "id": uuid_list[index],
            "comment_id": comment_uuid,
            "commented_by": user_uuid
        })
        
    SeedGen.write_pretty_xml(SeedGen.tuple_to_xml(data_list=comment_data, table_name="comments"),"comments.xml")


if __name__ == "__main__":
    main()
