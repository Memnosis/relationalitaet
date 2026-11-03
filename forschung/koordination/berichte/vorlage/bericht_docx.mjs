#!/usr/bin/env node
// Gemeinsamer Berichtsgenerator Claude/GPT für Berichte an Nils (Regeln R2, R3, R7). Owner: Claude.
// Aufruf:  node forschung/koordination/berichte/vorlage/bericht_docx.mjs BERICHT.json AUSGABE.docx
//          node … --pruefen BERICHT.json      (nur Inhalt prüfen, kein DOCX)
// Benötigt: npm-Paket `docx` (v9). Berichte sind intern (R6): Ausgabe ins Repository wird verweigert.
//
// Aufbau (Vorgabe Nils, 03.11.2026):
//   1. ROTER RAHMEN ganz oben: alle Entscheidungen und Freigaben in Kurzform, mit Antwortformat.
//      Er erscheint immer, auch wenn nichts offen ist ("keine offene Entscheidung").
//   2. Ampel · Abwesenheit (R7, falls ausgelöst) · Grafiken · Erledigt · Hängt · Nächste Schritte
//   3. ANHANG A: ausführliche Erklärung jeder Entscheidung (R3, alle Felder Pflicht)
//      ANHANG B: Fundstellen
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
let docx;
try { docx = require("docx"); } catch { docx = require(path.join(process.env.NODE_PATH || "", "docx")); }
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, BorderStyle,
  AlignmentType, HeadingLevel, ImageRun, ShadingType, PageNumber, Footer, Header, LevelFormat } = docx;

const ROT = "C0392B", ROT_HELL = "FDEDEC", GRAU = "BFBFBF", TEXT2 = "555555";
const AMPEL = { gruen: ["1E7B4F", "grün"], gelb: ["9A6700", "gelb"], rot: [ROT, "rot"] };
const R3_FELDER = ["worum", "warum_jetzt", "optionen", "empfehlung_begruendung", "wenn_nicht", "hintergrund"];

export function pruefen(b) {
  const f = [];
  const muss = (cond, msg) => { if (!cond) f.push(msg); };
  for (const k of ["nummer", "titel", "datum", "ersteller", "typ", "entscheidungen", "ampel"]) muss(k in b, `Pflichtfeld fehlt: ${k}`);
  muss(["claude", "gpt"].includes(b.ersteller), "ersteller muss claude oder gpt sein");
  muss(["regelbericht", "abwesenheitsbericht"].includes(b.typ), "typ muss regelbericht oder abwesenheitsbericht sein");
  if (b.typ === "abwesenheitsbericht") muss(b.abwesenheit && b.abwesenheit.ki && b.abwesenheit.seit_commit, "Abwesenheitsbericht braucht abwesenheit.ki und abwesenheit.seit_commit (R7)");
  const ids = new Set();
  for (const e of b.entscheidungen || []) {
    const id = e.id || "?";
    muss(!ids.has(id), `doppelte Entscheidungs-ID ${id}`); ids.add(id);
    for (const k of ["id", "art", "prio", "frage_kurz", "optionen_kurz", "empfehlung", "antwortformat", "erklaerung"]) muss(k in e, `${id}: Kurzform-Feld fehlt: ${k}`);
    muss(["entscheidung", "freigabe"].includes(e.art), `${id}: art muss entscheidung oder freigabe sein`);
    muss(["P0", "P1", "P2"].includes(e.prio), `${id}: prio muss P0, P1 oder P2 sein`);
    muss((e.frage_kurz || "").length <= 160, `${id}: frage_kurz länger als 160 Zeichen – Details gehören in den Anhang`);
    muss(e.empfehlung && "claude" in e.empfehlung && "gpt" in e.empfehlung, `${id}: Empfehlung beider KIs nötig (Wert darf "ausstehend" sein)`);
    const x = e.erklaerung || {};
    for (const k of R3_FELDER) muss(x[k] && (!Array.isArray(x[k]) || x[k].length), `${id}: Anhang-Feld fehlt (R3): ${k}`);
    const opt = x.optionen || [];
    muss(opt.length >= 2 && opt.length <= 4, `${id}: 2 bis 4 Optionen nötig`);
    for (const o of opt) muss(o.id && o.text && o.folgen, `${id}: jede Option braucht id, text, folgen`);
  }
  for (const a of b.ampel || []) muss(a.farbe in AMPEL, `Ampelfarbe unbekannt: ${a.farbe}`);
  for (const g of b.grafiken || []) muss(g.textalternative, `Grafik ohne Textalternative: ${g.datei}`);
  return f;
}

