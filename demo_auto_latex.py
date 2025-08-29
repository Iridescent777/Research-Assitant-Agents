#!/usr/bin/env python3
"""
Demo script for automated LaTeX compilation
This script demonstrates the auto_create_and_compile functionality
"""

import sys
import os

# Add the agent_scholar tools to the path
sys.path.append('AgentScholar-UI/agent_scholar/tools/compose_tools')

from latex_compiler import LaTeXProjectCompiler

def main():
    print("🚀 Automated LaTeX Compilation Demo")
    print("=" * 50)
    
    # Test content for reinforcement learning paper
    content = """\\section{Introduction}
Reinforcement learning (RL) is a subfield of machine learning that focuses on training agents to make sequential decisions in an environment to maximize cumulative rewards.

\\section{Core Concepts}
\\subsection{Agent and Environment}
In reinforcement learning, an agent interacts with an environment by taking actions and receiving feedback in the form of rewards or penalties.

\\section{Conclusion}
Reinforcement learning represents a powerful paradigm for autonomous decision-making systems.
"""
    
    # Test references
    references = """@article{sutton2018reinforcement,
  title={Reinforcement learning: An introduction},
  author={Sutton, Richard S and Barto, Andrew G},
  journal={MIT press},
  year={2018}
}"""
    
    print("📝 Creating reinforcement learning paper...")
    
    try:
        # Use the automated compilation method
        success, project_path, pdf_path = LaTeXProjectCompiler.auto_create_and_compile(
            project_name='reinforcement_learning_demo',
            content=content,
            references=references,
            title='Reinforcement Learning: A Comprehensive Overview',
            author='AI Research Team'
        )
        
        if success:
            print(f"✅ SUCCESS! PDF generated at: {pdf_path}")
            print(f"📁 Project location: {project_path}")
            
            # Check if PDF exists and get its size
            if os.path.exists(pdf_path):
                size = os.path.getsize(pdf_path) / 1024
                print(f"📊 PDF file size: {size:.1f} KB")
            else:
                print("⚠️  PDF file not found at expected location")
        else:
            print("❌ Compilation failed")
            print(f"📁 Project location: {project_path}")
            
    except Exception as e:
        print(f"💥 Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
