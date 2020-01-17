# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 23:06:03 2020

@author: ritu raj
"""

import db_con
def test_chk():
    id1=db_con.check_id('krishna')
    print(id1)
    assert id1==1