#!/usr/bin/env python3
"""
Multi-Agent Paper Generation System
整合研究、写作和编译能力的多智能体协作系统
"""

import os
import sys
import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from pathlib import Path

# Add the compose_tools to the path
sys.path.append('AgentScholar-UI/agent_scholar/tools/compose_tools')
from latex_compiler import LaTeXProjectCompiler

@dataclass
class PaperSection:
    """论文章节结构"""
    title: str
    content: str
    order: int
    agent: str

@dataclass
class ResearchPaper:
    """研究论文对象"""
    title: str
    abstract: str
    sections: List[PaperSection]
    references: List[str]
    author: str
    keywords: List[str]

class ResearchAgent:
    """研究智能体 - 负责文献调研和内容分析"""
    
    def __init__(self, name: str = "Research Agent"):
        self.name = name
        self.research_focus = []
        self.literature_summary = ""
    
    def conduct_research(self, topic: str) -> Dict[str, Any]:
        """进行文献调研"""
        print(f"🔍 {self.name} 开始调研主题: {topic}")
        
        # 模拟研究过程
        research_result = {
            "topic": topic,
            "key_findings": [
                f"{topic}领域的最新发展",
                f"{topic}的主要挑战和机遇",
                f"{topic}的应用前景"
            ],
            "literature_summary": f"基于对{topic}的深入调研，我们发现该领域正在快速发展...",
            "recommended_sections": [
                "引言和背景",
                "理论基础",
                "方法学",
                "应用案例",
                "挑战与展望",
                "结论"
            ]
        }
        
        self.literature_summary = research_result["literature_summary"]
        print(f"✅ {self.name} 完成调研")
        
        return research_result

class WritingAgent:
    """写作智能体 - 负责论文内容创作"""
    
    def __init__(self, name: str = "Writing Agent"):
        self.name = name
        self.writing_style = "academic"
    
    def write_section(self, section_title: str, research_data: Dict[str, Any], 
                      section_type: str = "general") -> str:
        """写作特定章节"""
        print(f"✍️ {self.name} 开始写作章节: {section_title}")
        
        # 根据章节类型生成内容
        if section_type == "introduction":
            content = self._write_introduction(section_title, research_data)
        elif section_type == "conclusion":
            content = self._write_conclusion(section_title, research_data)
        else:
            content = self._write_general_section(section_title, research_data)
        
        print(f"✅ {self.name} 完成章节: {section_title}")
        return content
    
    def _write_introduction(self, title: str, research_data: Dict[str, Any]) -> str:
        """写作引言"""
        return f"""\\section{{{title}}}
{research_data['topic']}是当前人工智能领域的重要研究方向。随着技术的不断进步，该领域在理论和应用方面都取得了显著进展。

本研究旨在深入分析{research_data['topic']}的发展现状，探讨其面临的挑战和机遇，并为未来的研究方向提供建议。

\\subsection{{研究背景}}
{research_data['literature_summary']}

\\subsection{{研究目标}}
本研究的主要目标包括：
\\begin{{enumerate}}
    \\item 分析{research_data['topic']}的理论基础和发展历程
    \\item 总结该领域的主要技术方法和应用案例
    \\item 识别当前面临的挑战和限制
    \\item 提出未来发展的建议和展望
\\end{{enumerate}}"""
    
    def _write_general_section(self, title: str, research_data: Dict[str, Any]) -> str:
        """写作一般章节"""
        return f"""\\section{{{title}}}
基于对{research_data['topic']}的深入研究，我们发现该领域具有以下特点：

\\subsection{{主要特征}}
{research_data['topic']}具有以下主要特征：
\\begin{{itemize}}
    \\item 技术先进性：采用最新的算法和方法
    \\item 应用广泛性：在多个领域都有重要应用
    \\item 发展潜力大：具有广阔的发展前景
\\end{{itemize}}

\\subsection{{技术方法}}
该领域主要采用以下技术方法：
\\begin{{enumerate}}
    \\item 深度学习方法
    \\item 强化学习算法
    \\item 多智能体协作
    \\item 知识图谱技术
\\end{{enumerate}}"""
    
    def _write_conclusion(self, title: str, research_data: Dict[str, Any]) -> str:
        """写作结论"""
        return f"""\\section{{{title}}}
本研究对{research_data['topic']}进行了全面的分析和总结。

\\subsection{{主要贡献}}
本研究的主要贡献包括：
\\begin{{itemize}}
    \\item 系统梳理了{research_data['topic']}的发展现状
    \\item 分析了该领域面临的主要挑战
    \\item 提出了未来发展的建议
\\end{{itemize}}

\\subsection{{未来展望}}
{research_data['topic']}作为人工智能的重要分支，具有巨大的发展潜力。未来研究应重点关注：
\\begin{{enumerate}}
    \\item 理论方法的创新和完善
    \\item 实际应用的拓展和深化
    \\item 技术标准的建立和规范
    \\item 伦理问题的探讨和解决
\\end{{enumerate}}

我们相信，随着研究的深入和技术的进步，{research_data['topic']}将在更多领域发挥重要作用，为人类社会的发展做出更大贡献。"""

