# 官方样例清单

这份清单是 `drawio-skill` 的官方样例导航版。

目的不是简单罗列链接，而是帮助你在生成或修改图之前，先找到最接近的“官方图种语言”。

## 1. 先理解资源类型

你提供的这些链接直接访问时，很多会返回原始 XML 或 `.drawio` 文本，这很正常。

在 skill 里要这样理解它们：

| 类型 | 后缀 | 含义 | 使用方式 |
|------|------|------|----------|
| 官方示例 | `.drawio` | 完整 draw.io 文件，通常可直接打开 | 适合参考页面结构、节点组织、连线风格 |
| 模板库模板 | `.xml` | draw.io 模板 XML | 适合参考样式体系、布局语言、卡片结构 |
| 博客示例 | `.drawio` | 通常更强调技巧、视觉表达或特殊场景 | 适合借鉴高级排版、信息图、复杂布线 |

## 2. 使用这些样例的规则

- 先选最接近的图种家族，再开始画图。
- 不要直接复制样例内容，只复用结构语言、布局方法、连线节奏和视觉系统。
- 如果链接标题和实际文件名不完全一致，以原始资源内容为准。
- 如果是 `.xml` 模板，不要把它当成现成业务图；它更适合提取版式和样式。
- 新建图时，优先参考 1 到 2 个同家族样例，不要混杂太多家族。

## 3. 图表类型目录

下列目录按你提供的完整分类整理。

- 软件开发和敏捷
- UML 图
- 模型和线框图
- IT 和基础设施图
- 安全
- 机架和机柜示意图
- 树状图和组织结构图
- 思维导图和概念图
- 工业与工程
- 电路图和逻辑图
- 石川图（鱼骨图）
- 流程图
- 泳道图和跨职能流程图
- BPMN 图
- 商业与市场营销
- PERT 图和甘特图
- 时间表和路线图
- 信息图表
- 科学与教育插图

## 4. 软件开发和敏捷

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| Gitflow 流程图 | 官方示例 `.drawio` | 适合参考分支流、版本流程、并行分支关系 | [gitflow-examples.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/gitflow-examples.drawio) |
| Gemfile 依赖关系图 | 官方示例 `.drawio` | 适合参考依赖图、模块图、关系可视化 | [gemfile-dependency-graph.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/gemfile-dependency-graph.drawio) |
| 各种样式的看板 | 官方示例 `.drawio` | 适合参考看板、状态列、任务流转布局 | [kanban-examples.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/kanban-examples.drawio) |
| C4 模型：系统上下文图、容器图、组件图和类图 | 官方示例 `.drawio` | 这条材料中给出的链接指向 `aws-simple-architecture.drawio`，使用时应以实际文件内容为准 | [aws-simple-architecture.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/aws-simple-architecture.drawio) |

## 5. UML 图

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| UML 用例图 | 官方示例 `.drawio` | 适合参与者与系统能力、角色边界 | [uml-use-case-example.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/uml-use-case-example.drawio) |
| UML 类图 | 官方示例 `.drawio` | 适合实体结构、属性/方法、关系建模 | [class-diagram-example.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/class-diagram-example.drawio) |
| 序列图 | 官方示例 `.drawio` | 适合时序交互、条件分支、循环片段 | [sequence-diagram-examples.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/sequence-diagram-examples.drawio) |
| 组件图 | 官方示例 `.drawio` | 适合组件职责、依赖关系、接口与端口 | [uml-component-example.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/uml-component-example.drawio) |
| 复合结构图 | 官方示例 `.drawio` | 适合分类器内部结构、部件协作关系 | [uml-composite-structure-collaboration-use-example.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/uml-composite-structure-collaboration-use-example.drawio) |
| 部署图 | 官方示例 `.drawio` | 适合部署节点、工件与环境映射 | [uml-deployment-example.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/uml-deployment-example.drawio) |
| 活动图 | 官方示例 `.drawio` | 适合工作流、分叉/汇合、泳道场景 | [uml-activity-example.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/uml-activity-example.drawio) |
| UML 状态图 | 博客示例 `.drawio` | 适合状态迁移、异常恢复、监控补充页 | [uml-state-diagram-smart-lock.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/uml-state-diagram-smart-lock.drawio) |

