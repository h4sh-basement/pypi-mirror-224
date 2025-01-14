#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
from collections import OrderedDict
from hashlib import md5

from django.db.models.fields import DecimalField
from django.db.models.query import QuerySet, RawQuerySet
from django.utils.safestring import mark_safe

from .columns import Column, BoundColumn, SequenceColumn
from .utils import get_callable_or_not_queryset
from .widgets import SearchBox, InfoLabel, Pagination, LengthMenu, StdButton


class BaseTable(object):

    def __init__(self, data=None):
        self.data = TableData(data, self)

        # Make a copy so that modifying this will not touch the class definition.
        self.columns = copy.deepcopy(self.base_columns)
        # Build table add-ons
        self.addons = TableWidgets(self)

    @staticmethod
    def extrajavascript(*args, **kwargs):
        return ""

    @property
    def rows(self):
        rows = []
        for obj in self.data:
            # Binding object to each column of each row, so that
            # data structure for each row is organized like this:
            # { boundcol0: td, boundcol1: td, boundcol2: td }
            row = OrderedDict()
            columns = [BoundColumn(obj, col) for col in self.columns if col.space]
            for col in columns:
                row[col] = col.html
            rows.append(row)
        return rows

    @property
    def header_rows(self):
        """
        [ [header1], [header3, header4] ]
        """
        # TO BE FIX: refactor
        header_rows = []
        headers = [col.header for col in self.columns]
        for header in headers:
            if len(header_rows) <= header.row_order:
                header_rows.append([])
            header_rows[header.row_order].append(header)
        return header_rows


class TableData(object):
    def __init__(self, data, table):
        model = getattr(table.opts, "model", None)
        if (data is not None and not hasattr(data, "__iter__") or
                data is None and model is None):
            raise ValueError("Model option or QuerySet-like object data"
                             "is required.")
        if data is None:
            self.queryset = model.objects.all()
        elif isinstance(data, QuerySet) or isinstance(data, RawQuerySet):
            self.queryset = data
        else:
            self.list = list(data)

    @property
    def data(self):
        return self.queryset if hasattr(self, "queryset") else self.list

    def __len__(self):
        return (self.queryset.count() if hasattr(self, 'queryset')
                else len(self.list))

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, key):
        return self.data[key]


class TableDataMap(object):
    """
    A data map that represents relationship between Table instance and
    Model.
    """
    map = {}

    @classmethod
    def register(cls, token, model, columns, queryset):
        if token not in TableDataMap.map:
            TableDataMap.map[token] = (model, columns, queryset)

    @classmethod
    def get_model(cls, token):
        return TableDataMap.map.get(token)[0]

    @classmethod
    def get_columns(cls, token):
        return TableDataMap.map.get(token)[1]

    @classmethod
    def get_queryset(cls, token, request):
        model = TableDataMap.get_model(token)
        if model is None:
            return None
        queryset = TableDataMap.map.get(token)[2]
        return get_callable_or_not_queryset(request, model, queryset)


class TableWidgets(object):
    def __init__(self, table):
        opts = table.opts
        self.search_box = SearchBox(opts.search, opts.search_placeholder)
        self.length_menu = LengthMenu(opts.length_menu)
        self.info_label = InfoLabel(opts.info, opts.info_format)
        self.pagination = Pagination(opts.pagination,
                                     opts.page_length,
                                     opts.pagination_first,
                                     opts.pagination_last,
                                     opts.pagination_prev,
                                     opts.pagination_next)
        # self.ext_button = ExtButton(opts.ext_button)
        self.ext_button = opts.ext_button if opts.ext_button else {}
        self.std_button = StdButton(opts.std_button,
                                    opts.std_button_refresh,
                                    opts.std_button_create,
                                    opts.std_button_print,
                                    opts.std_button_pdf,
                                    opts.std_button_excel,
                                    opts.std_button_copy,
                                    opts.std_button_ret)

    def render_dom(self):
        dom = ''
        # if self.search_box.visible or self.ext_button:
        if self.search_box.visible:
            dom += "<'row'" + ''.join([("<'ext-btn'>" if self.ext_button else ''), self.search_box.dom]) + ">"
        dom += "rt"
        dom += "<'row'"
        if self.info_label.visible or self.pagination.visible or self.length_menu.visible:
            dom += ''.join([self.info_label.dom, self.pagination.dom, self.length_menu.dom])
        # if not self.search_box.visible and not self.ext_button and self.std_button.visible:
        if not self.search_box.visible and self.std_button.visible:
            dom += "<'col-sm-3 col-md-3 col-lg-3 text-right'B>"
        dom += ">"
        return mark_safe(dom)


