import copy
from typing import List, Union

from tablate.library.calcs.calc_column_widths import calc_column_widths
from tablate.library.checkers.set_attr_resolver import set_attr_resolver
from tablate.library.initializers.mappers.element.base.base_frame_mapper import base_frame_mapper
from tablate.library.initializers.mappers.element.base.base_rows_mapper import base_rows_mapper
from tablate.library.initializers.mappers.element.html.html_rows_mapper import html_rows_mapper
from tablate.library.initializers.mappers.element.style_mapper import style_mapper
from tablate.library.initializers.mappers.attribute.column_attr import column_attr
from tablate.library.initializers.mappers.object.base_frame_input_to_store import base_frame_input_to_store
from tablate.library.initializers.mappers.object.html_frame_input_to_store import html_frame_input_to_store
from tablate.type.defaults import table_multiline_default, table_header_text_style_default, header_base_divider_default, \
    background_padding_default, frame_name_default, html_px_multiplier_default
from tablate.type.type_global import Globals
from tablate.type.type_store import TableBodyFrameStore, TableHeaderFrameStore, BaseFrameStore, HtmlFrameStore
from tablate.type.type_input import TableRowsInput, TableHeaderFrameStylesInput, TableBodyFrameStylesInput, \
    HtmlTableFrameStylesInput, HtmlTableHeaderStylesInput, HtmlTableBodyStylesInput, TableColumnInput
from tablate.type.primitives import FrameDivider, ColumnDivider, Multiline, MaxLines, HideHeader, ColumnPadding, \
    TextStyle, TextAlign, TextColor, Background, HtmlPxMultiplier, BackgroundPadding, FrameName
from tablate.type.type_style import FrameStyles, TextStyles, ColumnStyles, TableRowsStyles, HtmlTableRowsStyles


