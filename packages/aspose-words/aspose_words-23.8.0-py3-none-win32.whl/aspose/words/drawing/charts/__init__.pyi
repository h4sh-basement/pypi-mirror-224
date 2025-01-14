﻿import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class AxisBound:
    '''Represents minimum or maximum bound of axis values.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.
    
    Bound can be specified as a numeric, datetime or a special "auto" value.
    
    The instances of this class are immutable.'''
    
    @overload
    def __init__(self):
        '''Creates a new instance indicating that axis bound should be determined automatically by a word-processing
        application.'''
        ...
    
    @overload
    def __init__(self, value: float):
        '''Creates an axis bound represented as a number.'''
        ...
    
    @overload
    def __init__(self, datetime: datetime.datetime):
        '''Creates an axis bound represented as datetime value.'''
        ...
    
    @property
    def is_auto(self) -> bool:
        '''Returns a flag indicating that axis bound should be determined automatically.'''
        ...
    
    @property
    def value(self) -> float:
        '''Returns numeric value of axis bound.'''
        ...
    
    @property
    def value_as_date(self) -> datetime.datetime:
        '''Returns value of axis bound represented as datetime.'''
        ...
    
    ...

class AxisDisplayUnit:
    '''Provides access to the scaling options of the display units for the value axis.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    def __init__(self):
        ...
    
    @property
    def unit(self) -> aspose.words.drawing.charts.AxisBuiltInUnit:
        '''Gets or sets the scaling value of the display units as one of the predefined values.
        
        Default value is :attr:`AxisBuiltInUnit.NONE`. The :attr:`AxisBuiltInUnit.CUSTOM` and
        :attr:`AxisBuiltInUnit.PERCENTAGE` values are not available in some chart types; see
        :class:`AxisBuiltInUnit` for more information.'''
        ...
    
    @unit.setter
    def unit(self, value: aspose.words.drawing.charts.AxisBuiltInUnit):
        ...
    
    @property
    def custom_unit(self) -> float:
        '''Gets or sets a user-defined divisor to scale display units on the value axis.
        
        The property is not supported by MS Office 2016 new charts. Default value is 1.
        
        Setting this property sets the :attr:`AxisDisplayUnit.unit` property to
        :attr:`AxisBuiltInUnit.CUSTOM`.'''
        ...
    
    @custom_unit.setter
    def custom_unit(self, value: float):
        ...
    
    @property
    def document(self) -> aspose.words.DocumentBase:
        '''Returns the Document the title holder belongs.'''
        ...
    
    ...

class AxisScaling:
    '''Represents the scaling options of the axis.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    def __init__(self):
        ...
    
    @property
    def type(self) -> aspose.words.drawing.charts.AxisScaleType:
        '''Gets or sets scaling type of the axis.
        
        The :attr:`AxisScaleType.LINEAR` value is the only that is allowed in MS Office 2016 new charts.'''
        ...
    
    @type.setter
    def type(self, value: aspose.words.drawing.charts.AxisScaleType):
        ...
    
    @property
    def log_base(self) -> float:
        '''Gets or sets the logarithmic base for a logarithmic axis.
        
        The property is not supported by MS Office 2016 new charts.
        
        Valid range of a floating point value is greater than or equal to 2 and less than or
        equal to 1000. The property has effect only if :attr:`AxisScaling.type` is set to
        :attr:`AxisScaleType.LOGARITHMIC`.
        
        Setting this property sets the :attr:`AxisScaling.type` property to :attr:`AxisScaleType.LOGARITHMIC`.'''
        ...
    
    @log_base.setter
    def log_base(self, value: float):
        ...
    
    @property
    def minimum(self) -> aspose.words.drawing.charts.AxisBound:
        '''Gets or sets minimum value of the axis.
        
        The default value is "auto".'''
        ...
    
    @minimum.setter
    def minimum(self, value: aspose.words.drawing.charts.AxisBound):
        ...
    
    @property
    def maximum(self) -> aspose.words.drawing.charts.AxisBound:
        '''Gets or sets the maximum value of the axis.
        
        The default value is "auto".'''
        ...
    
    @maximum.setter
    def maximum(self, value: aspose.words.drawing.charts.AxisBound):
        ...
    
    ...

class BubbleSizeCollection:
    '''Represents a collection of bubble sizes for a chart series.
    
    The collection allows only changing bubble sizes. To add or insert new values to a chart series, or remove
    values, the appropriate methods of the :class:`ChartSeries` class can be used.
    
    Empty bubble size values are represented as System.Double.NaN.'''
    
    def __getitem__(self, index: int) -> float:
        '''Gets or sets the bubble size value at the specified index.'''
        ...
    
    def __setitem__(self, index: int, value: float):
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of items in this collection.'''
        ...
    
    ...

class Chart:
    '''Provides access to the chart shape properties.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    @property
    def series(self) -> aspose.words.drawing.charts.ChartSeriesCollection:
        '''Provides access to series collection.'''
        ...
    
    @property
    def title(self) -> aspose.words.drawing.charts.ChartTitle:
        '''Provides access to the chart title properties.'''
        ...
    
    @property
    def legend(self) -> aspose.words.drawing.charts.ChartLegend:
        '''Provides access to the chart legend properties.'''
        ...
    
    @property
    def axis_x(self) -> aspose.words.drawing.charts.ChartAxis:
        '''Provides access to properties of the X axis of the chart.'''
        ...
    
    @property
    def axis_y(self) -> aspose.words.drawing.charts.ChartAxis:
        '''Provides access to properties of the Y axis of the chart.'''
        ...
    
    @property
    def axis_z(self) -> aspose.words.drawing.charts.ChartAxis:
        '''Provides access to properties of the Z axis of the chart.'''
        ...
    
    @property
    def axes(self) -> aspose.words.drawing.charts.ChartAxisCollection:
        '''Gets a collection of all axes of this chart.'''
        ...
    
    @property
    def source_full_name(self) -> str:
        '''Gets the path and name of an xls/xlsx file this chart is linked to.'''
        ...
    
    @source_full_name.setter
    def source_full_name(self, value: str):
        ...
    
    ...

