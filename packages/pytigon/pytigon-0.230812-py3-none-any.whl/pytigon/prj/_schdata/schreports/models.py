import django
from django.db import models
from django.utils import timezone

from pytigon_lib.schdjangoext.fields import *
from pytigon_lib.schdjangoext.models import *
import pytigon_lib.schdjangoext.fields as ext_models
from pytigon_lib.schtools import schjson

from django.utils.translation import gettext_lazy as _
from django.contrib import admin

import os, os.path
import sys
from pytigon_lib.schhtml.htmltools import superstrip

import schelements.models


from pytigon_lib.schtools.schjson import json_dumps, json_loads

# from schlib.schdjangoext.django_ihtml import ihtml_to_html
# from django.template import Context, Template
from django.db.models import Max, Min

from schelements.models import *


class ReportDef(schelements.models.BaseObject):
    """
    Declaration:
        return Form()

    Template: django template

    child(name):
        child_header(name)
        child_table(name)

        <html></html>



    to_html:
        convert form data to html

    """

    class Meta:
        verbose_name = _("Report definition")
        verbose_name_plural = _("Reports definitions")
        default_permissions = ("add", "change", "delete", "list")
        app_label = "schreports"

        ordering = ["id"]

        permissions = [
            ("admin_repdef", "Can administer report definitions"),
        ]

    doc_type = models.CharField(
        "Associated document type", null=True, blank=True, editable=True, max_length=16
    )

    def __str__(self):
        return self.name

    def getsubrep(self, name):
        return ReportDef.objects.get(name=self.name + "/" + name)

    @staticmethod
    def get_rep_defs():
        repdef_list = ReportDef.objects.exclude(name__contains="/")
        return repdef_list

    def can_user_add(self, user):
        if self.doc_type:
            return DocHead.can_add(self.doc_type, user)
        else:
            return True

    def copy_to_clipboard(self):
        return {
            "action": "paste_from_clipboard",
            "table": "ReportDef",
            "objects": [
                {
                    "app": self.app,
                    "name": self.name,
                    "description": self.description,
                    "declaration": self.declaration,
                    "template_src": self.template_src,
                    "template": self.template,
                    "to_html_rec": self.to_html_rec,
                    "save_fun": self.save_fun,
                    "load_fun": self.load_fun,
                    "to_str_fun": self.to_str_fun,
                    "action_template": self.action_template,
                    "doc_type": self.doc_type,
                },
            ],
        }

    @classmethod
    def table_action(cls, list_view, request, data):
        if (
            "action" in data
            and data["action"] == "paste_from_clipboard"
            and "table" in data
            and data["table"] == "ReportDef"
        ):
            object_list = data["objects"]
            for obj_param in object_list:
                obj = ReportDef()
                obj.app = obj_param["app"]
                obj.name = "COPY: " + obj_param["name"]
                obj.description = obj_param["description"]
                obj.declaration = obj_param["declaration"]
                obj.template_src = obj_param["template_src"]
                obj.template = obj_param["template"]
                obj.to_html_rec = obj_param["to_html_rec"]
                obj.save_fun = obj_param["save_fun"]
                obj.load_fun = obj_param["load_fun"]
                obj.to_str_fun = obj_param["to_str_fun"]
                obj.action_template = obj_param["action_template"]
                obj.doc_type = obj_param["doc_type"]
                obj.save()
            print("PASTE: ", data)
            return True
        return standard_table_action(cls, list_view, request, data, ["copy", "paste"])


admin.site.register(ReportDef)


class Report(JSONModel):
    class Meta:
        verbose_name = _("Report")
        verbose_name_plural = _("Reports")
        default_permissions = ("add", "change", "delete", "list")
        app_label = "schreports"

        ordering = ["id"]

        ordering = ["parent_id", "order", "id"]

        permissions = [
            ("admin_report", "Can administer reports"),
        ]

    parent = ext_models.PtigForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        editable=False,
        verbose_name="Parent",
    )
    parent_doc = ext_models.PtigForeignKey(
        schelements.models.DocHead,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        editable=False,
        verbose_name="Parent document",
        db_index=True,
    )
    order = models.IntegerField(
        "Order number",
        null=True,
        blank=True,
        editable=True,
    )
    report_def_name = models.CharField(
        "Report definition name", null=False, blank=False, editable=True, max_length=64
    )
    date = models.DateTimeField(
        "Date",
        null=True,
        blank=True,
        editable=True,
    )

    def __str__(self):
        return self.report_def_name

    def template_for_object(self, view, context, doc_type):
        if doc_type == "pdf":
            x = ReportDef.objects.filter(name=self.report_def_name)
            if x.count() > 0:
                return "%s/report_%s_pdf.html" % (x[0].app, self.report_def_name)
        return None

    @staticmethod
    def get_rep_types():
        repdef_list = ReportDef.objects.exclude(name__contains="/")
        return [pos.name for pos in repdef_list]

    @staticmethod
    def get_rep_by_nagid(nagid):
        r = Report.objects.filter(parent_doc__id=nagid)
        if r.count() > 0:
            return r[0]
        else:
            return None

    @classmethod
    def filter(cls, value, view=None, request=None):
        if value == "main_reports":
            return Report.objects.filter(parent=None)
        else:
            return Report.objects.all()

    def getsubreps(self, name):
        return Report.objects.filter(parent=self).filter(report_def_name__endswith=name)

    def to_html(self):
        rep_def = ReportDef.objects.get(name=self.report_def_name)
        return rep_def.to_html(self)

    # def  __getattr__(self, name):
    #    if name.startswith('json_'):
    #        if not hasattr(self, '_data'):
    #            self._data = json_loads(self.data)
    #        if name[5:] in self._data:
    #            return self._data[name[5:]]
    #        else:
    #            return None
    #    else:
    #        return super().__getattr__(name)

    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.parent:
                m = Report.objects.filter(parent=self.parent).aggregate(Max("order"))[
                    "order__max"
                ]
                if m:
                    self.order = m + 1
                else:
                    self.order = 1
        super().save(*args, **kwargs)


admin.site.register(Report)


class Plot(models.Model):
    class Meta:
        verbose_name = _("Plot")
        verbose_name_plural = _("Polts")
        default_permissions = ("add", "change", "delete", "list")
        app_label = "schreports"

        ordering = ["id"]

        permissions = [
            ("admin_plot", "Can administer plots"),
        ]

    name = models.CharField(
        "Name", null=False, blank=False, editable=True, max_length=64
    )
    group = models.CharField(
        "Group", null=False, blank=False, editable=True, max_length=64
    )
    get_config = models.TextField(
        "Get config",
        null=True,
        blank=True,
        editable=False,
    )
    get_data = models.TextField(
        "Get data",
        null=True,
        blank=True,
        editable=False,
    )
    get_layout = models.TextField(
        "Get layout",
        null=True,
        blank=True,
        editable=False,
    )
    on_event = models.TextField(
        "On event",
        null=True,
        blank=True,
        editable=False,
    )
    permission = models.CharField(
        "Permission", null=True, blank=True, editable=True, max_length=64
    )

    def __str__(self):
        return self.name


admin.site.register(Plot)