const p = (text, o = {}) => new Paragraph({ spacing: { after: 80 }, ...o, children: Array.isArray(text) ? text : [new TextRun({ text: String(text), ...(o.run || {}) })] });
const fett = (t, o = {}) => new TextRun({ text: t, bold: true, ...o });
const n = (t, o = {}) => new TextRun({ text: t, ...o });
const rand = (farbe, staerke) => ({ style: BorderStyle.SINGLE, size: staerke, color: farbe });
const zelle = (kinder, breite, o = {}) => new TableCell({ width: { size: breite, type: WidthType.DXA }, margins: { top: 60, bottom: 60, left: 100, right: 100 }, children: kinder, ...o });
const h = (t, lvl = HeadingLevel.HEADING_1) => new Paragraph({ heading: lvl, children: [new TextRun(t)] });
const punkt = (kinder) => new Paragraph({ numbering: { reference: "punkte", level: 0 }, spacing: { after: 40 }, children: Array.isArray(kinder) ? kinder : [n(kinder)] });

function roterRahmen(b) {
  const BREITE = 9360, sp = [1700, 3700, 2160, 1800];
  const offen = b.entscheidungen || [];
  const titel = new TableRow({ children: [zelle([p([fett(offen.length ? `ENTSCHEIDUNGEN UND FREIGABEN · ${offen.length} offen · bitte antworten` : "ENTSCHEIDUNGEN UND FREIGABEN · keine offen", { color: "FFFFFF", size: 24 })])], BREITE, { columnSpan: 4, shading: { type: ShadingType.CLEAR, fill: ROT, color: "auto" } })] });
  const kopf = new TableRow({ tableHeader: true, children: ["ID · Prio", "Frage (kurz) · Optionen", "Empfehlung", "Antwort so"].map((t, i) => zelle([p([fett(t, { size: 18 })])], sp[i], { shading: { type: ShadingType.CLEAR, fill: ROT_HELL, color: "auto" } })) });
  const zeilen = offen.map((e, i) => new TableRow({ cantSplit: true, children: [
    zelle([p([fett(e.id, { size: 18 })]), p([n(`${e.prio} · ${e.art}`, { size: 16, color: TEXT2 })])], sp[0]),
    zelle([p([n(e.frage_kurz, { size: 20 })]), ...e.optionen_kurz.map(o => p([n(o, { size: 18, color: TEXT2 })], { spacing: { after: 20 } })), p([n(`→ Erklärung: Anhang A${i + 1}`, { size: 16, italics: true, color: TEXT2 })])], sp[1]),
    zelle([p([fett("Claude: ", { size: 18 }), n(String(e.empfehlung.claude), { size: 18 })]), p([fett("GPT: ", { size: 18 }), n(String(e.empfehlung.gpt), { size: 18 })])], sp[2]),
    zelle([p([fett(`„${e.antwortformat}“`, { size: 20 })])], sp[3]),
  ] }));
  const leer = offen.length ? [] : [new TableRow({ children: [zelle([p("Keine Entscheidung und keine Freigabe nötig. Du kannst den Bericht als Information lesen.")], BREITE, { columnSpan: 4 })] })];
  const innen = rand(GRAU, 4), aussen = rand(ROT, 24);
  return new Table({ width: { size: BREITE, type: WidthType.DXA }, columnWidths: sp,
    borders: { top: aussen, bottom: aussen, left: aussen, right: aussen, insideHorizontal: innen, insideVertical: innen },
    rows: [titel, ...(offen.length ? [kopf, ...zeilen] : leer)] });
}

