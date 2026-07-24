#!/usr/bin/env python3
"""draw.io inspection, normalization, and lint utilities.

Examples:
    python scripts/drawio_tools.py summary diagram.drawio
    python scripts/drawio_tools.py summary diagram.drawio --json
    python scripts/drawio_tools.py dump diagram.drawio --page 0
    python scripts/drawio_tools.py normalize diagram.drawio --in-place
    python scripts/drawio_tools.py normalize diagram.drawio --output normalized.drawio
    python scripts/drawio_tools.py lint diagram.drawio
    python scripts/drawio_tools.py lint diagram.drawio --page 0 --fail-on warn
"""

from __future__ import annotations

import argparse
import base64
import copy
from dataclasses import dataclass
import html
import json
import math
import re
import sys
import urllib.parse
import zlib
from collections import defaultdict
from pathlib import Path
import xml.etree.ElementTree as ET

FLOAT_TOLERANCE = 1e-6
INTERSECTION_TOLERANCE = 1.0
MIN_LINTABLE_NODE_AREA = 144.0
MIN_LINTABLE_NODE_SIDE = 12.0


@dataclass
class NodeBounds:
    id: str
    label: str
    x: float
    y: float
    width: float
    height: float
    style: str
    parent: str | None
    is_container: bool
    is_text: bool
    is_small: bool

    @property
    def center(self) -> tuple[float, float]:
        return (self.x + self.width / 2.0, self.y + self.height / 2.0)


@dataclass
class EdgePath:
    id: str
    label: str
    style: str
    source: str | None
    target: str | None
    points: list[tuple[float, float]]


def decode_compressed_diagram(payload: str) -> str:
    raw = base64.b64decode(payload)
    decoded = zlib.decompress(raw, -15).decode("utf-8")
    return urllib.parse.unquote(decoded)


def parse_xml(xml_text: str) -> ET.Element:
    return ET.fromstring(xml_text)


def detect_diagram_mode(diagram: ET.Element) -> str:
    children = list(diagram)
    if children:
        if children[0].tag == "mxGraphModel":
            return "inline_xml"
        return "inline_child"

    text = (diagram.text or "").strip()
    if not text:
        return "empty"
    if text.startswith("<mxGraphModel"):
        return "inline_text_xml"
    if "&lt;mxGraphModel" in text:
        return "escaped_xml"

    try:
        decoded = decode_compressed_diagram(text)
    except Exception:
        return "unknown"

    if decoded.lstrip().startswith("<mxGraphModel"):
        return "compressed"
    return "decoded_non_xml"


def graph_model_from_diagram(diagram: ET.Element) -> tuple[ET.Element, str]:
    mode = detect_diagram_mode(diagram)
    if mode == "inline_xml":
        return copy.deepcopy(list(diagram)[0]), mode

    text = (diagram.text or "").strip()
    if mode == "inline_text_xml":
        return parse_xml(text), mode
    if mode == "escaped_xml":
        return parse_xml(html.unescape(text)), mode
    if mode == "compressed":
        return parse_xml(decode_compressed_diagram(text)), mode

    raise ValueError(
        f"Unsupported diagram mode '{mode}' for page '{diagram.get('name', 'unknown')}'"
    )


def summarize_file(path: Path) -> dict:
    tree = ET.parse(path)
    root = tree.getroot()
    diagrams = root.findall("diagram")

    pages = []
    for index, diagram in enumerate(diagrams):
        mode = detect_diagram_mode(diagram)
        page_info = {
            "index": index,
            "id": diagram.get("id"),
            "name": diagram.get("name", f"Page-{index + 1}"),
            "mode": mode,
        }

        if mode not in {"empty", "unknown", "decoded_non_xml", "inline_child"}:
            model, _ = graph_model_from_diagram(diagram)
            cells = model.findall(".//mxCell")
            page_info.update(
                {
                    "page_width": model.get("pageWidth"),
                    "page_height": model.get("pageHeight"),
                    "cell_count": len(cells),
                    "vertex_count": sum(cell.get("vertex") == "1" for cell in cells),
                    "edge_count": sum(cell.get("edge") == "1" for cell in cells),
                }
            )

        pages.append(page_info)

    return {
        "file": str(path),
        "host": root.get("host"),
        "version": root.get("version"),
        "modified": root.get("modified"),
        "page_count": len(diagrams),
        "pages": pages,
    }


