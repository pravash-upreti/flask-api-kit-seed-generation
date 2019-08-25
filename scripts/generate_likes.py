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

    with open(os.getcwd()+"/data/posts/uuid.txt") as f:
        post_uuid_list = f.read().split('\n')

    with open(os.getcwd()+"/data/comments/uuid.txt") as f:
        comment_uuid_list = f.read().split('\n')

    likes_data=[]
    
    while range(200):        
        select_post_id = post_uuid_list[randrange(len(post_uuid_list))]
        select_user_id = uuid_list[randrange(len(uuid_list))]
        
        # check if the post is liked by users
        for like in likes_data:            
            try:
                if like["liked_by"]==select_user_id and like["post_id"]==select_post_id:
                    break
            except:
                pass
        else:
            likes_data.append({
                "id":str(UUID.uuid4()),
                "post_id":select_post_id,
                "liked_by":select_user_id
            })
            continue
        break

    while range(200, 500-1):
        select_comment_id = comment_uuid_list[randrange(len(comment_uuid_list))]
        select_user_id = uuid_list[randrange(len(uuid_list))]
        
        # check if the post is liked by users
        for like in likes_data:
            try:
                if like["liked_by"]==select_user_id and like["comment_id"]==select_comment_id:
                    break
            except:
                pass
        else:
            likes_data.append({
                "id":str(UUID.uuid4()),
                "comment_id":select_comment_id,
                "liked_by":select_user_id
            })
            continue
        break        
        
    SeedGen.write_pretty_xml(SeedGen.tuple_to_xml(data_list=likes_data, table_name="likes"),"likes.xml")


if __name__ == "__main__":
    main()
