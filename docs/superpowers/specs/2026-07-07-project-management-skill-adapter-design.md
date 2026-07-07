# Project-management skill adapter

## Goal

Make the imported project-management bundle discoverable and useful to the existing `.codex/agents/project-manager.toml` agent without retaining a second Claude-specific command or agent system.

## Design

- Add `.agents/skills/project-management/SKILL.md` as the single Codex entry point.
- Route Hatch Restore 2 planning through `restore2-orchestration` and repository governance first.
- Load at most one nested PM specialty when a task specifically needs portfolio, Scrum, Jira, Confluence, Atlassian, meeting, template, or communication expertise.
- Keep the 15 stdlib Python tools and their required references/assets.
- Update `project-manager.toml` to require the adapter for planning and delivery-management work.
- Do not treat bundled Atlassian configuration as active unless a compatible connector is available and explicitly needed.

## Remove

Remove redundant imported packaging and Claude-specific surfaces:

- Claude command definitions under `commands/`;
- the imported Claude agent under `agents/`;
- `.mcp.json` and obsolete `.codex/instructions.md` bootstrap files;
- imported overview, installation, implementation-summary, and scenario documents that duplicate skill content;
- `.DS_Store` metadata.

Nested `SKILL.md` files remain as progressively loaded references. Claude wording inside a retained specialty is corrected only when it changes runtime behavior or points to a removed path.

## Validation

- The adapter has valid skill frontmatter and resolves every referenced local path.
- `project_manager` explicitly invokes the adapter.
- No Claude command, Claude agent, missing sibling-repository, or removed bootstrap path remains reachable from the adapter.
- All retained Python files compile and all 15 tools return successful `--help`.
- Existing Git, hardware, protocol-evidence, and publication boundaries remain unchanged.