def print_summary(summary: dict) -> None:
    print(f"File: {summary['file']}")
    print(f"Host: {summary.get('host') or '-'}")
    print(f"Version: {summary.get('version') or '-'}")
    print(f"Modified: {summary.get('modified') or '-'}")
    print(f"Pages: {summary['page_count']}")
    print()
    for page in summary["pages"]:
        print(f"[{page['index']}] {page['name']} (id={page.get('id') or '-'})")
        print(f"  mode: {page['mode']}")
        if "page_width" in page:
            print(f"  size: {page['page_width']} x {page['page_height']}")
            print(
                f"  cells: {page['cell_count']}, vertices: {page['vertex_count']}, edges: {page['edge_count']}"
            )
        print()


def select_diagram(root: ET.Element, page_selector: str) -> ET.Element:
    diagrams = root.findall("diagram")
    if not diagrams:
        raise ValueError("No <diagram> elements found")

    if page_selector.isdigit():
        index = int(page_selector)
        if index < 0 or index >= len(diagrams):
            raise IndexError(f"Page index out of range: {index}")
        return diagrams[index]

    for diagram in diagrams:
        if diagram.get("name") == page_selector or diagram.get("id") == page_selector:
            return diagram

    raise ValueError(f"Could not find page '{page_selector}' by index, name, or id")


def normalize_file(input_path: Path, output_path: Path) -> list[str]:
    tree = ET.parse(input_path)
    root = tree.getroot()
    original_modes = []

    for diagram in root.findall("diagram"):
        model, mode = graph_model_from_diagram(diagram)
        original_modes.append(mode)
        for child in list(diagram):
            diagram.remove(child)
        diagram.text = None
        diagram.append(model)

    ET.indent(tree, space="  ")
    tree.write(output_path, encoding="utf-8", xml_declaration=False)
    return original_modes


def dump_page(path: Path, page_selector: str) -> str:
    tree = ET.parse(path)
    root = tree.getroot()
    diagram = select_diagram(root, page_selector)
    model, _ = graph_model_from_diagram(diagram)
    ET.indent(model, space="  ")
    return ET.tostring(model, encoding="unicode")


def load_diagram_and_page_info(
    path: Path, page_selector: str | None
) -> list[tuple[int, ET.Element, dict]]:
    tree = ET.parse(path)
    root = tree.getroot()
    diagrams = root.findall("diagram")

    selected = []
    for index, diagram in enumerate(diagrams):
        if page_selector is not None:
            chosen = select_diagram(root, page_selector)
            if diagram is not chosen:
                continue
        model, mode = graph_model_from_diagram(diagram)
        selected.append(
            (
                index,
                model,
                {
                    "index": index,
                    "id": diagram.get("id"),
                    "name": diagram.get("name", f"Page-{index + 1}"),
                    "mode": mode,
                },
            )
        )
        if page_selector is not None:
            break

    return selected


def cell_style(cell: ET.Element) -> str:
    return cell.get("style", "")


def cell_label(cell: ET.Element) -> str:
    value = html.unescape(cell.get("value", "") or "")
    value = value.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def style_value(style: str, key: str) -> str | None:
    for part in style.split(";"):
      if not part or "=" not in part:
          continue
      current_key, current_value = part.split("=", 1)
      if current_key == key:
          return current_value
    return None


def as_float(value: str | None, default: float = 0.0) -> float:
    if value is None or value == "":
        return default
    try:
        return float(value)
    except ValueError:
        return default


