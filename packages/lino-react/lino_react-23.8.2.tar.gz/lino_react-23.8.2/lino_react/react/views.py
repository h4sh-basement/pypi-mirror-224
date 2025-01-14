# -*- coding: UTF-8 -*-
# Copyright 2009-2023 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""Views for `lino_react.react`.
"""

from os import environ
import datetime
import re
import cgi
import ast
import json
import random
import html
from types import GeneratorType
from jinja2.exceptions import TemplateNotFound
from etgen.html import E, tostring
from etgen import html as xghtml

from django import http
from django.db import models
from django.conf import settings
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.core import exceptions
from django.utils import timezone
from django.utils.translation import gettext as _
from django.utils.translation import get_language
from django.core.exceptions import PermissionDenied

# from django.contrib import auth
from lino.core import auth
from lino.utils import isiterable
from lino.utils.jsgen import py2js
from lino.core import fields
from lino.core.elems import ComboFieldElement
from lino.core.fields import choices_for_field
from lino.core.gfks import ContentType
from lino.core import constants
from lino.core.requests import BaseRequest, PhantomRow
from lino.core.tablerequest import TableRequest
from lino.core.views import requested_actor, action_request
from lino.core.views import json_response, json_response_kw
from lino.core.views import choices_response
from lino.core.utils import navinfo
from lino.core.actions import ShowEmptyTable
from lino.core import kernel
from lino.core.store import get_atomizer

from lino.modlib.users.utils import get_user_profile, with_user_profile
from lino.api import rt
from lino.modlib.extjs.views import ApiElement, test_version_mismatch, elem2rec_empty


def find(itter, target, key=None):
    """Returns the index of an element in a callable which can be use a key function"""
    assert key == None or callable(key), "key shold be a function that takes the itter's item " \
                                         "and returns that wanted matched item"
    for i, x in enumerate(itter):
        if key:
            x = key(x)
        if x == target:
            return i
    else:
        return -1


# Taken from lino.modlib.extjs.views
NOT_FOUND = "%s has no row with primary key %r"

# class Callbacks(View):
#     def get(self, request, thread_id, button_id):
#         return settings.SITE.kernel.run_callback(request, thread_id, button_id)


class ApiElement(ApiElement):

    def post(self, request, app_label=None, actor=None, pk=None):
        # data = http.QueryDict(request.body)
        data = request.POST
        ar = action_request(
            app_label, actor, request, data, True,
            renderer=settings.SITE.plugins.react.renderer)
        if pk == '-99998':
            elem = ar.create_instance()
            ar.selected_rows = [elem]
        else:
            ar.set_selected_pks(pk)
        return settings.SITE.kernel.run_action(ar)

    def put(self, request, app_label=None, actor=None, pk=None):
        data = http.QueryDict(request.body)  # raw_post_data before Django 1.4
        # data = json.loads(request.body)
        # logger.info("20150130 %s", data)
        ar = action_request(
            app_label, actor, request, data, False,
            renderer=settings.SITE.plugins.react.renderer)
        ar.set_selected_pks(pk)
        return settings.SITE.kernel.run_action(ar)

    def delete(self, request, app_label=None, actor=None, pk=None):
        data = http.QueryDict(request.body)
        ar = action_request(
            app_label, actor, request, data, False,
            renderer=settings.SITE.plugins.react.renderer)
        ar.set_selected_pks(pk)
        return settings.SITE.kernel.run_action(ar)


class ApiList(View):
    def post(self, request, app_label=None, actor=None):
        ar = action_request(app_label, actor, request, request.POST, True)
        ar.get_status()
        ar.renderer = settings.SITE.kernel.default_renderer
        return settings.SITE.kernel.run_action(ar)

    def get(self, request, app_label=None, actor=None):
        vm = test_version_mismatch(request)
        if vm:
            return json_response(vm)
        ar = action_request(app_label, actor, request, request.GET, True)
        # Add this hack to support the 'sort' param which is different in Extjs6.
        # if ar.order_by and ar.order_by[0]:
        #     _sort = ast.literal_eval(ar.order_by[0])
        #     sort = _sort[0]['property']
        #     if _sort[0]['direction'] and _sort[0]['direction'] == 'DESC':
        #         sort = '-' + sort
        #     ar.order_by = [str(sort)]
        if not ar.get_permission():
            msg = "No permission to run {}".format(ar)
            # raise Exception(msg)
            raise PermissionDenied(msg)

        ar.renderer = settings.SITE.kernel.default_renderer
        rh = ar.ah

        fmt = request.GET.get(
            constants.URL_PARAM_FORMAT,
            ar.bound_action.action.default_format)

        action_name = request.GET.get(constants.URL_PARAM_ACTION_NAME)

        if action_name:
            return settings.SITE.kernel.run_action(ar)

        if fmt == constants.URL_FORMAT_JSON:
            if isinstance(ar.bound_action.action, ShowEmptyTable):
                elem = ar.create_instance()
                datarec = elem2rec_empty(ar, ar.ah, elem)
                return json_response(datarec)

            display_mode = request.GET.get(
                constants.URL_PARAM_DISPLAY_MODE, constants.DISPLAY_MODE_TABLE)

            if display_mode == constants.DISPLAY_MODE_STORY:
                html_text = ""
                rows = []
                for obj in ar.sliced_data_iterator:
                    html_text += obj.as_story_item(ar)
                    rows.append({'id': obj.pk})
            elif display_mode == constants.DISPLAY_MODE_LIST:
                html_text = ""
                rows = []
                for obj in ar.sliced_data_iterator:
                    par = ar.row_as_paragraph(obj)  # 20230207
                    par = ar.add_detail_link(obj, par)
                    # par = ar.obj2str(obj, par)
                    par = "<p>{}</p>".format(par)
                    # url = ar.renderer.obj2url(ar, obj)
                    # if url is not None:
                    #     url = html.escape(url)
                    #     # par += ' <a href="{}">(Detail)</a>'.format(url)
                    #     par = '<a href="{}">{}</a>'.format(url, par)
                    html_text += par
                    rows.append({'id': obj.pk})
            else:
                html_text = None
                def serialize(ar, row):
                    """Use display_mode to determine which serilisation store method and fields to use"""
                    if display_mode == constants.DISPLAY_MODE_TABLE:
                        return rh.store.row2list(ar, row)
                    elif display_mode == constants.DISPLAY_MODE_GALLERY:
                        # return rh.store.file2url(ar, row)
                        return row.get_gallery_item(ar)
                    else:
                        if display_mode == constants.DISPLAY_MODE_CARDS:
                            fields = rh.store.card_fields
                        else:
                            fields = rh.store.detail_fields
                        return rh.store.row2dict(ar,
                            row, fields=fields, card_title=ar.get_card_title(row))

                rows = [serialize(ar, row)
                        for row in ar.sliced_data_iterator]

            total_count = ar.get_total_count()
            if display_mode == constants.DISPLAY_MODE_TABLE:
                for row in ar.create_phantom_rows():
                    if ar.limit is None or len(rows) + 1 < ar.limit or ar.limit == total_count + 1:
                        d = serialize(ar, row)
                        rows.append(d)
                    total_count += 1
            # assert len(rows) <= ar.limit
            kw = dict(count=total_count,
                      rows=rows,
                      html_text=html_text,
                      success=True,
                      no_data_text=ar.no_data_text,
                      title=ar.get_title())
            if display_mode != constants.DISPLAY_MODE_TABLE:
                mc = ar.get_main_card()
                if mc is not None:
                    rows.insert(0, mc)
            if ar.actor.parameters:
                kw.update(
                    param_values=ar.actor.params_layout.params_store.pv2dict(
                        ar, ar.param_values))
            return json_response(kw)

        return settings.SITE.kernel.run_action(ar)


class ChoiceListModel(View):
    """
    Creates a large JSON model that contains all the choicelists + choices

    Note: This could be improved, or might cause issues due to changing language
    """

    def get(self, request):
        data = {str(cl): [{"key": py2js(c[0]).strip('"'), "text": py2js(c[1]).strip('"')} for c in cl.get_choices()] for
                cl in
                kernel.CHOICELISTS.values()}
        return json_response(data)


# Copied from lino.modlib.extjs.views.Choices line for line.
class Choices(View):
    def get(self, request, app_label=None, actor=None, field=None, **kw):
        """If `fldname` is specified, return a JSON object with two
        attributes `count` and `rows`, where `rows` is a list of
        `(display_text, value)` tuples.  Used by ComboBoxes or similar
        widgets.

        If `fldname` is not specified, returns the choices for the
        `record_selector` widget.

        """
        rpt = requested_actor(app_label, actor)
        emptyValue = None
        if field is None:
            ar = rpt.request(request=request)
            # ~ rh = rpt.get_handle(self)
            # ~ ar = ViewReportRequest(request,rh,rpt.default_action)
            # ~ ar = dbtables.TableRequest(self,rpt,request,rpt.default_action)
            # ~ rh = ar.ah
            # ~ qs = ar.get_data_iterator()
            qs = ar.data_iterator

            # ~ qs = rpt.request(self).get_queryset()

            def row2dict(obj, d):
                d[constants.CHOICES_TEXT_FIELD] = str(obj)
                # getattr(obj,'pk')
                d[constants.CHOICES_VALUE_FIELD] = obj.pk
                return d
        else:
            # NOTE: if you define a *parameter* with the same name as
            # some existing *data element* name, then the parameter
            # will override the data element here in choices view.
            field = rpt.get_param_elem(field) or rpt.get_data_elem(field)
            if field.blank:
                # logger.info("views.Choices: %r is blank",field)
                emptyValue = ''
            qs, row2dict = choices_for_field(rpt.request(request=request), rpt, field)

        return choices_response(rpt, request, qs, row2dict, emptyValue, field=field)


class DelayedValue(View):
    def get(self, request, app_label=None, actor=None, pk=None, field=None, **kw):
        rpt = requested_actor(app_label, actor)
        # ar = action_request(
        #     app_label, actor, request, request.GET, False,
        #     renderer=settings.SITE.plugins.react.renderer)
        # print("20210619a", ar)
        # rpt = requested_actor(app_label, actor)
        # rpt = ar.actor
        de = rpt.get_data_elem(field)
        if de is None:
            v = "{} has no data element {}".format(rpt, field)
        else:
            ar = rpt.request(request=request, renderer=settings.SITE.plugins.react.renderer)
            if pk == '-99998':
                row = None
            else:
                ar.set_selected_pks(pk)
                row = ar.selected_rows[0]
                # raise NotImplementedError()
            sf = get_atomizer(rpt, de, field)
            if sf is None:
                v = "Oops, get_atomizer({}, {}, {}) returned None".format(rpt, de, field)
            else:
                v = sf.full_value_from_object(row, ar)
            # v = de._lino_atomizer.full_value_from_object(row, ar)
        # print("20210619b", de, v)
        return json_response({'data': v})


# Also coppied from extjs.views line for line
class ActionParamChoices(View):
    # Examples: `welfare.pcsw.CreateCoachingVisit`
    def get(self, request, app_label=None, actor=None, an=None, field=None, **kw):
        actor = requested_actor(app_label, actor)
        ba = actor.get_url_action(an)
        if ba is None:
            raise Exception("Unknown action %r for %s" % (an, actor))
        field = ba.action.get_param_elem(field)
        qs, row2dict = choices_for_field(ba.request(request=request), ba.action, field)
        if field.blank:
            emptyValue = '<br/>'
        else:
            emptyValue = None
        return choices_response(actor, request, qs, row2dict, emptyValue, field=field)


class Restful(View):
    """
    Used to collaborate with a restful Ext.data.Store.
    """

    def post(self, request, app_label=None, actor=None, pk=None):
        rpt = requested_actor(app_label, actor)
        ar = rpt.request(request=request)

        instance = ar.create_instance()
        # store uploaded files.
        # html forms cannot send files with PUT or GET, only with POST
        if ar.actor.handle_uploaded_files is not None:
            ar.actor.handle_uploaded_files(instance, request)

        data = request.POST.get('rows')
        data = json.loads(data)
        ar.form2obj_and_save(data, instance, True)

        # Ext.ensible needs list_fields, not detail_fields
        ar.set_response(
            rows=[ar.ah.store.row2dict(
                ar, instance, ar.ah.store.list_fields)])
        return json_response(ar.response)

    # def delete(self, request, app_label=None, actor=None, pk=None):
    #     rpt = requested_actor(app_label, actor)
    #     ar = rpt.request(request=request)
    #     ar.set_selected_pks(pk)
    #     return delete_element(ar, ar.selected_rows[0])

    def get(self, request, app_label=None, actor=None, pk=None):
        """
        Works, but is ugly to get list and detail
        """
        rpt = requested_actor(app_label, actor)

        action_name = request.GET.get(constants.URL_PARAM_ACTION_NAME, None)
        fmt = request.GET.get(
            constants.URL_PARAM_FORMAT, constants.URL_FORMAT_JSON)
        sr = request.GET.getlist(constants.URL_PARAM_SELECTED)
        if not sr:
            sr = [pk]
        ar = rpt.request(request=request, selected_pks=sr)
        if pk is None:
            rh = ar.ah
            rows = [
                rh.store.row2dict(ar, row, rh.store.all_fields)
                for row in ar.sliced_data_iterator]
            kw = dict(count=ar.get_total_count(), rows=rows)
            kw.update(title=str(ar.get_title()))
            return json_response(kw)

        else:  # action_name=="detail": #ba.action.opens_a_window:
            if action_name:
                ba = rpt.get_url_action(action_name)
            else:
                ba = rpt.detail_action
            ah = ar.ah
            ar = ba.request(request=request, selected_pks=sr)
            elem = ar.selected_rows[0]
            if fmt == constants.URL_FORMAT_JSON:
                if pk == '-99999':
                    elem = ar.create_instance()
                    datarec = ar.elem2rec_insert(ah, elem)
                elif pk == '-99998':
                    elem = ar.create_instance()
                    datarec = elem2rec_empty(ar, ah, elem)
                elif elem is None:
                    datarec = dict(
                        success=False, message=NOT_FOUND % (rpt, pk))
                else:
                    datarec = ar.elem2rec_detailed(elem)
                return json_response(datarec)

    def put(self, request, app_label=None, actor=None, pk=None):
        rpt = requested_actor(app_label, actor)
        ar = rpt.request(request=request)
        ar.set_selected_pks(pk)
        elem = ar.selected_rows[0]
        rh = ar.ah

        data = http.QueryDict(request.body).get('rows')
        data = json.loads(data)
        a = rpt.get_url_action(rpt.default_list_action_name)
        ar = rpt.request(request=request, action=a)
        ar.renderer = settings.SITE.kernel.extjs_renderer
        ar.form2obj_and_save(data, elem, False)
        # Ext.ensible needs list_fields, not detail_fields
        ar.set_response(
            rows=[rh.store.row2dict(ar, elem, rh.store.list_fields)])
        return json_response(ar.response)


def http_response(ar, tplname, context):
    "Deserves a docstring"
    u = ar.get_user()
    lang = get_language()
    k = (u.user_type, lang)
    context = ar.get_printable_context(**context)
    context['ar'] = ar
    context['memo'] = ar.parse_memo  # MEMO_PARSER.parse
    env = settings.SITE.plugins.jinja.renderer.jinja_env
    template = env.get_template(tplname)

    response = http.HttpResponse(
        template.render(**context),
        content_type='text/html;charset="utf-8"')

    return response


# Give better name, does more then just XML, does all the connector responses.
def XML_response(ar, tplname, context):
    """
    Respone used for rendering XML views in react.
    Includes some helper functions for rendering.
    """
    # u = ar.get_user()
    # lang = get_language()
    # k = (u.user_type, lang)
    context = ar.get_printable_context(**context)
    context.update(constants=constants)
    # context['ar'] = ar
    # context['memo'] = ar.parse_memo  # MEMO_PARSER.parse
    env = settings.SITE.plugins.jinja.renderer.jinja_env
    try:
        template = env.get_template(tplname)
    except TemplateNotFound as e:
        return http.HttpResponseNotFound()

    def bind(*args):
        """Helper function to wrap a string in {}s"""
        args = [str(a) for a in args]
        return "{" + "".join(args) + "}"

    context.update(bind=bind)

    def p(*args):
        """Debugger helper; prints out all args put into the filter but doesn't include them in the template.
        usage: {{debug | p}}
        """
        print(args)
        return ""

    def zlib_compress(s):
        """
        Compress a complex value in order to get decompress by the controller afterwards
        :param s: value to get compressed.
        :return: Compressed value.
        """
        import zlib
        compressed = zlib.compress(str(s))
        return compressed.encode('base64')
        # return cgi.escape(s, quote=True)  # escapes "<", ">", "&" "'" and '"'

    def fields_search(searched_field, collections):
        """
        check if the fields is available in the set of collections
        :param searched_field: searched field
        :param collections: set of fields
        :return: True if the field is present in the collections,False otherwise.
        """
        if searched_field:
            for field in collections:
                if searched_field == field:
                    return True
        return False

    env.filters.update(dict(p=p, zlib_compress=zlib_compress, fields_search=fields_search))
    content_type = "text/xml" if tplname.endswith(".xml") else \
        "application/javascript" if tplname.endswith(".js") else \
            "application/json"
    response = http.HttpResponse(
        template.render(**context),
        content_type=content_type + ';charset="utf-8"')

    return response


class SWView(TemplateView):
    template_name = 'react/service-worker.js'
    content_type = 'application/javascript'

class WBView(TemplateView):
    content_type = 'application/javascript'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.template_name = 'react/' + kwargs['workbox']


class MainHtml(View):
    def get(self, request, *args, **kw):
        """Returns a json struct for the main user dashboard."""
        # ~ logger.info("20130719 MainHtml")
        settings.SITE.startup()
        # ~ raise Exception("20131023")
        rnd = settings.SITE.plugins.react.renderer
        ar = BaseRequest(request, renderer=rnd)
        # Add to reqeust not ar, as there's error if passing ar to get_main_html
        request.requesting_panel = "dashboard-main"
        html = settings.SITE.get_main_html(ar)
        html = rnd.html_text(html)
        ar.success(html=html)
        return json_response(ar.response, ar.content_type)


class DashboardItem(View):
    def get(self, request, index, *args, **kw):
        """Returns a rendered HTML version the requested user dashboard."""
        ar = BaseRequest(request)
        ar.renderer = settings.SITE.plugins.react.renderer
        ar.requesting_panel = f"dashboard-{index}"
        dash = ar.get_user().get_preferences().dashboard_items
        if len(dash) > index:
            item = dash[index]
            # print("20210112 DashboardItem.get()", index, item.actor)
            # html = ar.show_story([dash[index]])
            html = ''.join(item.render(ar))
        else:
            html = ""
        kw = dict(html=html)
        vm = test_version_mismatch(request)
        if vm:
            kw.update(vm)
        ar.success(**kw)
        return json_response(ar.response, ar.content_type)


class Null(View):
    """Just returns 200, used in an iframe to cause the browser to trigger "Do you want to remember this pw" dialog"""

    def post(self, request):
        return http.HttpResponse()

    def get(self, request):
        return http.HttpResponse()


class Authenticate(View):
    def get(self, request, *args, **kw):
        action_name = request.GET.get(constants.URL_PARAM_ACTION_NAME)
        if True or action_name == 'logout':
            username = request.session.pop('username', None)
            auth.logout(request)
            # request.user = settings.SITE.user_model.get_anonymous_user()
            # request.session.pop('password', None)
            # ~ username = request.session['username']
            # ~ del request.session['password']
            target = '/'
            return http.HttpResponseRedirect(target)

            # ar = BaseRequest(request)
            # ar.success("User %r logged out." % username)
            # return ar.renderer.render_action_response(ar)
        raise http.Http404()

    def post(self, request, *args, **kw):
        """logs the user in and builds the linoweb.js file for the logged in user"""
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        user = auth.authenticate(
            request, username=username, password=password)
        auth.login(request, user, backend=u'lino.core.auth.backends.ModelBackend')

        # target = '/user/settings/'
        def result():
            if settings.SITE.developer_site_cache:
                settings.SITE.plugins.react.renderer.build_js_cache(False)
            # http.HttpResponseRedirect(target) # Seems that fetch has some issues with this...
            return json_response({"success": True})

        return with_user_profile(user.user_type, result)
        # ar = BaseRequest(request)
        # mw = auth.get_auth_middleware()
        # msg = mw.authenticate(username, password, request)
        # if msg:
        #     request.session.pop('username', None)
        #     ar.error(msg)
        # else:
        #     request.session['username'] = username
        #     # request.session['password'] = password
        #     # ar.user = request....
        #     ar.success(("Now logged in as %r" % username))
        #     # print "20150428 Now logged in as %r (%s)" % (username, user)
        # return ar.renderer.render_action_response(ar)


class Index(View):
    """
    Main app entry point,
    Also builds linoweb file for current user type.
    Content is mostly in the :xfile:`react/main.html` template.
    """

    def get(self, request):

        user = request.user
        if True:  # user.user_type.level >= UserLevels.admin:
            if request.subst_user:
                user = request.subst_user

        def getit():
            ui = settings.SITE.plugins.react
            # if not settings.SITE.build_js_cache_on_startup:
            #     ui.renderer.build_js_cache(False)
            ar = BaseRequest(
                # user=user,
                request=request,
                renderer=ui.renderer)
            context = dict(
                # title=ar.get_title(),
                # heading=ar.get_title(),
                # main=main,
                front_end=ui,
                request=request,
                user=user,  # Current user
            )
            context.update(ar=ar)

            no_cache = ""
            if 'update_found' in request.GET:
                no_cache = "?mtime={}".format(random.randint(111111, 999999))
            context.update(no_cache=no_cache)
            context = ar.get_printable_context(**context)
            env = settings.SITE.plugins.jinja.renderer.jinja_env
            template = env.get_template("react/main.html")
            resp = http.HttpResponse(
                template.render(**context),
                content_type='text/html;charset="utf-8"')

            if 'update_found' in request.GET:
                resp['Clear-Site-Data'] = '"cache", "storage"'

            return resp

        return with_user_profile(user.user_type, getit)


class UserSettings(View):
    """
    Ajax interface for getting the current session/user settings."""

    def get(self, request):
        request = BaseRequest(request)
        u = request.user
        su = request.subst_user
        su_name = request.subst_user.get_full_name() if su else ""

        # not_anon = u.is_authenticated if type(u.is_authenticated) == bool else u.is_authenticated()
        not_anon = u.is_authenticated

        def getit():
            # print(20200419, settings.SITE.build_media_url(*settings.SITE.plugins.react.renderer.lino_js_parts()))
            if (settings.SITE.developer_site_cache
                and not settings.SITE.never_build_site_cache):
                settings.SITE.plugins.react.renderer.build_js_cache(False)

            user_settings = dict(
                user_type=u.user_type,
                dashboard_items=len(u.get_preferences().dashboard_items),
                email=u.email,
                # [d.serialize() for d in u.get_preferences().dashboard_items],
                lang=get_language(),
                site_data=settings.SITE.build_site_cache_url(*settings.SITE.plugins.react.renderer.lino_js_parts()),
                site_name=settings.SITE.project_dir.name,
                logged_in=not_anon,
                username=u.get_full_name() if not_anon else _("Anonymous"),
                su_name=su_name,  # subst_user # must be passed as param in get_user_settings request,
                act_as_subtext=_("You are authorised to act as the following users."),
                act_as_title_text=_("Act as another user"),
                act_as_button_text=_("Act as another user"),
                act_as_self_text=_("Stop acting as another user"),
                # #3070: Add id and the text of "My setting" menu
                my_setting_text=settings.SITE.is_installed('users') and settings.SITE.plugins.users.my_setting_text or _("My settings"),
                user_id=u.pk,
            )

            if su_name:
                user_settings["user_id"] = user_settings["su_id"] = su.id
                user_settings["su_user_type"] = su.user_type

            if not_anon:
                user_settings["authorities"] = u.get_authorities()
                user_settings["dashboard_layout"] = u.dashboard_layout

                if settings.SITE.plugins.users.allow_online_registration:
                    require_verification = not u.is_verified()
                    if require_verification and u.verification_code_sent_on is not None:
                        user_settings['require_verification'] = True
                        expiry_time = (u.verification_code_sent_on + datetime.timedelta(
                            minutes=settings.SITE.plugins.users.verification_code_expires
                        ))
                        with timezone.override('UTC'):
                            expiry_stamp = datetime.datetime.timestamp(
                                timezone.make_naive(expiry_time))
                        user_settings['code_expiry'] = expiry_stamp

            return json_response(user_settings)

        # f = open('non-existent-file.txt', 'r')

        return with_user_profile((su or u).user_type, getit)
        # return http.HttpResponse(status=500)