class ChartAxis:
    '''Represents the axis options of the chart.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    @property
    def type(self) -> aspose.words.drawing.charts.ChartAxisType:
        '''Returns type of the axis.'''
        ...
    
    @property
    def category_type(self) -> aspose.words.drawing.charts.AxisCategoryType:
        '''Gets or sets type of the category axis.
        
        Only text categories (:attr:`AxisCategoryType.CATEGORY`) are allowed in MS Office 2016 new charts.'''
        ...
    
    @category_type.setter
    def category_type(self, value: aspose.words.drawing.charts.AxisCategoryType):
        ...
    
    @property
    def crosses(self) -> aspose.words.drawing.charts.AxisCrosses:
        '''Specifies how this axis crosses the perpendicular axis.
        
        Default value is :attr:`AxisCrosses.AUTOMATIC`.
        
        The property is not supported by MS Office 2016 new charts.'''
        ...
    
    @crosses.setter
    def crosses(self, value: aspose.words.drawing.charts.AxisCrosses):
        ...
    
    @property
    def crosses_at(self) -> float:
        '''Specifies where on the perpendicular axis the axis crosses.
        
        The property has effect only if :attr:`ChartAxis.crosses` are set to :attr:`AxisCrosses.CUSTOM`.
        It is not supported by MS Office 2016 new charts.
        
        The units are determined by the type of axis. When the axis is a value axis, the value of the property
        is a decimal number on the value axis. When the axis is a time category axis, the value is defined as
        an integer number of days relative to the base date (30/12/1899). For a text category axis, the value is
        an integer category number, starting with 1 as the first category.'''
        ...
    
    @crosses_at.setter
    def crosses_at(self, value: float):
        ...
    
    @property
    def reverse_order(self) -> bool:
        '''Returns or sets a flag indicating whether values of axis should be displayed in reverse order, i.e.
        from max to min.
        
        The property is not supported by MS Office 2016 new charts. Default value is ``False``.'''
        ...
    
    @reverse_order.setter
    def reverse_order(self, value: bool):
        ...
    
    @property
    def major_tick_mark(self) -> aspose.words.drawing.charts.AxisTickMark:
        '''Returns or sets the major tick marks.'''
        ...
    
    @major_tick_mark.setter
    def major_tick_mark(self, value: aspose.words.drawing.charts.AxisTickMark):
        ...
    
    @property
    def minor_tick_mark(self) -> aspose.words.drawing.charts.AxisTickMark:
        '''Returns or sets the minor tick marks for the axis.'''
        ...
    
    @minor_tick_mark.setter
    def minor_tick_mark(self, value: aspose.words.drawing.charts.AxisTickMark):
        ...
    
    @property
    def tick_label_position(self) -> aspose.words.drawing.charts.AxisTickLabelPosition:
        '''Returns or sets the position of the tick labels on the axis.
        
        The property is not supported by MS Office 2016 new charts.'''
        ...
    
    @tick_label_position.setter
    def tick_label_position(self, value: aspose.words.drawing.charts.AxisTickLabelPosition):
        ...
    
    @property
    def major_unit(self) -> float:
        '''Returns or sets the distance between major tick marks.
        
        Valid range of a value is greater than zero. The property has effect for time category and
        value axes.
        
        Setting this property sets the :attr:`ChartAxis.major_unit_is_auto` property to ``False``.'''
        ...
    
    @major_unit.setter
    def major_unit(self, value: float):
        ...
    
    @property
    def major_unit_is_auto(self) -> bool:
        '''Gets or sets a flag indicating whether default distance between major tick marks shall be used.
        
        The property has effect for time category and value axes.'''
        ...
    
    @major_unit_is_auto.setter
    def major_unit_is_auto(self, value: bool):
        ...
    
    @property
    def major_unit_scale(self) -> aspose.words.drawing.charts.AxisTimeUnit:
        '''Returns or sets the scale value for major tick marks on the time category axis.
        
        The property has effect only for time category axes.'''
        ...
    
    @major_unit_scale.setter
    def major_unit_scale(self, value: aspose.words.drawing.charts.AxisTimeUnit):
        ...
    
    @property
    def minor_unit(self) -> float:
        '''Returns or sets the distance between minor tick marks.
        
        Valid range of a value is greater than zero. The property has effect for time category and
        value axes.
        
        Setting this property sets the :attr:`ChartAxis.minor_unit_is_auto` property to ``False``.'''
        ...
    
    @minor_unit.setter
    def minor_unit(self, value: float):
        ...
    
    @property
    def minor_unit_is_auto(self) -> bool:
        '''Gets or sets a flag indicating whether default distance between minor tick marks shall be used.
        
        The property has effect for time category and value axes.'''
        ...
    
    @minor_unit_is_auto.setter
    def minor_unit_is_auto(self, value: bool):
        ...
    
    @property
    def minor_unit_scale(self) -> aspose.words.drawing.charts.AxisTimeUnit:
        '''Returns or sets the scale value for minor tick marks on the time category axis.
        
        The property has effect only for time category axes.'''
        ...
    
    @minor_unit_scale.setter
    def minor_unit_scale(self, value: aspose.words.drawing.charts.AxisTimeUnit):
        ...
    
    @property
    def base_time_unit(self) -> aspose.words.drawing.charts.AxisTimeUnit:
        '''Returns or sets the smallest time unit that is represented on the time category axis.
        
        The property has effect only for time category axes.'''
        ...
    
    @base_time_unit.setter
    def base_time_unit(self, value: aspose.words.drawing.charts.AxisTimeUnit):
        ...
    
    @property
    def number_format(self) -> aspose.words.drawing.charts.ChartNumberFormat:
        '''Returns a :class:`ChartNumberFormat` object that allows defining number formats for the axis.'''
        ...
    
    @property
    def tick_label_offset(self) -> int:
        '''Gets or sets the distance of labels from the axis.
        
        The property represents a percentage of the default label offset.
        
        Valid range is from 0 to 1000 percent inclusive. Default value is 100%.
        
        The property has effect only for category axes. It is not supported by MS Office 2016 new charts.'''
        ...
    
    @tick_label_offset.setter
    def tick_label_offset(self, value: int):
        ...
    
    @property
    def display_unit(self) -> aspose.words.drawing.charts.AxisDisplayUnit:
        '''Specifies the scaling value of the display units for the value axis.
        
        The property has effect only for value axes.'''
        ...
    
    @property
    def axis_between_categories(self) -> bool:
        '''Gets or sets a flag indicating whether the value axis crosses the category axis between categories.
        
        The property has effect only for value axes. It is not supported by MS Office 2016 new charts.'''
        ...
    
    @axis_between_categories.setter
    def axis_between_categories(self, value: bool):
        ...
    
    @property
    def scaling(self) -> aspose.words.drawing.charts.AxisScaling:
        '''Provides access to the scaling options of the axis.'''
        ...
    
    @property
    def tick_label_spacing(self) -> int:
        '''Gets or sets the interval, at which tick labels are drawn.
        
        The property has effect for text category and series axes. It is not supported by MS Office 2016
        new charts. Valid range of a value is greater than or equal to 1.
        
        Setting this property sets the :attr:`ChartAxis.tick_label_spacing_is_auto` property to ``False``.'''
        ...
    
    @tick_label_spacing.setter
    def tick_label_spacing(self, value: int):
        ...
    
    @property
    def tick_label_spacing_is_auto(self) -> bool:
        '''Gets or sets a flag indicating whether automatic interval of drawing tick labels shall be used.
        
        Default value is ``True``.
        
        The property has effect for text category and series axes. It is not supported by MS Office 2016
        new charts.'''
        ...
    
    @tick_label_spacing_is_auto.setter
    def tick_label_spacing_is_auto(self, value: bool):
        ...
    
    @property
    def tick_label_alignment(self) -> aspose.words.ParagraphAlignment:
        '''Gets or sets text alignment of axis tick labels.
        
        This property has effect only for multi-line labels.
        
        Default value is :attr:`aspose.words.ParagraphAlignment.CENTER`.
        
        .'''
        ...
    
    @tick_label_alignment.setter
    def tick_label_alignment(self, value: aspose.words.ParagraphAlignment):
        ...
    
    @property
    def tick_mark_spacing(self) -> int:
        '''Gets or sets the interval, at which tick marks are drawn.
        
        The property has effect for text category and series axes. It is not supported by MS Office 2016
        new charts.
        
        Valid range of a value is greater than or equal to 1.'''
        ...
    
    @tick_mark_spacing.setter
    def tick_mark_spacing(self, value: int):
        ...
    
    @property
    def hidden(self) -> bool:
        '''Gets or sets a flag indicating whether this axis is hidden or not.
        
        Default value is ``False``.'''
        ...
    
    @hidden.setter
    def hidden(self, value: bool):
        ...
    
    @property
    def has_major_gridlines(self) -> bool:
        '''Gets or sets a flag indicating whether the axis has major gridlines.'''
        ...
    
    @has_major_gridlines.setter
    def has_major_gridlines(self, value: bool):
        ...
    
    @property
    def has_minor_gridlines(self) -> bool:
        '''Gets or sets a flag indicating whether the axis has minor gridlines.'''
        ...
    
    @has_minor_gridlines.setter
    def has_minor_gridlines(self, value: bool):
        ...
    
    @property
    def document(self) -> aspose.words.DocumentBase:
        '''Returns the Document the title holder belongs.'''
        ...
    
    ...

class ChartAxisCollection:
    '''Represents a collection of chart axes.'''
    
    def __getitem__(self, index: int) -> aspose.words.drawing.charts.ChartAxis:
        '''Gets the axis at the specified index.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of axes in this collection.'''
        ...
    
    ...

class ChartDataLabel:
    '''Represents data label on a chart point or trendline.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.
    
    On a series, the :class:`ChartDataLabel` object is a member of the :class:`ChartDataLabelCollection`.
    The :class:`ChartDataLabelCollection` contains a :class:`ChartDataLabel` object for each point.'''
    
    def clear_format(self) -> None:
        '''Clears format of this data label. The properties are set to the default values defined in the parent data
        label collection.'''
        ...
    
    @property
    def index(self) -> int:
        '''Specifies the index of the containing element.
        This index shall determine which of the parent's children collection this element applies to.
        Default value is 0.'''
        ...
    
    @property
    def show_category_name(self) -> bool:
        '''Allows to specify if category name is to be displayed for the data labels on a chart.
        Default value is ``False``.'''
        ...
    
    @show_category_name.setter
    def show_category_name(self, value: bool):
        ...
    
    @property
    def show_bubble_size(self) -> bool:
        '''Allows to specify if bubble size is to be displayed for the data labels on a chart.
        Applies only to Bubble charts.
        Default value is ``False``.'''
        ...
    
    @show_bubble_size.setter
    def show_bubble_size(self, value: bool):
        ...
    
    @property
    def show_legend_key(self) -> bool:
        '''Allows to specify if legend key is to be displayed for the data labels on a chart.
        Default value is ``False``.'''
        ...
    
    @show_legend_key.setter
    def show_legend_key(self, value: bool):
        ...
    
    @property
    def show_percentage(self) -> bool:
        '''Allows to specify if percentage value is to be displayed for the data labels on a chart.
        Default value is ``False``.'''
        ...
    
    @show_percentage.setter
    def show_percentage(self, value: bool):
        ...
    
    @property
    def show_series_name(self) -> bool:
        '''Returns or sets a Boolean to indicate the series name display behavior for the data labels on a chart.
        ``True`` to show the series name; ``False`` to hide. By default ``False``.'''
        ...
    
    @show_series_name.setter
    def show_series_name(self, value: bool):
        ...
    
    @property
    def show_value(self) -> bool:
        '''Allows to specify if values are to be displayed in the data labels.
        Default value is ``False``.'''
        ...
    
    @show_value.setter
    def show_value(self, value: bool):
        ...
    
    @property
    def show_leader_lines(self) -> bool:
        '''Allows to specify if data label leader lines need be shown.
        Default value is ``False``.
        
        Applies to Pie charts only.
        Leader lines create a visual connection between a data label and its corresponding data point.'''
        ...
    
    @show_leader_lines.setter
    def show_leader_lines(self, value: bool):
        ...
    
    @property
    def show_data_labels_range(self) -> bool:
        '''Allows to specify if values from data labels range to be displayed in the data labels.
        Default value is ``False``.'''
        ...
    
    @show_data_labels_range.setter
    def show_data_labels_range(self, value: bool):
        ...
    
    @property
    def separator(self) -> str:
        '''Gets or sets string separator used for the data labels on a chart.
        The default is a comma, except for pie charts showing only category name and percentage, when a line break
        shall be used instead.'''
        ...
    
    @separator.setter
    def separator(self, value: str):
        ...
    
    @property
    def is_visible(self) -> bool:
        '''Returns ``True`` if this data label has something to display.'''
        ...
    
    @property
    def number_format(self) -> aspose.words.drawing.charts.ChartNumberFormat:
        '''Returns number format of the parent element.'''
        ...
    
    @property
    def is_hidden(self) -> bool:
        '''Gets/sets a flag indicating whether this label is hidden.
        The default value is ``False``.'''
        ...
    
    @is_hidden.setter
    def is_hidden(self, value: bool):
        ...
    
    @property
    def font(self) -> aspose.words.Font:
        '''Provides access to the font formatting of this data label.'''
        ...
    
    @property
    def format(self) -> aspose.words.drawing.charts.ChartFormat:
        '''Provides access to fill and line formatting of the data label.'''
        ...
    
    ...

class ChartDataLabelCollection:
    '''Represents a collection of :class:`ChartDataLabel`.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.drawing.charts.ChartDataLabel:
        '''Returns :class:`ChartDataLabel` for the specified index.'''
        ...
    
    def clear_format(self) -> None:
        '''Clears format of all :class:`ChartDataLabel` in this collection.'''
        ...
    
    @property
    def count(self) -> int:
        '''Returns the number of :class:`ChartDataLabel` in this collection.'''
        ...
    
    @property
    def show_category_name(self) -> bool:
        '''Allows to specify whether category name is to be displayed for the data labels of the entire series.
        Default value is ``False``.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_category_name` property.'''
        ...
    
    @show_category_name.setter
    def show_category_name(self, value: bool):
        ...
    
    @property
    def show_bubble_size(self) -> bool:
        '''Allows to specify whether bubble size is to be displayed for the data labels of the entire series.
        Applies only to Bubble charts.
        Default value is ``False``.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_bubble_size` property.'''
        ...
    
    @show_bubble_size.setter
    def show_bubble_size(self, value: bool):
        ...
    
    @property
    def show_legend_key(self) -> bool:
        '''Allows to specify whether legend key is to be displayed for the data labels of the entire series.
        Default value is ``False``.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_legend_key` property.'''
        ...
    
    @show_legend_key.setter
    def show_legend_key(self, value: bool):
        ...
    
    @property
    def show_percentage(self) -> bool:
        '''Allows to specify whether percentage value is to be displayed for the data labels of the entire series.
        Default value is ``False``. Applies only to Pie charts.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_percentage` property.'''
        ...
    
    @show_percentage.setter
    def show_percentage(self, value: bool):
        ...
    
    @property
    def show_series_name(self) -> bool:
        '''Returns or sets a Boolean to indicate the series name display behavior for the data labels of the entire series.
        ``True`` to show the series name; ``False`` to hide. By default ``False``.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_series_name` property.'''
        ...
    
    @show_series_name.setter
    def show_series_name(self, value: bool):
        ...
    
    @property
    def show_value(self) -> bool:
        '''Allows to specify whether values are to be displayed in the data labels of the entire series.
        Default value is ``False``.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_value` property.'''
        ...
    
    @show_value.setter
    def show_value(self, value: bool):
        ...
    
    @property
    def show_leader_lines(self) -> bool:
        '''Allows to specify whether data label leader lines need be shown for the data labels of the entire series.
        Default value is ``False``.
        
        Applies to Pie charts only.
        Leader lines create a visual connection between a data label and its corresponding data point.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_leader_lines` property.'''
        ...
    
    @show_leader_lines.setter
    def show_leader_lines(self, value: bool):
        ...
    
    @property
    def show_data_labels_range(self) -> bool:
        '''Allows to specify whether values from data labels range to be displayed in the data labels of the entire series.
        Default value is ``False``.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_data_labels_range` property.'''
        ...
    
    @show_data_labels_range.setter
    def show_data_labels_range(self, value: bool):
        ...
    
    @property
    def separator(self) -> str:
        '''Gets or sets string separator used for the data labels of the entire series.
        The default is a comma, except for pie charts showing only category name and percentage, when a line break
        shall be used instead.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.separator` property.'''
        ...
    
    @separator.setter
    def separator(self, value: str):
        ...
    
    @property
    def number_format(self) -> aspose.words.drawing.charts.ChartNumberFormat:
        '''Gets an :class:`ChartNumberFormat` instance allowing to set number format for the data labels of the
        entire series.'''
        ...
    
    @property
    def font(self) -> aspose.words.Font:
        '''Provides access to the font formatting of the data labels of the entire series.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.font` property.'''
        ...
    
    @property
    def format(self) -> aspose.words.drawing.charts.ChartFormat:
        '''Provides access to fill and line formatting of the data labels.'''
        ...
    
    ...