## 6. 模型和线框图

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| 应用模型（模板库） | 模板 `.xml` | 适合应用原型、结构草图、界面布局模型 | [bootstrap_1.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/layout/bootstrap_1.xml) |

## 7. IT 和基础设施图

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| 简易 AWS 架构 | 官方示例 `.drawio` | 适合 AWS Cloud、VPC、AZ、子网分层 | [aws-simple-architecture.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/aws-simple-architecture.drawio) |
| 从 Cloudockit 导出的 3D AWS 图 | 模板 `.xml` | 适合更展示型的 AWS 3D 视觉表达 | [aws_3d_2.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/cloud/aws_3d_2.xml) |
| 从 Cloudcraft 导出的物联网 AWS 图 | 官方示例 `.drawio` | 适合 IoT 基础设施和多设备边界 | [aws-internet-of-things.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/aws-internet-of-things.drawio) |
| IBM IoT 基础架构图（模板库） | 模板 `.xml` | 适合 IoT 平台和设备云接入结构 | [ibm_iot_architecture.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/cloud/ibm_iot_architecture.xml) |
| Google Cloud Platform 基础架构图（模板库） | 模板 `.xml` | 适合 GCP IoT、MQTT、Pub/Sub 拓扑 | [internet_of_things_mqtt_to_pubsub_broker.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/gcp/internet_of_things_mqtt_to_pubsub_broker.xml) |
| Veaam 基础架构图（模板库） | 官方示例 `.drawio` | 适合网络基础设施和设备关系图 | [veaam-network-diagram.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/veaam-network-diagram.drawio) |

## 8. 安全

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| 威胁建模 | 博客示例 `.drawio` | 包含数据流图、流程图、攻击树，适合安全建模 | [threat-modelling.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/threat-modelling.drawio) |

## 9. 机架和机柜示意图

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| 基本 IT 服务器机架图 | 官方示例 `.drawio` | 适合机架、设备位、服务器排布 | [rack-diagram-simple-server.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/rack-diagram-simple-server.drawio) |
| Arista 机架图（模板库） | 模板 `.drawio` | 适合网络设备机架布局 | [arista.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/network/arista.drawio) |
| 机柜结构图（模板库） | 模板 `.xml` | 适合电柜/机柜结构布局 | [cabinet_2.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/engineering/cabinet_2.xml) |

## 10. 树状图和组织结构图

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| 使用路径点形状的组织结构图模板 | 博客示例 `.drawio` | 适合树状图、层级图、特殊连接点 | [waypoint-shape.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/waypoint-shape.drawio) |
| 由 CSV 和格式化数据生成的组织结构图 | 博客示例 `.drawio` | 适合 CSV 导入驱动的组织图和层级图 | [CSVimport-examples.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/CSVimport-examples.drawio) |

## 11. 思维导图和概念图

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| UML 2.5 概念图 | 官方示例 `.drawio` | 适合概念总览图、知识地图 | [concept-map-uml-diagrams-overview.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/concept-map-uml-diagrams-overview.drawio) |
| 生物思维导图（模板库） | 模板 `.xml` | 适合思维导图和分层知识图 | [living_beings_mind_map.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/maps/living_beings_mind_map.xml) |

## 12. 工业与工程

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| 精益地图模板 | 模板 `.xml` | 适合价值流、精益改进、业务模式梳理 | [lean_mapping_2.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/business/lean_mapping_2.xml) |
| 工程流程图 | 模板 `.xml` | 适合工程过程、流程设备与处理链 | [process_flow_diagram.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/engineering/process_flow_diagram.xml) |

## 13. 电路图和逻辑图

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| 电路图，模板已修改为使用路径点形状 | 官方示例 `.drawio` | 适合接触点、电线连接、电路布线 | [circuit-logic-examples.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/circuit-logic-examples.drawio) |
| 逻辑图，模板已修改为使用航点形状 | 官方示例 `.drawio` | 适合逻辑关系、线条跳跃、未连接交叉显示 | [circuit-logic-examples.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/circuit-logic-examples.drawio) |

