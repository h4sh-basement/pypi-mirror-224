#!/usr/bin/env python3
"""
This test script shows that you can kreate komponents from konfig file.
After this you can fientune them further in python.
In general it is preferred to not use a script but use `python3 -m kreate`
"""

from kreate.kore import AppDef, App
from kreate.kube import KustApp, KubeCli

def kreate_appdef(appdef_filename:str) -> AppDef:
    # ignore passed in appdef
    return AppDef("tests/script/appdef.yaml")

def kreate_app(appdef: AppDef) -> App:
    app = KustApp(appdef)
    app.konfigure_from_konfig()
    # find the (main) Deployment and modify it a bit
    #TODO: This did work:
    app.depl.main.label("this-is-added","by-script")
    return app

KubeCli().run(kreate_appdef, kreate_app)
