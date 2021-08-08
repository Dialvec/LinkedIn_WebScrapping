# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 19:33:30 2021

@author: Dialvec
"""

import os
import utils
import pandas as pd

class NewDatabase:
    
    def __init__(self, df_path):
        
        self.__path = df_path
        
        if (os.path.exists(df_path) == True):
            self.__df = pd.read_csv(df_path, index_col=0)
            
        else:
            self.__df = pd.DataFrame(columns = utils.COLNAMES)
    
    def get_df_path(self):
        return self.__path
    
    def get_df(self):
        return self.__df
    
    def add_chunk(self, df_chunk):
        df = self.get_df()
        self.__df = df.append(df_chunk, ignore_index=True)
    
    def save(self):
        self.get_df().to_csv( self.get_df_path() )