function tabelle(kopf, zeilen, sp) {
  const r = rand(GRAU, 4);
  return new Table({ width: { size: sp.reduce((a, c) => a + c, 0), type: WidthType.DXA }, columnWidths: sp,
    borders: { top: r, bottom: r, left: r, right: r, insideHorizontal: r, insideVertical: r },
    rows: [new TableRow({ tableHeader: true, children: kopf.map((t, i) => zelle([p([fett(t, { size: 18 })])], sp[i], { shading: { type: ShadingType.CLEAR, fill: "F2F2F2", color: "auto" } })) }),
      ...zeilen.map(z => new TableRow({ cantSplit: true, children: z.map((t, i) => zelle(Array.isArray(t) ? t : [p([n(String(t), { size: 18 })])], sp[i])) }))] });
}

function anhangA(b) {
  const out = [new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun("Anhang A · Ausführliche Erklärungen zu den Entscheidungen")] })];
  if (!b.entscheidungen.length) out.push(p("Keine offenen Entscheidungen."));
  b.entscheidungen.forEach((e, i) => {
    const x = e.erklaerung;
    out.push(h(`A${i + 1} · ${e.id} · ${e.frage_kurz}`, HeadingLevel.HEADING_2));
    out.push(p([fett("Worum geht es? "), n(x.worum)]));
    out.push(p([fett("Warum jetzt? "), n(x.warum_jetzt)]));
    out.push(tabelle(["Option", "Was passiert", "Folgen"], x.optionen.map(o => [o.id, o.text, o.folgen]), [900, 3900, 4560]));
    out.push(p(""));
    out.push(p([fett("Empfehlung Claude: "), n(x.empfehlung_begruendung.claude || String(e.empfehlung.claude))]));
    out.push(p([fett("Empfehlung GPT: "), n(x.empfehlung_begruendung.gpt || String(e.empfehlung.gpt))]));
    out.push(p([fett("Wenn nicht entschieden: "), n(x.wenn_nicht)]));
    out.push(p([fett("Antwortformat: "), n(`„${e.antwortformat}“`)]));
    out.push(p([fett("Hintergrund: "), n([].concat(x.hintergrund).join(" · "), { color: TEXT2 })]));
  });
  return out;
}

