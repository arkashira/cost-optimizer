# Product Requirements Document (PRD)  
**Project:** cost-optimizer  
**Owner:** Senior Product/Engineering Lead  
**Date:** 2026‑06‑17  
**Status:** Draft → Review → Approved  

---  

## 1. Vision & Problem Statement  

B2C SaaS companies that embed generative‑AI features (e.g., chat, summarisation, image generation) face rapidly rising **variable costs per active user** due to per‑token or per‑call pricing from third‑party AI providers.  
These companies lack a unified, data‑driven way to:

1. **Identify** high‑cost usage patterns across their product fleet.  
2. **Optimize** prompts, model selection, and request batching to reduce token consumption without degrading user experience.  
3. **Replace** expensive API calls with cheaper alternatives (e.g., open‑source models, cached responses, rule‑based fallbacks).  

The result is **unpredictable margins**, higher churn risk, and limited ability to price competitively.  

**cost‑optimizer** will be a SaaS‑ready platform that ingests usage telemetry, applies AI‑aware optimization heuristics, and surfaces actionable recommendations and automated remediation pipelines.

---

## 2. Target Users & Personas  

| Persona | Role | Pain Points | Desired Outcome |
|---------|------|-------------|-----------------|
| **Product Manager (AI‑Feature)** | Defines AI‑driven product roadmaps | Unclear cost impact of new prompts; budget overruns | Real‑time cost visibility & ROI forecasts |
| **DevOps / Platform Engineer** | Operates cloud infra & API gateways | Manual, error‑prone throttling; scaling spikes | Automated throttling, batching, and fallback orchestration |
| **Data Scientist / Prompt Engineer** | Crafts prompts & model pipelines | High token usage for marginal quality gains | Prompt‑level cost‑quality analytics & optimization suggestions |
| **Finance Analyst (SaaS)** | Tracks unit economics | Variable cost per user fluctuates wildly | Predictable cost per user metric & cost‑saving recommendations |

---

## 3. Goals & Success Metrics  

| Goal | Success Metric | Target (12 mo) |
|------|----------------|----------------|
| **Reduce variable AI cost per active user** | Avg. cost/active‑user ↓ | 30 % reduction |
| **Increase cost‑visibility** | % of AI calls with cost tag | 100 % coverage |
| **Accelerate remediation** | Avg. time from alert → fix | < 4 h |
| **Adoption** | # of SaaS customers onboarded | 15 paying customers |
| **Revenue** | ARR from cost‑optimizer | $1.2 M |

---

## 4. Key Features (Prioritized)  

| Priority | Feature | Description | MVP Acceptance Criteria |
|----------|---------|-------------|--------------------------|
| **P1** | **Telemetry Ingestion Engine** | Securely collect per‑request data (model, tokens, latency, user‑id, feature flag) via SDKs & API gateway plugins. | • SDKs for Node, Python, Go.<br>• Data stored in PG + ClickHouse for analytics.<br>• 99 % data completeness in test env. |
| **P1** | **Cost Attribution Dashboard** | Visualize cost per feature, per model, per user segment; export CSV/JSON. | • Real‑time cost chart per day.<br>• Filters: model, region, user tier.<br>• Export works for last 90 days. |
| **P2** | **Prompt & Model Optimizer** | Apply heuristics (prompt trimming, temperature tuning, model downgrade) and suggest the cheapest model that meets a quality SLA. | • Generates at least one actionable suggestion for 80 % of high‑cost prompts.<br>• Quality regression < 5 % in A/B test. |
| **P2** | **Automated Remediation Engine** | Deploy selected optimizations automatically (e.g., switch model, enable caching, batch calls) via feature‑flag service. | • End‑to‑end test: change applied within 2 min of approval.<br>• Rollback capability. |
| **P3** | **Alternative Model Marketplace** | Catalog open‑source models (vLLM, SGLang) with cost‑vs‑quality benchmarks; enable one‑click switch. | • 5 curated models available.<br>• Cost comparison table auto‑generated. |
| **P3** | **Alerting & SLA Monitoring** | Configurable alerts (cost spikes, latency breaches) via webhook, Slack, email. | • Alert fires within 1 min of threshold breach.<br>• No false‑positive rate > 2 %. |
| **P4** | **Predictive Cost Forecasting** | Time‑series model (using existing `auto` dataset) to forecast next‑month AI spend under current usage patterns. | • Forecast error ≤ 10 % on held‑out data.<br>• UI shows confidence interval. |
| **P4** | **Compliance & Data Governance** | GDPR‑ready data handling, token‑level anonymisation, audit logs. | • All stored data encrypted at rest.<br>• Exportable audit log for 30 days. |