class ChartDataPoint:
    '''Allows to specify formatting of a single data point on the chart.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.
    
    On a series, the :class:`ChartDataPoint` object is a member of the :class:`ChartDataPointCollection`.
    The :class:`ChartDataPointCollection` contains a :class:`ChartDataPoint` object for each point.'''
    
    def clear_format(self) -> None:
        '''Clears format of this data point. The properties are set to the default values defined in the parent series.'''
        ...
    
    @property
    def index(self) -> int:
        '''Index of the data point this object applies formatting to.'''
        ...
    
    @property
    def explosion(self) -> int:
        '''Specifies the amount the data point shall be moved from the center of the pie.
        Can be negative, negative means that property is not set and no explosion should be applied.
        Applies only to Pie charts.'''
        ...
    
    @explosion.setter
    def explosion(self, value: int):
        ...
    
    @property
    def invert_if_negative(self) -> bool:
        '''Specifies whether the parent element shall inverts its colors if the value is negative.'''
        ...
    
    @invert_if_negative.setter
    def invert_if_negative(self, value: bool):
        ...
    
    @property
    def bubble_3d(self) -> bool:
        '''Specifies whether the bubbles in Bubble chart should have a 3-D effect applied to them.'''
        ...
    
    @bubble_3d.setter
    def bubble_3d(self, value: bool):
        ...
    
    @property
    def format(self) -> aspose.words.drawing.charts.ChartFormat:
        '''Provides access to fill and line formatting of this data point.'''
        ...
    
    @property
    def marker(self) -> aspose.words.drawing.charts.ChartMarker:
        '''Specifies chart data marker.'''
        ...
    
    ...

