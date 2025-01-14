from typing import List, Set, Union

from lnschema_core import File, Registry, Run, Transform
from lnschema_core.models import format_field_value

LAMIN_GREEN_LIGHTER = "#10b981"
LAMIN_GREEN_DARKER = "#065f46"
GREEN_FILL = "honeydew"
TRANSFORM_EMOJIS = {"notebook": "📔", "app": "🖥️", "pipeline": "🧩"}


def view_lineage(file: File, with_children: bool = True):
    """Graph of data lineage.

    Notes:
        For more info, see tutorial: :doc:`/guide/data-lineage`.

    Examples:
        >>> file.view_lineage()
    """
    try:
        import graphviz
    except ImportError:
        raise ImportError(
            "Drawing diagrams requires 'graphviz' to be installed. This requires the"
            " Python package 'graphviz' and the associated binary. We recommend to"
            " install 'graphviz' using your operating systems' package manager or from"
            " conda."
        )

    all_runs = _get_all_parent_runs(file)
    if with_children:
        all_runs.update(_get_all_child_runs(file))
    df_edges = _df_edges_from_runs(all_runs)

    file_label = _label_file_run(file)

    u = graphviz.Digraph(
        file.id,
        node_attr={
            "fillcolor": GREEN_FILL,
            "color": LAMIN_GREEN_DARKER,
            "fontname": "Helvetica",
            "fontsize": "10",
        },
        edge_attr={"arrowsize": "0.5"},
    )

    def add_node(
        record: Union[Run, File], node_id: str, node_label: str, u: graphviz.Digraph
    ):
        if isinstance(record, Run):
            style = "rounded,filled"
            shape = "box"
            fillcolor = "gainsboro"
        else:
            style = "rounded,filled"
            shape = "box"
            fillcolor = GREEN_FILL
        u.node(
            node_id,
            label=node_label,
            shape=shape,
            style=style,
            fillcolor=fillcolor,
        )

    for _, row in df_edges.iterrows():
        add_node(row["source_record"], row["source"], row["source_label"], u)
        if row["target_record"] not in df_edges["source_record"]:
            add_node(row["target_record"], row["target"], row["target_label"], u)

        u.edge(row["source"], row["target"], color="dimgrey")
    # label the searched file
    u.node(
        file.id,
        label=file_label,
        style="rounded,filled",
        fillcolor=LAMIN_GREEN_LIGHTER,
        shape="box",
    )

    return u


def view_parents(
    record: Registry, field: str, with_children: bool = False, distance: int = 100
):
    """Graph of parents."""
    if not hasattr(record, "parents"):
        return NotImplementedError(
            f"Parents view is not supported for {record.__class__.__name__}!"
        )
    import graphviz
    import pandas as pd

    df_edges = _df_edges_from_parents(record=record, field=field, distance=distance)
    if with_children:
        df_edges = pd.concat(
            [
                df_edges,
                _df_edges_from_parents(
                    record=record, field=field, distance=distance, children=True
                ),
            ]
        ).drop_duplicates()

    record_label = record.__getattribute__(field)

    u = graphviz.Digraph(
        record.id,
        node_attr={
            "color": LAMIN_GREEN_DARKER,
            "fillcolor": GREEN_FILL,
            "shape": "box",
            "style": "rounded,filled",
            "fontname": "Helvetica",
            "fontsize": "10",
        },
        edge_attr={"arrowsize": "0.5"},
    )
    u.node(
        record_label.replace(":", "_"),
        label=_add_emoji(record, record_label),
        fillcolor=LAMIN_GREEN_LIGHTER,
    )
    for _, row in df_edges.iterrows():
        u.node(row["source"], label=_add_emoji(record, row["source_label"]))
        u.edge(row["source"], row["target"], color="dimgrey")

    return u


def _get_parents(record: Registry, field: str, distance: int, children: bool = False):
    """Recursively get parent records within a distance."""
    if children:
        key = "parents"
    else:
        key = "children"
    model = record.__class__
    condition = f"{key}__{field}"
    results = model.filter(**{condition: record.__getattribute__(field)}).all()
    if distance < 2:
        return results

    d = 2
    while d < distance:
        condition = f"{key}__{condition}"
        records = model.filter(**{condition: record.__getattribute__(field)}).all()

        if len(records) == 0:
            return results

        results = results | records
        d += 1
    return results


