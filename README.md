# Distributed File Synchronization System (Dropbox-lite)

A lightweight distributed file synchronization system that demonstrates 
**consistency, replication, and fault tolerance** concepts from distributed systems.

---

## Features (Phase 1 - MVP)
- Upload and download files via CLI client
- File versioning (latest + history)
- Basic consistency (last-writer-wins)
- Metadata stored in SQLite/Postgres
- Unit tests & CI pipeline

---

## Planned Features (Phase 2)
- Multi-node replication with leader election
- Conflict resolution (CRDTs, vector clocks)
- Eventual vs strong consistency modes
- Web dashboard for monitoring sync
- Metrics + observability (Prometheus, Grafana)

---

## Project Structure
- client/ # CLI client
- server/ # Server API
- docs/ # Architecture & design
- demo/ # Demo scripts
- tests/ # Automated tests

---

## Quick Start
```bash
# Clone repo
git clone https://github.com/soumadip/sdb-distributed-sync.git
cd distributed-sync

# Install dependencies
pip install -r requirements.txt

# Start server
python server/main.py

# In another terminal, run client
python client/main.py upload sample.txt
python client/main.py download sample.txt
```

---

## System Architecture
![Architecture Diagram](docs/diagrams/architecture.png)

---

## Demo
![Demo](docs/demo.gif)

You can try the CLI by cloning the repo:
```bash
git clone https://github.com/soumadip/sdb-distributed-sync.git
cd distributed-sync
pip install -r requirements.txt
python server/server.py
python client/client.py upload demo/sample.txt
```

## Roadmap
- [x] Single-node file sync
- [ ] Multi-replica setup with leader election
- [ ] Eventual vs strong consistency demo
- [ ] Web dashboard (React + FastAPI)
- [ ] Observability (Prometheus/Grafana)

---

## Tests
```bash
pytest tests/
```

---

## Tech Stack
- **Python** (FastAPI for server, CLI client)
- **SQLite** (metadata storage)
- **GitHub Actions** (CI/CD)
- **GitHub Pages** (project showcase)

---

## Live Showcase
👉 Visit the [Project Page](https://soumadip.github.io/sdb-distributed-sync/)  
(to be set up with GitHub Pages)

---

## Contributing
PRs welcome! Ideas for conflict resolution strategies or CRDT integration are highly appreciated.

---

## License
MIT License © 2025 SOUMADIP BISWAS