class ChartDataPointCollection:
    '''Represents collection of a :class:`ChartDataPoint`.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.drawing.charts.ChartDataPoint:
        '''Returns :class:`ChartDataPoint` for the specified index.'''
        ...
    
    def clear_format(self) -> None:
        '''Clears format of all :class:`ChartDataPoint` in this collection.'''
        ...
    
    @property
    def count(self) -> int:
        '''Returns the number of :class:`ChartDataPoint` in this collection.'''
        ...
    
    ...

class ChartFormat:
    '''Represents the formatting of a chart element.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    @property
    def fill(self) -> aspose.words.drawing.Fill:
        '''Gets fill formatting for the parent chart element.'''
        ...
    
    @property
    def stroke(self) -> aspose.words.drawing.Stroke:
        '''Gets line formatting for the parent chart element.'''
        ...
    
    @property
    def shape_type(self) -> aspose.words.drawing.charts.ChartShapeType:
        '''Gets or sets the shape type of the parent chart element.
        
        Currently, the property can only be used for data labels.'''
        ...
    
    @shape_type.setter
    def shape_type(self, value: aspose.words.drawing.charts.ChartShapeType):
        ...
    
    ...

class ChartLegend:
    '''Represents chart legend properties.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    @property
    def legend_entries(self) -> aspose.words.drawing.charts.ChartLegendEntryCollection:
        '''Returns a collection of legend entries for all series and trendlines of the parent chart.'''
        ...
    
    @property
    def position(self) -> aspose.words.drawing.charts.LegendPosition:
        '''Specifies the position of the legend on a chart.
        Default value is :attr:`LegendPosition.RIGHT`.'''
        ...
    
    @position.setter
    def position(self, value: aspose.words.drawing.charts.LegendPosition):
        ...
    
    @property
    def overlay(self) -> bool:
        '''Determines whether other chart elements shall be allowed to overlap legend.
        Default value is ``False``.'''
        ...
    
    @overlay.setter
    def overlay(self, value: bool):
        ...
    
    ...

class ChartLegendEntry:
    '''Represents a chart legend entry.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.
    
    A legend entry corresponds to a specific chart series or trendline.
    
    The text of the entry is the name of the series or trendline. The text cannot be changed.'''
    
    @property
    def is_hidden(self) -> bool:
        '''Gets or sets a value indicating whether this entry is hidden in the chart legend.
        The default value is **false**.
        
        When a chart legend entry is hidden, it does not affect the corresponding chart series or trendline that
        is still displayed on the chart.'''
        ...
    
    @is_hidden.setter
    def is_hidden(self, value: bool):
        ...
    
    @property
    def font(self) -> aspose.words.Font:
        '''Provides access to the font formatting of this legend entry.'''
        ...
    
    ...

class ChartLegendEntryCollection:
    '''Represents a collection of chart legend entries.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.drawing.charts.ChartLegendEntry:
        '''Returns :class:`ChartLegendEntry` for the specified index.'''
        ...
    
    @property
    def count(self) -> int:
        '''Returns the number of :class:`ChartLegendEntry` in this collection.'''
        ...
    
    ...

