#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Item(models.Model):
    text = models.TextField(default='')
