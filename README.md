# RAG AI Specialist

An open-source Retrieval-Augmented Generation (RAG) agent designed to assist assessors with NIST SP 800-171 compliance audits. It combines a tamper-evident event ledger, a sanitized vector store, and a plugin architecture—while never storing raw CUI in its index.

---

## 🚀 Key Features

- **CUI Protection**  
  No raw Controlled Unclassified Information (CUI) is ever indexed or written to chain—only salted hashes and pointers.

- **NIST 800-171 Expertise**  
  Pre-loaded catalog of ~90 controls (`docs/nist-800-171/controls.yaml`) with direct mappings to your code modules (`control-mapping.xlsx`).

- **Audit Ledger**  
  Permissioned blockchain for every ingest, query, feedback, and roll-up event—fulfills tamper-evidence requirements (e.g. AU-9).

- **Vector Store**  
  Sanitized embeddings + a weekly “memory optimizer” that clusters, summarizes, and prunes to avoid bloat.

- **Configurable Agent**  
  External YAML for persona, memory policies, and behavior rules—loaded “just-in-time” to keep your token window lean.

- **Plugin System**  
  Drop-in audit modules (SSH config checks, registry audits, custom controls). Write one class, register in `config/plugins.yaml`, and you’re live.

- **Federated Sharing**  
  Secure pub/sub over MQTT (or Kafka) for agents to exchange summaries, embedding pointers, and plugin manifests—no CUI ever crosses the wire.

---

## 📂 Repository Layout

```
rag-ai-specialist/
├── config/
│   ├── default.yaml              # Base endpoints, thresholds, etc.
│   ├── production.yaml           # Hardened, encrypted secrets
│   ├── agent/
│   │   ├── persona.yaml          # Agent identity & tone
│   │   ├── memory_policy.yaml    # Retention & summarization rules
│   │   └── behaviors/
│   │       ├── nist-800-171.yaml # Control→guidance mappings
│   │       └── rag-settings.yaml # Chunk sizes, retrieval params
│   └── plugins.yaml              # Enabled audit plugins
│   └── network.yaml              # Broker URLs, topics, cert paths
│
├── docs/
│   ├── index.md                  # GitHub Pages site
│   └── nist-800-171/
│       ├── controls.yaml         # Master list of controls
│   └   └── control-mapping.xlsx  # Control→code mapping
│
├── src/
│   ├── __main__.py               # FastAPI / CLI entry point
│   ├── ingest/                   # Data ingestion pipelines
│   ├── embed/                    # Embedding logic
│   ├── store/                    # Vector store integration
│   ├── retrieve/                 # Retrieval & query modules
│   ├── generate/                 # LLM prompt & generation logic
│   ├── api/                      # REST endpoints
│   ├── ui/                       # Optional web/chat UI
│   ├── compliance/
│   │   ├── controls.py           # Load & query NIST controls
│   │   └── ledger.py             # Blockchain event logger
│   ├── config/
│   │   ├── manager.py            # JIT config loader & summarizer
│   │   └── retrieval_adapter.py  # Config vector retrieval
│   ├── plugins/
│   │   ├── base.py               # PluginBase interface
│   │   └── plugin_manager.py     # Discover & load plugins
│   ├── network/
│   │   ├── peer_manager.py       # Peer discovery & auth
│   │   └── broker_client.py      # Pub/sub wrapper
│   └── memory_optimizer.py       # Clustering & summarization job
│
├── tests/                        # Unit & integration tests
├── scripts/
│   └── optimize_memory.sh        # Cron job wrapper
│
├── .github/
│   └── workflows/
│       ├── ci.yml                # Lint, test & scan
│       └── cd.yml                # Build & deploy
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── LICENSE
```

## ⚙️ Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/CptNope/rag-ai-specialist.git
   cd rag-ai-specialist
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure**  
   - Copy `config/default.yaml` → `config/production.yaml`, secure secrets via environment or vault.  
   - Edit `config/agent/*.yaml` and `config/plugins.yaml` to suit your needs.  
   - Populate `docs/nist-800-171/controls.yaml` if you’ve custom controls.

4. **Launch containers**  
   ```bash
   docker-compose up -d
   ```

## 🚀 Usage

- **Ingest data**  
  ```bash
  python src/ingest/fetcher.py --source /path/to/documents
  ```
- **Start the API**  
  ```bash
  python src/__main__.py
  ```
- **Query the agent**  
  ```bash
  curl -X POST http://localhost:8000/api/query \
    -H "Content-Type: application/json" \
    -d '{"query":"Show me AC 3.1.1 implementation status."}'
  ```

## ✅ Compliance & Auditing

- **Control catalog:** `docs/nist-800-171/controls.yaml`  
- **Mapping sheet:** `docs/nist-800-171/control-mapping.xlsx`  
- **Ledger:** `src/compliance/ledger.py` logs every action on-chain.  
- **Memory optimizer:** Weekly summarization and prune job (`scripts/optimize_memory.sh`).

## 🔌 Plugins

1. Create a new class in `src/plugins/` inheriting from `PluginBase`.  
2. Implement `run(self, target: dict) -> dict`.  
3. Register it in `config/plugins.yaml`.  
4. Restart the service—your new audit is live.

## 🌐 Federation & Sharing

Configure `config/network.yaml`:

```yaml
broker:
  url: "mqtts://broker.example.com:8883"
  cert: "certs/agent.crt"
  key:  "certs/agent.key"
topics:
  events:     "rag-ai/events"
  embeddings: "rag-ai/embeddings"
  plugins:    "rag-ai/plugins"
```

Agents will publish/subscribe to share sanitized summaries, embedding pointers, and plugin manifests—never raw CUI.

## 🤝 Contributing

1. Fork the repository.  
2. Create your feature branch.  
3. Write tests in `tests/`.  
4. Submit a pull request.  

Please review `docs/nist-800-171/README.md` for compliance guidance before contributing any new features.

## 📄 License

MIT © 2025 CptNope
