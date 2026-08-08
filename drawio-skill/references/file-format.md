# draw.io 文件格式与编辑工作流

## 1. 外层结构

典型 `.drawio` 文件结构：

```xml
<mxfile ...>
  <diagram id="..." name="Page-1">
    <mxGraphModel>...</mxGraphModel>
  </diagram>
</mxfile>
```

但实际文件里，`<diagram>` 里的内容不一定是直接可读的 XML。

## 2. 在官方样例里观察到的 3 种主要模式

当前官方样例目录共 25 个文件：

- 23 个文件主要使用压缩 `diagram` 文本
- 2 个文件直接内联 `<mxGraphModel>`

样例中实际出现的模式如下：

| 模式 | 表现形式 | 是否适合直接补丁 | 建议动作 |
|------|-----------|------------------|----------|
| `compressed` | `<diagram>` 文本是 base64 + deflate + URL encoding | 否 | 先 `normalize` |
| `inline_xml` | `<diagram>` 下直接挂 `<mxGraphModel>` 子节点 | 是 | 直接局部编辑 |
| `inline_text_xml` / `escaped_xml` | 文本里是 XML 或转义 XML | 视情况 | 通常也先 `normalize` |

## 3. 为什么先检查再编辑

如果把压缩页当普通 XML 直接改：

- 很容易改坏整个 page
- 很难定位具体节点
- 无法精确调整 `mxCell` 和 `mxGeometry`

因此已有文件的默认流程应该是：

1. `summary`
2. `normalize`（如果不是 `inline_xml`）
3. 正常编辑
4. 需要时导出 PNG

## 4. 推荐命令

### 4.1 查看文件摘要

```bash
python scripts/drawio_tools.py summary path/to/file.drawio
```

输出会包含：

- 文件级元信息
- page 数量
- 每页名称、id、编码模式
- cell / vertex / edge 数量

### 4.2 导出某一页的 XML

```bash
python scripts/drawio_tools.py dump path/to/file.drawio --page 0
python scripts/drawio_tools.py dump path/to/file.drawio --page "Page-1"
```

### 4.3 把文件归一化成可编辑形式

```bash
python scripts/drawio_tools.py normalize path/to/file.drawio --in-place
```

或输出到新文件：

```bash
python scripts/drawio_tools.py normalize path/to/file.drawio --output normalized.drawio
```

## 5. 归一化后的编辑约束

归一化之后，继续遵守这些规则：

- 保留 `<mxfile>` 根节点属性
- 保留 `<diagram id>` 与 `name`
- 保留页面顺序
- 尽量保留原有 `mxCell id`
- 只改需要改的 page

## 6. 多页图处理

官方样例中很多文件是多页图，例如：

- `bpmn-2-example.drawio`
- `gitflow-examples.drawio`
- `sequence-diagram-examples.drawio`
- `threat-modelling.drawio`
- `timeline-infographic-shapes-vertical.drawio`
- `uml-state-diagram-smart-lock.drawio`

修改多页图时：

- 先确认用户要改哪一页
- 如果改动跨页，保持页面命名风格一致
- 最终答复里列出改动页名

## 7. 新建文件的最小骨架

如果从零创建 `.drawio`，优先直接写内联 XML 版本：

```xml
<mxfile host="app.diagrams.net" version="21.6.9">
  <diagram id="page-1" name="Page-1">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1019" pageHeight="1320" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

这样后续维护成本最低。
