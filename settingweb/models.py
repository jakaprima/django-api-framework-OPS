# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SettingWeb(models.Model):
	nama_web = models.CharField(max_length=35)
	deskripsi_web = models.CharField(max_length=60)
	def __str__(self):
		return self.nama_web

