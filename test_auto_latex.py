#!/usr/bin/env python3
"""
Test script for automated LaTeX compilation
This script demonstrates how to use the LaTeXProjectCompiler.auto_create_and_compile method
to automatically create a LaTeX project and generate a PDF.
"""

import sys
import os

# Add the agent_scholar tools to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'AgentScholar-UI', 'agent_scholar', 'tools', 'compose_tools'))

from latex_compiler import LaTeXProjectCompiler

def test_reinforcement_learning_paper():
    """Test creating a reinforcement learning paper automatically."""
    
    # Define the project details
    project_name = "reinforcement_learning_paper"
    title = "Reinforcement Learning: A Comprehensive Overview"
    author = "AI Research Team"
    
    # Define the LaTeX content
    content = """
\\section{Introduction}
Reinforcement learning (RL) is a subfield of machine learning that focuses on training agents to make sequential decisions in an environment to maximize cumulative rewards. This approach has gained significant attention due to its success in various domains, including game playing, robotics, and autonomous systems.

\\section{Core Concepts}
\\subsection{Agent and Environment}
In reinforcement learning, an agent interacts with an environment by taking actions and receiving feedback in the form of rewards or penalties. The goal is to learn an optimal policy that maximizes the expected cumulative reward over time.

\\subsection{Markov Decision Process}
Reinforcement learning problems are typically modeled as Markov Decision Processes (MDPs), which consist of:
\\begin{itemize}
    \\item States: The current situation of the environment
    \\item Actions: Available choices for the agent
    \\item Transitions: How the environment changes based on actions
    \\item Rewards: Feedback signals for the agent's behavior
\\end{itemize}

\\section{Key Algorithms}
\\subsection{Q-Learning}
Q-learning is a model-free reinforcement learning algorithm that learns the quality of actions, telling an agent what action to take under what circumstances.

\\subsection{Deep Q-Networks (DQN)}
DQN combines Q-learning with deep neural networks, enabling the application of reinforcement learning to high-dimensional state spaces.

\\subsection{Policy Gradient Methods}
Policy gradient methods directly optimize the policy function, making them suitable for continuous action spaces and complex environments.

\\section{Applications}
Reinforcement learning has been successfully applied to:
\\begin{itemize}
    \\item Game playing (AlphaGo, AlphaStar)
    \\item Robotics and autonomous systems
    \\item Recommendation systems
    \\item Financial trading
    \\item Healthcare and drug discovery
\\end{itemize}

\\section{Challenges and Future Directions}
Despite significant progress, reinforcement learning faces several challenges:
\\begin{itemize}
    \\item Sample efficiency and exploration
    \\item Safety and robustness
    \\item Multi-agent coordination
    \\item Transfer learning and generalization
\\end{itemize}

\\section{Conclusion}
Reinforcement learning represents a powerful paradigm for autonomous decision-making systems. As research continues to address current limitations, we can expect broader adoption and more sophisticated applications across various domains.
"""
    
    # Define references (optional)
    references = """@article{sutton2018reinforcement,
  title={Reinforcement learning: An introduction},
  author={Sutton, Richard S and Barto, Andrew G},
  journal={MIT press},
  year={2018}
}

@article{mnih2015human,
  title={Human-level control through deep reinforcement learning},
  author={Mnih, Volodymyr and Kavukcuoglu, Koray and Silver, David and Rusu, Andrei A and Veness, Joel and Bellemare, Marc G and Graves, Alex and Riedmiller, Martin and Fidjeland, Andreas K and Ostrovski, Georg and others},
  journal={nature},
  volume={518},
  number={7540},
  pages={529--533},
  year={2015},
  publisher={Nature Publishing Group}
}

@article{schulman2017proximal,
  title={Proximal policy optimization algorithms},
  author={Schulman, John and Wolski, Filip and Dhariwal, Prafulla and Radford, Alec and Klimov, Oleg},
  journal={arXiv preprint arXiv:1707.06347},
  year={2017}
}"""
    
    print(f"🚀 Starting automated LaTeX compilation for: {title}")
    print(f"📁 Project directory: result/{project_name}")
    print(f"👤 Author: {author}")
    print("=" * 60)
    
    try:
        # Use the automated compilation method
        success, project_path, pdf_path = LaTeXProjectCompiler.auto_create_and_compile(
            project_name=project_name,
            content=content,
            references=references,
            base_dir="result",
            title=title,
            author=author
        )
        
        if success:
            print("✅ SUCCESS! LaTeX paper automatically created and compiled!")
            print(f"📁 Project location: {project_path}")
            print(f"📄 PDF generated at: {pdf_path}")
            print(f"📊 File size: {os.path.getsize(pdf_path) / 1024:.1f} KB")
            
            # List all generated files
            print("\n📋 Generated files:")
            for file in os.listdir(project_path):
                file_path = os.path.join(project_path, file)
                if os.path.isfile(file_path):
                    size = os.path.getsize(file_path) / 1024
                    print(f"   - {file} ({size:.1f} KB)")
                else:
                    print(f"   - {file}/ (directory)")
                    
        else:
            print("❌ FAILED! LaTeX compilation was unsuccessful.")
            print(f"📁 Project location: {project_path}")
            if pdf_path:
                print(f"📄 PDF path: {pdf_path}")
            
    except Exception as e:
        print(f"💥 ERROR during automated compilation: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🔧 Testing Automated LaTeX Compilation System")
    print("=" * 60)
    
    # Test the reinforcement learning paper creation
    test_reinforcement_learning_paper()
    
    print("\n" + "=" * 60)
    print("�� Test completed!")