---

## 5. Scope  

### In‑Scope  
- End‑to‑end data pipeline from SDK → storage → analytics.  
- Core dashboard & alerting UI (React + Tailwind).  
- Integration with existing Axentx BRAIN for model benchmarking.  
- Automated remediation via feature‑flag service (LaunchDarkly‑compatible).  
- Initial marketplace of 5 open‑source models (vLLM, SGLang).  

### Out‑of‑Scope (Phase 2+)  
- Direct billing integration with AI providers.  
- Multi‑cloud cost‑allocation (focus on AWS/GCP first).  
- Advanced ML‑driven prompt rewriting (beyond heuristic trimming).  
- White‑label SaaS offering (initially a single‑tenant product).  

---

## 6. Assumptions & Dependencies  

| Assumption | Impact if Invalid |
|------------|-------------------|
| SaaS customers can instrument SDKs with < 5 ms overhead. | May need lighter‑weight agents or server‑side injection. |
| Third‑party AI providers expose per‑token pricing via API. | Will fallback to manual pricing tables. |
| Existing Axentx BRAIN contains up‑to‑date model performance data. | Need to ingest fresh benchmark data. |
| Customers have a feature‑flag system compatible with our remediation API. | Provide a minimal built‑in flag service as fallback. |

**Dependencies**  
- **vLLM** and **SGLang** repos (verified frameworks) for open‑source model serving.  
- Axentx BRAIN vector store for similarity search of prompts & cost patterns.  
- Cloud data warehouse (ClickHouse) for high‑throughput analytics.  

---

## 7. Milestones & Timeline  

| Milestone | Deliverable | Owner | Target Date |
|-----------|-------------|-------|-------------|
| **M1 – Foundations** | SDKs, ingestion pipeline, raw storage | Backend Team | 2026‑07‑15 |
| **M2 – Visibility** | Cost dashboard, basic alerts | Frontend & Ops | 2026‑08‑30 |
| **M3 – Optimization Loop** | Prompt optimizer, remediation engine | ML & Platform | 2026‑10‑15 |
| **M4 – Marketplace** | Open‑source model catalog, one‑click switch | Product & Infra | 2026‑11‑30 |
| **M5 – Beta Launch** | 5 pilot SaaS customers onboarded, feedback loop | PM/Customer Success | 2026‑12‑20 |
| **M6 – GA Release** | Full product, SLA monitoring, forecasting | All | 2027‑02‑15 |

---

## 8. Risks & Mitigations  

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Low adoption due to integration effort | Medium | High | Provide pre‑built SDKs & auto‑discovery agents; offer professional services for onboarding. |
| Inaccurate cost attribution (missing tokens) | Low | Medium | Validate SDKs against known API logs; implement checksum verification. |
| Model quality regression after downgrade | Medium | High | Enforce quality SLA thresholds; A/B testing before auto‑apply. |
| Data privacy breach (token leakage) | Low | Critical | Token‑level hashing, encryption at rest, strict IAM policies. |
| Vendor lock‑in to a single cloud | Low | Medium | Abstract storage layer; support both AWS and GCP in v1. |

---

## 9. Acceptance Criteria (Definition of Done)

- All P1 features are production‑ready, documented, and covered by unit + integration tests (≥ 80 % coverage).  
- End‑to‑end latency from request to cost tag ≤ 50 ms.  
- Security audit completed (OWASP Top 10) with no critical findings.  
- Pilot customers report ≥ 20 % cost reduction within 30 days of activation.  
- Documentation (README, SDK guides, API spec) published in the `cost-optimizer` repo.  

---  

*Prepared by the product/engineering lead. Reviewers: PM, CTO, Security Lead.*
