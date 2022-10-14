from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = '博客系统管理后台'
    site_title = '登录后台系统'
    index_title = '后台管理'

custom_site = CustomSite(name='cus_admin')