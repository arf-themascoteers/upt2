# ML + GIS Learning Journey

**Current position: Step 1a (as of 2026-05-10)**

## Phase 0 — Hello World with local LLMs
- 0a. Run Ollama locally — pull a model, query it from terminal  ✓
- 0b. Query Ollama from Python — understand the API  ✓
- 0c. Build a minimal chatbot (CLI, no UI) using Ollama  ✓
- 0d. Add memory/context to the chatbot (conversation history)  ✓

## Phase 1 — Customization and fine-tuning
- 1a. Fine-tune or prompt-engineer a model on custom text data (includes LoRA)  ← CURRENT
- 1b. Feed structured data (MySQL) into a model pipeline
- 1c. Feed GIS data (shapefiles) — understand spatial-to-text conversion
- 1d. Fine-tune a pretrained geospatial vision model (Prithvi-EO-2.0 + LoRA) on wetland data (Sentinel-2 + aerial RGB, binary water classification)
- 1e. Train a small model from scratch (tiny transformer on custom text)

## Phase 2 — ChatWimmera (QGIS plugin with chat UI)
- 2a. Build a QGIS plugin (hello world level)
- 2b. Embed a chat UI into QGIS
- 2c. Connect the chat to a local LLM — ChatWimmera MVP
- 2d. Ground answers in Wimmera datasets (RAG pattern with vector database)

## Phase 3 — MLOps on Azure/AWS
- 3a. Deploy a model pipeline on Azure or AWS
- 3b. Add monitoring, versioning — MLOps basics
- 3c. Expose model via MCP (Model Context Protocol) for tool/agent integration

## Phase 4 — OpenClaw
- 4a. Iterate toward OpenClaw — open-source Claude-like assistant
