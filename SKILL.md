# Skill: Nexus-Brain (V1.0) - AI Orchestrator

Nexus-Brain connects the local SRE monitoring (**Nexus-Safe**) with the advanced reasoning of **OpenCode** (via Codex Iliad).

## 🧠 Intelligent Workflow
Instead of simple procedural restarts, Nexus-Brain follows this logic:
1. **Detection**: `monitor.py` identifies a service failure.
2. **Analysis**: The Agent extracts the last 100 lines of logs.
3. **Reasoning**: The Agent calls OpenCode with the logs: `opencode run "Analyze these logs and suggest a fix: [LOGS]"`
4. **Action**: 
   - If it's an **infrastructure** issue (DB down), the Agent performs a controlled restart.
   - If it's a **code** issue, the Agent reports the exact cause and fix proposed by OpenCode/Codex.

## 🚀 Commands
- **/nexus-brain check** : Run a full diagnostic using OpenCode for any non-healthy service.
- **/nexus-brain reason <service>** : Force an AI analysis of a specific service's logs.

## ⚙️ Configuration
Uses local `opencode` binary and configuration.