def build_cell_maps(model: ET.Element) -> tuple[dict[str, ET.Element], dict[str, list[ET.Element]]]:
    cells = model.findall(".//mxCell")
    cell_map = {cell.get("id"): cell for cell in cells if cell.get("id")}
    children_by_parent: dict[str, list[ET.Element]] = defaultdict(list)
    for cell in cells:
        parent_id = cell.get("parent")
        if parent_id:
            children_by_parent[parent_id].append(cell)
    return cell_map, children_by_parent


def is_text_cell(cell: ET.Element) -> bool:
    style = cell_style(cell)
    return "text;" in style or "edgeLabel" in style


def absolute_offset(
    cell_id: str | None, cell_map: dict[str, ET.Element], memo: dict[str, tuple[float, float]]
) -> tuple[float, float]:
    if not cell_id or cell_id not in cell_map:
        return (0.0, 0.0)
    if cell_id in memo:
        return memo[cell_id]

    cell = cell_map[cell_id]
    parent_id = cell.get("parent")
    base_x, base_y = absolute_offset(parent_id, cell_map, memo)
    geometry = cell.find("mxGeometry")
    if geometry is not None and geometry.get("relative") != "1":
        base_x += as_float(geometry.get("x"))
        base_y += as_float(geometry.get("y"))

    memo[cell_id] = (base_x, base_y)
    return memo[cell_id]


def is_container_cell(
    cell: ET.Element, children_by_parent: dict[str, list[ET.Element]], width: float, height: float
) -> bool:
    style = cell_style(cell)
    if any(
        token in style
        for token in ("swimlane", "mxgraph.aws4.group", "shape=mxgraph.aws4.group", "group;")
    ):
        return True
    child_vertices = [
        child
        for child in children_by_parent.get(cell.get("id", ""), [])
        if child.get("vertex") == "1" and not is_text_cell(child)
    ]
    if len(child_vertices) >= 2 and width >= 120 and height >= 80:
        return True
    if width >= 180 and height >= 100 and (
        "verticalAlign=top" in style
        or "dashed=1" in style
        or "spacingLeft=" in style
        or "fillColor=none" in style
    ):
        return True
    if width >= 180 and height >= 100 and not cell_label(cell):
        return True
    return False


def collect_node_bounds(model: ET.Element) -> dict[str, NodeBounds]:
    cell_map, children_by_parent = build_cell_maps(model)
    memo: dict[str, tuple[float, float]] = {}
    nodes: dict[str, NodeBounds] = {}

    for cell_id, cell in cell_map.items():
        if cell.get("vertex") != "1":
            continue
        geometry = cell.find("mxGeometry")
        if geometry is None or geometry.get("relative") == "1":
            continue

        width = as_float(geometry.get("width"))
        height = as_float(geometry.get("height"))
        if width <= 0 or height <= 0:
            continue

        parent_offset = absolute_offset(cell.get("parent"), cell_map, memo)
        x = parent_offset[0] + as_float(geometry.get("x"))
        y = parent_offset[1] + as_float(geometry.get("y"))
        label = cell_label(cell)
        style = cell_style(cell)
        is_text = is_text_cell(cell)
        is_small = (
            width < MIN_LINTABLE_NODE_SIDE
            and height < MIN_LINTABLE_NODE_SIDE
            or width * height < MIN_LINTABLE_NODE_AREA
        )
        nodes[cell_id] = NodeBounds(
            id=cell_id,
            label=label,
            x=x,
            y=y,
            width=width,
            height=height,
            style=style,
            parent=cell.get("parent"),
            is_container=is_container_cell(cell, children_by_parent, width, height),
            is_text=is_text,
            is_small=is_small,
        )

    return nodes


def parent_chain(cell_id: str | None, cell_map: dict[str, ET.Element]) -> list[str]:
    chain = []
    current = cell_id
    while current and current in cell_map:
        parent_id = cell_map[current].get("parent")
        if not parent_id or parent_id in chain:
            break
        chain.append(parent_id)
        current = parent_id
    return chain