def _df_edges_from_parents(
    record: Registry, field: str, distance: int, children: bool = False
):
    """Construct a DataFrame of edges as the input of graphviz.Digraph."""
    key = "children" if children else "parents"
    parents = _get_parents(
        record=record, field=field, distance=distance, children=children
    )
    records = parents | record.__class__.objects.filter(id=record.id)
    df = records.distinct().df(include=[f"{key}__{field}"])
    df_edges = df[[f"{key}__{field}", field]]
    df_edges = df_edges.explode(f"{key}__{field}")
    df_edges.dropna(axis=0, inplace=True)
    df_edges.rename(
        columns={f"{key}__{field}": "source", field: "target"}, inplace=True
    )
    df_edges = df_edges.drop_duplicates()

    # colons messes with the node formatting:
    # https://graphviz.readthedocs.io/en/stable/node_ports.html
    df_edges["source_label"] = df_edges["source"]
    df_edges["target_label"] = df_edges["target"]
    df_edges["source"] = df_edges["source"].str.replace(":", "_")
    df_edges["target"] = df_edges["target"].str.replace(":", "_")
    return df_edges


def _add_emoji(record: Registry, label: str):
    if record.__class__.__name__ == "Transform":
        emoji = TRANSFORM_EMOJIS.get(record.type, "💫")
    elif record.__class__.__name__ == "Run":
        emoji = TRANSFORM_EMOJIS.get(record.transform.type, "💫")
    else:
        emoji = ""
    return f"{emoji} {label}"


def _get_all_parent_runs(file: File):
    """Get all input file runs recursively."""
    all_runs = {file.run}

    runs = [file.run]
    while any([r.input_files.exists() for r in runs if r is not None]):
        inputs = []
        for r in runs:
            inputs += r.input_files.all()
        runs = [f.run for f in inputs]
        all_runs.update(runs)
    return all_runs


def _get_all_child_runs(file: File):
    """Get all output file runs recursively."""
    all_runs: Set[Run] = set()

    runs = {f.run for f in file.run.output_files.all()}
    while runs.difference(all_runs):
        all_runs.update(runs)
        child_runs: Set[Run] = set()
        for r in runs:
            child_runs.update(
                Run.filter(input_files__id__in=r.output_files.list("id")).list()
            )
        runs = child_runs
    return all_runs


def _label_file_run(record: Union[File, Run]):
    if isinstance(record, File):
        if record.description is None:
            name = record.key
        else:
            name = record.description.replace("&", "&amp;")

        return (
            rf'<{name}<BR/><FONT COLOR="GREY" POINT-SIZE="10"'
            rf' FACE="Monospace">id={record.id}<BR/>suffix={record.suffix}</FONT>>'
        )
    elif isinstance(record, Run):
        name = f'{record.transform.name.replace("&", "&amp;")}'
        return (
            rf'<{TRANSFORM_EMOJIS.get(str(record.transform.type), "💫")} {name}<BR/><FONT COLOR="GREY" POINT-SIZE="10"'  # noqa
            rf' FACE="Monospace">id={record.id}<BR/>type={record.transform.type},'
            rf" user={record.created_by.name}<BR/>run_at={format_field_value(record.run_at)}</FONT>>"  # noqa
        )


def _df_edges_from_runs(all_runs: List[Run]):
    import pandas as pd

    df_values = []
    for run in all_runs:
        if run is None:
            continue
        if run.input_files.exists():
            df_values.append((run.input_files.list(), run))
        if run.output_files.exists():
            df_values.append((run, run.output_files.list()))
    df = pd.DataFrame(df_values, columns=["source_record", "target_record"])
    df = df.explode("source_record")
    df = df.explode("target_record")
    df = df.drop_duplicates()
    df["source"] = [i.id for i in df["source_record"]]
    df["target"] = [i.id for i in df["target_record"]]
    df["source_label"] = df["source_record"].apply(_label_file_run)
    df["target_label"] = df["target_record"].apply(_label_file_run)
    return df


def _transform_emoji(transform: Transform):
    return TRANSFORM_EMOJIS.get(transform.type, "💫")
