#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/7 2:44 下午
# @Author : zhenyu lei
# @File : main.py
# @desc : 启动文件

from fastapi import FastAPI

app = FastAPI()
# get_organelle_from_reads.py -1 YJMH_R1.fq.gz -2 YJMH_R2.fq.gz -F embplant_pt -w 0.6 -o output-plastome -R 15 -t 4 -k 21,45,65,85,105