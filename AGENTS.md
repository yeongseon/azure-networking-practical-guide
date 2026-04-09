# AGENTS.md

Guidance for AI agents working in this repository.

## Project Overview

**Azure Networking Practical Guide** — a documentation hub for designing, operating, and troubleshooting Azure networking — VNet, subnet, NSG, DNS, routing, private connectivity, and hybrid networking.

- **Live site**: <https://yeongseon.github.io/azure-networking-practical-guide/>
- **Repository**: <https://github.com/yeongseon/azure-networking-practical-guide>

## Repository Structure

```text
.
├── .github/
│   └── workflows/              # GitHub Pages deployment
├── docs/
│   ├── assets/                 # Images, icons
│   ├── best-practices/         # Production patterns and anti-patterns
│   ├── javascripts/            # Mermaid zoom JS
│   ├── operations/             # Day-2 operational execution
│   ├── platform/               # Architecture and design decisions
│   ├── reference/              # CLI cheatsheet, decision guides
│   ├── start-here/             # Overview, learning paths
│   ├── stylesheets/            # Custom CSS
│   └── troubleshooting/        # Diagnosis and resolution
└── mkdocs.yml                  # MkDocs Material configuration
```

## Content Categories

| Section | Purpose |
|---|---|
| **Start Here** | Entry points, learning paths, overview |
| **Platform** | Architecture, design decisions — WHAT and HOW it works |
| **Best Practices** | Production patterns — HOW to use the platform well |
| **Operations** | Day-2 execution — HOW to run in production |
| **Troubleshooting** | Diagnosis and resolution |
| **Reference** | Quick lookup — CLI, decision guides |

## Documentation Conventions

### File Naming

- All files: `topic-name.md` (kebab-case)
- Index files: `index.md` in each directory

### CLI Command Style

```bash
# ALWAYS use long flags for readability
az network vnet create --resource-group $RG --name $VNET_NAME --location $LOCATION

# NEVER use short flags in documentation
az network vnet create -g $RG -n $VNET_NAME  # ❌ Don't do this
```

### Variable Naming Convention

| Variable | Description | Example |
|----------|-------------|---------|
| `$RG` | Resource group name | `rg-networking-demo` |
| `$VNET_NAME` | Virtual network name | `vnet-hub-001` |
| `$SUBNET_NAME` | Subnet name | `snet-app-001` |
| `$NSG_NAME` | Network security group | `nsg-app-001` |
| `$LOCATION` | Azure region | `koreacentral` |
| `$SUBSCRIPTION_ID` | Subscription identifier placeholder | `<subscription-id>` |

### PII Removal (Quality Gate)

**CRITICAL**: All CLI output examples MUST have PII removed.

**Must mask (real Azure identifiers):**

- Subscription IDs: `<subscription-id>`
- Tenant IDs: `<tenant-id>`
- Object IDs: `<object-id>`
- Resource IDs containing real subscription/tenant
- Emails: Remove or mask as `user@example.com`
- IP addresses: Use RFC 5737 ranges (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24)
- Secrets/Tokens: NEVER include

**OK to keep (synthetic example values):**

- Demo correlation IDs: `a1b2c3d4-e5f6-7890-abcd-ef1234567890`
- Example request IDs in logs
- Placeholder domains: `example.com`, `contoso.com`
- Sample resource names used consistently in docs

The goal is to prevent leaking **real Azure account information**, not to mask obviously-fake example values that aid readability.

### Admonition Indentation Rule

For MkDocs admonitions (`!!!` / `???`), every line in the body must be indented by **4 spaces**.

```markdown
!!! warning "Important"
    This line is correctly indented.

    - List item also inside
```

### Mermaid Diagrams

All architectural diagrams use Mermaid. Every documentation page should include at least one diagram. Test with `mkdocs build --strict`.

### Nested List Indentation

All nested list items MUST use **4-space indent** (Python-Markdown standard).

### Tail Section Naming

Every document ends with these tail sections (in this order):

| Section | Purpose | Content |
|---|---|---|
| `## See Also` | Internal cross-links within this repository | Links to other pages in this guide |
| `## Sources` | External authoritative references | Links to Microsoft Learn (primary) |

- `## See Also` is required on every page.
- `## Sources` is required when external references are cited.
- Order is always `## See Also` → `## Sources` (never reversed).

### Canonical Document Templates

#### Platform docs

```text
# Title
Brief introduction (1-2 sentences)
## Main Content
### Subsections
## See Also
## Sources
```

#### Best Practices docs

```text
# Title
Brief introduction
## Why This Matters
## Recommended Practices
## Common Mistakes / Anti-Patterns
## Validation Checklist
## See Also
## Sources
```

#### Operations docs

```text
# Title
Brief introduction
## Prerequisites
## When to Use
## Procedure
## Verification
## Rollback / Troubleshooting
## See Also
## Sources
```

#### Troubleshooting docs

```text
# Title
## Symptom
## Possible Causes
## Diagnosis Steps
## Resolution
## Prevention
## See Also
## Sources
```

#### Reference docs

```text
# Title
Brief introduction
## Topic/Command Groups
## Usage Notes
## See Also
## Sources
```

## Build & Preview

```bash
# Install MkDocs dependencies
pip install mkdocs-material mkdocs-minify-plugin

# Build documentation (strict mode catches broken links)
mkdocs build --strict

# Local preview
mkdocs serve
```

## Git Commit Style

```text
type: short description
```

Allowed types: `feat`, `fix`, `docs`, `chore`, `refactor`

## Related Projects

| Repository | Description |
|---|---|
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service practical guide |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions practical guide |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps practical guide |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring practical guide |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage practical guide |
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines practical guide |

## Tutorial Validation Tracking

Every tutorial document supports **validation frontmatter** that records when and how it was last tested against a real deployment.

### Frontmatter Schema

Add a `validation` block inside the YAML frontmatter (`---` fences) of any tutorial file:

```yaml
---
hide:
  - toc
validation:
  az_cli:
    last_tested: 2026-04-09
    cli_version: "2.83.0"
    result: pass
  bicep:
    last_tested: null
    result: not_tested
---
```

### Agent Rules for Validation

1. **After deploying a tutorial end-to-end**, add or update the `validation` frontmatter with the current date, CLI version, and `result: pass`.
2. **If a tutorial step fails during validation**, set `result: fail` and note the issue.
3. **Never fabricate validation dates.**
4. **After updating frontmatter**, regenerate the dashboard:
    ```bash
    python3 scripts/generate_validation_status.py
    ```
5. **Include the regenerated dashboard** (`docs/reference/validation-status.md`) in the same commit.
6. **Do not manually edit** `docs/reference/validation-status.md` — it is auto-generated.
