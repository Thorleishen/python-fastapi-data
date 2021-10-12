#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/7 4:20 下午
# @Author : zhenyu lei
# @File : models.py
# @desc :
from tortoise import fields, models


class Users(models.Model):
    """
    The User model
    """

    id = fields.IntField(pk=True)
    #: This is a username
    username = fields.CharField(max_length=20, unique=True)
    name = fields.CharField(max_length=50, null=True)
    family_name = fields.CharField(max_length=50, null=True)
    category = fields.CharField(max_length=30, default="misc")
    password_hash = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def full_name(self) -> str:
        """
        Returns the best name
        """
        if self.name or self.family_name:
            return f"{self.name or ''} {self.family_name or ''}".strip()
        return self.username

    class Meta:
        table = '用户表'
        table_description = ''
        abstract = False


# 解决多类型下的orm
class ManyTypeModel(object):
    __models = {}

    @classmethod
    def create_model(cls, ctype):
        if ctype not in cls.__models:
            table_name = f'table_name_{ctype}'

            class Role(models.Model):
                """
                The Tole model
                """

                id = fields.IntField(pk=True)
                #: This is a username
                username = fields.CharField(max_length=20, unique=True)
                name = fields.CharField(max_length=50, null=True)
                family_name = fields.CharField(max_length=50, null=True)
                category = fields.CharField(max_length=30, default="misc")
                password_hash = fields.CharField(max_length=128, null=True)
                created_at = fields.DatetimeField(auto_now_add=True)
                modified_at = fields.DatetimeField(auto_now=True)

                def full_name(self) -> str:
                    """
                    Returns the best name
                    """
                    if self.name or self.family_name:
                        return f"{self.name or ''} {self.family_name or ''}".strip()
                    return self.username

                class Meta:
                    table = table_name
                    table_description = ''
                    abstract = False
            cls.__models[ctype] = Role
        return cls.__models[ctype]