class CoordinationAgent:
    """协调智能体 - 负责任务分配和流程管理"""
    
    def __init__(self, name: str = "Coordination Agent"):
        self.name = name
        self.agents = {}
        self.workflow_status = {}
    
    def register_agent(self, agent_type: str, agent: Any):
        """注册智能体"""
        self.agents[agent_type] = agent
        print(f"📝 {self.name} 注册了 {agent_type}: {agent.name}")
    
    def coordinate_paper_generation(self, topic: str, author: str = "AI Research Team") -> ResearchPaper:
        """协调论文生成流程"""
        print(f"🎯 {self.name} 开始协调论文生成: {topic}")
        
        # 1. 研究阶段
        research_agent = self.agents.get("research")
        if not research_agent:
            raise ValueError("研究智能体未注册")
        
        research_result = research_agent.conduct_research(topic)
        
        # 2. 写作阶段
        writing_agent = self.agents.get("writing")
        if not writing_agent:
            raise ValueError("写作智能体未注册")
        
        # 生成论文结构
        paper = ResearchPaper(
            title=topic,
            abstract=f"本研究对{topic}进行了深入分析，探讨了其发展现状、挑战和机遇。",
            sections=[],
            references=[],
            author=author,
            keywords=[topic, "人工智能", "研究进展"]
        )
        
        # 生成各个章节
        section_order = 1
        
        # 引言
        intro_content = writing_agent.write_section("引言", research_result, "introduction")
        paper.sections.append(PaperSection("引言", intro_content, section_order, "Writing Agent"))
        section_order += 1
        
        # 理论基础
        theory_content = writing_agent.write_section("理论基础", research_result, "general")
        paper.sections.append(PaperSection("理论基础", theory_content, section_order, "Writing Agent"))
        section_order += 1
        
        # 方法学
        method_content = writing_agent.write_section("方法学", research_result, "general")
        paper.sections.append(PaperSection("方法学", method_content, section_order, "Writing Agent"))
        section_order += 1
        
        # 应用案例
        application_content = writing_agent.write_section("应用案例", research_result, "general")
        paper.sections.append(PaperSection("应用案例", application_content, section_order, "Writing Agent"))
        section_order += 1
        
        # 挑战与展望
        challenge_content = writing_agent.write_section("挑战与展望", research_result, "general")
        paper.sections.append(PaperSection("挑战与展望", challenge_content, section_order, "Writing Agent"))
        section_order += 1
        
        # 结论
        conclusion_content = writing_agent.write_section("结论", research_result, "conclusion")
        paper.sections.append(PaperSection("结论", conclusion_content, section_order, "Writing Agent"))
        
        # 生成参考文献
        paper.references = [
            "@article{example2024,",
            "  title={Example Research Paper},",
            "  author={AI Research Team},",
            "  journal={AI Journal},",
            "  year={2024}",
            "}"
        ]
        
        print(f"✅ {self.name} 完成论文协调生成")
        return paper

