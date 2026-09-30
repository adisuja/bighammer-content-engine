/** @OnlyCurrentDoc */
/**
 * BigHammer review studio - shared feedback store (Google Apps Script web app bound to a Google Sheet).
 * Deploy: Extensions > Apps Script in the "BigHammer review log" sheet, paste this file,
 * Deploy > New deployment > Web app, Execute as: Me, Who has access: Anyone. Put the /exec URL
 * into queue/posts.json as "sync_url" and republish.
 * Stores one row per event: approvals and feedback notes. Append-only; the site derives state.
 */
const SHEET = "events";
const COLS = ["id", "t", "post", "kind", "name", "role", "value", "text"];
const safe_ = (v) => { v = String(v || ""); return /^[=+\-@]/.test(v) ? "'" + v : v; };  // never let a note become a formula

function sheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sh = ss.getSheetByName(SHEET);
  if (!sh) { sh = ss.insertSheet(SHEET); sh.appendRow(COLS); sh.setFrozenRows(1); }
  return sh;
}

function doGet() {
  const rows = sheet_().getDataRange().getValues().slice(1);
  const out = rows.filter(r => r[0]).map(r => ({
    id: String(r[0]), t: r[1] instanceof Date ? r[1].toISOString() : String(r[1]), post: String(r[2]),
    kind: String(r[3]), name: String(r[4]), role: String(r[5]), value: r[6] === true || r[6] === "TRUE", text: String(r[7] || "")
  }));
  return ContentService.createTextOutput(JSON.stringify(out)).setMimeType(ContentService.MimeType.JSON);
}

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const ev = JSON.parse(e.postData.contents);
    if (!ev.id || !ev.post || ["approve", "comment"].indexOf(ev.kind) < 0) throw new Error("bad event");
    const sh = sheet_();
    const ids = sh.getRange(1, 1, Math.max(sh.getLastRow(), 1), 1).getValues().flat();
    if (ids.indexOf(ev.id) < 0) {
      sh.appendRow([safe_(ev.id), String(ev.t), safe_(ev.post), safe_(ev.kind), safe_(String(ev.name || "").slice(0, 80)), safe_(ev.role),
                    ev.kind === "approve" ? !!ev.value : "", safe_(String(ev.text || "").slice(0, 5000))]);
    }
    return ContentService.createTextOutput(JSON.stringify({ ok: true })).setMimeType(ContentService.MimeType.JSON);
  } finally { lock.releaseLock(); }
}