## 14. 石川图（鱼骨图）

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| 石川图在制造和营销中的应用 | 博客示例 `.drawio` | 适合根因分析、因果分析、问题追踪 | [ishikawa-diagram-examples.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/ishikawa-diagram-examples.drawio) |

## 15. 流程图

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| 基础流程图，基于基础模板设计 | 模板 `.xml` | 适合简单分支流程和基础工作流 | [flowchart.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/basic/flowchart.xml) |
| 工作流程（流程图） | 模板 `.xml` | 适合业务工作流和职责传递 | [workflow_2.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/flowcharts/workflow_2.xml) |
| 事件驱动流程图 | 模板 `.xml` | 适合 EPC、事件驱动流程链 | [epc_2.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/flowcharts/epc_2.xml) |
| 使用 CSV 文件生成流程图并格式化数据 | 博客示例 `.drawio` | 适合数据驱动批量生成流程图 | [CSVimport-examples.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/CSVimport-examples.drawio) |

## 16. 泳道图和跨职能流程图

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| 跨职能流程图，基于基本模板着色 | 模板 `.xml` | 适合跨角色、跨部门泳道流程 | [cross.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/basic/cross.xml) |
| 带泳道的流程图（模板库） | 官方示例 `.xml` | 适合带泳道的流程图布局语言 | [WorkflowFlowchart.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/WorkflowFlowchart.xml) |

## 17. BPMN 图

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| BPMN 图 | 官方示例 `.xml` | 适合基础 BPMN 图形与语义 | [BPMN.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/BPMN.xml) |
| 订单处理流程的 BPMN 图 | 博客示例 `.drawio` | 适合订单处理、带角色的 BPMN 流程 | [bpmn-2-example.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/bpmn-2-example.drawio) |
| BPMN 编排和编舞模型 | 博客示例 `.drawio` | 适合多角色消息传递和协作场景 | [bpmn-2-example.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/bpmn-2-example.drawio) |

## 18. 商业与市场营销

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| 企业业务模型（模板库） | 模板 `.xml` | 适合商业结构和业务块梳理 | [business_model_1.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/business/business_model_1.xml) |
| 商业模式画布（模板库） | 模板 `.xml` | 适合商业模式画布、价值主张分析 | [business_model_canvas_1.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/business/business_model_canvas_1.xml) |
| 在线购买杂货的客户故事地图 | 博客示例 `.drawio` | 适合用户故事、旅程与任务分层 | [story-map.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/story-map.drawio) |
| 入站营销流程（模板库） | 模板 `.xml` | 适合营销漏斗和阶段转化图 | [accd.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/business/accd.xml) |

## 19. PERT 图和甘特图

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| 带有首选路径的 PERT 图（模板库） | 模板 `.xml` | 适合关键路径和任务依赖 | [pert_4.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/business/pert_4.xml) |
| PERT 图（模板库） | 模板 `.xml` | 适合常规 PERT 图和项目计划 | [pert_5.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/business/pert_5.xml) |
| 甘特图（模板库） | 模板 `.xml` | 适合项目时间计划和任务排期 | [gantt_1.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/templates/tables/gantt_1.xml) |

## 20. 时间表和路线图

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| 项目开发路线图 | 官方示例 `.drawio` | 适合项目里程碑、阶段路线图 | [timeline-example.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/timeline-example.drawio) |
| 使用信息图表形状创建水平时间轴 | 官方示例 `.drawio` | 适合水平时间轴和里程碑展示 | [timeline-infographic-shapes-horizontal.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/timeline-infographic-shapes-horizontal.drawio) |
| 使用信息图表形状创建垂直时间轴 | 官方示例 `.drawio` | 适合垂直时间线和阶段展开 | [timeline-infographic-shapes-vertical.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/timeline-infographic-shapes-vertical.drawio) |
| 项目阶段及参与团队 | 博客示例 `.drawio` | 适合项目阶段与团队协作关系图 | [project-phase-timeline.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/project-phase-timeline.drawio) |

