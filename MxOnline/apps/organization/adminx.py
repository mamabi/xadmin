#coding:utf-8
__author__ = 'Peter'
__date__ = '2017/11/27 14:47'

import xadmin

from .models import CityDict, CourseOrg, Teacher

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    
class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums','image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums','image', 'address', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums','image', 'address', 'city', 'add_time']

class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_years', 'work_company']
    search_fields = ['name', 'org__name', 'work_years', 'work_company',]
    list_filter = ['name', 'org__name', 'work_years', 'work_company']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)