def is_ancestor(
    ancestor_id: str | None, descendant_id: str | None, cell_map: dict[str, ET.Element]
) -> bool:
    if not ancestor_id or not descendant_id:
        return False
    return ancestor_id in parent_chain(descendant_id, cell_map)


def direct_point(geometry: ET.Element, point_name: str) -> tuple[float, float] | None:
    for point in geometry.findall("mxPoint"):
        if point.get("as") == point_name:
            return (as_float(point.get("x")), as_float(point.get("y")))
    return None


def collect_edge_paths(model: ET.Element, nodes: dict[str, NodeBounds]) -> list[EdgePath]:
    edges = []
    for cell in model.findall(".//mxCell"):
        if cell.get("edge") != "1":
            continue

        geometry = cell.find("mxGeometry")
        if geometry is None:
            continue

        source_id = cell.get("source")
        target_id = cell.get("target")
        source_point = direct_point(geometry, "sourcePoint")
        target_point = direct_point(geometry, "targetPoint")

        if source_point is None and source_id in nodes:
            source_point = nodes[source_id].center
        if target_point is None and target_id in nodes:
            target_point = nodes[target_id].center

        intermediate = []
        for points_array in geometry.findall("Array"):
            if points_array.get("as") != "points":
                continue
            for point in points_array.findall("mxPoint"):
                intermediate.append((as_float(point.get("x")), as_float(point.get("y"))))

        path = []
        if source_point is not None:
            path.append(source_point)
        path.extend(intermediate)
        if target_point is not None:
            path.append(target_point)

        edges.append(
            EdgePath(
                id=cell.get("id", ""),
                label=cell_label(cell),
                style=cell_style(cell),
                source=source_id,
                target=target_id,
                points=path,
            )
        )

    return edges


def rect_intersection_area(a: NodeBounds, b: NodeBounds) -> float:
    overlap_w = min(a.x + a.width, b.x + b.width) - max(a.x, b.x)
    overlap_h = min(a.y + a.height, b.y + b.height) - max(a.y, b.y)
    if overlap_w <= 0 or overlap_h <= 0:
        return 0.0
    return overlap_w * overlap_h


def line_segments(points: list[tuple[float, float]]) -> list[tuple[tuple[float, float], tuple[float, float]]]:
    segments = []
    for start, end in zip(points, points[1:]):
        if math.dist(start, end) <= FLOAT_TOLERANCE:
            continue
        segments.append((start, end))
    return segments


def orientation(a: tuple[float, float], b: tuple[float, float], c: tuple[float, float]) -> int:
    value = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
    if abs(value) <= FLOAT_TOLERANCE:
        return 0
    return 1 if value > 0 else 2


def on_segment(
    a: tuple[float, float], b: tuple[float, float], c: tuple[float, float]
) -> bool:
    return (
        min(a[0], c[0]) - FLOAT_TOLERANCE <= b[0] <= max(a[0], c[0]) + FLOAT_TOLERANCE
        and min(a[1], c[1]) - FLOAT_TOLERANCE <= b[1] <= max(a[1], c[1]) + FLOAT_TOLERANCE
    )


def segment_intersection(
    p1: tuple[float, float],
    q1: tuple[float, float],
    p2: tuple[float, float],
    q2: tuple[float, float],
) -> tuple[bool, tuple[float, float] | None]:
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        denom = (p1[0] - q1[0]) * (p2[1] - q2[1]) - (p1[1] - q1[1]) * (p2[0] - q2[0])
        if abs(denom) <= FLOAT_TOLERANCE:
            return True, None
        px_num = (
            (p1[0] * q1[1] - p1[1] * q1[0]) * (p2[0] - q2[0])
            - (p1[0] - q1[0]) * (p2[0] * q2[1] - p2[1] * q2[0])
        )
        py_num = (
            (p1[0] * q1[1] - p1[1] * q1[0]) * (p2[1] - q2[1])
            - (p1[1] - q1[1]) * (p2[0] * q2[1] - p2[1] * q2[0])
        )
        return True, (px_num / denom, py_num / denom)

    if o1 == 0 and on_segment(p1, p2, q1):
        return True, p2
    if o2 == 0 and on_segment(p1, q2, q1):
        return True, q2
    if o3 == 0 and on_segment(p2, p1, q2):
        return True, p1
    if o4 == 0 and on_segment(p2, q1, q2):
        return True, q1
    return False, None


