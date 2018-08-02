# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "research_repository"
app_title = "Research Repository"
app_publisher = "of the institute as a whole, departments and individual faculty member:ssn"
app_description = "A web based application to maintain the records related to research contribution of all faculty members in an institute, as a measure of research outcome"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sasirekhas@ssn.edu.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/research_repository/css/research_repository.css"
# app_include_js = "/assets/research_repository/js/research_repository.js"

# include js, css files in header of web template
# web_include_css = "/assets/research_repository/css/research_repository.css"
# web_include_js = "/assets/research_repository/js/research_repository.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "research_repository.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "research_repository.install.before_install"
# after_install = "research_repository.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "research_repository.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"research_repository.tasks.all"
# 	],
# 	"daily": [
# 		"research_repository.tasks.daily"
# 	],
# 	"hourly": [
# 		"research_repository.tasks.hourly"
# 	],
# 	"weekly": [
# 		"research_repository.tasks.weekly"
# 	]
# 	"monthly": [
# 		"research_repository.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "research_repository.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "research_repository.event.get_events"
# }