class TableOptions(object):
    def __init__(self, options=None):
        self.model = getattr(options, 'model', None)

        # ajax option
        self.ajax = getattr(options, 'ajax', False)
        self.ajax_source = getattr(options, 'ajax_source', None)

        # id attribute of <table> tag
        self.id = getattr(options, 'id', None)

        # build attributes for <table> tag, use bootstrap
        # css class "table table-boarded" as default style
        attrs = getattr(options, 'attrs', {})
        attrs['class'] = 'table ' + attrs.get('class', 'table-striped table-hover table-condensed')
        self.attrs = mark_safe(' '.join(['%s="%s"' % (attr_name, attr)
                                         for attr_name, attr in attrs.items()]))
        # build attributes for <thead> and <tbody>
        thead_attrs = getattr(options, 'thead_attrs', {})
        self.thead_attrs = mark_safe(' '.join(['%s="%s"' % (attr_name, attr)
                                               for attr_name, attr in thead_attrs.items()]))
        tbody_attrs = getattr(options, 'tbody_attrs', {})
        self.tbody_attrs = mark_safe(' '.join(['%s="%s"' % (attr_name, attr)
                                               for attr_name, attr in tbody_attrs.items()]))

        # scrolling option
        self.scrollable = getattr(options, 'scrollable', False)
        self.scrollinner = getattr(options, 'scrollinner', "100%")
        self.fixed_columns = getattr(options, 'fixed_columns', None)
        self.fixed_columns_width = getattr(options, 'fixed_columns_width', None)

        # inspect sorting option
        self.sort = []
        for column, order in getattr(options, 'sort', []):
            if not isinstance(column, int):
                raise ValueError('Sorting option must be organized by following'
                                 ' forms: [(0, "asc"), (1, "desc")]')
            if order not in ('asc', 'desc'):
                raise ValueError('Order value must be "asc" or "desc", '
                                 '"%s" is unsupported.' % order)
            self.sort.append((column, order))

        # options for table add-on
        self.search = getattr(options, 'search', True)
        self.search_placeholder = getattr(options, 'search_placeholder', 'Localizar')

        self.info = getattr(options, 'info', True)
        self.info_format = getattr(options, 'info_format', None)

        self.pagination = getattr(options, 'pagination', True)
        self.page_length = getattr(options, 'page_length', 25)
        self.pagination_first = getattr(options, 'pagination_first', 'Primeira')
        self.pagination_last = getattr(options, 'pagination_last', 'Última')
        self.pagination_prev = getattr(options, 'pagination_prev', 'Anterior')
        self.pagination_next = getattr(options, 'pagination_next', 'Próxima')

        self.length_menu = getattr(options, 'length_menu', True)

        self.ext_button = getattr(options, 'ext_button', False)

        self.std_button = getattr(options, 'std_button', True)
        self.std_button_refresh = getattr(options, 'std_button_refresh', True)
        self.std_button_create_href = getattr(options, 'std_button_create_href', 'add/')
        self.std_button_create = getattr(options, 'std_button_create',
                                         {'text': 'Incluir', 'icon': 'fa fa-plus-square fa-fw',
                                          'href': self.std_button_create_href, "className": 'btn btn-primary btn-sm', })
        self.std_button_print = getattr(options, 'std_button_print', True)
        self.std_button_pdf = getattr(options, 'std_button_pdf', True)
        self.std_button_excel = getattr(options, 'std_button_excel', True)
        self.std_button_copy = getattr(options, 'std_button_copy', False)
        self.std_button_ret = getattr(options, 'std_button_ret', None)  # {"txt": "Cancelar", action='cancel'})

        self.zero_records = getattr(options, 'zero_records', u'Sem registros')

        # Se há campo a ser totalizado no rodapé
        self.totals = getattr(options, 'totals', False)
        self.decimal_places = getattr(options, 'decimal_places', 0)

        # Se saveState é false, então apesar de usar os filtros de select, sempre volta para a primeira página,
        # senão volta para a página salva
        self.stateSave = getattr(options, 'stateSave', True)

        # Queryset para filtro do que será listado. Pode ser QuerySet ou function com request
        self.queryset = getattr(options, 'queryset', None)

        # Form para título do relatório
        self.titleForm = getattr(options, 'titleForm', None)

        # Form para rodapé do relatório
        self.footerForm = getattr(options, 'footerForm', None)


class TableMetaClass(type):
    """ Meta class for create Table class instance.
    """

    def __new__(cls, name, bases, attrs):
        opts = TableOptions(attrs.get('Meta', None))
        # take class name in lower case as table's id
        if opts.id is None:
            # from django.utils.crypto import get_random_string
            # if self.id:
            #     self.id += get_random_string(length=10)
            # else:
            #     self.id = get_random_string(length=10)
            opts.id = name.lower()  # +get_random_string(length=10)
        attrs['opts'] = opts

        # extract declared columns
        columns = []
        for attr_name, attr in attrs.items():
            # print('attr_name=%', attr_name, 'attr=', attr)
            if isinstance(attr, SequenceColumn):
                columns.extend(attr)
            elif isinstance(attr, Column):
                # Não precisa render para decimal pois o valor já vai formatado no campo de valor do AJAX,
                # mas pega decimal_places
                try:
                    f = opts.model._meta.get_field(attr_name)
                    if f and isinstance(f, DecimalField) and f.decimal_places > 0:
                        attr.decimal_places = f.decimal_places
                    # Seta header para o nome do campo no modelo se o header é nulo
                    if f and attr.header.text == None:
                        attr.header.text = f.verbose_name
                except Exception as v:
                    pass
                if attr.totals and not opts.totals:
                    opts.totals = True
                columns.append(attr)
        columns.sort(key=lambda x: x.instance_order)

        # If this class is subclassing other tables, add their fields as
        # well. Note that we loop over the bases in reverse - this is
        # necessary to preserve the correct order of columns.
        parent_columns = []
        for base in bases[::-1]:
            if hasattr(base, "base_columns"):
                parent_columns = base.base_columns + parent_columns
        base_columns = parent_columns + columns

        # For ajax data source, store columns into global hash map with
        # unique token key. So that, columns can be get to construct data
        # on views layer.
        token = md5(name.encode('utf-8')).hexdigest()
        if opts.ajax:
            TableDataMap.register(token, opts.model, copy.deepcopy(base_columns), opts.queryset)

        attrs['token'] = token
        attrs['base_columns'] = base_columns

        return super(TableMetaClass, cls).__new__(cls, name, bases, attrs)


Table = TableMetaClass('Table', (BaseTable,), {})