class ChartMarker:
    '''Represents a chart data marker.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    @property
    def symbol(self) -> aspose.words.drawing.charts.MarkerSymbol:
        '''Gets or sets chart marker symbol.'''
        ...
    
    @symbol.setter
    def symbol(self, value: aspose.words.drawing.charts.MarkerSymbol):
        ...
    
    @property
    def size(self) -> int:
        '''Gets or sets chart marker size.
        Default value is 7.'''
        ...
    
    @size.setter
    def size(self, value: int):
        ...
    
    @property
    def format(self) -> aspose.words.drawing.charts.ChartFormat:
        '''Provides access to fill and line formatting of this marker.'''
        ...
    
    ...

class ChartMultilevelValue:
    '''Represents a value for charts that display multilevel data.'''
    
    @overload
    def __init__(self, level1: str, level2: str, level3: str):
        '''Initializes a new instance of this class that represents a three-level value.'''
        ...
    
    @overload
    def __init__(self, level1: str, level2: str):
        '''Initializes a new instance of this class that represents a two-level value.'''
        ...
    
    @overload
    def __init__(self, level1: str):
        '''Initializes a new instance of this class that represents a single-level value.'''
        ...
    
    @property
    def level1(self) -> str:
        '''Gets the name of the chart top level that this value refers to.'''
        ...
    
    @property
    def level2(self) -> str:
        '''Gets the name of the chart intermediate level that this value refers to.'''
        ...
    
    @property
    def level3(self) -> str:
        '''Gets the name of the chart bottom level that this value refers to.'''
        ...
    
    ...

class ChartNumberFormat:
    '''Represents number formatting of the parent element.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    @property
    def format_code(self) -> str:
        '''Gets or sets the format code applied to a data label.
        
        Number formatting is used to change the way a value appears in data label and can be used in some very creative ways.
        The examples of number formats:
        Number - "#,##0.00"
        
        Currency - "\\"$\\"#,##0.00"
        
        Time - "[$-x-systime]h:mm:ss AM/PM"
        
        Date - "d/mm/yyyy"
        
        Percentage - "0.00%"
        
        Fraction - "# ?/?"
        
        Scientific - "0.00E+00"
        
        Text - "@"
        
        Accounting - "_-\\"$\\"\* #,##0.00_-;-\\"$\\"\* #,##0.00_-;_-\\"$\\"\* \\"-\\"??_-;_-@_-"
        
        Custom with color - "[Red]-#,##0.0"'''
        ...
    
    @format_code.setter
    def format_code(self, value: str):
        ...
    
    @property
    def is_linked_to_source(self) -> bool:
        '''Specifies whether the format code is linked to a source cell.
        Default is true.
        
        The NumberFormat will be reset to general if format code is linked to source.'''
        ...
    
    @is_linked_to_source.setter
    def is_linked_to_source(self, value: bool):
        ...
    
    ...

class ChartSeries:
    '''Represents chart series properties.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    @overload
    def add(self, x_value: aspose.words.drawing.charts.ChartXValue) -> None:
        '''Adds the specified X value to the chart series. If the series supports Y values and bubble sizes, they will
        be empty for the X value.'''
        ...
    
    @overload
    def add(self, x_value: aspose.words.drawing.charts.ChartXValue, y_value: aspose.words.drawing.charts.ChartYValue) -> None:
        '''Adds the specified X and Y values to the chart series.'''
        ...
    
    @overload
    def add(self, x_value: aspose.words.drawing.charts.ChartXValue, y_value: aspose.words.drawing.charts.ChartYValue, bubble_size: float) -> None:
        '''Adds the specified X value, Y value and bubble size to the chart series.'''
        ...
    
    @overload
    def insert(self, index: int, x_value: aspose.words.drawing.charts.ChartXValue) -> None:
        '''Inserts the specified X value into the chart series at the specified index. If the series supports Y values
        and bubble sizes, they will be empty for the X value.
        
        The corresponding data point with default formatting will be inserted into the data point collection. And,
        if data labels are displayed, the corresponding data label with default formatting will be inserted too.'''
        ...
    
    @overload
    def insert(self, index: int, x_value: aspose.words.drawing.charts.ChartXValue, y_value: aspose.words.drawing.charts.ChartYValue) -> None:
        '''Inserts the specified X and Y values into the chart series at the specified index.
        
        The corresponding data point with default formatting will be inserted into the data point collection. And,
        if data labels are displayed, the corresponding data label with default formatting will be inserted too.'''
        ...
    
    @overload
    def insert(self, index: int, x_value: aspose.words.drawing.charts.ChartXValue, y_value: aspose.words.drawing.charts.ChartYValue, bubble_size: float) -> None:
        '''Inserts the specified X value, Y value and bubble size into the chart series at the specified index.
        
        The corresponding data point with default formatting will be inserted into the data point collection. And,
        if data labels are displayed, the corresponding data label with default formatting will be inserted too.'''
        ...
    
    def remove(self, index: int) -> None:
        '''Removes the X value, Y value, and bubble size, if supported, from the chart series at the specified index.
        The corresponding data point and data label are also removed.'''
        ...
    
    def clear(self) -> None:
        '''Removes all data values from the chart series. Format of all individual data points and data labels is cleared.'''
        ...
    
    def clear_values(self) -> None:
        '''Removes all data values from the chart series with preserving the format of the data points and data labels.'''
        ...
    
    @property
    def explosion(self) -> int:
        '''Specifies the amount the data point shall be moved from the center of the pie.
        Can be negative, negative means that property is not set and no explosion should be applied.
        Applies only to Pie charts.'''
        ...
    
    @explosion.setter
    def explosion(self, value: int):
        ...
    
    @property
    def invert_if_negative(self) -> bool:
        '''Specifies whether the parent element shall inverts its colors if the value is negative.'''
        ...
    
    @invert_if_negative.setter
    def invert_if_negative(self, value: bool):
        ...
    
    @property
    def marker(self) -> aspose.words.drawing.charts.ChartMarker:
        '''Specifies a data marker. Marker is automatically created when requested.'''
        ...
    
    @property
    def bubble_3d(self) -> bool:
        '''Specifies whether the bubbles in Bubble chart should have a 3-D effect applied to them.'''
        ...
    
    @bubble_3d.setter
    def bubble_3d(self, value: bool):
        ...
    
    @property
    def data_points(self) -> aspose.words.drawing.charts.ChartDataPointCollection:
        '''Returns a collection of formatting objects for all data points in this series.'''
        ...
    
    @property
    def name(self) -> str:
        '''Gets or sets the name of the series, if name is not set explicitly it is generated using index.
        By default returns Series plus one based index.'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def smooth(self) -> bool:
        '''Allows to specify whether the line connecting the points on the chart shall be smoothed using Catmull-Rom splines.'''
        ...
    
    @smooth.setter
    def smooth(self, value: bool):
        ...
    
    @property
    def has_data_labels(self) -> bool:
        '''Gets or sets a flag indicating whether data labels are displayed for the series.'''
        ...
    
    @has_data_labels.setter
    def has_data_labels(self, value: bool):
        ...
    
    @property
    def data_labels(self) -> aspose.words.drawing.charts.ChartDataLabelCollection:
        '''Specifies the settings for the data labels for the entire series.'''
        ...
    
    @property
    def format(self) -> aspose.words.drawing.charts.ChartFormat:
        '''Provides access to fill and line formatting of the series.'''
        ...
    
    @property
    def legend_entry(self) -> aspose.words.drawing.charts.ChartLegendEntry:
        '''Gets a legend entry for this chart series.'''
        ...
    
    @property
    def series_type(self) -> aspose.words.drawing.charts.ChartSeriesType:
        '''Gets the type of this chart series.'''
        ...
    
    @property
    def x_values(self) -> aspose.words.drawing.charts.ChartXValueCollection:
        '''Gets a collection of X values for this chart series.'''
        ...
    
    @property
    def y_values(self) -> aspose.words.drawing.charts.ChartYValueCollection:
        '''Gets a collection of Y values for this chart series.'''
        ...
    
    @property
    def bubble_sizes(self) -> aspose.words.drawing.charts.BubbleSizeCollection:
        '''Gets a collection of bubble sizes for this chart series.'''
        ...
    
    ...

