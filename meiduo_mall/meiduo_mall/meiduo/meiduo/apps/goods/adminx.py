import xadmin
from xadmin import views

from . import models


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True
    
    
xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "美多商城运营管理系统"  # 设置站点标题
    site_footer = "美多商城集团有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠
    
    
xadmin.site.register(views.CommAdminView, GlobalSettings)


class SKUAdmin(object):
    # def save_model(self, request, obj, form, change):
    #     obj.save()
    #     from celery_tasks.html.tasks import generate_static_sku_detail_html
    #     generate_static_sku_detail_html.delay(obj.id)
    model_icon = 'fa fa-gift'  # 模型图标
    list_display = ['id', 'name', 'price', 'stock', 'sales', 'comments']
    search_fields = ['id', 'name']
    list_filter = ['category']
    list_editable = ['price', 'stock']  # xadmin独有
    show_detail_fields = ['name']
    list_export = ['xls', 'csv', 'xml']
    readonly_fields = ['sales', 'comments']


class SKUSpecificationAdmin(object):
    # def save_model(self, request, obj, form, change):
    #     obj.save()
    #     from celery_tasks.html.tasks import generate_static_sku_detail_html
    #     generate_static_sku_detail_html.delay(obj.sku.id)
    #
    # def delete_model(self, request, obj):
    #     sku_id = obj.sku.id
    #     obj.delete()
    #     from celery_tasks.html.tasks import generate_static_sku_detail_html
    #     generate_static_sku_detail_html.delay(sku_id)
    model_icon = 'fa  fa-bookmark'

    def save_models(self):
        # 保存数据对象
        obj = self.new_obj
        obj.save()
    
        # 补充自定义行为
        from celery_tasks.html.tasks import generate_static_sku_detail_html
        generate_static_sku_detail_html.delay(obj.sku.id)

    def delete_model(self):
        # 删除数据对象
        obj = self.obj
        sku_id = obj.sku.id
        obj.delete()
    
        # 补充自定义行为
        from celery_tasks.html.tasks import generate_static_sku_detail_html
        generate_static_sku_detail_html.delay(sku_id)


class SKUImageAdmin(object):
    # def save_model(self, request, obj, form, change):
    #     obj.save()
    #     from celery_tasks.html.tasks import generate_static_sku_detail_html
    #     generate_static_sku_detail_html.delay(obj.sku.id)
    #
    #     # 设置SKU默认图片
    #     sku = obj.sku
    #     if not sku.default_image_url:
    #         sku.default_image_url = obj.image.url
    #         sku.save()
    #
    # def delete_model(self, request, obj):
    #     sku_id = obj.sku.id
    #     obj.delete()
    #     from celery_tasks.html.tasks import generate_static_sku_detail_html
    #     generate_static_sku_detail_html.delay(sku_id)
    model_icon = 'fa  fa-cogs'

    def save_models(self):
        # 保存数据对象
        obj = self.new_obj
        obj.save()
    
        # 补充自定义行为
        from celery_tasks.html.tasks import generate_static_sku_detail_html
        generate_static_sku_detail_html.delay(obj.sku.id)

    def delete_model(self):
        # 删除数据对象
        obj = self.obj
        sku_id = obj.sku.id
        obj.delete()
    
        # 补充自定义行为
        from celery_tasks.html.tasks import generate_static_sku_detail_html
        generate_static_sku_detail_html.delay(sku_id)


class GoodsCategoryAdmin(object):
    # def save_model(self, request, obj, form, change):
    #     obj.save()
    #     from celery_tasks.html.tasks import generate_static_list_category_html
    #     generate_static_list_category_html.delay()
    #
    # def delete_model(self, request, obj):
    #     obj.delete()
    #     from celery_tasks.html.tasks import generate_static_list_category_html
    #     generate_static_list_category_html.delay()
    # model_icon = 'fa  fa-crosshairs'
    
    def save_models(self):
        # 保存数据对象
        obj = self.new_obj
        obj.save()
    
        # 补充自定义行为
        from celery_tasks.html.tasks import generate_static_sku_detail_html
        generate_static_sku_detail_html.delay(obj.sku.id)

    def delete_model(self):
        # 删除数据对象
        obj = self.obj
        sku_id = obj.sku.id
        obj.delete()
    
        # 补充自定义行为
        from celery_tasks.html.tasks import generate_static_sku_detail_html
        generate_static_sku_detail_html.delay(sku_id)


# xadmin.site.register()
xadmin.site.register(models.GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(models.GoodsChannel)
xadmin.site.register(models.Goods)
xadmin.site.register(models.Brand)
xadmin.site.register(models.GoodsSpecification)
xadmin.site.register(models.SpecificationOption)
xadmin.site.register(models.SKU, SKUAdmin)
xadmin.site.register(models.SKUSpecification, SKUSpecificationAdmin)
xadmin.site.register(models.SKUImage)