class CompilationAgent:
    """编译智能体 - 负责LaTeX编译和PDF生成"""
    
    def __init__(self, name: str = "Compilation Agent"):
        self.name = name
    
    def compile_paper(self, paper: ResearchPaper, project_name: str = None) -> Dict[str, Any]:
        """编译论文为PDF"""
        print(f"🔨 {self.name} 开始编译论文: {paper.title}")
        
        if not project_name:
            project_name = paper.title.lower().replace(" ", "_").replace("：", "").replace("-", "_")
            project_name = f"{project_name}_paper"
        
        # 组合LaTeX内容
        content = ""
        for section in sorted(paper.sections, key=lambda x: x.order):
            content += section.content + "\n\n"
        
        # 组合参考文献
        references = "\n".join(paper.references)
        
        # 使用LaTeX编译器
        try:
            success, project_path, pdf_path = LaTeXProjectCompiler.auto_create_and_compile(
                project_name=project_name,
                content=content,
                references=references,
                title=paper.title,
                author=paper.author
            )
            
            if success:
                result = {
                    "status": "success",
                    "message": f"论文 '{paper.title}' 编译成功！",
                    "project_path": project_path,
                    "pdf_path": pdf_path,
                    "project_name": project_name
                }
                print(f"✅ {self.name} 编译成功: {pdf_path}")
            else:
                result = {
                    "status": "error",
                    "message": f"论文 '{paper.title}' 编译失败",
                    "project_path": project_path,
                    "error": "LaTeX编译失败"
                }
                print(f"❌ {self.name} 编译失败")
            
            return result
            
        except Exception as e:
            error_result = {
                "status": "error",
                "message": f"编译过程中发生错误: {str(e)}",
                "error_type": type(e).__name__
            }
            print(f"💥 {self.name} 编译错误: {e}")
            return error_result

class MultiAgentPaperSystem:
    """多智能体论文生成系统"""
    
    def __init__(self):
        """初始化多智能体系统"""
        self.coordinator = CoordinationAgent()
        self.research_agent = ResearchAgent()
        self.writing_agent = WritingAgent()
        self.compilation_agent = CompilationAgent()
        
        # 注册智能体
        self.coordinator.register_agent("research", self.research_agent)
        self.coordinator.register_agent("writing", self.writing_agent)
        self.coordinator.register_agent("compilation", self.compilation_agent)
        
        print("🚀 多智能体论文生成系统初始化完成！")
    
    def generate_paper(self, topic: str, author: str = "AI Research Team") -> Dict[str, Any]:
        """生成完整论文"""
        print(f"🎯 开始生成论文: {topic}")
        print("=" * 60)
        
        try:
            # 1. 协调生成论文内容
            paper = self.coordinator.coordinate_paper_generation(topic, author)
            
            # 2. 编译生成PDF
            compilation_result = self.compilation_agent.compile_paper(paper)
            
            # 3. 返回结果
            if compilation_result["status"] == "success":
                final_result = {
                    "status": "success",
                    "message": f"论文 '{topic}' 生成完成！",
                    "paper": {
                        "title": paper.title,
                        "author": paper.author,
                        "sections_count": len(paper.sections),
                        "abstract": paper.abstract
                    },
                    "compilation": compilation_result,
                    "workflow": "研究 → 写作 → 编译 → PDF生成"
                }
            else:
                final_result = {
                    "status": "partial_success",
                    "message": f"论文内容生成成功，但编译失败",
                    "paper": {
                        "title": paper.title,
                        "author": paper.author,
                        "sections_count": len(paper.sections),
                        "abstract": paper.abstract
                    },
                    "compilation": compilation_result,
                    "workflow": "研究 → 写作 → 编译失败"
                }
            
            print("=" * 60)
            print(f"🏁 论文生成流程完成！状态: {final_result['status']}")
            
            return final_result
            
        except Exception as e:
            error_result = {
                "status": "error",
                "message": f"论文生成过程中发生错误: {str(e)}",
                "error_type": type(e).__name__,
                "workflow": "流程中断"
            }
            print(f"💥 论文生成失败: {e}")
            return error_result

def main():
    """主函数 - 演示多智能体系统"""
    print("🧪 测试多智能体论文生成系统")
    print("=" * 60)
    
    # 创建系统
    system = MultiAgentPaperSystem()
    
    # 生成论文
    topic = "多智能体系统协作与协调"
    result = system.generate_paper(topic, "AI研究团队")
    
    # 显示结果
    print(f"\n📊 生成结果:")
    print(f"  状态: {result['status']}")
    print(f"  消息: {result['message']}")
    print(f"  工作流: {result['workflow']}")
    
    if result['status'] in ['success', 'partial_success']:
        paper_info = result['paper']
        print(f"  论文标题: {paper_info['title']}")
        print(f"  作者: {paper_info['author']}")
        print(f"  章节数量: {paper_info['sections_count']}")
    
    if result['status'] == 'success':
        compilation_info = result['compilation']
        print(f"  PDF路径: {compilation_info['pdf_path']}")
        print(f"  项目路径: {compilation_info['project_path']}")
    
    return result

if __name__ == "__main__":
    main()
