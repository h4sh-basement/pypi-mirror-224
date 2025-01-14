# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FilterField(Component):
    """A FilterField component.
Common wrapper for filters/inputs and their labels

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional)

- active (boolean; optional)

- className (string; optional)

- dois (list of strings; optional)

- label (string; optional)

- tooltip (string; optional)

- units (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mp_components'
    _type = 'FilterField'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, units=Component.UNDEFINED, dois=Component.UNDEFINED, active=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'active', 'className', 'dois', 'label', 'tooltip', 'units']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'active', 'className', 'dois', 'label', 'tooltip', 'units']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FilterField, self).__init__(children=children, **args)
