# LLM Prompt: Create Laundry Status Dashboard Card

Use this prompt with an LLM that has MCP access to your Home Assistant server to create the dashboard card.

---

## Prompt

```
Create a Home Assistant dashboard card (or section) for laundry status tracking. This should be a persistent, at-a-glance indicator that tells me whether laundry is sitting in the washing machine and needs to be moved to the dryer.

### Entities available

These entities already exist and are working:

- `input_boolean.laundry_needs_moving` — ON when laundry is sitting in the washer and hasn't been moved to the dryer. Can be toggled OFF to manually dismiss.
- `input_boolean.washing_machine_on` — ON when the washing machine is currently running.
- `input_boolean.dryer_on` — ON when the dryer is currently running.
- `sensor.washing_machine_estimated_remaining` — Minutes remaining in the wash cycle (55 min cycle).
- `sensor.dryer_estimated_remaining` — Minutes remaining in the dryer cycle (120 min cycle).
- `sensor.laundry_waiting_duration` — Minutes since the laundry was flagged as needing to be moved. Has a `status` attribute with human-readable text ("All clear", "Waiting X minutes", "Waiting over an hour", "Overdue - Xh waiting").
- `sensor.washing_machine_random_message` — Fun random message when wash finishes.
- `sensor.dryer_random_message` — Fun random message when dryer finishes.

### What I want the card to show

1. **Primary status indicator** — Large, prominent visual showing the current laundry state:
   - **All Clear** (green/neutral) — Nothing needs attention. Show when `input_boolean.laundry_needs_moving` is OFF and neither machine is running.
   - **Washing** (blue/active) — Washing machine is running. Show estimated time remaining.
   - **Move to Dryer!** (orange/amber warning) — Laundry is sitting in the washer! This is the main alert state. Show how long it's been waiting using `sensor.laundry_waiting_duration`. This should be visually prominent — the whole point of this card.
   - **Drying** (blue/active) — Dryer is running. Show estimated time remaining.

2. **Dismiss button** — When in the "Move to Dryer!" state, include a way to tap/toggle `input_boolean.laundry_needs_moving` to dismiss (mark as done / moved).

3. **Visual design**:
   - Use conditional formatting so the card changes colour/appearance based on state.
   - Use appropriate MDI icons: `mdi:washing-machine` for washing, `mdi:tumble-dryer` for drying, `mdi:washing-machine-alert` for needs-moving, `mdi:check-circle` for all clear.
   - The "needs moving" state should escalate visually — maybe more urgent colour after 60+ minutes.

4. **Keep it simple** — This is a single card or small group of cards. No complex multi-tab layouts. It should work on mobile and on a wall-mounted tablet.

### Technical notes

- I have these HACS frontend cards installed and available: `button-card`, `card-mod`, `auto-entities`, `template-entity-row`, `config-template-card`, `mini-graph-card`, `bar-card`.
- Feel free to use `button-card` with custom templates for the best visual result, or use native HA cards with `card-mod` for styling — whatever gives the cleanest result.
- Place this card in an existing dashboard or create a new Lovelace view called "Laundry".
```

---