def points_close(a: tuple[float, float], b: tuple[float, float], tolerance: float = INTERSECTION_TOLERANCE) -> bool:
    return math.dist(a, b) <= tolerance


def rect_edges(node: NodeBounds) -> list[tuple[tuple[float, float], tuple[float, float]]]:
    top_left = (node.x, node.y)
    top_right = (node.x + node.width, node.y)
    bottom_left = (node.x, node.y + node.height)
    bottom_right = (node.x + node.width, node.y + node.height)
    return [
        (top_left, top_right),
        (top_right, bottom_right),
        (bottom_right, bottom_left),
        (bottom_left, top_left),
    ]


def point_in_rect(point: tuple[float, float], node: NodeBounds) -> bool:
    return (
        node.x + FLOAT_TOLERANCE < point[0] < node.x + node.width - FLOAT_TOLERANCE
        and node.y + FLOAT_TOLERANCE < point[1] < node.y + node.height - FLOAT_TOLERANCE
    )


def segment_intersects_rect(
    start: tuple[float, float], end: tuple[float, float], node: NodeBounds
) -> bool:
    if point_in_rect(start, node) or point_in_rect(end, node):
        return True
    for rect_start, rect_end in rect_edges(node):
        intersects, _ = segment_intersection(start, end, rect_start, rect_end)
        if intersects:
            return True
    return False


def issue(
    page: dict,
    severity: str,
    code: str,
    message: str,
    details: dict | None = None,
) -> dict:
    payload = {
        "page_index": page["index"],
        "page_name": page["name"],
        "severity": severity,
        "code": code,
        "message": message,
    }
    if details:
        payload["details"] = details
    return payload


