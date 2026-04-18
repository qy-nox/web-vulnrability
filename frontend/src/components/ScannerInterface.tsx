import React from "react";
import { type VulnerabilityItem } from "./VulnerabilityDisplay";

type Props = {
  progress: number;
  onScanStarted: (scanId: string) => void;
  onProgress: (progress: number) => void;
  onVulnerabilitiesLoaded: (items: VulnerabilityItem[]) => void;
};

export default function ScannerInterface({
  progress,
  onScanStarted,
  onProgress,
  onVulnerabilitiesLoaded,
}: Props): JSX.Element {
  const [url, setUrl] = React.useState("https://example.com");
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState("");

  const startScan = async (): Promise<void> => {
    setLoading(true);
    setError("");
    onProgress(10);

    try {
      const scanResponse = await fetch("http://localhost:8000/api/scan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });
      const scanData = await scanResponse.json();
      onScanStarted(scanData.scan_id);
      onProgress(65);

      const vulnResponse = await fetch("http://localhost:8000/api/vulnerabilities");
      const vulnData = await vulnResponse.json();
      onVulnerabilitiesLoaded(vulnData.items ?? []);
      onProgress(100);
    } catch (scanError) {
      setError(`Failed to run scan: ${String(scanError)}`);
      onProgress(0);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="card">
      <h2>Start Scan</h2>
      <div className="row">
        <input
          value={url}
          onChange={(event) => setUrl(event.target.value)}
          placeholder="https://target.example"
          aria-label="Target URL"
        />
        <button type="button" onClick={() => void startScan()} disabled={loading}>
          {loading ? "Scanning..." : "Start"}
        </button>
      </div>
      <div className="progress">
        <div className="progress-bar" style={{ width: `${progress}%` }} />
      </div>
      {!!error && <p className="error">{error}</p>}
    </section>
  );
}