class ChartSeriesCollection:
    '''Represents collection of a :class:`ChartSeries`.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.drawing.charts.ChartSeries:
        '''Returns a :class:`ChartSeries` at the specified index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the collection.'''
        ...
    
    @overload
    def add(self, series_name: str, categories: list[str], values: list[float]) -> aspose.words.drawing.charts.ChartSeries:
        '''Adds new :class:`ChartSeries` to this collection.
        Use this method to add series to any type of Bar, Column, Line and Surface charts.
        
        :returns: Recently added :class:`ChartSeries` object.'''
        ...
    
    @overload
    def add(self, series_name: str, x_values: list[float], y_values: list[float]) -> aspose.words.drawing.charts.ChartSeries:
        '''Adds new :class:`ChartSeries` to this collection.
        Use this method to add series to any type of Scatter charts.
        
        :returns: Recently added :class:`ChartSeries` object.'''
        ...
    
    @overload
    def add(self, series_name: str, dates: list[datetime.datetime], values: list[float]) -> aspose.words.drawing.charts.ChartSeries:
        '''Adds new :class:`ChartSeries` to this collection.
        Use this method to add series to any type of Area, Radar and Stock charts.'''
        ...
    
    @overload
    def add(self, series_name: str, x_values: list[float], y_values: list[float], bubble_sizes: list[float]) -> aspose.words.drawing.charts.ChartSeries:
        '''Adds new :class:`ChartSeries` to this collection.
        Use this method to add series to any type of Bubble charts.
        
        :returns: Recently added :class:`ChartSeries` object.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes a :class:`ChartSeries` at the specified index.
        
        :param index: The zero-based index of the :class:`ChartSeries` to remove.'''
        ...
    
    def clear(self) -> None:
        '''Removes all :class:`ChartSeries` from this collection.'''
        ...
    
    def add_double(self, series_name: str, x_values: list[float], y_values: list[float]) -> aspose.words.drawing.charts.ChartSeries:
        ...
    
    def add_date(self, series_name: str, dates: list[datetime.datetime], values: list[float]) -> aspose.words.drawing.charts.ChartSeries:
        ...
    
    @property
    def count(self) -> int:
        '''Returns the number of :class:`ChartSeries` in this collection.'''
        ...
    
    ...

class ChartTitle:
    '''Provides access to the chart title properties.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    @property
    def text(self) -> str:
        '''Gets or sets the text of the chart title.
        If ``None`` or empty value is specified, auto generated title will be shown.
        
        Use :attr:`ChartTitle.show` option if you need to hide the Title.'''
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    @property
    def overlay(self) -> bool:
        '''Determines whether other chart elements shall be allowed to overlap title.
        By default overlay is ``False``.'''
        ...
    
    @overlay.setter
    def overlay(self, value: bool):
        ...
    
    @property
    def show(self) -> bool:
        '''Determines whether the title shall be shown for this chart.
        Default value is ``True``.'''
        ...
    
    @show.setter
    def show(self, value: bool):
        ...
    
    ...

class ChartXValue:
    '''Represents an X value for a chart series.
    
    This class contains a number of static methods for creating an X value of a particular type. The
    :attr:`ChartXValue.value_type` property allows you to determine the type of an existing X value.
    
    All non-null X values of a chart series must be of the same :class:`ChartXValueType` type.'''
    
    @staticmethod
    def from_string(self, value: str) -> aspose.words.drawing.charts.ChartXValue:
        '''Creates a :class:`ChartXValue` instance of the :attr:`ChartXValueType.STRING` type.'''
        ...
    
    @staticmethod
    def from_double(self, value: float) -> aspose.words.drawing.charts.ChartXValue:
        '''Creates a :class:`ChartXValue` instance of the :attr:`ChartXValueType.DOUBLE` type.'''
        ...
    
    @staticmethod
    def from_date_time(self, value: datetime.datetime) -> aspose.words.drawing.charts.ChartXValue:
        '''Creates a :class:`ChartXValue` instance of the :attr:`ChartXValueType.DATE_TIME` type.'''
        ...
    
    @staticmethod
    def from_time_span(self, value: datetime.timespan) -> aspose.words.drawing.charts.ChartXValue:
        '''Creates a :class:`ChartXValue` instance of the :attr:`ChartXValueType.TIME` type.'''
        ...
    
    @staticmethod
    def from_multilevel_value(self, value: aspose.words.drawing.charts.ChartMultilevelValue) -> aspose.words.drawing.charts.ChartXValue:
        '''Creates a :class:`ChartXValue` instance of the :attr:`ChartXValueType.MULTILEVEL` type.'''
        ...
    
    @property
    def value_type(self) -> aspose.words.drawing.charts.ChartXValueType:
        '''Gets the type of the X value stored in the object.'''
        ...
    
    @property
    def string_value(self) -> str:
        '''Gets the stored string value.'''
        ...
    
    @property
    def double_value(self) -> float:
        '''Gets the stored numeric value.'''
        ...
    
    @property
    def date_time_value(self) -> datetime.datetime:
        '''Gets the stored datetime value.'''
        ...
    
    @property
    def time_value(self) -> datetime.timespan:
        '''Gets the stored time value.'''
        ...
    
    @property
    def multilevel_value(self) -> aspose.words.drawing.charts.ChartMultilevelValue:
        '''Gets the stored multilevel value.'''
        ...
    
    ...

class ChartXValueCollection:
    '''Represents a collection of X values for a chart series.
    
    All items of the collection other than **null** must have the same :attr:`ChartXValue.value_type`.
    
    The collection allows only changing X values. To add or insert new values to a chart series, or remove values,
    the appropriate methods of the :class:`ChartSeries` class can be used.'''
    
    def __getitem__(self, index: int) -> aspose.words.drawing.charts.ChartXValue:
        '''Gets or sets the X value at the specified index.
        
        Empty values are represented as **null**.'''
        ...
    
    def __setitem__(self, index: int, value: aspose.words.drawing.charts.ChartXValue):
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of items in this collection.'''
        ...
    
    ...

class ChartYValue:
    '''Represents an Y value for a chart series.
    
    This class contains a number of static methods for creating an Y value of a particular type. The
    :attr:`ChartYValue.value_type` property allows you to determine the type of an existing Y value.
    
    All non-null Y values of a chart series must be of the same :class:`ChartYValueType` type.'''
    
    @staticmethod
    def from_double(self, value: float) -> aspose.words.drawing.charts.ChartYValue:
        '''Creates a :class:`ChartYValue` instance of the :attr:`ChartYValueType.DOUBLE` type.'''
        ...
    
    @staticmethod
    def from_date_time(self, value: datetime.datetime) -> aspose.words.drawing.charts.ChartYValue:
        '''Creates a :class:`ChartYValue` instance of the :attr:`ChartYValueType.DATE_TIME` type.'''
        ...
    
    @staticmethod
    def from_time_span(self, value: datetime.timespan) -> aspose.words.drawing.charts.ChartYValue:
        '''Creates a :class:`ChartYValue` instance of the :attr:`ChartYValueType.TIME` type.'''
        ...
    
    @property
    def value_type(self) -> aspose.words.drawing.charts.ChartYValueType:
        '''Gets the type of the Y value stored in the object.'''
        ...
    
    @property
    def double_value(self) -> float:
        '''Gets the stored numeric value.'''
        ...
    
    @property
    def date_time_value(self) -> datetime.datetime:
        '''Gets the stored datetime value.'''
        ...
    
    @property
    def time_value(self) -> datetime.timespan:
        '''Gets the stored time value.'''
        ...
    
    ...

class ChartYValueCollection:
    '''Represents a collection of Y values for a chart series.
    
    All items of the collection other than **null** must have the same :attr:`ChartYValue.value_type`.
    
    The collection allows only changing Y values. To add or insert new values to a chart series, or remove values,
    the appropriate methods of the :class:`ChartSeries` class can be used.'''
    
    def __getitem__(self, index: int) -> aspose.words.drawing.charts.ChartYValue:
        '''Gets or sets the Y value at the specified index.
        
        Empty values are represented as **null**.'''
        ...
    
    def __setitem__(self, index: int, value: aspose.words.drawing.charts.ChartYValue):
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of items in this collection.'''
        ...
    
    ...