def lint_page(model: ET.Element, page: dict) -> list[dict]:
    cell_map, _ = build_cell_maps(model)
    nodes = collect_node_bounds(model)
    edges = collect_edge_paths(model, nodes)
    issues: list[dict] = []

    background = (model.get("background") or "").strip().lower()
    if background and background not in {"none", "transparent"}:
        issues.append(
            issue(
                page,
                "warn",
                "background_not_transparent",
                "mxGraphModel sets a solid background color. Transparent backgrounds usually look better in docs and slides.",
                {"background": background},
            )
        )

    text_like_nodes = [node for node in nodes.values() if node.label]
    if text_like_nodes and not (model.get("defaultFontFamily") or "").strip():
        issues.append(
            issue(
                page,
                "warn",
                "missing_default_font_family",
                "Page contains text but mxGraphModel does not set defaultFontFamily.",
            )
        )

    for cell in model.findall(".//mxCell"):
        style = cell_style(cell)
        if "edgeLabel" not in style:
            continue
        geometry = cell.find("mxGeometry")
        if geometry is None:
            continue
        has_offset = any(point.get("as") == "offset" for point in geometry.findall("mxPoint"))
        if not has_offset:
            issues.append(
                issue(
                    page,
                    "warn",
                    "edge_label_no_offset",
                    f"Edge label '{cell_label(cell) or cell.get('id', '')}' does not define an offset.",
                    {"cell_id": cell.get("id")},
                )
            )

    lintable_nodes = [
        node
        for node in nodes.values()
        if not node.is_text and not node.is_container and not node.is_small
    ]

    all_nodes = list(nodes.values())

    for edge in edges:
        if edge.source is None or edge.target is None:
            issues.append(
                issue(
                    page,
                    "warn",
                    "dangling_edge",
                    f"Edge {edge.id} is missing a source or target connection.",
                    {"edge_id": edge.id, "label": edge.label},
                )
            )
        if len(edge.points) < 2:
            issues.append(
                issue(
                    page,
                    "warn",
                    "unroutable_edge",
                    f"Edge {edge.id} does not have enough points to form a path.",
                    {"edge_id": edge.id, "label": edge.label},
                )
            )
        bends = max(0, len(edge.points) - 2)
        if bends >= 5:
            issues.append(
                issue(
                    page,
                    "warn",
                    "edge_too_many_bends",
                    f"Edge {edge.id} has {bends} bends. Consider rerouting for readability.",
                    {"edge_id": edge.id, "label": edge.label, "bends": bends},
                )
            )

    for index, node_a in enumerate(lintable_nodes):
        for node_b in lintable_nodes[index + 1 :]:
            if (
                is_ancestor(node_a.id, node_b.id, cell_map)
                or is_ancestor(node_b.id, node_a.id, cell_map)
            ):
                continue
            overlap_area = rect_intersection_area(node_a, node_b)
            if overlap_area <= 0:
                continue
            issues.append(
                issue(
                    page,
                    "error" if overlap_area >= 400 else "warn",
                    "node_overlap",
                    f"Nodes '{node_a.label or node_a.id}' and '{node_b.label or node_b.id}' overlap.",
                    {
                        "node_a": node_a.id,
                        "node_b": node_b.id,
                        "overlap_area": round(overlap_area, 2),
                    },
                )
            )

    edge_segments = [(edge, line_segments(edge.points)) for edge in edges]
    for edge, segments in edge_segments:
        seen_edge_node_pairs: set[tuple[str, str]] = set()
        for start, end in segments:
            for node in lintable_nodes:
                if node.id in {edge.source, edge.target}:
                    continue
                if is_ancestor(node.id, edge.source, cell_map) or is_ancestor(
                    node.id, edge.target, cell_map
                ):
                    continue
                if (edge.id, node.id) in seen_edge_node_pairs:
                    continue
                if segment_intersects_rect(start, end, node):
                    seen_edge_node_pairs.add((edge.id, node.id))
                    issues.append(
                        issue(
                            page,
                            "error",
                            "edge_through_node",
                            f"Edge {edge.id} passes through node '{node.label or node.id}'.",
                            {"edge_id": edge.id, "node_id": node.id},
                        )
                    )
                    break

    for index, (edge_a, segments_a) in enumerate(edge_segments):
        related_a = {edge_a.source, edge_a.target}
        for edge_b, segments_b in edge_segments[index + 1 :]:
            related_b = {edge_b.source, edge_b.target}
            if related_a & related_b:
                continue

            found_crossing = False
            for segment_a in segments_a:
                for segment_b in segments_b:
                    intersects, point = segment_intersection(
                        segment_a[0], segment_a[1], segment_b[0], segment_b[1]
                    )
                    if not intersects:
                        continue

                    endpoints = [segment_a[0], segment_a[1], segment_b[0], segment_b[1]]
                    if point is not None and any(points_close(point, endpoint) for endpoint in endpoints):
                        continue

                    issues.append(
                        issue(
                            page,
                            "error",
                            "edge_crossing",
                            f"Edge {edge_a.id} crosses edge {edge_b.id}.",
                            {
                                "edge_a": edge_a.id,
                                "edge_b": edge_b.id,
                                "point": None
                                if point is None
                                else [round(point[0], 2), round(point[1], 2)],
                            },
                        )
                    )
                    found_crossing = True
                    break
                if found_crossing:
                    break

    return issues


