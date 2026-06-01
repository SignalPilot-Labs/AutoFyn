/**
 * Regression test for rendering the `stuck_recovery` audit event.
 *
 * The event type was registered in db/constants.py, types.ts (union +
 * AUDIT_EVENT_META), and reached the frontend — but it had no case in
 * milestoneFromAudit(), so a stuck-subagent interrupt silently produced no
 * feed entry. The user saw a round end and a new one begin with no visible
 * reason. This locks the render so the recovery is transparent.
 */

import { describe, it, expect } from "vitest";
import { milestoneFromAudit } from "@/lib/groupEventHelpers";
import type { FeedEvent } from "@/lib/types";

function stuckRecoveryEvent(details: Record<string, unknown>): FeedEvent {
  return {
    _kind: "audit",
    data: {
      id: 1,
      run_id: "test-run",
      ts: "2026-06-01T16:41:44Z",
      event_type: "stuck_recovery",
      details,
    },
  };
}

describe("milestoneFromAudit — stuck_recovery", () => {
  // milestoneFromAudit returns a GroupedEvent union; stuck_recovery is the
  // "control" variant. Narrow before reading `text` so tsc is satisfied.
  function controlText(event: FeedEvent): string {
    const result = milestoneFromAudit(event);
    expect(result).not.toBeNull();
    expect(result?.type).toBe("control");
    if (result?.type !== "control") throw new Error("expected a control row");
    return result.text;
  }

  it("renders a control row naming the interrupted subagent(s) and idle time", () => {
    const text = controlText(
      stuckRecoveryEvent({
        stuck: [
          { agent_id: "aafe6f97", agent_type: "security-reviewer", idle_seconds: 605, total_seconds: 1332 },
        ],
      }),
    );

    expect(text).toContain("security-reviewer");
    expect(text).toContain("605s");
  });

  it("lists every stuck agent and uses the max idle time", () => {
    const text = controlText(
      stuckRecoveryEvent({
        stuck: [
          { agent_type: "security-reviewer", idle_seconds: 300 },
          { agent_type: "code-explorer", idle_seconds: 720 },
        ],
      }),
    );

    expect(text).toContain("security-reviewer");
    expect(text).toContain("code-explorer");
    expect(text).toContain("720s");
  });

  it("falls back gracefully when the stuck payload is missing", () => {
    const text = controlText(stuckRecoveryEvent({}));
    expect(text).toContain("subagent");
  });
});
