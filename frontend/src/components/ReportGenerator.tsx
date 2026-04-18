import React from "react";
import { type VulnerabilityItem } from "./VulnerabilityDisplay";

type Props = {
  scanId: string;
  vulnerabilities: VulnerabilityItem[];
};

const download = (filename: string, body: string, type: string): void => {
  const blob = new Blob([body], { type });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = filename;
  anchor.click();
  URL.revokeObjectURL(url);
};

export default function ReportGenerator({ scanId, vulnerabilities }: Props): JSX.Element {
  const payload = {
    scan_id: scanId,
    generated_at: new Date().toISOString(),
    findings_count: vulnerabilities.length,
    vulnerabilities,
  };

  const exportJson = (): void => {
    download(`${scanId || "scan"}-report.json`, JSON.stringify(payload, null, 2), "application/json");
  };

  const exportCsv = (): void => {
    const rows = vulnerabilities.map((item) => `${item.id},${item.title},${item.severity},${item.cvss_score}`);
    download(`${scanId || "scan"}-report.csv`, `id,title,severity,cvss\n${rows.join("\n")}`, "text/csv");
  };

  const exportHtml = (): void => {
    const content = `
      <html><body><h1>Scan ${scanId}</h1><p>Findings: ${vulnerabilities.length}</p></body></html>
    `;
    download(`${scanId || "scan"}-report.html`, content, "text/html");
  };

  const exportPdf = (): void => {
    download(`${scanId || "scan"}-report.pdf`, "PDF export placeholder", "application/pdf");
  };

  return (
    <section className="card">
      <h2>Report Generation</h2>
      <div className="row">
        <button type="button" onClick={exportHtml} disabled={!scanId}>
          HTML
        </button>
        <button type="button" onClick={exportPdf} disabled={!scanId}>
          PDF
        </button>
        <button type="button" onClick={exportJson} disabled={!scanId}>
          JSON
        </button>
        <button type="button" onClick={exportCsv} disabled={!scanId}>
          CSV
        </button>
      </div>
    </section>
  );
}