class IChartDataPoint:
    '''Contains properties of a single data point on the chart.'''
    
    @property
    def explosion(self) -> int:
        '''Specifies the amount the data point shall be moved from the center of the pie.
        Can be negative, negative means that property is not set and no explosion should be applied.
        Applies only to Pie charts.'''
        ...
    
    @explosion.setter
    def explosion(self, value: int):
        ...
    
    @property
    def invert_if_negative(self) -> bool:
        '''Specifies whether the parent element shall inverts its colors if the value is negative.'''
        ...
    
    @invert_if_negative.setter
    def invert_if_negative(self, value: bool):
        ...
    
    @property
    def marker(self) -> aspose.words.drawing.charts.ChartMarker:
        '''Specifies a data marker. Marker is automatically created when requested.'''
        ...
    
    @property
    def bubble_3d(self) -> bool:
        '''Specifies whether the bubbles in Bubble chart should have a 3-D effect applied to them.'''
        ...
    
    @bubble_3d.setter
    def bubble_3d(self, value: bool):
        ...
    
    ...

class AxisBuiltInUnit:
    '''Specifies the display units for an axis.'''
    
    NONE: int
    CUSTOM: int
    BILLIONS: int
    HUNDRED_MILLIONS: int
    HUNDREDS: int
    HUNDRED_THOUSANDS: int
    MILLIONS: int
    TEN_MILLIONS: int
    TEN_THOUSANDS: int
    THOUSANDS: int
    TRILLIONS: int
    PERCENTAGE: int

class AxisCategoryType:
    '''Specifies type of a category axis.'''
    
    AUTOMATIC: int
    CATEGORY: int
    TIME: int

class AxisCrosses:
    '''Specifies the possible crossing points for an axis.'''
    
    AUTOMATIC: int
    MAXIMUM: int
    MINIMUM: int
    CUSTOM: int

class AxisScaleType:
    '''Specifies the possible scale types for an axis.'''
    
    LINEAR: int
    LOGARITHMIC: int

class AxisTickLabelPosition:
    '''Specifies the possible positions for tick labels.'''
    
    HIGH: int
    LOW: int
    NEXT_TO_AXIS: int
    NONE: int
    DEFAULT: int

class AxisTickMark:
    '''Specifies the possible positions for tick marks.'''
    
    CROSS: int
    INSIDE: int
    OUTSIDE: int
    NONE: int

class AxisTimeUnit:
    '''Specifies the unit of time for axes.'''
    
    AUTOMATIC: int
    DAYS: int
    MONTHS: int
    YEARS: int

class ChartAxisType:
    '''Specifies type of chart axis.'''
    
    CATEGORY: int
    SERIES: int
    VALUE: int

class ChartSeriesType:
    '''Specifies a type of a chart series.'''
    
    AREA: int
    AREA_STACKED: int
    AREA_PERCENT_STACKED: int
    AREA_3D: int
    AREA_3D_STACKED: int
    AREA_3D_PERCENT_STACKED: int
    BAR: int
    BAR_STACKED: int
    BAR_PERCENT_STACKED: int
    BAR_3D: int
    BAR_3D_STACKED: int
    BAR_3D_PERCENT_STACKED: int
    BUBBLE: int
    BUBBLE_3D: int
    COLUMN: int
    COLUMN_STACKED: int
    COLUMN_PERCENT_STACKED: int
    COLUMN_3D: int
    COLUMN_3D_STACKED: int
    COLUMN_3D_PERCENT_STACKED: int
    COLUMN_3D_CLUSTERED: int
    DOUGHNUT: int
    LINE: int
    LINE_STACKED: int
    LINE_PERCENT_STACKED: int
    LINE_3D: int
    PIE: int
    PIE_3D: int
    PIE_OF_BAR: int
    PIE_OF_PIE: int
    RADAR: int
    SCATTER: int
    STOCK: int
    SURFACE: int
    SURFACE_3D: int
    TREEMAP: int
    SUNBURST: int
    HISTOGRAM: int
    PARETO: int
    PARETO_LINE: int
    BOX_AND_WHISKER: int
    WATERFALL: int
    FUNNEL: int
    REGION_MAP: int

