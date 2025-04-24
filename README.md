# RAG AI Specialist

An AI-driven specialist designed to assist assessors in NIST SP 800-171 compliance audits. This Retrieval-Augmented Generation (RAG) agent provides:

- **Controlled Unclassified Information (CUI) protection**: No raw CUI is stored in the vector index or on-chain—only hashed pointers.
- **NIST 800-171 expertise**: Pre-loaded catalog of ~90 controls with metadata and mappings to code modules.
- **Tamper-evident audit ledger**: Permissioned blockchain for event logging (ingest, query, feedback, roll-ups).
- **Vector store**: Sanitized embeddings with periodic memory optimization (clustering & summarization).
- **Configurable agent personality & memory**: External YAML configurations for persona, memory policies, behaviors.
- **Plugin system**: Easily add custom audits (e.g., SSH config checks, Windows registry audits).
- **Federated learning & sharing**: Secure pub/sub network to exchange summaries, embeddings, and plugin manifests.

---
## Architecture Overview

```
rag-ai-specialist/
├── config/
│   ├── default.yaml            # Base settings (endpoints, thresholds)
│   ├── agent/
│   │   ├── persona.yaml
│   │   ├── memory_policy.yaml
│   │   └── behaviors/
│   │       ├── nist-800-171.yaml
│   │       └── rag-settings.yaml
│   └── plugins.yaml
├── docs/
│   ├── index.md                # GitHub Pages site
│   └── nist-800-171/
│       ├── controls.yaml
│       └── control-mapping.xlsx
├── src/
│   ├── __main__.py
│   ├── compliance/
│   │   ├── controls.py
│   │   └── policies/
│   ├── plugins/
│   │   ├── base.py
│   │   └── plugin_manager.py
│   ├── config/
│   │   ├── manager.py
│   │   └── retrieval_adapter.py
│   ├── network/
│   │   ├── peer_manager.py
│   │   └── broker_client.py
│   └── ingest/, embed/, retrieve/, generate/, api/, ui/
├── tests/
├── scripts/
│   └── optimize_memory.sh
├── .github/
│   └── workflows/
└── Dockerfile, docker-compose.yml
```
