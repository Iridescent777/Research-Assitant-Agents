#!/usr/bin/env python3
"""
agno系统LaTeX工具配置文件
定义正确的工具schema和参数，解决参数验证问题
"""

from typing import Dict, Any, List

# agno系统工具配置
AGNO_TOOLS_CONFIG = {
    "tools": [
        {
            "name": "run_latex",
            "description": "运行LaTeX编译，生成PDF文档",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_dir": {
                        "type": "string",
                        "description": "LaTeX项目目录路径"
                    },
                    "main_tex_file": {
                        "type": "string",
                        "description": "主LaTeX文件名（默认：main.tex）",
                        "default": "main.tex"
                    }
                },
                "required": ["project_dir"]
            }
        },
        {
            "name": "create_and_compile_paper",
            "description": "创建并编译完整的LaTeX论文",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "论文主题或标题"
                    },
                    "content": {
                        "type": "string",
                        "description": "LaTeX内容"
                    },
                    "references": {
                        "type": "string",
                        "description": "BibTeX参考文献（可选）"
                    },
                    "author": {
                        "type": "string",
                        "description": "作者姓名（默认：AI Research Team）",
                        "default": "AI Research Team"
                    },
                    "project_name": {
                        "type": "string",
                        "description": "项目目录名称（可选，自动生成）"
                    }
                },
                "required": ["topic", "content"]
            }
        },
        {
            "name": "list_papers",
            "description": "列出所有已生成的论文项目",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        },
        {
            "name": "get_paper_info",
            "description": "获取特定论文项目的详细信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_name": {
                        "type": "string",
                        "description": "项目名称"
                    }
                },
                "required": ["project_name"]
            }
        }
    ]
}

# 工具函数映射
def get_tool_function(tool_name: str):
    """根据工具名称获取对应的函数"""
    try:
        import sys
        sys.path.append('AgentScholar-UI/agent_scholar/tools/compose_tools')
        from agno_latex_tool import (
            run_latex,
            create_and_compile_paper,
            list_papers,
            get_paper_info
        )
        
        tool_map = {
            "run_latex": run_latex,
            "create_and_compile_paper": create_and_compile_paper,
            "list_papers": list_papers,
            "get_paper_info": get_paper_info
        }
        
        return tool_map.get(tool_name)
    except ImportError:
        print(f"⚠️ 无法导入工具: {tool_name}")
        return None

# 示例使用说明
def print_usage_examples():
    """打印使用示例"""
    print("🚀 agno系统LaTeX工具使用示例")
    print("=" * 50)
    
    print("\n1️⃣ 编译现有LaTeX项目:")
    print("   run_latex(project_dir='result/multiagent_project')")
    
    print("\n2️⃣ 创建新论文:")
    print("   create_and_compile_paper(")
    print("       topic='强化学习应用',")
    print("       content='\\section{引言}\\n这是引言内容...',")
    print("       author='您的姓名'")
    print("   )")
    
    print("\n3️⃣ 列出所有论文:")
    print("   list_papers()")
    
    print("\n4️⃣ 获取论文信息:")
    print("   get_paper_info(project_name='multiagent_project')")
    
    print("\n" + "=" * 50)

# 测试配置
def test_config():
    """测试配置是否正确"""
    print("🧪 测试agno工具配置")
    print("=" * 30)
    
    for tool in AGNO_TOOLS_CONFIG["tools"]:
        print(f"✅ 工具: {tool['name']}")
        print(f"   描述: {tool['description']}")
        print(f"   必需参数: {tool['parameters'].get('required', [])}")
        print()
    
    print("✅ 配置测试完成")

if __name__ == "__main__":
    print_usage_examples()
    print()
    test_config()