export function bauen(b, basis = ".") {
  const k = [];
  k.push(new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun(`Bericht ${b.nummer} · ${b.titel}`)] }));
  const gegen = b.gegengelesen ? `${b.gegengelesen.von}: ${b.gegengelesen.status}` : "ausstehend";
  k.push(p([n(`${b.datum} · erstellt von ${b.ersteller === "claude" ? "Claude" : "GPT"} · gegengelesen von ${gegen} · ${b.typ === "abwesenheitsbericht" ? "ABWESENHEITSBERICHT (R7)" : "Regelbericht (R2)"}`, { color: TEXT2, size: 18 })]));
  k.push(roterRahmen(b), p(""));
  k.push(h("1 · Ampel und Kernaussage"));
  k.push(tabelle(["Strang", "Stand", "Kernaussage"], b.ampel.map(a => [a.strang, [p([fett(`● ${AMPEL[a.farbe][1]}`, { color: AMPEL[a.farbe][0], size: 18 })])], a.satz]), [1800, 1100, 6460]));
  if (b.abwesenheit) {
    const a = b.abwesenheit;
    k.push(h("2 · Abwesenheit (R7)"));
    k.push(p([fett(`${a.ki === "claude" ? "Claude" : "GPT"} war abwesend `), n(`seit Commit ${a.seit_commit}${a.stunden ? `, ${a.stunden} h` : ""}${a.schritte ? `, ${a.schritte} Arbeitsschritte der anderen KI` : ""}. Auslöser: ${[].concat(a.ausloeser || []).join(", ") || "—"}.`)]));
    for (const x of a.folgen || []) k.push(punkt(x));
    k.push(p([fett("Nachhol-Analyse: "), n(a.nachholanalyse || "ausstehend – die zurückkehrende KI analysiert alle Schritte seit dem genannten Commit, bevor sie neue eigene Arbeit beginnt.")]));
  }
  let nr = b.abwesenheit ? 2 : 1;
  const nh = (t) => h(`${++nr} · ${t}`);
  if ((b.grafiken || []).length) {
    k.push(nh("Fortschritt in Grafiken"));
    for (const g of b.grafiken) {
      const dat = path.resolve(basis, g.datei);
      if (fs.existsSync(dat)) k.push(new Paragraph({ alignment: AlignmentType.CENTER, children: [new ImageRun({ type: "png", data: fs.readFileSync(dat), transformation: { width: g.breite || 600, height: g.hoehe || 300 }, altText: { title: g.titel, description: g.textalternative, name: g.titel } })] }));
      k.push(p([fett(g.titel + ": "), n(g.textalternative, { color: TEXT2, size: 18 })]));
    }
  }
  k.push(nh("Erledigt (mit Nachweis)"));
  for (const e of b.erledigt || []) k.push(punkt([n(e.text + " "), n(e.nachweis ? `[${e.nachweis}]` : "", { color: TEXT2, size: 16 })]));
  k.push(nh("Was hängt und warum"));
  if ((b.haengt || []).length) k.push(tabelle(["Blocker", "Verantwortlich"], b.haengt.map(x => [x.text, x.verantwortlich]), [7160, 2200]));
  else k.push(p("Nichts."));
  k.push(nh("Nächste Schritte"));
  for (const [ki, liste] of Object.entries(b.naechste || {})) { k.push(p([fett(ki === "claude" ? "Claude" : ki === "gpt" ? "GPT" : ki)])); for (const x of liste) k.push(punkt(x)); }
  k.push(...anhangA(b));
  k.push(h("Anhang B · Fundstellen"));
  for (const f of b.fundstellen || []) k.push(punkt([n(f, { size: 18 })]));
  return new Document({
    creator: b.ersteller, title: `Bericht ${b.nummer}`,
    styles: { default: { document: { run: { font: "Arial", size: 21 } } },
      paragraphStyles: [
        { id: "Title", name: "Title", basedOn: "Normal", run: { size: 40, bold: true, font: "Arial" }, paragraph: { spacing: { after: 120 } } },
        { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 28, bold: true, font: "Arial" }, paragraph: { spacing: { before: 300, after: 120 }, outlineLevel: 0 } },
        { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 24, bold: true, font: "Arial" }, paragraph: { spacing: { before: 220, after: 100 }, outlineLevel: 1 } }] },
    numbering: { config: [{ reference: "punkte", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] }] },
    sections: [{
      properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1134, right: 1134, bottom: 1134, left: 1134 } } },
      headers: { default: new Header({ children: [p([n(`Bericht ${b.nummer} an Nils · intern, nicht öffentlich`, { size: 16, color: TEXT2 })], { alignment: AlignmentType.RIGHT })] }) },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: ["Seite ", PageNumber.CURRENT, " von ", PageNumber.TOTAL_PAGES], size: 16, color: TEXT2 })] })] }) },
      children: k }],
  });
}

async function main() {
  const args = process.argv.slice(2);
  const nurPruefen = args[0] === "--pruefen";
  const [ein, aus] = nurPruefen ? args.slice(1) : args;
  if (!ein || (!nurPruefen && !aus)) { console.error("Aufruf: bericht_docx.mjs BERICHT.json AUSGABE.docx | --pruefen BERICHT.json"); process.exit(2); }
  const b = JSON.parse(fs.readFileSync(ein, "utf8"));
  const fehler = pruefen(b);
  if (fehler.length) { console.error("Bericht ungültig:\n- " + fehler.join("\n- ")); process.exit(1); }
  if (nurPruefen) { console.log(`Bericht ${b.nummer}: gültig (${b.entscheidungen.length} Entscheidungen im roten Rahmen, ${b.entscheidungen.length} Erklärungen im Anhang)`); return; }
  const repo = path.resolve(new URL("../../../../", import.meta.url).pathname);
  const ziel = path.resolve(aus);
  if (ziel.startsWith(repo + path.sep)) { console.error("Verweigert: Berichte an Nils sind intern (R6) und gehören nicht ins öffentliche Repository."); process.exit(3); }
  fs.writeFileSync(ziel, await Packer.toBuffer(bauen(b, path.dirname(path.resolve(ein)))));
  console.log(`geschrieben: ${ziel}`);
}

if (import.meta.url === `file://${process.argv[1]}`) main();
