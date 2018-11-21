#!/usr/bin/env python
# coding=utf-8

import jieba

class BotRequest:

    def __init__(self, query):
        self.original_query = query[:]
        
        self.query_type = ""
        self.pure_query = ""
        self.query_segment_results = []
    
    def make_query_clean(self, drop_char_set):
        '''
            clean the original query
            Args:
                drop_char_set = set(str) : the char need to be dropped from original query
            Returns:
                ret = int
        '''
        ret = 0

        return ret
    
    def segment_query(self):
        '''
            segment the query into word list
            Args:
            Returns:
                ret = int
        '''
        ret = 0

        return ret