class ChartShapeType:
    '''Specifies the shape type of chart elements.'''
    
    DEFAULT: int
    RECTANGLE: int
    ROUND_RECTANGLE: int
    ELLIPSE: int
    DIAMOND: int
    TRIANGLE: int
    RIGHT_TRIANGLE: int
    PARALLELOGRAM: int
    TRAPEZOID: int
    HEXAGON: int
    OCTAGON: int
    PLUS: int
    STAR: int
    ARROW: int
    HOME_PLATE: int
    CUBE: int
    ARC: int
    LINE: int
    PLAQUE: int
    CAN: int
    DONUT: int
    STRAIGHT_CONNECTOR1: int
    BENT_CONNECTOR2: int
    BENT_CONNECTOR3: int
    BENT_CONNECTOR4: int
    BENT_CONNECTOR5: int
    CURVED_CONNECTOR2: int
    CURVED_CONNECTOR3: int
    CURVED_CONNECTOR4: int
    CURVED_CONNECTOR5: int
    CALLOUT1: int
    CALLOUT2: int
    CALLOUT3: int
    ACCENT_CALLOUT1: int
    ACCENT_CALLOUT2: int
    ACCENT_CALLOUT3: int
    BORDER_CALLOUT1: int
    BORDER_CALLOUT2: int
    BORDER_CALLOUT3: int
    ACCENT_BORDER_CALLOUT1: int
    ACCENT_BORDER_CALLOUT2: int
    ACCENT_BORDER_CALLOUT3: int
    RIBBON: int
    RIBBON2: int
    CHEVRON: int
    PENTAGON: int
    NO_SMOKING: int
    SEAL4: int
    SEAL6: int
    SEAL7: int
    SEAL8: int
    SEAL10: int
    SEAL12: int
    SEAL16: int
    SEAL24: int
    SEAL32: int
    WEDGE_RECT_CALLOUT: int
    WEDGE_R_RECT_CALLOUT: int
    WEDGE_ELLIPSE_CALLOUT: int
    WAVE: int
    FOLDED_CORNER: int
    LEFT_ARROW: int
    DOWN_ARROW: int
    UP_ARROW: int
    LEFT_RIGHT_ARROW: int
    UP_DOWN_ARROW: int
    IRREGULAR_SEAL1: int
    IRREGULAR_SEAL2: int
    LIGHTNING_BOLT: int
    HEART: int
    QUAD_ARROW: int
    LEFT_ARROW_CALLOUT: int
    RIGHT_ARROW_CALLOUT: int
    UP_ARROW_CALLOUT: int
    DOWN_ARROW_CALLOUT: int
    LEFT_RIGHT_ARROW_CALLOUT: int
    UP_DOWN_ARROW_CALLOUT: int
    QUAD_ARROW_CALLOUT: int
    BEVEL: int
    LEFT_BRACKET: int
    RIGHT_BRACKET: int
    LEFT_BRACE: int
    RIGHT_BRACE: int
    LEFT_UP_ARROW: int
    BENT_UP_ARROW: int
    BENT_ARROW: int
    STRIPED_RIGHT_ARROW: int
    NOTCHED_RIGHT_ARROW: int
    BLOCK_ARC: int
    SMILEY_FACE: int
    VERTICAL_SCROLL: int
    HORIZONTAL_SCROLL: int
    CIRCULAR_ARROW: int
    UTURN_ARROW: int
    CURVED_RIGHT_ARROW: int
    CURVED_LEFT_ARROW: int
    CURVED_UP_ARROW: int
    CURVED_DOWN_ARROW: int
    CLOUD_CALLOUT: int
    ELLIPSE_RIBBON: int
    ELLIPSE_RIBBON2: int
    FLOW_CHART_PROCESS: int
    FLOW_CHART_DECISION: int
    FLOW_CHART_INPUT_OUTPUT: int
    FLOW_CHART_PREDEFINED_PROCESS: int
    FLOW_CHART_INTERNAL_STORAGE: int
    FLOW_CHART_DOCUMENT: int
    FLOW_CHART_MULTIDOCUMENT: int
    FLOW_CHART_TERMINATOR: int
    FLOW_CHART_PREPARATION: int
    FLOW_CHART_MANUAL_INPUT: int
    FLOW_CHART_MANUAL_OPERATION: int
    FLOW_CHART_CONNECTOR: int
    FLOW_CHART_PUNCHED_CARD: int
    FLOW_CHART_PUNCHED_TAPE: int
    FLOW_CHART_SUMMING_JUNCTION: int
    FLOW_CHART_OR: int
    FLOW_CHART_COLLATE: int
    FLOW_CHART_SORT: int
    FLOW_CHART_EXTRACT: int
    FLOW_CHART_MERGE: int
    FLOW_CHART_OFFLINE_STORAGE: int
    FLOW_CHART_ONLINE_STORAGE: int
    FLOW_CHART_MAGNETIC_TAPE: int
    FLOW_CHART_MAGNETIC_DISK: int
    FLOW_CHART_MAGNETIC_DRUM: int
    FLOW_CHART_DISPLAY: int
    FLOW_CHART_DELAY: int
    FLOW_CHART_ALTERNATE_PROCESS: int
    FLOW_CHART_OFFPAGE_CONNECTOR: int
    LEFT_RIGHT_UP_ARROW: int
    SUN: int
    MOON: int
    BRACKET_PAIR: int
    BRACE_PAIR: int
    DOUBLE_WAVE: int
    ACTION_BUTTON_BLANK: int
    ACTION_BUTTON_HOME: int
    ACTION_BUTTON_HELP: int
    ACTION_BUTTON_INFORMATION: int
    ACTION_BUTTON_FORWARD_NEXT: int
    ACTION_BUTTON_BACK_PREVIOUS: int
    ACTION_BUTTON_END: int
    ACTION_BUTTON_BEGINNING: int
    ACTION_BUTTON_RETURN: int
    ACTION_BUTTON_DOCUMENT: int
    ACTION_BUTTON_SOUND: int
    ACTION_BUTTON_MOVIE: int
    SINGLE_CORNER_SNIPPED: int
    TOP_CORNERS_SNIPPED: int
    DIAGONAL_CORNERS_SNIPPED: int
    TOP_CORNERS_ONE_ROUNDED_ONE_SNIPPED: int
    SINGLE_CORNER_ROUNDED: int
    TOP_CORNERS_ROUNDED: int
    DIAGONAL_CORNERS_ROUNDED: int
    HEPTAGON: int
    CLOUD: int
    SWOOSH_ARROW: int
    TEARDROP: int
    SQUARE_TABS: int
    PLAQUE_TABS: int
    PIE: int
    WEDGE_PIE: int
    INVERSE_LINE: int
    MATH_PLUS: int
    MATH_MINUS: int
    MATH_MULTIPLY: int
    MATH_DIVIDE: int
    MATH_EQUAL: int
    MATH_NOT_EQUAL: int
    NON_ISOSCELES_TRAPEZOID: int
    LEFT_RIGHT_CIRCULAR_ARROW: int
    LEFT_RIGHT_RIBBON: int
    LEFT_CIRCULAR_ARROW: int
    FRAME: int
    HALF_FRAME: int
    FUNNEL: int
    GEAR6: int
    GEAR9: int
    DECAGON: int
    DODECAGON: int
    DIAGONAL_STRIPE: int
    CORNER: int
    CORNER_TABS: int
    CHORD: int
    CHART_PLUS: int
    CHART_STAR: int
    CHART_X: int

class ChartType:
    '''Specifies type of a chart.'''
    
    AREA: int
    AREA_STACKED: int
    AREA_PERCENT_STACKED: int
    AREA_3D: int
    AREA_3D_STACKED: int
    AREA_3D_PERCENT_STACKED: int
    BAR: int
    BAR_STACKED: int
    BAR_PERCENT_STACKED: int
    BAR_3D: int
    BAR_3D_STACKED: int
    BAR_3D_PERCENT_STACKED: int
    BUBBLE: int
    BUBBLE_3D: int
    COLUMN: int
    COLUMN_STACKED: int
    COLUMN_PERCENT_STACKED: int
    COLUMN_3D: int
    COLUMN_3D_STACKED: int
    COLUMN_3D_PERCENT_STACKED: int
    COLUMN_3D_CLUSTERED: int
    DOUGHNUT: int
    LINE: int
    LINE_STACKED: int
    LINE_PERCENT_STACKED: int
    LINE_3D: int
    PIE: int
    PIE_3D: int
    PIE_OF_BAR: int
    PIE_OF_PIE: int
    RADAR: int
    SCATTER: int
    STOCK: int
    SURFACE: int
    SURFACE_3D: int

class ChartXValueType:
    '''Allows to specify type of an X value of a chart series.'''
    
    STRING: int
    DOUBLE: int
    DATE_TIME: int
    TIME: int
    MULTILEVEL: int

class ChartYValueType:
    '''Allows to specify type of an Y value of a chart series.'''
    
    DOUBLE: int
    DATE_TIME: int
    TIME: int

class LegendPosition:
    '''Specifies the possible positions for a chart legend.'''
    
    NONE: int
    BOTTOM: int
    LEFT: int
    RIGHT: int
    TOP: int
    TOP_RIGHT: int

class MarkerSymbol:
    '''Specifies marker symbol style.'''
    
    DEFAULT: int
    CIRCLE: int
    DASH: int
    DIAMOND: int
    DOT: int
    NONE: int
    PICTURE: int
    PLUS: int
    SQUARE: int
    STAR: int
    TRIANGLE: int
    X: int