def table_init(columns: List[TableColumnInput],
               rows: List[TableRowsInput],

               name: FrameName,

               frame_divider: FrameDivider,
               multiline: Multiline,
               max_lines: MaxLines,
               background: Background,
               background_padding: BackgroundPadding,

               multiline_header: Multiline,
               max_lines_header: MaxLines,
               hide_header: HideHeader,

               column_divider: ColumnDivider,
               column_padding: ColumnPadding,
               header_base_divider: FrameDivider,

               row_line_divider: FrameDivider,
               odd_row_background: Background,
               even_row_background: Background,

               text_style: TextStyle,
               text_align: TextAlign,
               text_color: TextColor,

               header_styles: TableHeaderFrameStylesInput,

               html_px_multiplier: HtmlPxMultiplier,
               html_styles: HtmlTableFrameStylesInput,

               html_header_styles: HtmlTableHeaderStylesInput,

               global_options: Globals) -> (Union[TableHeaderFrameStore, None], TableBodyFrameStore):
    ####################################################################################################################

    columns = copy.deepcopy(columns)
    rows = copy.deepcopy(rows)

    ####################################################################################################################
    header_styles = base_frame_input_to_store(header_styles, frame_type="table")
    # body_styles = base_frame_input_to_store(body_styles, frame_type="table")
    html_styles = html_frame_input_to_store(html_styles, frame_type="table")
    html_header_styles = html_frame_input_to_store(html_header_styles, frame_type="table")
    # html_body_styles = html_frame_input_to_store(html_body_styles, frame_type="table")

    background_padding = background_padding if background_padding is not None else set_attr_resolver(
        instance=global_options.console.outer_styles,
        attr="background_padding",
        default=background_padding_default)

    name = name if name is not None else frame_name_default
    hide_header = hide_header if hide_header is not None else False

    #############################################
    #############################################
    #############################################

    table_all_frame_defaults = base_frame_mapper(frame_input=global_options.console.frame_styles)
    table_all_frame_defaults.multiline = multiline if multiline else table_multiline_default
    table_all_base_defaults = BaseFrameStore(frame_styles=base_frame_mapper(frame_input=table_all_frame_defaults,
                                                                            frame_defaults=global_options.console.frame_styles),
                                             column_styles=global_options.console.column_styles,
                                             text_styles=global_options.console.text_styles)

    table_all_html_defaults = HtmlFrameStore(html_frame_styles=global_options.html.html_frame_styles,
                                             html_column_styles=global_options.html.html_column_styles,
                                             html_text_styles=global_options.html.html_text_styles)

    table_all_html_defaults.html_frame_styles.html_multiline = table_all_frame_defaults.multiline

    #############################################

    table_styles = style_mapper(base_input=BaseFrameStore(frame_styles=FrameStyles(frame_divider=frame_divider,
                                                                                   max_lines=max_lines,
                                                                                   multiline=multiline,
                                                                                   background=background),
                                                          column_styles=ColumnStyles(column_divider=column_divider,
                                                                                     padding=column_padding,
                                                                                     background_padding=background_padding),
                                                          text_styles=TextStyles(text_style=text_style,
                                                                                 text_align=text_align,
                                                                                 text_color=text_color)),
                                base_defaults=table_all_base_defaults,
                                html_input=html_styles,
                                html_defaults=table_all_html_defaults,
                                html_px_multiplier=html_px_multiplier,
                                global_options=global_options)

    ####################################################################################################################

    header_base_frame_defaults = copy.deepcopy(table_styles.frame_styles)
    header_base_frame_defaults.frame_divider = header_base_divider if header_base_divider else header_base_divider_default
    header_base_frame_defaults.multiline = multiline_header if multiline_header else table_multiline_default
    header_base_frame_defaults.max_lines = max_lines_header

    header_base_text_defaults = copy.deepcopy(table_styles.text_styles)
    header_base_text_defaults.text_style = table_header_text_style_default

    compiled_header_styles = style_mapper(base_input=header_styles,
                                          html_input=html_header_styles,
                                          base_defaults=BaseFrameStore(frame_styles=header_base_frame_defaults,
                                                                       column_styles=table_styles.column_styles,
                                                                       text_styles=header_base_text_defaults),
                                          html_defaults=HtmlFrameStore(html_frame_styles=table_styles.html_frame_styles,
                                                                       html_column_styles=table_styles.html_column_styles,
                                                                       html_text_styles=table_styles.html_text_styles),
                                          html_px_multiplier=html_px_multiplier,
                                          global_options=global_options)

    ####################################################################################################################

    html_body_rows_styles = set_attr_resolver(html_styles, "html_row_styles", HtmlTableRowsStyles())

    body_base_row_styles = base_rows_mapper(rows_input=TableRowsStyles(row_line_divider=row_line_divider,
                                                                       evens_background=even_row_background,
                                                                       odds_background=odd_row_background))
    body_html_row_styles = html_rows_mapper(html_rows_input=html_body_rows_styles,
                                            base_rows_defaults=body_base_row_styles)

    #############################################
    #############################################
    #############################################

    columns = calc_column_widths(columns=columns, global_options=global_options)

    header_column_list = []
    rows_column_list = []

    for column_item in columns:
        column_item["string"] = column_item["string"] if "string" in column_item else column_item["key"]

        head_column_dict = column_attr(column_dict=column_item,
                                       base_frame_styles=compiled_header_styles.frame_styles,
                                       base_column_styles=compiled_header_styles.column_styles,
                                       base_text_styles=compiled_header_styles.text_styles,
                                       html_frame_styles=compiled_header_styles.html_frame_styles,
                                       html_column_styles=compiled_header_styles.html_column_styles,
                                       html_text_styles=compiled_header_styles.html_text_styles,
                                       html_px_multiplier=html_px_multiplier if html_px_multiplier is not None else html_px_multiplier_default)

        body_column_dict = column_attr(column_dict=column_item,
                                       base_frame_styles=table_styles.frame_styles,
                                       base_column_styles=table_styles.column_styles,
                                       base_text_styles=table_styles.text_styles,
                                       html_frame_styles=table_styles.html_frame_styles,
                                       html_column_styles=table_styles.html_column_styles,
                                       html_text_styles=table_styles.html_text_styles,
                                       html_px_multiplier=html_px_multiplier if html_px_multiplier is not None else html_px_multiplier_default)

        header_column_list.append(head_column_dict)

        rows_column_list.append(body_column_dict)

    header_frame_store: Union[TableHeaderFrameStore, None]

    if not hide_header:
        header_frame_store = TableHeaderFrameStore(type="table_header",
                                                   name=name,
                                                   column_list=header_column_list,
                                                   frame_styles=compiled_header_styles.frame_styles,
                                                   column_styles=compiled_header_styles.column_styles,
                                                   text_styles=compiled_header_styles.text_styles,
                                                   html_frame_styles=compiled_header_styles.html_frame_styles,
                                                   html_column_styles=compiled_header_styles.html_column_styles,
                                                   html_text_styles=compiled_header_styles.html_text_styles)
    else:
        header_frame_store = None

    body_frame_store = TableBodyFrameStore(type="table_body",
                                           name=name,
                                           hide_header=hide_header,
                                           column_list=rows_column_list,
                                           row_list=rows,
                                           frame_styles=table_styles.frame_styles,
                                           row_styles=body_base_row_styles,
                                           column_styles=table_styles.column_styles,
                                           text_styles=table_styles.text_styles,
                                           html_frame_styles=table_styles.html_frame_styles,
                                           html_row_styles=body_html_row_styles,
                                           html_column_styles=table_styles.html_column_styles,
                                           html_text_styles=table_styles.html_text_styles)

    return header_frame_store, body_frame_store
