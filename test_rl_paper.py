#!/usr/bin/env python3
"""
Test script for creating reinforcement learning paper
"""

import os
import sys

print("🔍 诊断强化学习论文创建问题")
print("=" * 50)

# 检查当前目录
print(f"当前工作目录: {os.getcwd()}")

# 检查result目录
result_dir = "result"
if os.path.exists(result_dir):
    print(f"✅ result目录存在: {result_dir}")
    contents = os.listdir(result_dir)
    print(f"📁 result目录内容: {contents}")
else:
    print(f"❌ result目录不存在: {result_dir}")

# 尝试导入LaTeX编译器
try:
    sys.path.append('AgentScholar-UI/agent_scholar/tools/compose_tools')
    from latex_compiler import LaTeXProjectCompiler
    print("✅ 成功导入LaTeXProjectCompiler")
    
    # 尝试创建强化学习论文
    print("\n🚀 尝试创建强化学习论文...")
    
    content = """\\section{引言}
强化学习是机器学习的一个重要分支，专注于训练智能体通过与环境交互来学习最优策略。

\\section{核心概念}
\\subsection{智能体与环境}
在强化学习中，智能体通过采取行动并从环境获得奖励反馈来学习。

\\section{主要算法}
\\subsection{Q学习}
Q学习是一种无模型的强化学习算法，用于学习行动的价值函数。

\\section{应用领域}
强化学习已成功应用于游戏、机器人、自动驾驶等多个领域。

\\section{结论}
强化学习为自主决策系统提供了强大的理论基础。
"""

    references = """@article{sutton2018reinforcement,
  title={Reinforcement learning: An introduction},
  author={Sutton, Richard S and Barto, Andrew G},
  journal={MIT press},
  year={2018}
}"""

    success, project_path, pdf_path = LaTeXProjectCompiler.auto_create_and_compile(
        project_name='reinforcement_learning_paper',
        content=content,
        references=references,
        title='强化学习：理论与实践',
        author='AI研究团队'
    )
    
    if success:
        print(f"✅ 成功！PDF已生成在: {pdf_path}")
        print(f"📁 项目位置: {project_path}")
        
        # 检查文件是否真的存在
        if os.path.exists(pdf_path):
            size = os.path.getsize(pdf_path) / 1024
            print(f"📊 PDF文件大小: {size:.1f} KB")
        else:
            print("⚠️  PDF文件路径存在但文件不存在")
            
    else:
        print("❌ 编译失败")
        print(f"📁 项目位置: {project_path}")
        
except ImportError as e:
    print(f"❌ 导入LaTeXProjectCompiler失败: {e}")
except Exception as e:
    print(f"💥 创建论文时出错: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 50)
print("🏁 诊断完成")