def lint_file(path: Path, page_selector: str | None = None) -> dict:
    pages = []
    for _, model, page in load_diagram_and_page_info(path, page_selector):
        page_issues = lint_page(model, page)
        pages.append(
            {
                "page_index": page["index"],
                "page_name": page["name"],
                "issue_count": len(page_issues),
                "issues": page_issues,
            }
        )

    severity_counts = {"error": 0, "warn": 0}
    for page in pages:
        for lint_issue in page["issues"]:
            severity_counts[lint_issue["severity"]] += 1

    return {
        "file": str(path),
        "page_count": len(pages),
        "severity_counts": severity_counts,
        "pages": pages,
    }


def print_lint_report(report: dict, max_issues: int) -> None:
    print(f"Lint report: {report['file']}")
    print(
        f"Errors: {report['severity_counts']['error']}, warnings: {report['severity_counts']['warn']}"
    )
    print()

    printed = 0
    for page in report["pages"]:
        print(f"[{page['page_index']}] {page['page_name']}: {page['issue_count']} issue(s)")
        for lint_issue in page["issues"]:
            if printed >= max_issues:
                print("  ... truncated ...")
                return
            print(
                f"  - {lint_issue['severity'].upper()} {lint_issue['code']}: {lint_issue['message']}"
            )
            printed += 1
        print()


def lint_exit_code(report: dict, fail_on: str) -> int:
    if fail_on == "none":
        return 0
    if fail_on == "error" and report["severity_counts"]["error"] > 0:
        return 1
    if fail_on == "warn" and (
        report["severity_counts"]["error"] > 0 or report["severity_counts"]["warn"] > 0
    ):
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Inspect and normalize .drawio files")
    subparsers = parser.add_subparsers(dest="command", required=True)

    summary_parser = subparsers.add_parser("summary", help="Print a file summary")
    summary_parser.add_argument("path", type=Path)
    summary_parser.add_argument("--json", action="store_true", dest="as_json")

    dump_parser = subparsers.add_parser("dump", help="Dump one page as mxGraphModel XML")
    dump_parser.add_argument("path", type=Path)
    dump_parser.add_argument(
        "--page",
        default="0",
        help="Page index, name, or id. Defaults to the first page.",
    )

    normalize_parser = subparsers.add_parser(
        "normalize", help="Convert pages to inline <mxGraphModel> form"
    )
    normalize_parser.add_argument("path", type=Path)
    output_group = normalize_parser.add_mutually_exclusive_group(required=True)
    output_group.add_argument("--in-place", action="store_true")
    output_group.add_argument("--output", type=Path)

    lint_parser = subparsers.add_parser(
        "lint", help="Check overlaps, edge crossings, and connector routing issues"
    )
    lint_parser.add_argument("path", type=Path)
    lint_parser.add_argument(
        "--page",
        help="Optional page index, name, or id. Defaults to linting all pages.",
    )
    lint_parser.add_argument("--json", action="store_true", dest="as_json")
    lint_parser.add_argument(
        "--fail-on",
        choices=("none", "error", "warn"),
        default="error",
        help="Exit code policy. Defaults to failing only on errors.",
    )
    lint_parser.add_argument(
        "--max-issues",
        type=int,
        default=100,
        help="Maximum number of issues to print in text mode.",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "summary":
        summary = summarize_file(args.path)
        if args.as_json:
            print(json.dumps(summary, ensure_ascii=False, indent=2))
        else:
            print_summary(summary)
        return 0

    if args.command == "dump":
        print(dump_page(args.path, args.page))
        return 0

    if args.command == "normalize":
        output_path = args.path if args.in_place else args.output
        original_modes = normalize_file(args.path, output_path)
        print(f"Normalized: {args.path}")
        print(f"Output: {output_path}")
        print(f"Original page modes: {', '.join(original_modes)}")
        return 0

    if args.command == "lint":
        report = lint_file(args.path, args.page)
        if args.as_json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print_lint_report(report, args.max_issues)
        return lint_exit_code(report, args.fail_on)

    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    sys.exit(main())