## 21. 信息图表

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| draw.io 众多集成方案信息图 | 博客示例 `.drawio` | 适合平台生态、产品能力总览 | [diagram-integrations.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/diagram-integrations.drawio) |
| 使用剪贴画制作信息图 | 官方示例 `.xml` | 适合通用信息图和图文布局 | [Infographic.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/Infographic.xml) |
| 使用信息图形状库制作信息图 | 官方示例 `.xml` | 适合更偏结构化的信息图 | [Infographic_2.xml](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/Infographic_2.xml) |
| 信息图表形状库中的分层形状 | 博客示例 `.drawio` | 适合分层信息图和曲线连接器 | [infographic-shape-library-layers.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/infographic-shape-library-layers.drawio) |
| 演示文稿中幻灯片的项目步骤 | 官方示例 `.drawio` | 适合步骤型信息图和演示页视觉布局 | [infographic-project-steps.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/infographic-project-steps.drawio) |
| 带标注和图标的信息图 | 官方示例 `.drawio` | 适合注释型信息图 | [infographic-example-1.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/infographic-example-1.drawio) |
| 深色背景信息图，带有标注和图标 | 官方示例 `.drawio` | 适合深色背景信息图 | [infographic-example-2.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/infographic-example-2.drawio) |
| 六层信息图 | 官方示例 `.drawio` | 适合层级式结构信息图 | [infographic-example-3.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/infographic-example-3.drawio) |
| 五层信息图 | 官方示例 `.drawio` | 适合多层步骤式结构 | [infographic-example-4.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/infographic-example-4.drawio) |
| 深色背景上的横向分层信息图 | 官方示例 `.drawio` | 适合横向多层信息展示 | [infographic-example-5.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/infographic-example-5.drawio) |

## 22. 科学与教育插图

| 名称 | 类型 | 说明 | 链接 |
|------|------|------|------|
| 细胞培养示意图，使用 Bioicons 集成 | 官方示例 `.drawio` | 适合生物流程、实验示意 | [cell-culture-flow.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/cell-culture-flow.drawio) |
| 水循环插图，基于 draw.io 模板修改 | 官方示例 `.drawio` | 适合科普流程图和自然循环示意 | [infographic-water-cycle.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/infographic-water-cycle.drawio) |
| 在线白板编辑器主题图文教程 | 博客示例 `.drawio` | 适合教程型视觉说明和操作步骤图 | [board-visual-tutorial.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/board-visual-tutorial.drawio) |
| 包含数学排版的公式参考表 | 官方示例 `.drawio` | 适合数学公式、表格与文本形状结合 | [maths-examples.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/examples/maths-examples.drawio) |
| 焦距计算 | 博客示例 `.drawio` | 适合物理光学和标注式示意图 | [focus-lens.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/focus-lens.drawio) |
| 光线穿过棱镜 | 博客示例 `.drawio` | 适合射线、光谱和科学解释图 | [light-spectrum.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/light-spectrum.drawio) |
| 马的各个部位 | 博客示例 `.drawio` | 适合标注型教育插图 | [horse-labelled.drawio](https://raw.githubusercontent.com/jgraph/drawio-diagrams/dev/blog/horse-labelled.drawio) |

## 23. 当前材料中未给出具体链接的图种

你给出的总目录里还提到了这些大类，但在本批材料中没有附上具体 raw 链接：

- 维恩图
- 平面图

在 skill 中如果用户提到这两类图，应该：

1. 先按图种目标选择最近似的已有家族参考。
2. 再结合 draw.io 内置形状库或模板库补足。
3. 不要因为本文件缺少链接就退回到默认平庸布局。

## 24. 在 skill 中如何使用这份清单

### 如果是新建图

- 先按领域选大类
- 再按图种选 1 到 2 个最接近的官方样例
- 再结合 [connector-routing.md](connector-routing.md) 规划通道
- 再结合 [visual-systems.md](visual-systems.md) 选择视觉系统

### 如果是修改图

- 先判断当前图最像哪个官方家族
- 再用对应家族的布局语言修正
- 如果图的主要问题是交叉、遮挡、乱连接，优先修连线而不是先换颜色

### 如果图种不明确

按下面顺序判断：

1. 是否强调时间顺序
2. 是否强调角色/泳道
3. 是否强调静态结构
4. 是否强调部署和边界
5. 是否强调因果分析
6. 是否强调展示性信息图

判断完再选样例。
