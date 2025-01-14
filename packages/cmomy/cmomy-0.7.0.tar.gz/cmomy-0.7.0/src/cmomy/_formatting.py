# mypy: disable-error-code="no-untyped-def, no-untyped-call"
"""pretty formatting for notebook."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from xarray.core import formatting as ff
    from xarray.core import formatting_html as fm
else:
    import lazy_loader as lazy

    ff = lazy.load("xarray.core.formatting")
    fm = lazy.load("xarray.core.formatting_html")


def short_numpy_repr(*args, **kwargs):
    if hasattr(ff, "short_array_repr"):
        f = ff.short_array_repr
    elif hasattr(ff, "short_numpy_repr"):
        f = ff.short_numpy_repr
    else:
        f = repr
    return f(*args, **kwargs)


def tuple_to_str(x):
    """Convert tuple to a string."""
    if len(x) == 0:
        return "*empty*"

    out = ", ".join(map(str, x))

    if len(x) > 1:
        out = f"({out})"

    return out


def numpy_section(x):
    """Create numpy array section."""
    # "unique" id to expand/collapse the section
    # fmt: off
    data_id = "section-" + str(fm.uuid.uuid4())  # type: ignore
    collapsed = (
        "checked"
        if fm._get_boolean_with_default("display_expand_data", default=True)  # type: ignore
        else ""
    )

    preview = fm.escape(ff.format_array_flat(x, max_width=70))  # type: ignore

    # short data repr
    text = fm.escape(short_numpy_repr(x))  # type: ignore
    # fmt: on

    data_repr = f"<pre>{text}</pre>"
    data_icon = fm._icon("icon-database")

    return (
        "<div class='xr-array-wrap'>"
        f"<input id='{data_id}' class='xr-array-in' type='checkbox' {collapsed}>"
        f"<label for='{data_id}' title='Show/hide data repr'>{data_icon}</label>"
        f"<div class='xr-array-preview xr-preview'><span>{preview}</span></div>"
        f"<div class='xr-array-data'>{data_repr}</div>"
        "</div>"
    )


def repr_html(x):
    """Create html output."""
    # build the cmomy header
    obj_type = type(x).__name__

    keys = [k for k in ["mom", "mom_dims", "val_shape", "val_dims"] if hasattr(x, k)]

    attrs = {}
    for k in keys:
        v = getattr(x, k)
        if len(v) > 0:
            attrs[k] = tuple_to_str(v)

    dims = {}
    for k in ["mom", "val_shape"]:
        if k in attrs:
            dims[k] = attrs.pop(k)

    # dims = {k: attrs[k] for k in ["mom", "val_shape"] if k in attrs}

    header_components = [
        f"<div class='xr-obj-type'>{obj_type}</div>",
        fm.format_dims(dims, {}),
    ]

    sections = [
        fm._mapping_section(
            mapping=attrs,
            name="Info",
            details_func=fm.summarize_attrs,
            max_items_collapse=5,
            expand_option_name="display_expand_attrs",
        )
    ]

    if hasattr(x.values, "_repr_html_"):
        sections += []

        out = fm._obj_repr(
            x.values,
            header_components,
            sections,
        )

        out = out + x.values._repr_html_()

    else:
        sections += [numpy_section(x.data)]
        header_components += [
            f"<div class='xr-obj-type'>{type(x.values)}</div>",
        ]
        out = fm._obj_repr(x.values, header_components, sections)

    return out
